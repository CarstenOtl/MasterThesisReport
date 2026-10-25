# Chapter 3 cross-reference: thesis vs NUTS vs forgeUltra vs ROS 2 deployment

Audit date: 2026-10-23. Five read-only agents checked every factual claim in
`source/chapter03.tex` against `additional/NUTS.md`, `~/code/forgeUltra/`, and
`~/code/inspirehand-franka-ros2-ws-/`. Detailed claim-by-claim tables with
file:line evidence are in the sibling files:

| File | Thesis slice |
| --- | --- |
| `xref_A_system.md` | §3.1 Problem Formulation, §3.2 Platform / Thread Model / Action Contract (ch03:1–81) |
| `xref_B_teacher.md` | §3.3 Privileged Teacher Training (ch03:82–127), appendix tab:teacher-obs, tab:ppo |
| `xref_C_hybrid.md` | §3.4 Hybrid Teacher, Disturbances, Sim-to-Real, Dataset (ch03:128–179), tab:datasets |
| `xref_D_student.md` | §3.5 Student Distillation, Flow Matching, Online DAgger, Baselines (ch03:180–300), tab:flow |
| `xref_E_eval_deploy.md` | §3.6 Evaluation Protocol (ch03:301–320) + deployment-side audit of all of ch03 |

Known author decisions were respected and are not re-flagged: the paper's
teacher description is kept although the Sep-10 dataset checkpoint lacks some
features; ten-trial statistics stand. The four most consequential findings
below were re-verified by hand in the code after the agents reported.

## A. Hard mismatches (text says something the code contradicts)

| # | Where | Thesis says | Sources say | Fix |
| --- | --- | --- | --- | --- |
| A1 | ch03:72 | Grasp frame is "a fixed offset from the flange" with origin at the pad midpoint | FR3 env: origin is the **live** thumb/index fingertip midpoint, x = current thumb→index, z = reset approach direction stored in flange coords and transported (`forge_franka_env.py:1059–1086`, `grasp_frame.py:53–80`). Deployment uses the same live frame via `PolicyGoal.tool_in_flange`. The flange-fixed frame is the obsolete KUKA path. | Rewrite as a live fingertip-midpoint frame whose approach axis is fixed at reset and carried with the flange. |
| A2 | ch03:96 | `R^target` pays 250 "over a five-step hold within 5° of the target" | Code: paid over the first five steps once directional progress ≥ 55° with grasped_once ∧ proper_grip; one-sided, "any farther overshoot remains legal" (`forge_franka_env.py:1379` v1, v2 `:1595`; `vanilla_threading.yaml:123`). The ±5° window in NUTS is the paper's description of the release gate, not the reward. | "…over the first five steps in which at least 55° of clockwise rotation is held with a live proper grasp; overshoot is not penalized." |
| A3 | ch03:234, 244, 251; tab:flow; fig caption | 29-D proprioception, auxiliary nut-position head with unit weight, 64.6 s clock, Sep-10 dataset = "the student" | The deployment runner's default checkpoint (`run_policy_rollout.py:20–24`) is `m24-dr-disturbed-dp3-no-finger-velocity-seed0-20261013-135143-648368`: `proprio_dim 26`, `hand_velocity_observation omitted`, `vision_nut_position_head False`, `trajectory_progress_duration_s 46.6`, trained on dataset `…20261013-132348`. This is also the only CUDA hardware run (2026-10-16). forgeUltra HANDOVER/todo do not document this run. | Decide which student is "the" student. If the 10-13 one: rewrite §3.5.3, tab:flow, tab:datasets, and ch05 accordingly (26-D, no aux head, new dataset id/frame count). If the 09-10 one: ch05 must say the hardware trials used a different checkpoint, or the hardware trials must be rerun. |
| A4 | ch03:218, 220; tab:flow | "N = 16 at deployment", "samples in sixteen steps" | `flow_policy.py:454–462`: 16 on CUDA, **2 on CPU**; workcell PC has no GPU (`README.md:61–79`). The 2026-10-16 hardware run used CUDA/16. Offline first-action MAE 0.0072 (2 steps) vs 0.0052 (16). | State the GPU/CPU rule and which applied to the reported trials. |

## B. Partials: true in simulation or for one source, not for all

