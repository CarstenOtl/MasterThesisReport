# Cross-reference audit D: thesis §3.5 Student Policy Distillation (chapter03.tex 180–300)

Sources and abbreviations
- THESIS = `/home/carsten/code/MasterThesisReport/thesis/source/chapter03.tex` (line numbers below), plus `appendix.tex` (Table `tab:flow`, lines 72–101) and `notation.tex` (lines 35–46).
- NUTS = `/home/carsten/code/MasterThesisReport/additional/NUTS.md`.
- FU = `/home/carsten/code/forgeUltra/`.
- DEP = `/home/carsten/code/inspirehand-franka-ros2-ws-/`.
- "09-10 student" = `sequential_threading_cycle10_hybrid_teacher_d415_20ep` (FU/HANDOVER.md:175–217; DEP `apps/policy_rollout/checkpoints/README.md`).
- "10-13 student" = `m24-dr-disturbed-dp3-no-finger-velocity-seed0-20261013-135143-648368` (DEP `run_policy_rollout.py:20–24` default checkpoint; its `nn/flow_config.json`).

Verdict key: CONSISTENT / MISMATCH / PARTIAL / UNVERIFIED.

---

## 0. Headline findings (read these first)

| # | Finding | Severity |
|---|---|---|
| H1 | **The student the deployment stack actually loads is not the student the thesis describes.** `DEP/apps/policy_rollout/run_policy_rollout.py:20–24` defaults to the 10-13 checkpoint, whose `nn/flow_config.json` records `proprio_dim: 26`, `hand_velocity_observation: omitted`, `vision_nut_position_head: False`, `trajectory_progress_duration_s: 46.6` (699 steps), trained on dataset `sequential-threading-dual-supervision-20261013-132348` (`DEP/docs/policy_rollout_training_gap_todo.md:155–158`). The thesis (l. 234, 244, 240, 251; Table `tab:flow`) describes the 09-10 student: 29-D proprioception, auxiliary nut-position head with unit weight, 64.6 s clock, dataset `…20260910-181107-771583` with 19,486 frames. The thesis text is CONSISTENT with FU/HANDOVER.md:175–217 and with `DEP/apps/policy_rollout/checkpoints/README.md`, but MISMATCHes the checkpoint that ran on hardware on 2026-10-13/16 (gap doc l. 253–268). Neither FU/HANDOVER.md nor FU/todo.md documents the 10-13 run (grep for `20261013`, `m24-dr`, `no-finger-velocity` returns nothing; FU `git log` head is `c5b8533`). | **MISMATCH (thesis vs deployment)** |
| H2 | **Inference steps at deployment.** Thesis l. 218 "N = 16 at deployment" and l. 220 "samples in sixteen steps". `DEP/apps/policy_rollout/policy_rollout/flow_policy.py:454–462` defaults to 16 steps on CUDA and **2 steps on CPU**; `DEP/README.md:73–79` states the workcell PC has no NVIDIA GPU and runs the CPU setup. However, the first hardware run with the final stack was on CUDA with 16 steps (gap doc l. 266–268: "first hardware run on CUDA … 16 flow steps … 0 missed deadlines"). So 16 is true for the GPU runs, not for the CPU default. | PARTIAL |
| H3 | **ACT-style Transformer regression baseline does not exist in forgeUltra.** `FU/distillation/utils/action_heads/` contains only `conditional_flow_matching.py`, `deterministic_mlp.py`, `dextrah_concat.py`, `dextrah_recurrent.py`; grep for `action_quer|learned_quer|ACT|DETR|cvae|transformer_regression` over `distillation/`, `forge_ultra/`, `docs/`, `HANDOVER.md`, `todo.md`, `README.md` finds nothing. Only NUTS l. 338–343 describes it. Confirms the existing `% TODO(unsure)` at l. 298. | UNVERIFIED (code) |
| H4 | **NUTS disagrees with thesis and code on three student facts** (author knows paper and code differ; listed for completeness): (a) NUTS l. 246–247 "fusion yields the 320-D condition c_t" vs thesis 256-D / code `condition_dim: 256` (NUTS Fig. 2 caption l. 97–99 itself says "256-D state feature", so the paper is internally inconsistent); (b) NUTS l. 233–235 "e^m_t is the one-hot encoding of the active phase m_t ∈ M from (1)" (six phases) vs thesis/code three-way one-hot; (c) NUTS l. 226–227, 208, 219–220 `D = D_sim ∪ D_real` with human-corrected replays vs thesis sim-only `D = D_sim`. | noted |
| H5 | **"The same flow-matching student can be trained online" (l. 186, 276) is only partly true.** The online flow trainer shares the head class and hyperparameters, but its registered agent (`FU/distillation/config/agents/ablations/dagger_flow_matching_agent.yaml`) uses the DUSt3R-style `two_channel_rgbd_encoder` (not DP3), the `conditional_flow_matching_native_osc` head (native raw-action labels, **no** cyclic process-phase conditioning), aux weight 0.01 (not 1.0), and the README quickstart runs it with privileged `nut_pose_6d`. | PARTIAL |
| H6 | **"The recurrent and Transformer baselines share the observation and action contracts of the flow student" (l. 297).** The LSTM's OSC variant does share the 9-D unified filtered target with scale `[3,4,16,3,3,3,2,2,2]` and clip 1 (`dagger_lstm_agent.yaml:71–91`), but its observation is `proprio_rgbd_vision_teacher_action.yaml` (q10 + q̇10 + prev unified 9 + a 4-D full-task phase one-hot when `full_task`) with the `two_channel_rgbd_encoder`, trained **online** (DAgger, default β = 0), not offline on DP3 features from the fixed dataset as NUTS (c) l. 348–353 states. | PARTIAL |
| H7 | **Latency (l. 247 `\tbd` on RTX 5090).** No RTX 5090 number exists in either repo. Measured numbers that do exist: `DEP/apps/policy_rollout/README.md:83–99`: 16 steps 11.7 ms mean / 12.0 ms max on an RTX 3060 Laptop GPU (vision ≈2 ms + ≈0.6 ms per step), 13.5 ms through the compose setup; CPU i7-12700H 92 / 225 ms at 16 steps, 16 / 18 ms at 2 steps; hardware run steady max 21 ms per tick on CUDA (gap doc l. 266–267). | UNVERIFIED → data available |

