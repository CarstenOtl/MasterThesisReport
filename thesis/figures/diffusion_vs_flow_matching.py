"""Generate Figure 2.3 (fig:diffusion-vs-fm): diffusion vs. conditional flow matching.

Two-dimensional toy action space with a Gaussian source p0 = N(0, I) and a bimodal
data distribution p1 (two Gaussian clusters). Both models are exact, not sketched:

(a) Diffusion: variance-preserving SDE with a linear beta schedule. The score of the
    noised Gaussian mixture is analytic, so the reverse SDE is integrated with
    Euler-Maruyama over many steps. One forward noising path is shown dashed.
(b) Conditional flow matching: the minimizer of the flow-matching loss for the
    straight-line path x^l = (1-l) x0 + l x1 is E[x1 - x0 | x^l = x], which is
    analytic for a Gaussian mixture. Trajectories use a few explicit Euler steps.

Run from the thesis folder:  python figures/diffusion_vs_flow_matching.py
"""
import sys
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

OUT = Path(__file__).with_suffix(".pdf")

mpl.rcParams.update({
    "text.usetex": True,
    "text.latex.preamble": (
        r"\usepackage[T1]{fontenc}"
        r"\usepackage{amsmath}"
        r"\usepackage[expert,charter,cal=cmcal]{mathdesign}"
        r"\renewcommand{\vec}[1]{\boldsymbol{#1}}"
    ),
    "font.family": "serif",
    "font.size": 8.5,
    "axes.linewidth": 0.6,
})

# --- toy problem -------------------------------------------------------------
MU = np.array([[-2.2, 2.6], [2.2, 2.6]])   # data modes
S = 0.35                                   # data std per mode
PI = np.array([0.5, 0.5])                  # mode weights
BLUE, ORANGE, GRAY = "#0065BD", "#E37222", "#7F7F7F"
MODE_COLORS = [BLUE, ORANGE]

# Seeds chosen for a legible layout: endpoints near the modes, six per mode, and a
# forward noising path that stays inside the frame. The models themselves are exact.
rng = np.random.default_rng(17)
rng_fwd = np.random.default_rng(378)
rng_demo = np.random.default_rng(0)
N_TRAJ = 12
x_start = rng.standard_normal((200, 2))
x_start = x_start[np.linalg.norm(x_start, axis=1) < 1.8][:N_TRAJ]  # bulk of p0, shared by both panels


def gmm_posterior(x, means, var):
    """Mode responsibilities w_k(x) for isotropic Gaussian components."""
    d2 = ((x[:, None, :] - means[None]) ** 2).sum(-1)          # (N, K)
    logw = np.log(PI)[None] - 0.5 * d2 / var[None] - np.log(var)[None]
    logw -= logw.max(1, keepdims=True)
    w = np.exp(logw)
    return w / w.sum(1, keepdims=True)


# --- (a) diffusion: VP-SDE ---------------------------------------------------
B0, B1 = 0.1, 20.0
beta = lambda t: B0 + t * (B1 - B0)
alpha = lambda t: np.exp(-0.5 * (B0 * t + 0.5 * (B1 - B0) * t**2))


def score(x, t):
    a = alpha(t)
    means = a * MU
    var = np.full(len(MU), a**2 * S**2 + 1.0 - a**2)
    w = gmm_posterior(x, means, var)
    return -(w[:, :, None] * (x[:, None, :] - means[None]) / var[None, :, None]).sum(1)


N_DIFF = 100
ts = np.linspace(1.0, 1e-3, N_DIFF + 1)
x = x_start.copy()
diff_paths = [x.copy()]
for t0, t1 in zip(ts[:-1], ts[1:]):  # probability-flow ODE of the VP-SDE, integrated backward
    dt = t0 - t1
    b = beta(t0)
    x = x + 0.5 * b * (x + score(x, t0)) * dt
    diff_paths.append(x.copy())
diff_paths = np.stack(diff_paths, 1)                            # (N, steps, 2)

# forward noising of one demonstrated action (stochastic, coarser grid for legibility)
ts_fwd = np.linspace(1e-3, 1.0, 31)
x_fwd = (MU[1] + S * np.array([0.3, -0.2]))[None]
fwd_path = [x_fwd.copy()]
for t0, t1 in zip(ts_fwd[:-1], ts_fwd[1:]):
    dt = t1 - t0
    b = beta(t0)
    x_fwd = x_fwd - 0.5 * b * x_fwd * dt + np.sqrt(b * dt) * rng_fwd.standard_normal(x_fwd.shape)
    fwd_path.append(x_fwd.copy())
fwd_path = np.concatenate(fwd_path, 0)