| # | Where | Issue | Fix |
| --- | --- | --- | --- |
| B1 | ch03:147, 240 | Phase "derived from the same physical events" at deployment. Hardware has no nut-angle sensor; the release event is a grasp-frame **yaw proxy** (guarded by fingertip-separation and step vetoes since 2026-10-18; fired spuriously in earlier runs). Return gate is physical as in sim. | Qualify: release from grasp-frame yaw proxy on hardware; return validated as in sim. |
| B2 | ch03:96 | `P^force` "excess wrist force": code penalizes summed thumb+index pad contact force on the nut above a per-episode threshold U(5,10) N; no wrist sensor. NUTS uses the same loose wording. | "excess fingertip contact force on the nut". |
| B3 | ch03:96 | Grasp latch "five consecutive steps": 5 in V1 configs, **10 in every V2 config** (the configs that have the table penalties and grip-loss termination described in the same paragraph). No single config has 5 + grip-loss termination. | Author decision: pick V2 recipe (10) or state both. |
| B4 | ch03:74, tab:dr | Dead zone "below which wrench components are zeroed": applied threshold is U(0,1)·[5,5,5,1,1,1] resampled at reset and every 2 s; above threshold the component is reduced by it; **absent on hardware and in nominal replay**. | Describe as randomized training perturbation, absent in replay and on the robot. |
| B5 | ch03:72 | EMA factor "sampled per episode from [0.025,0.1]": fixed at midpoint 0.0625 (fingers 0.1875) when DR is off, i.e. for demonstration collection, evaluation, and on the robot. | Add the fixed-value clause. |
| B6 | ch03:72 | Clip "0.02 m and 0.097 rad per step": component-wise per axis / Euler angle at every 120 Hz substep; 1 kHz on the robot against measured grasp pose. | Say component-wise, per physics substep / 1 kHz. |
| B7 | ch03:174 | "the behavior that the demonstrations record is robust to controller and calibration deviations": demonstrations were collected with task DR **disabled** (nominal gains, EMA 0.0625, no dead zone, zero observation noise). Only the teacher was trained under DR. | Rephrase: demos record a policy that was trained to succeed under those deviations; the recorded trajectories themselves are nominal. |
| B8 | ch03:169, 178 | "640×480 center-cropped to 640×360 and downscaled by two in both domains": only the physical stream is cropped; the simulator renders directly at 320×180 with the scaled crop intrinsics. | Rewrite as one shared intrinsic model reached by different paths. |
| B9 | ch03:45 | "Isaac Lab 2.3": repo README/docs/all experiment notes say **2.3.2**; NUTS says 2.2.1 (archived code). | Write 2.3.2; drop the TODO. |
| B10 | ch03:49 | "observation contracts … identical for both robots": FR3 teacher has FR3-specific normalized joint-torque channels. | "task code, rewards, training recipe shared; robot asset, workcell profile, reset poses, and robot-specific proprioceptive channels differ". |
| B11 | ch03:43 | "remaining fingers hold a curled posture": 1.10 rad in sim, fully closed (1.333 rad) on hardware. | State both. |
| B12 | ch03:186, 276 | "the same flow-matching student can be trained online": the registered online agent uses the two-channel RGB-D encoder (not DP3), native action labels (not the unified filtered target), no phase conditioning, aux weight 0.01. | "a flow head with the same architecture"; note the recipe differences. |
| B13 | ch03:297 | "recurrent and Transformer baselines share the observation and action contracts": LSTM shares the 9-D action contract but uses the two-channel encoder, a 4-way full-task phase code, and is trained online (default β = 0), not offline on D. | Rewrite the LSTM description. |
| B14 | ch03:297–298 | ACT-style Transformer regression baseline: **does not exist in forgeUltra** (only `conditional_flow_matching`, `deterministic_mlp`, `dextrah_concat`, `dextrah_recurrent` heads). Only NUTS describes it. Confirms existing TODO. | Remove, or source from the paper repo. |
| B15 | ch03:314 | Offline teacher-fit reports "target saturation": no saturation metric exists in `evaluate_teacher_offline.py`; it exists only in the deployment recorded-rollout evaluator. | Drop from the offline-fit list. |
| B16 | ch03:305 vs ch04 | Ladder promises three rungs; ch04 `tab:ladder-results` reports offline fit and closed loop only, no teacher-forced-clock result. | Add a row or say the mode is a debugging step not reported. |
| B17 | ch03:318 | "completed cycle" never defined operationally: in code = release gate (≥55°) fired **and** return validated (5 mm/5°/0.15 rad within 16 s); a trial ends at first transition failure, early termination, or step budget (1500 ticks on hardware). Simulator summary reports target-minus-achieved (sign opposite to the thesis convention). | Add the definition; note the sign convention of the tooling. |
| B18 | ch03:318 | "on hardware [the nut angle] is read from an angular scale": no code trace; rollout software logs `threading_turn_progress_rad = NaN` on hardware. Not contradicted, but should be stated as a manual reading with its resolution. | State explicitly. |
| B19 | ch03:244 | "Learned positional embeddings mark the ten token positions; they encode only the offset of an action inside the chunk": the ten slots are condition + time + 8 actions. | Minor rewording. |
| B20 | appendix tab:teacher-obs | 39-D/69-D matches forgeUltra at commit `eaddc28` (2026-10-14); HEAD adds 7 normalized FR3 joint torques → 46/76. Fingertip-force channel also has per-episode gain U(0.8,1.2) and bias U(−1,1) N. | State the commit/config the table describes, or add the rows. |
| B21 | tab:dr | Yaw curriculum row applies to the single-size teacher only; multi-size configs set yaw delta 0 and no ADR. | Add "(single-size teacher)". |
| B22 | ch03:126 | Pickup reward summary omits reach bonuses, engagement bonus 350, alignment and goal-velocity penalties. | Extend the list or say "among others". |
| B23 | ch03:178 | "chunks that cross a physical reset are masked": no explicit mask; episode files contain no reset rows and windows never span episodes. | Reword. |
| B24 | ch03:237 | Colour "normalized to [−1,1]": forgeUltra DP3 encoder does `colour*2−1` (consistent); deployment `dp3.py:140` clamps to [0,1] before handing to the same vendored encoder class, so likely consistent end to end. Low priority; confirm once. | Check. |