---

## 1. Claim-by-claim table

### 1.1 Section intro (l. 182) and §3.5.1 "From Behavior Cloning to Online Distillation" (l. 186)

| Thesis (line, quote) | NUTS | forgeUltra | Deployment | Verdict / rewrite |
|---|---|---|---|---|
| 182 "teacher … acts on privileged simulator state … student replaces it with one visuomotor policy … without a phase switch or separate networks" | l. 64–66, 225–236 | Single `ConditionalJointFlowPolicy` (`conditional_flow_matching.py:330–643`); phase enters only as an additive one-hot embedding (l. 385–395, 535) | `flow_policy.py:507–525` loads exactly one network | CONSISTENT |
| 186 "demonstrations themselves contain recoveries, because the closed-loop teacher was disturbed by impulses" | l. 283–286 "30 random arm impulses to each demonstration" | HANDOVER.md:185–187 (30 impulses per episode, one per policy/waypoint/return segment); 09-10 dataset | n/a | CONSISTENT |
| 186 "student predicts action chunks and executes a temporal ensemble of overlapping chunks" | not in NUTS (NUTS never mentions the temporal ensemble; only "prediction horizon of eight", l. 314–315) | `FlowActionChunkEnsembler` `conditional_flow_matching.py:244–301`; used in `evaluate_flow.py:349–352, 481, 1171–1207` | `flow_policy.py:410–438, 501–505, 583` | CONSISTENT (omitted in NUTS) |
| 186 "the same flow-matching student can be trained online with the hybrid teacher labeling the states that the student visits" | not in NUTS | Online trainer exists (`ablation_online_dagger_flow_matching/`), but default agent uses `two_channel_rgbd_encoder` + `conditional_flow_matching_native_osc` (no phase conditioning, native action labels) – `dagger_flow_matching_agent.yaml:1–8, 43–55` | n/a | PARTIAL. Rewrite: "a flow-matching head with the same architecture and hyperparameters can be trained online …; the registered online recipe differs in its vision encoder, action representation, and phase conditioning (Section 3.5.5)." |
| 186 "its comparison with the offline variant in Chapter 4 is pending" | n/a | `TODO_draft.md:43` "no successful rollout exists" | n/a | CONSISTENT |
| 186 "the ten-cycle dataset is rendered once under visual randomization and reused unchanged by the full method and ablations (b) to (d)" | l. 335–337 "matched training and evaluation budgets"; but (a)–(d) were trained on the real-world-augmented dataset (l. 340, 348–349) | HANDOVER.md:175–189 (visual DR enabled in the 09-10 dataset). No (b)–(d) retrain on the sim-only dataset is documented; `TODO_draft.md:19` lists it as outstanding | n/a | UNVERIFIED (forward-looking; author aware) |
| 186 "the offline flow student sustained ten cycles (Chapter 4)" | Table I (e) sim 10.0 ± 0.0 (l. 318) | HANDOVER.md:219–226: one seed-0 closed-loop replay, 10/10 cycles, 1,072 ticks / 71.75 s | n/a | CONSISTENT (ten-trial stats confirmed per author) |
| 186 "Online DAgger serves as a comparison in simulation" | n/a | trainer exists; no result | n/a | CONSISTENT as intent |

### 1.2 §3.5.2 Flow matching (l. 190–220)

| Thesis | NUTS | forgeUltra | Deployment | Verdict / rewrite |
|---|---|---|---|---|
| 190 p₀ = N(0, I), p₁ = q; vector field, flow, push-forward | l. 268–270 "transports Gaussian noise to the conditional action distribution" | Source `x_0 = torch.randn_like(x_1)` (`train_offline.py:811`), target `x_1` = action chunk (l. 808) | same solver (`DEP/flow_matching.py:34–75`) | CONSISTENT |
| 191–200 eq:fm, eq:marginal-field, eq:cfm; "same gradient … differ by a constant" | not in NUTS (cites Lipman) | not implemented (theory); code trains the conditional objective | n/a | CONSISTENT (standard Lipman et al. 2023 result; λ ~ U[0,1] matches `torch.rand`, l. 812) |
| 201–205 "Gaussian with mean λx¹ and std 1−λ"; eq:interpolant x^λ = (1−λ)x⁰ + λx¹; conditional field x¹ − x⁰ | l. 262–266 "U^λ_t = (1−λ)U⁰_t + λU^D_t, U̇^λ_t = U^D_t − U⁰_t" | `FU/flow_matching/flow_matching/path/affine.py:89–90` `x_t = sigma_t*x_0 + alpha_t*x_1`, `dx_t = d_sigma_t*x_0 + d_alpha_t*x_1`; `scheduler.py:104–113` CondOT α_t = t, σ_t = 1−t; path built by `local_flow_matching.py:34–40` (`CondOTProbPath`) | n/a | CONSISTENT (same convention: x_0 noise, x_1 data, target x_1 − x_0) |
| 205 "straight conditional paths … few integration steps suffice" | implied | n/a | n/a | CONSISTENT (standard) |
| 208 observation y_t = (O^RGBD, s_t, p_t, e^m_t) | l. 229–235 identical | `encode_condition(head_rgb, head_depth, proprio, trajectory_progress, cyclic_process_phase)` `conditional_flow_matching.py:416–435` | `flow_policy.py:547–583` same inputs | CONSISTENT |
| 208 target U^D_t ∈ R^{H×9} | l. 256–258 | `x_1 = batch[action_key].flatten(1)` with `joint_dim=9`, `action_horizon=8` (`train_offline.py:808`; `control_domains.py:19,37`) | `flow_config.json` joint_dim 9, horizon 8 | CONSISTENT |
| 209–214 eq:student-objective (squared ℓ₂ norm over the chunk), expectation over (y, U^D) ~ D, U⁰ ~ N, λ ~ U[0,1] | eq. (7), l. 259–268 identical | `flow_loss = F.mse_loss(prediction, sample.dx_t)` (`train_offline.py:854`) = squared norm divided by H·9 = 72 (constant factor, same minimizer); λ `torch.rand` (l. 812) | n/a | CONSISTENT (note: code reports the per-element mean; if the thesis ever quotes "flow MSE 0.0077" from HANDOVER it is the per-element mean, not ‖·‖²) |
| 214–217 eq:euler, explicit Euler, uniform grid λ_n = n/N | l. 314–315 "16 ODE integration steps" (solver type not named) | `local_flow_matching.py:72–79` `ODESolver(...).sample(step_size=1/steps, method="euler", time_grid=[0,1])` via torchdiffeq fixed grid | `DEP/flow_matching.py:68–75` identical | CONSISTENT |
| 218 "N = 16 at deployment" | l. 314–315 | `offline_flow_matching_dp3_agent.yaml` `sampling.integration_steps: 16`; `sample(steps=16)` default (l. 610); HANDOVER.md:221–222 | **CUDA → 16, CPU → 2** (`flow_policy.py:454–462`; `run_policy_rollout.py:65–70, 284–290`); `DEP/README.md:73–79` workcell PC is CPU-only; hardware run of 2026-10-16 used CUDA/16 (gap doc l. 266) | PARTIAL. Rewrite: "with N = 16, the value the student was trained and evaluated with; the ROS 2 runner keeps N = 16 on a GPU host and falls back to N = 2 on the CPU-only workcell PC so that the 15 Hz period is met." |
| 218 "condition c_t is computed once per chunk … N velocity evaluations cost only the Transformer" | n/a | `sample()` encodes condition once (l. 618–626) and `CachedConditionVelocity` reuses it (`local_flow_matching.py:65–70`) | same (`DEP/flow_matching.py:56–66`) | CONSISTENT |
| 220 regression head converges to conditional mean; flow head multimodal | l. 61–67, 104–112 (motivation) | n/a | n/a | CONSISTENT (standard) |
| 220 "trains with a plain regression target without a noise schedule, and samples in sixteen steps" | l. 314–315 | no schedule beyond CondOT α/σ (`scheduler.py:104–113`); 16 steps default | 16 on GPU / 2 on CPU | CONSISTENT / see H2 |
| 220 "a zero-noise sample at the source mean is available as a diagnostic" | n/a | `sample(noise=…)` (l. 628–636); `evaluate_teacher_offline.py:513` "Gaussian flow noise or a zero-noise diagnostic"; `tests/test_flow_policy.py:361` | not exposed (seeded Gaussian only, `flow_policy.py:503, 580`) | CONSISTENT |