# --- (b) conditional flow matching: exact marginal velocity field ------------
def velocity(x, lam):
    a, b = 1.0 - lam, lam
    means = b * MU
    var_s = a**2 + b**2 * S**2
    w = gmm_posterior(x, means, np.full(len(MU), var_s))
    cov = b * S**2 - a                                           # Cov(x1 - x0, x^l) per dim
    v_k = MU[None] + (cov / var_s) * (x[:, None, :] - means[None])
    return (w[:, :, None] * v_k).sum(1)


N_FM = 4
lams = np.linspace(0.0, 1.0, N_FM + 1)
x = x_start.copy()
fm_paths = [x.copy()]
for l0, l1 in zip(lams[:-1], lams[1:]):
    x = x + (l1 - l0) * velocity(x, l0)
    fm_paths.append(x.copy())
fm_paths = np.stack(fm_paths, 1)


def end_mode(paths):
    return np.argmin(((paths[:, -1, None, :] - MU[None]) ** 2).sum(-1), 1)


# --- plotting ----------------------------------------------------------------
def draw_densities(ax):
    for r, alph in [(2.0, 0.10), (1.0, 0.18)]:
        ax.add_patch(Ellipse((0, 0), 2 * r, 2 * r, color=GRAY, alpha=alph, lw=0, zorder=0))
    for k, c in enumerate(MODE_COLORS):
        for r, alph in [(2.0, 0.12), (1.0, 0.22)]:
            ax.add_patch(Ellipse(MU[k], 2 * r * S, 2 * r * S, color=c, alpha=alph, lw=0, zorder=0))
    demos = MU[rng_demo.integers(0, 2, 60)] + S * rng_demo.standard_normal((60, 2))
    ax.scatter(*demos.T, s=2.5, c="k", lw=0, zorder=1)
    ax.text(0, -2.35, r"noise $p_0=\mathcal{N}(\vec{0},\boldsymbol{I})$", ha="center", va="top", color="#404040")
    ax.text(0, 3.45, r"demonstrated actions $p_1$", ha="center", va="bottom", color="#404040")


def setup(ax, title):
    ax.set_xlim(-3.7, 3.7)
    ax.set_ylim(-3.0, 3.9)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel(r"$u_1$", labelpad=1)
    ax.set_ylabel(r"$u_2$", labelpad=1)
    ax.set_title(title, fontsize=9, pad=4)
    ax.text(3.55, -2.85, r"conditioned on $\vec{c}$", ha="right", va="bottom", fontsize=7.5,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GRAY, lw=0.5))


fig, (ax_d, ax_f) = plt.subplots(1, 2, figsize=(6.1, 3.25))
fig.subplots_adjust(left=0.035, right=0.995, bottom=0.05, top=0.93, wspace=0.08)

# (a) diffusion
setup(ax_d, r"(a) Diffusion")
draw_densities(ax_d)
ax_d.plot(*fwd_path.T, lw=0.6, color="#909090", zorder=2)
ax_d.annotate("", xy=fwd_path[-1], xytext=fwd_path[-2],
              arrowprops=dict(arrowstyle="-|>", lw=0.6, color="#909090", mutation_scale=7))
ax_d.text(2.05, 0.3, r"forward:\\add noise", ha="left", va="center", fontsize=7.5, color="#606060")
for p, k in zip(diff_paths, end_mode(diff_paths)):
    ax_d.plot(*p.T, lw=0.6, color=MODE_COLORS[k], marker="o", ms=0.7, zorder=3)
    ax_d.plot(*p[0], "o", ms=2.2, color="k", zorder=4)
    ax_d.plot(*p[-1], "o", ms=2.2, mfc="white", mec=MODE_COLORS[k], mew=0.7, zorder=4)
ax_d.text(-3.55, 0.55, rf"reverse:\\{N_DIFF} steps", ha="left", va="center", fontsize=7.5)

# (b) flow matching
setup(ax_f, r"(b) Conditional flow matching")
draw_densities(ax_f)
gx, gy = np.meshgrid(np.linspace(-3.0, 3.0, 9), np.linspace(-2.0, 3.2, 7))
grid = np.stack([gx.ravel(), gy.ravel()], 1)
v = velocity(grid, 0.5)
ax_f.quiver(*grid.T, *v.T, color="#C4C4C4", angles="xy", scale_units="xy", scale=9.0,
            width=0.004, headwidth=3.5, headlength=4, zorder=1)
ax_f.text(-3.55, -1.75, r"$\vec{v}_\theta(\cdot,\lambda{=}0.5\mid\vec{c})$", ha="left", va="center",
          fontsize=7.5, color="#606060")
# one straight-line training pair (eq. fm-line)
u0, u1 = np.array([2.35, -1.45]), MU[1] + S * np.array([0.3, -0.3])
ax_f.annotate("", xy=u1, xytext=u0,
              arrowprops=dict(arrowstyle="-|>", ls=(0, (2, 1.5)), lw=0.6, color="#404040",
                              mutation_scale=7, shrinkA=0, shrinkB=2))