## C. TODOs in chapter 3 that this audit can now resolve

| TODO | Resolution |
| --- | --- |
| ch03:46 Isaac Lab version | 2.3.2 (B9). |
| ch03:48 arm precision/repeatability claim | No measurement in either repo; drop the clause or add a number. |
| ch03:241 six-phase vs three-way one-hot | Code and deployment are three-way; NUTS says six-way. Keep text as is. |
| ch03:248 inference latency | No RTX 5090 figure exists. Measured: RTX 3060 Laptop 11.7 ms mean / 12.0 ms max per 16-step pass (vision ≈2 ms + ≈0.6 ms/step), 13.5 ms through compose; CPU i7-12700H 92/225 ms at 16 steps, 16/18 ms at 2 steps; hardware 2026-10-16 16–26 ms per tick incl. ROS, 0 missed deadlines in 360 steps (`apps/policy_rollout/README.md:79–99`, gap doc). |
| ch03:252 proprio standardization | Confirmed: none applied (`dextrah_concat.py:127`, `dataset.py` computes only nut-position stats). Close the TODO. |
| ch03:298 ACT baseline | Confirmed absent from forgeUltra (B14). |
| ch03:12 mainpipeline.pdf | Not checked (figure). |

## D. Facts the chapter omits that a reader of a methodology chapter needs

- Collection ran with task DR off and without PhysX enhanced determinism; the recorded trajectories use the nominal controller constants that the robot also uses (gains 565/28, nullspace 10/6.32, EMA 0.0625, no dead zone).
- Only the final return is physically gated; the four release waypoints advance on a timer.
- Impulse details: isotropic direction in world frame, constant force for one 15 Hz step, on one of `fr3_link1..7`.
- Camera calibration quality: 27.46 mm / 3.50° fit RMSE, status "measured", 11 of 12 samples; 6 px principal-point offset listed as an open gap.
- Point-cloud crop box numbers (camera-frame AABB x∈[−0.39,0.12], y∈[−0.25,0.20], z∈[0.61,1.17] m).
- AdamW weight decay 0.01 (PyTorch default), no LR schedule; final LayerNorm after the Transformer; ×1000 scaling inside the sinusoidal time embedding; EMA weights loaded by default.
- Hardware control stack: impedance + watchdog 1 kHz, controller state to policy 50 Hz, hand driver 50 Hz with ≈0.17 s actuator lag, torque-rate limit 1 N m/ms, per-tick clip at 1 kHz plus `max_policy_step` 0.036 m/0.18 rad, tracking-fault abort 0.08 m/0.35 rad, compliance centre at live fingertip midpoint, Desk must carry the hand load for the mass-weighted nullspace.
- Documented residual sim/real controller differences: arm armature in M, damping on arm-only `J q̇` vs mean fingertip velocity in sim, no Coriolis, 1 kHz vs 120 Hz.
- "Handover" in the full-task variant is a same-hand regrasp at the engaged nut, not a bimanual transfer.
- The deployment runner refuses checkpoints whose intrinsics/crop disagree with the camera profile or whose proprio width disagrees with `hand_velocity_observation`.

## E. Where NUTS and the code disagree (thesis already follows the code)

- Condition width: NUTS §III.E says 320-D, NUTS Fig. 2 and code say 256-D.
- Phase one-hot: NUTS six-way, code three-way.
- Release gate: NUTS "within ±5° with a grasp dwell", code one-sided ≥55° with no grasp condition.
- Dataset: NUTS `D_sim ∪ D_real`, thesis sim-only by decision.
- Isaac Lab 2.2.1 (NUTS) vs 2.3.2 (repo).