### 1.3 §3.5.3 Student architecture (l. 224–252)

**Figure caption (l. 228)**

| Thesis | NUTS | forgeUltra | Deployment | Verdict |
|---|---|---|---|---|
| 228 RGB-D → point cloud → 64-D; 29-D proprio MLP; concat visual first; linear → 256-D; progress and phase embeddings added; non-causal Transformer over eight action tokens + condition token + sinusoidal time; aux head regresses nut position from visual feature | l. 237–252 (64-D, 128–128 MLP, "320-D" condition, 4-layer non-causal Transformer, sinusoidal flow-time) | all as stated: `dextrah_concat.py:33`, `conditional_flow_matching.py:345–354, 376–395, 508, 535, 195–241, 355–363` | 10-13 checkpoint has **no aux head** and 26-D proprio (`flow_config.json`) | CONSISTENT with code/09-10; MISMATCH with deployed 10-13 student (H1); NUTS 320-D (H4) |

**Observation encoding and late fusion (l. 234)**

| Thesis | NUTS | forgeUltra | Deployment | Verdict / rewrite |
|---|---|---|---|---|
| "Following DextrAH-RGB, … fused by concatenation, visual feature before encoded proprioception" | l. 252–254 DEXTRAH-RGB cited for augmentation; fusion order not stated | `dextrah_concat.py:23–33` `torch.cat((visual, proprio))`, comment l. 156–158 | same class vendored (`flow_policy.py` imports) | CONSISTENT |
| "29-D proprioception: ten controlled joint positions, ten joint velocities, previous filtered 9-D action" | not in NUTS | `observations/student.py:28` `NATIVE_OSC_PROPRIO_DIM = 29`, l. 117 "[q10, qdot10, previous_command]", l. 164; HANDOVER.md:682 | `flow_policy.py:514–523` reads dim from checkpoint; **10-13 checkpoint: 26-D** (`flow_config.json`); gap doc l. 20–23, 155–162 | CONSISTENT for 09-10; MISMATCH for deployed student. Rewrite (if the 10-13 student is the reported one): "the 26-D proprioception, consisting of the ten joint positions, the seven arm joint velocities, and the previous filtered 9-D action". |
| "128–128 MLP with ELU" | l. 244–245 "128–128 ELU MLP" | `FlowPolicyConfig.proprio_hidden_dims=(128,128)`, `fusion_activation="elu"` (l. 40–41); yaml `hidden_dims: [128,128], activation: elu` | same config | CONSISTENT |
| "concatenation of 64-D visual and 128-D proprio feature projected by a linear layer with ELU to the 256-D condition" | l. 246–247 says **320-D** | `self.condition = Sequential(Linear(192, 256), ELU())` (l. 352–354); `condition_dim=256` (l. 37, yaml) | `flow_config.json` condition_dim 256 | CONSISTENT with code; MISMATCH with NUTS III.E (320); NUTS Fig. 2 says 256 |
| "privileged ablations … nut position (3-D) or nut position with canonical axis-angle orientation (6-D) appended to the proprioception" | not in NUTS | `offline_flow_matching_dp3_agent.yaml` variants `nut_pose_3d` (`privileged_pose: xyz`, vector_dim 40) and `nut_pose_6d` (`xyz_axis_angle`, from `quaternion_wxyz`, 43); `student.py:35–40` object feature dims 3/6 | n/a | CONSISTENT ("canonical" axis-angle not verified in code; UNVERIFIED wording) |
| "ablation that removes the hand velocities: the three pinch-joint velocities are dropped, proprioception becomes 26-D" | not in NUTS | `student.py:30–34, 106–107, 127–136` (drops q̇[7:10]); `ablation_offline_flow_matching/README.md:189–190, 245` | **This is the deployed configuration** (`flow_config.json`, gap doc l. 155–162) | CONSISTENT as a description; see H1 for framing ("ablation" vs deployed) |

**Vision encoder (l. 237)**