um = 0.5 * (u0 + u1)
ax_f.plot(*um, "D", ms=2.6, color="#404040", zorder=5)
ax_f.plot(*u0, "o", ms=2.2, color="#404040", zorder=5)
ax_f.text(um[0] - 0.12, um[1], r"$\vec{u}^{\lambda}$", ha="right", va="center", fontsize=8)
ax_f.text(u0[0] + 0.12, u0[1], r"$\vec{u}^{0}$", ha="left", va="center", fontsize=8)
ax_f.text(um[0] + 0.12, um[1] + 0.1, r"target\\$\vec{u}^{1}-\vec{u}^{0}$", ha="left", va="center",
          fontsize=7.5, color="#404040")
for p, k in zip(fm_paths, end_mode(fm_paths)):
    ax_f.plot(*p.T, lw=0.7, color=MODE_COLORS[k], marker="o", ms=1.6, zorder=3)
    ax_f.plot(*p[0], "o", ms=2.2, color="k", zorder=4)
    ax_f.plot(*p[-1], "o", ms=2.2, mfc="white", mec=MODE_COLORS[k], mew=0.7, zorder=4)
ax_f.text(-3.55, 0.55, rf"{N_FM} Euler steps", ha="left", va="center", fontsize=7.5)

fig.savefig(OUT)
if len(sys.argv) > 1:  # optional PNG preview path
    fig.savefig(sys.argv[1], dpi=200)
print(f"wrote {OUT}")


# --- 3-D version: generation time runs left to right --------------------------
# Axes: x = generation time (0 = noise, 1 = data), y = u_2, z = u_1. Each vertical
# slice is a copy of the 2-D action space at one point in time.
OUT_3D = OUT.with_name(OUT.stem + "_3d.pdf")
U1L, U2L = (-3.6, 3.6), (-2.8, 3.8)
N_CLOUD = 300
rng_cloud = np.random.default_rng(5)
cloud0 = rng_cloud.standard_normal((N_CLOUD, 2))
cloud1 = MU[rng_cloud.integers(0, 2, N_CLOUD)] + S * rng_cloud.standard_normal((N_CLOUD, 2))

# intermediate denoising samples: integrate a cloud of noise samples with the same sampler
DIFF_SLICES = [0, 25, 50, 75, 100]  # denoising steps shown as slices
x = cloud0.copy()
diff_cloud = {0: x.copy()}
for i, (t0, t1) in enumerate(zip(ts[:-1], ts[1:]), start=1):
    b = beta(t0)
    x = x + 0.5 * b * (x + score(x, t0)) * (t0 - t1)
    if i in DIFF_SLICES:
        diff_cloud[i] = x.copy()
diff_cloud_mode = end_mode(np.stack([cloud0, diff_cloud[N_DIFF]], 1))


def draw_slice(ax, t, label, fill="#F2F2F2"):
    yy, zz = np.meshgrid(U2L, U1L)
    ax.plot_surface(np.full_like(yy, t), yy, zz, color=fill, alpha=0.45, lw=0, shade=False)
    ax.plot([t] * 5, [U2L[0], U2L[1], U2L[1], U2L[0], U2L[0]], [U1L[0], U1L[0], U1L[1], U1L[1], U1L[0]],
            color="#B0B0B0", lw=0.5)
    ax.text(t, 0.5 * sum(U2L), U1L[1] + 0.4, label, ha="center", va="bottom", fontsize=7.5, color="#404040")


def draw_cloud(ax, t, pts, colors, s=1.2, alpha=0.55):
    ax.scatter(np.full(len(pts), t), pts[:, 1], pts[:, 0], s=s, c=colors, lw=0, alpha=alpha,
               depthshade=False)


def setup_3d(ax, title, xlabel, xticks, xticklabels):
    ax.set_xlim(0, 1)
    ax.set_ylim(*U2L)
    ax.set_zlim(*U1L)
    ax.set_box_aspect((3.2, 1.0, 1.0), zoom=2.0)
    ax.set_proj_type("ortho")
    ax.view_init(elev=12, azim=-74)
    ax.computed_zorder = False  # draw in call order
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels, fontsize=7.5)
    ax.tick_params(axis="x", pad=-3)
    ax.set_yticks([])
    ax.set_zticks([])
    ax.set_xlabel(xlabel, labelpad=-6)
    ax.set_ylabel(r"$u_2$", labelpad=-14)
    ax.set_zlabel(r"$u_1$", labelpad=-14)
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.set_pane_color((1, 1, 1, 0))
        axis._axinfo["grid"]["linewidth"] = 0.0
    pos = ax.get_position(original=True)  # transAxes maps to the square 3-D viewport, so place labels in figure coords
    ax.figure.text(pos.x0 + 0.01, pos.y1 - 0.01, title, ha="left", va="top", fontsize=9)
    ax.figure.text(pos.x1 - 0.01, pos.y1 - 0.01, r"conditioned on $\vec{c}$", ha="right", va="top",
                   fontsize=7.5, bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GRAY, lw=0.5))


def draw_paths_3d(ax, paths, t, lw, ms):
    for p, k in zip(paths, end_mode(paths)):
        ax.plot(t, p[:, 1], p[:, 0], lw=lw, color=MODE_COLORS[k], marker="o", ms=ms)
        ax.plot(0.0, p[0, 1], p[0, 0], "o", ms=2.2, color="k")
        ax.plot(1.0, p[-1, 1], p[-1, 0], "o", ms=2.2, mfc="white", mec=MODE_COLORS[k], mew=0.7)


mode_rgb = np.array(MODE_COLORS)
fig3 = plt.figure(figsize=(6.1, 5.0))
ax3d = fig3.add_subplot(2, 1, 1, projection="3d")
ax3f = fig3.add_subplot(2, 1, 2, projection="3d")
fig3.subplots_adjust(left=0.0, right=1.0, bottom=0.0, top=1.0, hspace=0.0)

# (a) diffusion: x = fraction of the denoising iterations done
setup_3d(ax3d, r"(a) Diffusion", r"denoising step",
         [s / N_DIFF for s in DIFF_SLICES], [str(s) for s in DIFF_SLICES])
for s in DIFF_SLICES:
    t = s / N_DIFF
    label = r"noise $p_0$" if s == 0 else (r"data $p_1$" if s == N_DIFF else "")
    draw_slice(ax3d, t, label)
    colors = np.full(N_CLOUD, GRAY) if s == 0 else mode_rgb[diff_cloud_mode]
    draw_cloud(ax3d, t, diff_cloud[s], colors)
ax3d.plot(1.0 - ts_fwd, fwd_path[:, 1], fwd_path[:, 0], lw=0.6, color="#909090")
ax3d.text(0.88, 0.5 * sum(U2L), 3.4, r"forward: add noise", fontsize=7.5, color="#606060",
          ha="right", va="bottom")
draw_paths_3d(ax3d, diff_paths, np.linspace(0.0, 1.0, N_DIFF + 1), lw=0.6, ms=0.5)

# (b) flow matching: x = flow time lambda
setup_3d(ax3f, r"(b) Conditional flow matching", r"$\lambda$", list(lams), [f"{l:g}" for l in lams])
gq = np.stack([g.ravel() for g in np.meshgrid(np.linspace(-3.0, 3.0, 7), np.linspace(-2.2, 3.2, 6))], 1)
for lam in lams:
    if lam in (0.0, 1.0):
        draw_slice(ax3f, lam, r"noise $p_0$" if lam == 0.0 else r"data $p_1$")
        draw_cloud(ax3f, lam, cloud0 if lam == 0.0 else cloud1,
                   np.full(N_CLOUD, GRAY) if lam == 0.0 else mode_rgb[end_mode(np.stack([cloud1, cloud1], 1))])
    else:
        draw_slice(ax3f, lam, rf"$\vec{{v}}_\theta(\cdot,{lam:g}\mid\vec{{c}})$")
        vq = velocity(gq, lam) / 4.0
        ax3f.quiver(np.full(len(gq), lam), gq[:, 1], gq[:, 0], np.zeros(len(gq)), vq[:, 1], vq[:, 0],
                    color="#7A7A7A", lw=0.7, arrow_length_ratio=0.3)
# one straight-line training pair (eq. fm-line), straight in (lambda, u)
ax3f.plot([0.0, 1.0], [u0[1], u1[1]], [u0[0], u1[0]], ls=(0, (2, 1.5)), lw=0.8, color="#202020")
ax3f.plot(0.5, um[1], um[0], "D", ms=2.8, color="#202020")
ax3f.plot(0.0, u0[1], u0[0], "o", ms=2.4, color="#202020")
ax3f.text(0.5, um[1], um[0] + 0.3, r"$\vec{u}^{\lambda}$", fontsize=8, ha="center", va="bottom")
ax3f.text(0.0, u0[1], u0[0] + 0.3, r"$\vec{u}^{0}$", fontsize=8, ha="center", va="bottom")
draw_paths_3d(ax3f, fm_paths, lams, lw=0.8, ms=2.0)

# 3-D axes clip their artists to a square viewport; the wide box needs the full panel width
for ax in (ax3d, ax3f):
    for artist in ax.get_children():
        artist.set_clip_on(False)
fig3.savefig(OUT_3D)
if len(sys.argv) > 2:  # optional PNG preview path for the 3-D version
    fig3.savefig(sys.argv[2], dpi=200)
print(f"wrote {OUT_3D}")