| Thesis | NUTS | forgeUltra | Deployment | Verdict / rewrite |
|---|---|---|---|---|
| "follows DP3" | l. 237–243 | `rgb_pointcloud_dp3_encoder.py:1–19`, yaml `reference.method: DP3 RSS 2024` | `flow_policy.py:520–521` requires `rgb_pointcloud_dp3_encoder` | CONSISTENT |
| "back-projected through calibrated intrinsics; reject non-finite depth, depth outside [0.10, 2.0] m, or outside a fixed crop box covering the workspace with 40 mm margin" | not in NUTS | l. 138–150; yaml `depth_min_m 0.10, depth_max_m 2.0, crop_min/max`, comment "expanded by 40 mm for M24 geometry"; HANDOVER.md:156–160 | `flow_config.json` same values | CONSISTENT |
| "centered and scaled by fixed workspace constants; color normalized to [−1, 1]" | n/a | l. 152 `(xyz − center)/scale`; l. 153–156 `colour*2−1` | same | CONSISTENT |
| "4096 sampled, randomly during training, fixed priority at evaluation" | n/a | l. 160–172 (`torch.rand` in training, golden-ratio `evaluation_priority` l. 93–97 otherwise); yaml `num_points: 4096` | same | CONSISTENT |
| "encoder pretraining fails fast if fewer than 128 valid points remain" | n/a | `vision_encoder_pretraining/train.py:153–155, 786–790`; HANDOVER.md:159–160 | n/a | CONSISTENT |
| "every frame of the retained dataset keeps more than 10,000 valid points" | n/a | HANDOVER.md:192–194 (10,542 min / 12,374 median / 15,366 max) for the 09-10 dataset | n/a | CONSISTENT for 09-10 dataset; UNVERIFIED for the 10-13 dataset |
| "PointNet 64, 128, 256, layer normalization, ReLU, global max pooling, ELU projection → 64-D" | l. 241–243 "64–128–256 pointwise layers and global max pooling … 64-D" | l. 99–123 (Linear–LayerNorm–ReLU ×3; output head LayerNorm–Linear–ELU); masked max-pool l. 200–205 | same | CONSISTENT (omits the LayerNorm before the projection and the validity masking of the max-pool) |
| "about 60,000 parameters and no pretrained backbone" | n/a | HANDOVER.md:203 "59,648 transferred encoder parameters"; yaml `transfer.note` "no generic pretrained checkpoint" | n/a | CONSISTENT |
| "initializes it from a pose-regression pretraining on rendered sweeps of a free-moving nut" | n/a | HANDOVER.md:156–172, 199–203 (robot-free M24 sweep, 32,000 frames, `best.pt` step 1000, position error 5.87 mm, hex-aware rotation 46.19°; encoder kept trainable) | `checkpoints/README.md` provenance section (same) for the 09-10 student; **unknown for the 10-13 student** (its `flow_config.json` carries no `vision_initialization`; the `checkpoint.pt` payload was not opened) | CONSISTENT for 09-10; UNVERIFIED for deployed |
| "image-space encoder: ImageNet-pretrained ResNet-18 stage-2 trunk on concat of RGB, log depth, validity mask; embedding of calibrated camera-frame XYZ pooled on 6×10 token grid; one spatial self-attention layer; learned-query pooling; ablation (b)" | l. 343–347 "(b) one-branch ImageNet-pretrained ResNet-18 stage-2 encoder that fuses RGB, log depth, validity, and calibrated XYZ geometry into a 64-D feature" | `one_channel_rgbd_encoder.py:14–30` (`resnet_stage="stage2"`, `token_grid=(6,10)`, `geometry_embedding = Linear(4→64)…` l. 82–85 on (x, y, z, valid-fraction) l. 139–161; one encoder layer l. 88; `control_query` pooling l. 96–100); yaml `one_channel_rgbd_encoder.yaml` | n/a | CONSISTENT (minor: the geometry embedding also takes the per-token valid fraction as a 4th channel) |
| "Adapt3R-style: frozen ResNet-18 layer-1 backbone, 512 points localized through depth, expressed in the live grasp frame, learned-query attention pooling" | not in NUTS | `adapt3r_head_encoder.py:73–83` (`layer1`, `requires_grad_(False)`), `num_points=512` (l. 37), transform `eef_from_head_camera` → **end-effector frame** (l. 15–19, 162–164), `MultiheadAttention` with 4 learned queries (l. 104–105; yaml `num_queries: 4, heads: 4`) | n/a | CONSISTENT; wording PARTIAL: code says "live end-effector frame" (`eef_from_head_camera`), thesis says "live grasp frame" – fine only if §3.3 defines the grasp frame as the end-effector frame |
| "All encoders consume the same 320×180 RGB-D pair" | l. 283–287 (RGB-D → point cloud at 15 Hz) | all vision yamls `image_shape: [180, 320]`; HANDOVER.md:153–155 | `checkpoints/README.md` "320x180 input" | CONSISTENT |

**Conditioning on progress and phase (l. 240)**

| Thesis | NUTS | forgeUltra | Deployment | Verdict / rewrite |
|---|---|---|---|---|
| "separate learned embeddings, 1–256–256 / 3–256–256 MLP with ELU, added to the 256-D condition" | l. 229–235 (progress and phase in y_t; no architecture) | `progress_condition = Linear(1,256)–ELU–Linear(256,256)` (l. 376–384); phase `Linear(3,256)–ELU–Linear(256,256)` (l. 385–395); additive l. 508, 535 | same class | CONSISTENT |
| "progress p_t maps the first timestamp of each demonstration to 0 and the last to 1" | l. 219–221 "normalized task progress" | `dataset.py:319–345` (`elapsed/duration`, endpoints forced to 0 and 1); trainer help l. 248–250 | n/a | CONSISTENT |
| "at deployment it advances with elapsed time from the start of the trial, normalized by the median demonstration duration stored in the checkpoint, clamped to 1" | not in NUTS | median: `dataset.py:346–348`; clock: `progress.py:65–100` (`min(max(progress,0),1)`, sim time from `prime_before_reset`) | `hardware.py:1875–1879` `progress = min(1.0, (tick_started − start)/runner.config.trajectory_progress_duration_s)`; duration 64.6 s (09-10) vs **46.6 s** (10-13) | CONSISTENT (value differs by checkpoint, H1) |
| "not a teacher-stage selector, not periodic, no cycle index" | n/a | by construction (scalar clock) | same | CONSISTENT |
| "three-way one-hot over the policy-controlled phases, the release waypoints, and the return" | l. 233–235 says one-hot over m_t ∈ M from eq. (1) (six phases) | `dataset.py:42–48` `CYCLIC_PROCESS_PHASE_FEATURES = ("policy","follow_waypoints","return_to_reset")`; mapping l. 145–174; trainer help l. 253–262 | `hardware.py:822` `PHASE_INDEX = {"policy":0, "follow_waypoints":1, "return_to_reset":2}`; `observation.py:95` | CONSISTENT with code and deployment; MISMATCH with NUTS (known; TODO l. 241) |
| "during training derived from recorded phase labels" | l. 219–222 | `dataset.py:305–317` from `replay_phase` | n/a | CONSISTENT |
| "during evaluation published by the cyclic coordinator from physical events" | n/a | `evaluate_flow.py:414–421` → `full_task.py:131–157` (from `cyclic_handover.active`/`phase_index`) | `hardware.py` `coordinator.process_phase()` (l. 1874); release gate on turn ≥ 55° via `grasp_yaw_proxy` on hardware (gap doc l. 258–264), return on convergence gates (l. 56–59) | CONSISTENT. Deployment caveat worth a sentence: on hardware there is no nut-angle sensor; the release event is inferred from a grasp-yaw proxy that has fired spuriously (gap doc l. 260–264). |
| "does not switch networks or action contracts; the student predicts the transition actions itself" | l. 62–66 | one network; unified 9-D label for policy and transitions (`unified_osc_action.py:1–18`) | same | CONSISTENT |

**Velocity network (l. 244)**

| Thesis | NUTS | forgeUltra | Deployment | Verdict / rewrite |
|---|---|---|---|---|
| "H = 8 action tokens of dim 9, each embedded linearly into 512-D; condition token; time token with 64-D sinusoidal encoding" | l. 247–251 | `_TrajectoryTransformer` l. 202–204 (`action_input`, `condition_input`, `time_input`), `_TimeEmbedding(64)` l. 180–192 (note angle = λ·freq·1000, then Linear 64→512) | same class | CONSISTENT |
| "Learned positional embeddings mark the ten token positions; they encode only the offset of an action inside the chunk" | n/a | `token_position = zeros(1, H+2, 512)` l. 205–207, added to all tokens l. 240 | same | PARTIAL: the ten embeddings also mark the condition and time slots (10 = 2 + 8). Rewrite: "Learned positional embeddings mark the ten token slots (condition, time, and the eight chunk offsets); no absolute time enters through them." |
| "Four pre-norm Transformer encoder layers, eight heads, 2048-D GELU feed-forward, no dropout, full self-attention; linear output per action token → 9-D velocity" | l. 247–250 "four-layer non-causal Transformer (512-D, eight heads, 2048-D GELU MLP)" | l. 208–223 (`norm_first=True`, `activation="gelu"`, dropout 0.0, final `LayerNorm`, `velocity_output` on `encoded[:, 2:]`); config defaults l. 44–48; yaml | `flow_config.json` 4/8/2048/0.0 | CONSISTENT (omits final LayerNorm) |
| "exponential moving average of its parameters with decay 0.999; inference uses the averaged weights" | Alg. 1 l. 8 (EMA α unspecified) | `--ema-decay` default 0.999 (`train_offline.py:371–378`; yaml); `update_ema_model` l. 304–319; `prefer_ema` default (`evaluate_flow.py:85–89`, yaml); HANDOVER.md:197–199, 212, 222 | `flow_policy.py:491–497` loads `ema_model` unless `--raw-weights` | CONSISTENT |
| "auxiliary head 64–128–3 MLP on visual feature, normalized coordinates, unit weight; discarded at deployment" | not in NUTS | `nut_position_head = Linear(64,128)–ELU–Linear(128,3)` l. 355–363; loss weight default 1.0 (`train_offline.py:364–368`); normalized target l. 826–835; HANDOVER.md:199, 204 (final aux error 0.083 mm) | 09-10 checkpoint: present, unused; **10-13 checkpoint: `vision_nut_position_head: False` (never trained)** | CONSISTENT for 09-10; MISMATCH for deployed (H1) |
| "AdamW, lr 1e-4, gradient-norm clipping 1.0, batches of 64 windows, 300 epochs" | l. 305–306 "300 epochs using eight-step action chunks" (optimizer not stated) | `torch.optim.AdamW(model.parameters(), lr=1e-4)` l. 708 (weight decay = PyTorch default 0.01, not set); `clip_grad_norm_(…, 1.0)` l. 862–864; batch 64 (l. 314, yaml); epochs CLI (yaml default 100; run used 300: HANDOVER.md:197) | 10-13 run also "300 epochs, EMA" (gap doc l. 155–156) | CONSISTENT. Omission: AdamW weight decay 0.01 (default), no LR schedule, shuffle on, `drop_last=False`. |
| "DextrAH-style RGB augmentation … saturation/contrast/brightness [0.5, 1.5], hue [−0.15, 0.15], motion blur p = 0.1" | l. 252–255 (lighting/texture randomization; not the per-sample jitter) | `dextrah_rgb_augmentation.py:16–23` exactly these ranges; yaml `dextrah_rgb_augmentation: true`; applied l. 788–789 | n/a | CONSISTENT. Omission: colour jitter probability 1.0, blur kernels 9–17 px with alpha 0.7, depth never augmented. |

**Action chunking and execution (l. 247)**

| Thesis | NUTS | forgeUltra | Deployment | Verdict / rewrite |
|---|---|---|---|---|
| "H = 8 at 15 Hz → 0.53 s" | l. 283, 306, 314 | 8/15 = 0.533 s | `--rate 15.0` default (`run_policy_rollout.py:63`); README l. 92–93 | CONSISTENT |
| "Chunk targets begin at the sample paired with the observation (target offset zero) … recorder stores the pre-step state with the command acting on it" | n/a | `train_offline.py:435–440` (offset 0 for OSC), help l. 268–272; HANDOVER.md:197, 527–528, 674 | `checkpoints/README.md` | CONSISTENT |
| "replans at every control step; command is a temporal ensemble of all still-valid proposals with weights 0.5^k for age k; decay zero recovers first-action execution" | not in NUTS | `FlowActionChunkEnsembler` l. 244–301 (weight `decay**age`, `proposal[:, age]`, validity masks reset by `invalidate`); default 0.5 (l. 247; yaml `temporal_ensemble_decay: 0.5`); HANDOVER.md:222 | `flow_policy.py:410–438` (same weights; no validity mask since one robot), default 0.5 (l. 474); `step()` every tick l. 547–583 | CONSISTENT |
| "ensemble operates in action space and is distinct from the parameter-space EMA" | n/a | two different classes (l. 244 vs 304) | same | CONSISTENT |
| "executed 9-D action is clipped to [−1, 1]" | n/a | online trainer clamps (`online_dagger_flow_matching.py:351–352`); offline evaluator: no explicit clamp found in `evaluate_flow.py`; the unified codec **raises** on commands outside ±1 (`unified_osc_action.py:159–180`, `require_bounded=True`) – where the sim path clamps (adapter behind `head_rgbd_env.py:219`) was not traced | `session.py:55–56` `raw.clamp(−1, 1)` and counts clipped elements | CONSISTENT for deployment; UNVERIFIED for the simulation evaluator |
| "decoded to the filtered Cartesian target … controller path unchanged, whose action smoothing is inverted analytically so the controller receives exactly the predicted target" | n/a | `unified_osc_action.py:1–18` (docstring: `EMA(inverse_ema(native(target))) == native(target)`), `forge_raw_native_action_for_filtered_target` l. 82–90; `osc_transition.py:332–337` | `session.py:57–59`: for `unified`, `filtered = bounded * native_scale` is fed straight to `forge_osc.decode_action_target(filtered_action, …)` (l. 313–349); the ROS path has no EMA stage for the unified representation, so no inversion is needed (the native branch would apply α = 0.0625 / 0.1875, l. 60–62) | CONSISTENT in effect; mechanism differs. Rewrite: "… in simulation the recorder's action smoothing is inverted analytically so the controller receives exactly the predicted target; on the robot the scaled target is handed to the Cartesian controller directly." |
| "inference latency … on an RTX 5090 is \tbd" | l. 288–290 only training times | nothing measured | `apps/policy_rollout/README.md:83–99`: 16 steps 11.7/12.0 ms (RTX 3060 Laptop), 13.5 ms in compose; CPU 92/225 ms; gap doc l. 266–267: 21 ms steady max per tick on hardware (CUDA) | UNVERIFIED (no 5090 figure exists). Suggest quoting the measured RTX 3060 Laptop / i7-12700H numbers and the 2-step CPU fallback. |

**Normalization (l. 251)**

| Thesis | NUTS | forgeUltra | Deployment | Verdict |
|---|---|---|---|---|
| "9-D label is the filtered Cartesian target divided by a fixed scale per component, bounding scripted transitions to [−1, 1]; no action statistics learned" | n/a | `UNIFIED_OSC_ACTION_REPRESENTATION.native_action_scale = [3,4,16,3,3,3,2,2,2]`, clip 1 (`unified_osc_action.py:27–36`); `native_to_unified` divides and checks bounds (l. 137–157); docstring l. 1–18 | `session.py:57` multiplies back; `flow_config.json` same scale; `checkpoints/README.md` | CONSISTENT |
| "Proprioceptive inputs are consumed in physical units" (TODO l. 252) | n/a | `dextrah_concat.py:127` `proprio.float()` only; `dataset.py` computes no proprio statistics (only nut-position mean/std l. 402–405) | `observation.py` `build_native_osc_proprio` raw | CONSISTENT – the TODO at l. 252 can be closed. Caveat: the previous-action component is in bounded unified units, not physical units; q, q̇ are raw rad / rad·s⁻¹. |
| "nut position of the auxiliary head is standardized by dataset statistics stored in the checkpoint" | n/a | `dataset.py:402–405`; config `nut_position_mean/std` l. 56–57, 587–596; buffers l. 364–373 | 10-13: identity stats (no head) | CONSISTENT (09-10) |

### 1.4 §3.5.4 Offline training and Algorithm 1 (l. 256–271)

| Thesis | NUTS | forgeUltra | Deployment | Verdict / rewrite |
|---|---|---|---|---|
| 256 "windows of H consecutive commands built from each episode without crossing episode boundaries; EMA copy maintained" | Alg. 1 l. 208–227 | `dataset.py:458–493` (per-episode windows); EMA l. 703–706 | n/a | CONSISTENT |
| Alg. 1 l. 1 "Collect simulated rollouts with π_HT under random arm impulses and visual DR" | NUTS Alg. 1 adds human-corrected replays (title l. 208; l. 216–221) | HANDOVER.md:175–189 | n/a | CONSISTENT with code/sim-only framing; differs from NUTS (known) |
| Alg. 1 l. 2 "Form H-step chunks from D = D_sim, masking resets and padding terminal chunks" | l. 221–223 identical wording | windows never span episodes; invalid-command windows skipped (`dataset.py:473–477`); `--terminal-hold-padding` repeats the last command (l. 431–447, 486–493; for OSC the last command is copied verbatim, for PD arm velocity is zeroed); HANDOVER.md:197 | n/a | CONSISTENT |
| Alg. 1 l. 4–8 sample (y, U^D), U⁰ ~ N, λ ~ U; encode; gradient step on eq. + aux loss; EMA θ̄ ← αθ̄ + (1−α)θ | NUTS Alg. 1 l. 5–8 identical | `train_offline.py:808–867`; `update_ema_model` l. 317 | n/a | CONSISTENT |
| Alg. 1 "Until convergence" | NUTS Alg. 1 l. 9 same | fixed 300 epochs, best/last checkpoint by stochastic epoch loss (HANDOVER.md:203–205) | n/a | PARTIAL (wording; a fixed epoch budget is used) |
| Alg. 1 "Return v_θ̄" | NUTS l. 10 | `prefer_ema` | `ema_model` default | CONSISTENT |

### 1.5 §3.5.5 Online DAgger with a flow head (l. 276–293)

| Thesis | NUTS | forgeUltra | Deployment | Verdict / rewrite |
|---|---|---|---|---|
| 276 "mixture of teacher and student control with teacher probability β" | not in NUTS | `intervention.py:114–160` `mix_policy_actions`; `online_dagger_flow_matching.py:435–442` | n/a | CONSISTENT |
| 276 "the hybrid teacher labels every visited state with its 9-D command" | n/a | l. 365 `teacher_supervision.command`; supervision `deterministic_hybrid_native_osc_sequence` with `policy_output: normalized_native_teacher_action` (`dagger_flow_matching_agent.yaml:43–55`) – i.e. the **native** bounded action, not the unified filtered target | n/a | PARTIAL. Rewrite: "… labels every visited state with its 9-D command in the native action coordinates of the teacher's controller (not the unified filtered target of the offline student)". |
| 276 "collects eight consecutive live teacher commands, pairs the sequence with the observation at its first step, stride-one overlapping supervision; one chunk completes per step once full" | n/a | `utils/action_chunks.py:46–53, 111–160`; `teacher_supervision_stride: 1`, `action_horizon: 8` (yaml; `online_dagger_flow_matching.py:108–113`) | n/a | CONSISTENT |
| 276 "sequences that cross a reset or the scripted handover are discarded" | n/a | `action_chunks.py:49–51, 90–91` (`invalidate` on reset/handover) | n/a | CONSISTENT |
| 276 "Multi-step online supervision therefore fixes β = 1 during collection" | n/a | `online_dagger_flow_matching.py:219–226` raises unless start = end = 1.0; yaml `intervention: start 1.0, end 1.0, decay_steps 0` | n/a | CONSISTENT |
| 276 "RGB-D latent encoded once per step and detached before entering the pending windows" | n/a | l. 309–322 (`visual_features.detach()`); `encode_visual_features` (`conditional_flow_matching.py:437–451`) | n/a | CONSISTENT |
| 276 "vision encoder trained by the immediate nut-position auxiliary objective at lr 1e-5; delayed flow objective at lr 1e-4" | n/a | l. 176–203 (two AdamW param groups); yaml `learning_rate 1.0e-4`, `vision_encoder_learning_rate 1.0e-5`; aux weight **0.01** (yaml `vision_nut_position_loss_weight: 0.01`) | n/a | CONSISTENT. Omission: online aux weight is 0.01, not the offline 1.0; gradient clip 1.0; EMA 0.999; checkpoint selection on a 0.99-EMA of the flow loss after iteration 1000. |
| 276 "Student rollouts during online training sample with eight Euler steps" | n/a | `integration_steps` default 8 (l. 128; yaml); rollout uses the EMA model and clamps the first action (l. 346–352); no temporal ensemble online | n/a | CONSISTENT. Omission: online rollouts execute the first action only (no temporal ensemble) from the EMA weights. |
| Alg. 2 l. 2–7 | n/a | matches l. 356–470 | n/a | CONSISTENT (β is always 1 in the registered recipe, so line 4's branch never takes the student action) |
| 293 "With a one-step horizon the constraint on β disappears … recurrent baseline implements fixed β, linear decay β_start→β_end, SafeDAgger takeover 0.10 / release 0.075 RMSE with hysteresis" | l. 87–90 cites DAgger and SafeDAgger | `ablation_online_dagger_lstm/utils/intervention.py:24–86` (`BetaSchedule`, `beta` or `start/end/decay_steps`), l. 88–146 (`action_rmse_threshold=0.10`, `release_action_rmse_threshold=0.075`, hysteresis comment l. 92) | n/a | CONSISTENT. Omission: the registered LSTM agent defaults to β = 0 (student always drives; `dagger_lstm_agent.yaml` "intervention: beta: 0.0", DextrAH behaviour). |

### 1.6 §3.5.6 Baseline students (l. 297–299)

| Thesis | NUTS | forgeUltra | Deployment | Verdict / rewrite |
|---|---|---|---|---|
| 297 "Three deterministic students serve as baselines" | (a)–(d) l. 338–353: single-cycle, ResNet, LSTM, Transformer | code has BC MLP and LSTM; no Transformer regression | n/a | PARTIAL (see H3) |
| 297 "recurrent and Transformer baselines share the observation and action contracts of the flow student" | (c) "same real-world-augmented dataset", DP3 vision + LSTM; (d) DP3 vision + Transformer | LSTM OSC variant: same 9-D unified target/scale/clip (`dagger_lstm_agent.yaml:71–91`) but observation `proprio_rgbd_vision_teacher_action.yaml` (33-D incl. 4-D full-task phase) with `two_channel_rgbd_encoder`, trained online | n/a | PARTIAL (H6). Rewrite: "The recurrent baseline shares the 9-D action contract; its observation uses the same proprioception but the two-branch RGB-D encoder and a four-way task-stage code, and it is trained online rather than from D." |
| 297 BC: "eight-frame history of measured joint positions and velocities, predicts two future commands, 512–512–512 MLP with batch normalization, acts at the physics rate, follows a reference cursor" | not in NUTS | `bc_agent.yaml` (`observation_horizon 8`, `action_horizon 2`, 120 Hz, `observation_keys [joint_pos, joint_vel]`, 17-D PD command), `deterministic_mlp.yaml` (`hidden_dims [512,512,512]`, `batch_norm true`, relu), `deterministic_mlp.py:117–124`; `train_bc.py:372–436` (reference-indexed live rollout) | n/a | CONSISTENT (details omitted: 17-D joint-PD targets, ReLU, lr 3e-4, batch 256, weight decay 1e-5) |
| 297 LSTM: "512-unit layer-normalized LSTM followed by 512–512–256 ELU MLP and a Gaussian head, deterministic action regression on the teacher command, deterministic mean as rollout command" | l. 349–353 identical | `dextrah_lstm_state_dependent_sigma.yaml` (`rnn units 512, layer_norm true, before_mlp true`; `mlp [512,512,256] elu`; continuous Gaussian space) selected by the `osc` control domain (`dagger_lstm_agent.yaml:76`); `supervision.objective: unified_filtered_osc_target_mse`, `student_rollout: deterministic_gaussian_mean` (l. 77–83) | n/a | CONSISTENT. Note: the PD-domain default head `dextrah_lstm.yaml` is a 1024-unit LSTM with a [512,256,128] MLP; the thesis numbers hold for the OSC variant only. |
| 297 Transformer regression: "deterministic ACT variant without the variational objective: four layers, eight heads, 512-D, 2048-D FF, eight learned action queries predicting an eight-step chunk" | l. 338–343 exactly this | **not found** (H3) | n/a | UNVERIFIED in code |
| 299 "last two baselines isolate the contribution of the generative head from chunking and backbone" | l. 328–333 (Q3) | n/a | n/a | CONSISTENT as design intent |

### 1.7 Appendix Table `tab:flow` (appendix.tex 75–101) and notation.tex

| Row | Source check | Verdict |
|---|---|---|
| action contract 9-D filtered Cartesian target, fixed scale, [−1, 1] | `unified_osc_action.py:27–36` | CONSISTENT |
| H = 8 (0.53 s at 15 Hz); target offset 0; terminal-hold padding yes | HANDOVER.md:197 | CONSISTENT (09-10); 10-13 padding/offset not documented → UNVERIFIED |
| proprioception 29-D | 09-10 yes; **deployed 10-13 is 26-D** | PARTIAL (H1) |
| proprio MLP 128–128 ELU; visual 64-D (4096 pts, 64–128–256, max pool); condition 256; embeddings 1–256–256 / 3–256–256; time 64-D sinusoidal; Transformer 4/8/512/2048 GELU pre-norm; CondOT path | code as cited above | CONSISTENT |
| AdamW 1e-4, clip 1.0, batch 64, 300 epochs; EMA 0.999 | `train_offline.py:708, 862–867`; HANDOVER.md:197 | CONSISTENT (weight decay 0.01 default omitted) |
| auxiliary loss weight 1.0 | 09-10 yes; **10-13 has no aux head** | PARTIAL (H1) |
| RGB augmentation ranges | `dextrah_rgb_augmentation.py:16–23` | CONSISTENT |
| sampler Euler N = 16 (online 8) | yaml; **deployment CPU default 2** | PARTIAL (H2) |
| temporal-ensemble decay 0.5 | yaml; `flow_policy.py:474` | CONSISTENT |
| notation.tex:37 `c_t ∈ R^256` | code 256; NUTS III.E 320 | CONSISTENT with code; MISMATCH NUTS |
| notation.tex:46 `D_sim, D` | NUTS `D = D_sim ∪ D_real` | known deviation |

---

## 2. Facts in code/NUTS that the thesis omits but a reader needs

1. **Which checkpoint was deployed** (H1): the ROS 2 runner's default is the 10-13 student (26-D proprioception, no auxiliary head, 46.6 s nominal duration, different dataset). If the thesis reports hardware results from October 2026 hardware runs, §3.5 must describe that student or state that the hardware student is the "no hand-velocity" variant retrained on the 10-13 dataset.
2. **CPU 2-step shortcut** (H2): `flow_policy.py:454–462`, `DEP/README.md:73–79`, `apps/policy_rollout/README.md:56–67, 83–99`; a seeded CUDA run does not reproduce a seeded CPU run (README l. 66–68).
3. **Measured latencies** (H7) instead of `\tbd`.
4. **AdamW weight decay 0.01** (PyTorch default, `train_offline.py:708`), no learning-rate schedule, `drop_last=False`.
5. **Final LayerNorm** after the Transformer encoder (`conditional_flow_matching.py:221`) and the **×1000 scaling** inside the sinusoidal time embedding (l. 191).
6. **Max-pool masking**: invalid points are masked out of the max-pool and an all-invalid frame yields a zero feature (`rgb_pointcloud_dp3_encoder.py:200–205`); evaluation sampling uses a golden-ratio stride priority (l. 93–97).
7. **Augmentation details**: colour jitter probability 1.0, motion-blur kernels 9–17 px with alpha 0.7, depth never augmented (`dextrah_rgb_augmentation.py:16–23`; trainer help l. 190–192).
8. **EMA weights loaded by default** at evaluation and deployment, raw weights behind a flag (`evaluate_flow.py:85–89`; `flow_policy.py:491–497`).
9. **Deployment contract assertions**: the runner refuses any checkpoint that is not 9-D OSC + vision + DP3 (`flow_policy.py:507–525`); the action is clamped and the number of clipped elements logged (`session.py:55–56`).
10. **Progress/phase input validation**: progress must lie in [0, 1] and the phase vector must be exactly one-hot or the model raises (`conditional_flow_matching.py:504–535`).
11. **Terminal-hold padding semantics** for OSC vs PD (`dataset.py:431–447`).
12. **Online recipe specifics**: no temporal ensemble, EMA weights for rollouts, first action clamped, aux weight 0.01, checkpoint selection by flow-loss EMA (0.99) after iteration 1000, native (not unified) action labels, two-channel encoder, no phase conditioning.
13. **LSTM agent default β = 0** and the SafeDAgger mode as an alternative (`dagger_lstm_agent.yaml`, `intervention.py:12–13`).
14. **Hardware phase source**: release detected from a grasp-yaw proxy (no nut-angle topic), which has produced false release events (gap doc l. 258–264); relevant to the sentence "published by the cyclic coordinator from physical events".
15. **Progress clock origin**: in simulation anchored before reset settling (`progress.py:80–84`); on hardware from the trial start tick (`hardware.py:1875–1879`).
16. **NUTS also states** (l. 288–290) student training takes ≈30 min on one RTX 5090 and (l. 252–255) that DEXTRAH-style lighting/texture randomization is applied during distillation; the thesis places the latter in the data-collection section, which matches the code (`README.md` "Distillation visual randomization": DR is applied during collection/online training, the offline trainer only adds per-sample RGB jitter).

---

## 3. Items the thesis can close or must keep open

- `% TODO(unsure)` l. 252 (proprio standardization): **close** – no standardization exists (`dextrah_concat.py:127`; `dataset.py`).
- `% TODO(unsure)` l. 241 (six-phase vs three-way): keep the note; code and deployment are three-way (`dataset.py:42–48`, `hardware.py:822`); NUTS says six-way.
- `% TODO(unsure)` l. 298 (ACT baseline): **confirmed absent** from forgeUltra; either remove the baseline from §3.5.6 or source it from the paper repository (`~/code/icra_2027`, not audited here).
- `% TODO(results)` l. 248 (latency): no RTX 5090 measurement exists; RTX 3060 Laptop and CPU numbers exist (H7).
- New: decide whether the thesis's "retained student" is the 09-10 (29-D, aux head) or the 10-13 (26-D, no aux head) student; §3.5.3, Table `tab:flow`, Table `tab:datasets`, and any hardware chapter must agree (H1).
