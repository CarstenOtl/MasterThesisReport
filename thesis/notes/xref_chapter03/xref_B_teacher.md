# Cross-reference audit: thesis §3.3 Privileged Teacher Training (chapter03.tex:82–127)

Sources: THESIS = `thesis/source/chapter03.tex` (+ `appendix.tex` tab:teacher-obs / tab:ppo, `notation.tex`); NUTS = `additional/NUTS.md`; CODE = `~/code/forgeUltra/` (paths relative to that repo); DEPLOY = `~/code/inspirehand-franka-ros2-ws-/`.

Reference configs used for the comparison (per the author's decision to describe the paper recipe, not the retained checkpoint):
- **V1 vanilla / ADR**: `forge_ultra/tasks/forge_franka_threading/config/tasks/vanilla_threading.yaml`, `.../threading_nut_initial_pose_adr.yaml` (hold 5 steps, no table penalties, no grip-loss termination; actor 37-D, critic 77-D).
- **V2 single-M24 DR**: `forge_ultra/tasks/forge_franka_threading_v2/config/tasks/m24_threading_domain_randomized.yaml` (extends V2 `threading_nut_initial_pose_adr.yaml`; yaw ADR + 20 mm depth + table penalties + grip-loss termination; hold 10 steps; actor 46-D, critic 76-D at HEAD).
- **V2 multi-size**: `.../multi_nut_threading_z_randomized.yaml` (one-hot, round robin, 20 mm depth, table penalties, grip-loss termination, hold 10; **no yaw randomization**; actor 40-D, critic 80-D).

Verdict legend: CONSISTENT / PARTIAL (true but incomplete or true for only some configs) / MISMATCH / UNVERIFIED.

---

## Summary of actionable findings (details in the tables below)

| # | Severity | Thesis location | Issue | Suggested rewrite |
|---|---|---|---|---|
| 1 | MISMATCH | l.96 "R^target pays 250 distributed over a five-step hold within 5° of the target" | Code pays once directional progress ≥ 55° with a live latched grasp; condition is one-sided, overshoot past 60° stays eligible (`forge_franka_env.py:1591-1609`, yaml comment "Any farther overshoot remains legal"). The ±5° window in NUTS (l.200-202) is the hybrid-teacher *release* gate, not the reward. | "…distributed over the first five steps in which at least 55° of clockwise rotation (five degrees short of the 60° target) is held with a live proper grasp; overshoot is not penalized." |
| 2 | PARTIAL | l.96 "has held for five consecutive steps" (grasp latch) | Five steps only in V1 configs (`vanilla_threading.yaml:106`); every V2 config, i.e. every config that has the table penalties and grip-loss termination claimed in the same paragraph, uses ten (`forge_franka_threading_v2/.../vanilla_threading.yaml` diff, `multi_nut_threading.yaml`, `threading_nut_initial_pose_adr.yaml` V2). No single config has 5 + grip-loss termination. | "…has held for ten consecutive control steps" (if the V2 recipe is the reference), or state both. Author decision. |
| 3 | PARTIAL | l.96 and eq. "excess wrist force (P^force, 0.05)" | Matches NUTS wording, but the code penalizes the reconstructed **net thumb+index pad contact force on the nut**, expressed in the hand grasp frame, above a per-episode threshold U(5,10) N (`forge_franka_env.py:1354-1377, 1963-1965`; `task_config.py:628`; `reward_terms.py:49-57`). No wrist sensor is involved. | "excess fingertip contact force on the nut (the summed thumb and index pad forces above a per-episode threshold)" |
| 4 | PARTIAL | appendix tab:teacher-obs (39-D actor / 69-D critic) | Matches forgeUltra at commit `eaddc28` (2026-10-14: fingertip forces only). HEAD (`7d610fa`, 2026-10-16) adds 7 normalized FR3 joint torques to actor and critic: 46-D / 76-D (`docs/distillation_observation_action_reference.md:17,48`). Vanilla is 37/77, multi-size 40/80 (HANDOVER.md:94-95). | Either add the row "arm joint torques (normalized) · 7 · gain U(0.9,1.1), bias U(−0.01,0.01), N(0,0.005)" to actor and critic (→ 46/76), or state the table describes the configuration without the joint-torque channel. |
| 5 | PARTIAL | tab:dr "fingertip forces N(0,1 N) per channel" | Code also applies per-episode gain U(0.8,1.2) and bias U(−1,1) N, clamps to ≥ 0 (`m24_threading_domain_randomized.yaml:44-49`, `sensor_noise.py:44-67`). Only the DR config enables this channel. | "per-episode gain U(0.8,1.2) and offset U(−1,1) N, plus N(0,1 N) per refresh, clamped to ≥ 0" |
| 6 | PARTIAL | l.86 critic list | Vanilla critic also carries the 3-D net contact force and the sampled force-penalty threshold (`configuration_schema.py:18-40`); DR critic also carries the 7 arm joint torques. | append "the net contact force and the sampled force-penalty threshold" (vanilla) or "the normalized arm joint torques" (DR). |
| 7 | PARTIAL | l.86 actor list | True component list, but the actor's fingertip quaternion has w and z zeroed with a per-episode sign flip, the angular velocity has x,y zeroed, and the previous-action roll/pitch entries are zeroed (`forge_franka_env.py:1315-1316,1327`; `policy_observations.py:111`). | Optional footnote: "The fingertip quaternion and angular velocity are reduced to their tilt components, and the roll/pitch entries of the previous action are masked." |
| 8 | PARTIAL | l.96 "R^turn … fraction of the distance to the fixed helical target pose" | Distance is a keypoint distance over nut keypoints (`forge_franka_env.py:1540-1547`), normalized by the distance at the grasp latch; the ratchet is rebased again on grasp loss/re-grasp (`threading.py:187-212`, `intermediate_terms.py:182-209`). | "…60 times the newly achieved fraction of the keypoint distance that remained to the fixed helical target when the grasp latched" |
| 9 | PARTIAL | l.126 pickup reward summary | Pickup reward also has a lift bonus, reach bonuses at both waypoints, an engagement success bonus (350), a nut-axis alignment penalty and a goal-velocity penalty; it has no action-rate penalty (`full_task_env/config/tasks/pickup_engage.yaml` reward_terms; `rewards/pickup.py`). | "…a lift term, keypoint progress and reach bonuses toward two waypoints, and alignment, braking, and engagement-success terms (Chapter 5)." |
| 10 | PARTIAL | tab:dr row "nut size round-robin (multi-size teacher)" together with the yaw-curriculum row | The multi-size configs set `held_asset_spawn_yaw_delta_range_deg: 0.0` and no ADR, so the multi-size teacher as configured has no yaw randomization. | Add "(single-size teacher)" to the yaw-curriculum row, or note the exception. |
| 11 | UNVERIFIED | l.124 / tab:ppo "512 parallel environments … about ten hours on one RTX 5090" | Exactly as NUTS l.280-287. In code, env count is a CLI argument (`train.py:213,349`; yaml `num_actors: 128` is overwritten; cfg default 500). A Sep-8 run name contains "512" (HANDOVER.md:408); the retained Sep-10 "no-adr" run's env count and wall-clock are not recorded in the repo. | Keep (NUTS-backed). |

---

## Claim-by-claim tables

### A. chapter03.tex l.84–86: setup, actor and critic observations, noise

| Thesis (line, quote) | NUTS | forgeUltra | Verdict / rewrite |
|---|---|---|---|
| l.84 "learns to approach the nut, acquire the pinch grasp, keep it under load while turning, and hold the target" | l.163-170 three stages approach / turning / completion | `rewards/threading.py:36-51` three stage groups | CONSISTENT |
| l.84 "observes privileged simulator state" | l.197-200 noisy fingertip pose, nut-relative grasp state, target error | actor sees noisy nut pose (`policy_observations.py:125-126`), critic clean state | CONSISTENT |
| l.86 "recurrent policy, hidden state h_t"; notation.tex:27-28 z^π_t = g_π(x_t, ξ_t), h_t | l.187-190 same symbols | LSTM actor `rl_games_ppo_cfg.yaml:40-45` | CONSISTENT |
| l.86 "PPO in an asymmetric actor–critic [Pinto2017]; critic observes more" | l.196-197 "asymmetric recurrent actor–critic" | `rl_games_ppo_cfg.yaml:97-124` central_value_config | CONSISTENT |
| l.86 actor comprises: fingertip (grasp-frame) pos rel. bolt frame + quaternion; EE lin/ang velocity by finite differences; fingertip pos rel. held nut + nut quaternion; pos/quat error to turning target; grasp-phase flag; previous filtered action; one-hot (multi-size) | l.197-201 same list ("nut-relative grasp state, turning-target error, grasp-phase flag, previous action, nut-size one-hot") | `vanilla_threading.yaml` actor_obs (13 enabled terms) + `policy_observations.py:113-129,165`; grasp flag = `threading_grasped_once` (`forge_franka_env.py:180-198`); velocities finite-differenced from noisy pose (`forge_franka_env.py:1319-1328`); "fingertip" = thumb/index pad midpoint control frame; actions EMA-filtered (`robot_control.py:71-76`) | CONSISTENT for vanilla/ADR/multi. PARTIAL details: quat w,z zeroed + sign flip, angvel x,y zeroed, prev-action roll/pitch zeroed (`forge_franka_env.py:1315-1316,1327`; `policy_observations.py:111`). DR config additionally feeds 2 fingertip forces + 7 joint torques to the actor (`m24_threading_domain_randomized.yaml:12-14`). See finding 7. |
| l.86 "Position terms receive Gaussian noise with 0.25 mm std per axis" | not in NUTS | `forge_franka_env.py:1301-1305` (randn·0.00025), held nut `:1334-1338` | CONSISTENT |
| l.86 "orientation terms 0.1°" | not in NUTS | random-axis Gaussian angle `forge_franka_env.py:1307-1313, 1340-1347` | CONSISTENT |
| l.86 "bolt frame a per-episode offset of 1 mm (calibration error)" | not in NUTS | `forge_franka_env.py:2082-2087` randn·0.001 per reset; used in `policy_observations.py:109-116` | CONSISTENT |
| l.86 critic: "same task and history structure using clean values + arm joint positions, complete nut and bolt pose, sampled controller gains, smoothing factor, thresholds, thumb and index contact forces" | l.201-204 "arm-joint positions, complete nut–bolt geometry, controller state, wrist and fingertip contact state" | `configuration_schema.py:18-40` (vanilla: + ft_force 3, force_threshold 1); DR: `m24_threading_domain_randomized.yaml:22-41` (+ arm_joint_torque 7) | PARTIAL, finding 6 |
| appendix tab:teacher-obs actor 39-D / critic 69-D (M24 single-size) | not in NUTS | 37/77 vanilla; 46/76 DR at HEAD (`docs/distillation_observation_action_reference.md:17,48`); 39/69 only at commit `eaddc28` (2026-10-14) | PARTIAL, finding 4 |
| appendix caption "multi-size: 40-D actor without fingertip forces, 80-D critic, 3-D one-hot" | l.204-205 one-hot conditions M24/M30/M36 | HANDOVER.md:91-95 "40 actor inputs, 80 critic inputs"; `multi_nut_threading.yaml` actor_obs | CONSISTENT |
| appendix rows: fingertip quat WXYZ; linvel/angvel finite differences of noisy pose; fingertip rel. nut noise "each body"; target errors inherit nut noise; flag no noise; forces N(0,1 N) clamped ≥0; prev action 9 | — | `policy_observations.py`, `forge_franka_env.py:1300-1347`, `docs/distillation_observation_action_reference.md:17-33` | CONSISTENT (force row: see finding 5) |
| appendix critic rows: 13 + 7 + 10 + 7 + 6 + 1 + 2 + 6 + 8 + 9 = 69 | — | matches `eaddc28` state_order; HEAD adds arm_joint_torque 7 | PARTIAL, finding 4 |

### B. chapter03.tex l.88: architecture and PPO

| Thesis | NUTS | forgeUltra | Verdict |
|---|---|---|---|
| "two-layer LSTM, 1024 units, layer normalization, then 512–128–64 MLP, ELU; actor and central critic share it" | l.205-207 | `rl_games_ppo_cfg.yaml:31-45` and `:109-124` (identical for central value) | CONSISTENT |
| "recurrent sequences span 128 control steps" | l.207 + l.148 ("span 128 control steps") | `seq_length: 128` (`:88`) | CONSISTENT |
| "rollout horizon 256 steps" | not in NUTS | `horizon_length: 256` (`:83`) | CONSISTENT |
| "diagonal Gaussian over the normalized action with state-dependent std" | l.148-149 diagonal Gaussian over a_t ∈ [−1,1]^9 (no std statement) | `continuous_a2c_logstd`, `fixed_sigma: False` (`:15,27`) | CONSISTENT |
| tab:ppo: minibatch 512; mini-epochs 4; γ 0.995; τ 0.95; lr 1e-4 adaptive, KL 0.008; ε 0.2; critic coef 2; entropy 0; grad-norm 1.0; bounds loss 1e-4; mixed precision | not in NUTS | `rl_games_ppo_cfg.yaml:60-89`; same in `distillation/config/agents/ppo_teacher.yaml` | CONSISTENT |
| tab:ppo: parallel environments 512; epochs 200 | l.280-281 "200 epochs in 512 environments" | `max_epochs: 200` (`:76`); envs from CLI (finding 11) | CONSISTENT with NUTS, env count UNVERIFIED in code |

### C. Equation (eq:reward) and l.96 reward terms

| Thesis | NUTS | forgeUltra | Verdict |
|---|---|---|---|
| eq. r_t = Σ w^r R − Σ w^p P; R = {center, face, grasp, turn, target}; P = {mag, Δa, align, force, settle, clear, contact} | l.156-162 identical eq. (5) | V1 terms `threading.py:36-51` (10 terms: no clear/contact); V2 adds clearance + table contact (+ a nut-wrench penalty whose default scales are 0, `forge_franka_env_cfg.py:309-313`) in `forge_franka_env.py:128-156` | CONSISTENT (V2) |
| "R^center rewards motion of the grasp center toward the nut center; R^face motion of thumb/index pads toward the designated opposing faces; both pay 20 × newly achieved fraction of the initial gap; repeated motion cannot accumulate" | l.163-171 "pay only new-best progress" | `threading.py:131-161`: relu(best − d)·20/gap0 (gap0 set at reset `forge_franka_env.py:2000-2003`, floor 2 cm), gated off after first latch; face term uses mean of the two face distances; scales `vanilla_threading.yaml` 20/20 | CONSISTENT (detail: face uses mean face distance; both terms switch off permanently after the latch) |
| "R^grasp one-time bonus of 100 when a proper grasp (simultaneous thumb and index contact on the designated faces, pinch line perpendicular to the nut axis) has held for five consecutive steps" | l.165-166 "marks acquisition of a stable, proper grasp" | bonus 100 on latch edge `threading.py:177-182`; proper grip = in_contact ∧ \|pinch·axis\| < 0.30 ∧ both face distances < 1 cm (`intermediate_terms.py:105-146`; `forge_franka_env_cfg.py:325`; yaml `grasp_face_tolerance_m 0.01`); latch after `threading_grasp_hold_steps` consecutive steps (`forge_franka_env.py:1565-1576`): **5 in V1, 10 in all V2** | PARTIAL, finding 2 |
| "R^turn pays 60 × newly achieved fraction of the distance to the fixed helical target pose, only while the acquired proper grasp remains live" | l.166-167 "grip-maintaining progress toward the fixed helical target" | `threading.py:184-212` + `intermediate_terms.py:182-209`: active = grasped_once ∧ proper_grip; distance = keypoint distance (`forge_franka_env.py:1540-1547`); gap = distance at latch, rebased on grasp loss; target = 60° turn + pitch descent from reset nut pose (`forge_franka_env.py:2007-2021`); scale 60, floor 3 mm | PARTIAL (minor), finding 8 |
| "R^target pays 250 distributed over a five-step hold within 5° of the target" | l.167-168 "rewards holding the target stably"; ±5° in l.200-202 is the release trigger | `forge_franka_env.py:1591-1609`: target_reached = grasped_once ∧ proper_grip ∧ progress ≥ 55°; `threading.py:235-243` pays 250/5 per step for steps ≤ 5 | MISMATCH, finding 1 |
| "P^mag large commands, 1e-3" | l.172 | −0.001·(‖Δp‖/p_thr + \|Δyaw\|/yaw_thr) `reward_terms.py:20-33`; `action_penalty_asset_scale: 0.001` | CONSISTENT (normalized position + yaw command) |
| "P^Δa abrupt action changes, 0.1" | l.172-173 | −0.1·‖a_t − a_{t−1}‖ on filtered actions `reward_terms.py:36-46`; `action_grad_penalty_scale: 0.1` | CONSISTENT |
| "P^align hand frame vs nut frame, 0.02" | l.173 | −0.02·0.25[(1−x̂·x̂')+(1−ẑ·ẑ')] `grasp_frame.py:360-381`, `threading.py:163-175` (active in all stages) | CONSISTENT |
| "P^force excess wrist force, 0.05" | l.173-174 "excess wrist force" | −0.05·relu(‖F_pads‖ − F_th), F = summed thumb+index pad contact force in grasp frame, F_th ~ U(5,10) N per reset (`forge_franka_env.py:1354-1377,1963-1965`; `task_config.py:628`) | PARTIAL, finding 3 |
| "P^settle residual rotation near target, 0.25 ω² from 50° onward" | l.174 | `threading.py:218-234`: −0.25·ω_axial² while grasped ∧ progress ≥ 50°; yaml 50.0 / 0.25 | CONSISTENT (ω = nut angular velocity about its axis; only with live grip) |
| "P^clear insufficient table clearance" | l.174-175 | V2 only: −2.0·relu((0.03 − d)/0.03)² (`forge_franka_env.py:131-135`, `reward_terms.py:123-133`, yaml margin 0.03 / scale 2.0) | CONSISTENT (V2) |
| "P^contact arm–table contact" | l.175 | V2 only: −0.05·relu(F_table − 2 N) (`forge_franka_env.py:136-139`) | CONSISTENT (V2) |

### D. l.96 success and termination

| Thesis | NUTS | forgeUltra | Verdict |
|---|---|---|---|
| "succeeds when ≥ 55° clockwise rotation is held with a live proper grasp for five steps" | not in NUTS | `threading_success_min_deg: 55`, `success_hold_steps: 5`; `forge_franka_env.py:1591-1609` | CONSISTENT |
| "terminates when the nut leaves the bolt by > 3 cm" | not in NUTS | `terminate_on_nut_far`, `max_nut_bolt_dist: 0.03`; `forge_franka_env.py:1640-1647` | CONSISTENT |
| "tilts by more than 60°" | not in NUTS | `max_nut_bolt_axis_tilt_deg: 60`; `:1649-1663` | CONSISTENT |
| "or releases the thread" | not in NUTS | `terminate_on_thread_release` (nut unscrews past `simplified_thread_upper_release_turns: 1.0`); `:1664-1669` | CONSISTENT |
| "and when the grasp is lost after it has latched … hard constraint" | not in NUTS | V2 only: `terminate_on_proper_grip_loss: true`; `:1670-1678` | CONSISTENT (V2); V1 lacks it |
| (not stated) | — | also always on: thread numerical failure (`:1629-1632`) and 30 s / 450-step time-out (`forge_franka_env_cfg.py:211-215`). HANDOVER.md:398-400 mentions a 5° pre-grasp rotation termination; **not found** in the Franka env code. | informational |

### E. l.98 and tab:dr domain randomization

| Thesis | NUTS | forgeUltra | Verdict |
|---|---|---|---|
| "nut mass ±5 g" / table U(−5,5) g per reset | l.176-178 (only rotation, axial height, controller settings mentioned) | events `object_scale_mass` [−0.005,0.005] add uniform, mode reset (`mdp/domain_randomization.py:28-32`) | CONSISTENT |
| "bolt friction static in [0.25,1.25]" / table "128 buckets" | not in NUTS | `fixed_physics_material` static [0.25,1.25], dynamic fixed 0.25, 128 buckets, mode **startup** (once per env, not per reset) | CONSISTENT (note: startup, bucketed) |
| caption "multiplicative factors 1+U(0,ℓ) or reciprocal with equal probability" | — | `task_math.py:129-140` | CONSISTENT |
| "proportional gains multiplicative ℓ=0.41 per axis and reset" | l.177-178 "controller settings" | `task_prop_gains_noise_level: [0.41]*6`; `forge_franka_env.py:1951-1953` at reset; derivative gains derived | CONSISTENT |
| "action smoothing factor U(0.025,0.1) per reset; fingers 3×" | — | `ema_factor_range`, `hand_ema_factor_scale: 3.0`, capped at 1 (`robot_control.py:71-76`; `forge_franka_env.py:1945`) | CONSISTENT |
| "position / rotation threshold multiplicative ℓ=0.25 / 0.29" | — | yaml; `forge_franka_env.py:1954-1959` | CONSISTENT |
| "dead zone U(0,[5,5,5,1,1,1]) N, N m, resampled every 2 s" | — | `randomize_dead_zone` rand·default, interval [2,2] s (`mdp/domain_randomization.py:18-21,48-52`); also at reset (`:1967-1969`) | CONSISTENT |
| "fingertip and nut position N(0,0.25 mm) per axis and refresh" | — | `forge_franka_env.py:1301-1305,1334-1338` | CONSISTENT |
| "fingertip and nut orientation random-axis angle N(0,0.1°)" | — | `:1307-1313,1340-1347` | CONSISTENT |
| "bolt frame N(0,1 mm) per axis and reset" | — | `:2082-2087` | CONSISTENT |
| "fingertip forces N(0,1 N) per channel" | — | DR config only; plus gain U(0.8,1.2), bias U(−1,1) N, clamp ≥ 0 | PARTIAL, finding 5 |
| "nut yaw curriculum 0 → ±30° in 5° steps at 80 % success"; l.98 "at least five episode lengths between expansions" | l.176-177 "randomize the nut's initial rotation" | `threading_nut_initial_pose_adr.yaml:101-113`; `forge_franka_env.py:278-318` (population task-success rate ≥ 0.80, min period 5·max_episode_length, promotion-only, DEXTRAH scheduler) | CONSISTENT (code uses ≥, thesis "exceeds"; negligible) |
| "nut axial height U(0,20) mm below nominal, full turn reserved" | l.177 "and axial height" | `threading_spawn_max_drop_m: 0.020`, fraction U(0,1) per reset (`forge_franka_env.py:2237-2252`; `spawn_height.py:206-215`); HANDOVER.md:81-83 | CONSISTENT |
| "nut size round-robin M24/M30/M36 (multi-size)" | l.204-205 | `forge_franka_multi_env.py:49-54`; `multi_nut_threading.yaml:7-8` | CONSISTENT; but multi-size configs have no yaw randomization (finding 10) |
| l.98 "the observation noise is small … because the actor's inputs are relative poses the student will later infer from a camera" | — | design rationale; `docs/forge_tg2_helical_policy_reference.md` §5 ("near-clean by design") | CONSISTENT (rationale) |
| (not in table) initial bolt/hand pose | — | Franka threading task is `ForgeTg2NutThreadDeterministic` (`task_config.py:647-668, 731`): all init-pose noises 0; `fixed_arm_pose_tcp_xyz_noise_m` (0,0,0) | table is complete on this point |

### F. l.124 multi-size variant and training compute

| Thesis | NUTS | forgeUltra | Verdict |
|---|---|---|---|
| "multi-size variant conditions one teacher on M24, M30, M36 through the one-hot and round-robin assignment" | l.204-205 | `multi_nut_threading*.yaml`, `forge_franka_multi_env.py:49-54`, HANDOVER.md:91-95 | CONSISTENT |
| "demonstrations collected with the single-size M24 teacher" | l.280 "retained M24 run" | HANDOVER.md:176-185 (`last_ForgeTg2_ep_200_rew_17628.744.pth`), `:2043` (V1 no-adr run) | CONSISTENT |
| "512 parallel environments for 200 epochs, about ten hours on one RTX 5090" | l.280-287 identical | epochs: `max_epochs: 200`; envs/time: not recorded for the retained run (finding 11) | CONSISTENT with NUTS; UNVERIFIED in code |

### G. l.126 pickup teacher

| Thesis | NUTS | forgeUltra | Verdict |
|---|---|---|---|
| "second expert, pickup teacher, trained with the same recipe" | not in NUTS | same rl_games config (`ppo_teacher.yaml` identical); README.md:43-48 quickstart uses `--num_envs 384`; `docs/experiments/exp_10_forge_franka_pickplace.md:125` ~17 h | PARTIAL: same PPO config, but env count/time differ from the threading numbers; "recipe" is acceptable if it means the PPO configuration |
| "grasping a loose nut from the table, lifting it, transporting it to a handoff pose above the bolt tip, and engaging it" | — | `pickup_engage.yaml:139-145` (G0 handoff 5 mm clearance, G1 engagement 1 mm depth) | CONSISTENT |
| "reward uses the same approach and grasp terms, a lift term, and keypoint progress toward two waypoints" | — | `pickup_engage.yaml` reward_terms (15 terms): face/center approach 20/20, grasp bonus 100 after 5 steps, lifting 40 to 4 cm + lift bonus 40, keypoint G0 30 / G1 100, reach bonuses 50/50, engagement success 350, z-alignment 2.0, G1 velocity penalty 20; no action-rate penalty | PARTIAL, finding 9 |
| "part of the full-task variant of the hybrid teacher … not part of the final threading pipeline, whose trials start from an engaged nut" | l.152-153 hybrid teacher | `distillation/config/hybrid_teacher.yaml` variants `full_task` vs `cyclic_threading` | CONSISTENT |

### H. Deployment repo (`inspirehand-franka-ros2-ws-`)

| Item | Finding |
|---|---|
| `docs/policy_rollout_training_gap_todo.md` | No reference to privileged state, critic, or teacher observation noise. "Teacher-forced" (l.161, 934) means feeding recorded student-format observations (RGB-D + 26/29-D proprio) from hybrid-teacher episodes to the student. n/a to §3.3. |
| `apps/policy_rollout/tests/diagnose_teacher_observation_inference.py:2-8` | "recorded teacher observations" = the episode's RGB-D, 29-D native-OSC proprio, progress, phase; not the 37/46-D privileged actor input. n/a. |
| Any other teacher reference in `apps/policy_rollout/` | Only checkpoint names (`sequential_threading_cycle10_hybrid_teacher_d415_20ep`) and OSC adapter notes. Teacher is sim-only; nothing to cross-check. |

---

## Appendix note for the author: which forgeUltra config matches the thesis text

- The §3.3 description (yaw ADR + 0–20 mm depth + table clearance/contact penalties + grip-loss termination + 2-D fingertip force in actor/critic) corresponds to **`forge_ultra/tasks/forge_franka_threading_v2/config/tasks/m24_threading_domain_randomized.yaml` as of commit `eaddc28` (2026-10-14)**. Two deltas remain even against that revision: the grasp latch is **10** consecutive steps (thesis: five), and the fingertip-force channel also has per-episode gain/bias randomization. At HEAD (`7d610fa`, 2026-10-16) the same file additionally enables 7 normalized FR3 joint torques in actor and critic (46-D / 76-D).
- The multi-size description corresponds to **`multi_nut_threading_z_randomized.yaml`** (40-D / 80-D), which has the depth randomization and table penalties but **no yaw randomization**.
- The V1 configs (`forge_franka_threading/config/tasks/vanilla_threading.yaml`, `threading_nut_initial_pose_adr.yaml`) match the "five consecutive steps" latch and are the family of the retained dataset checkpoint, but lack table penalties, depth randomization, and grip-loss termination (per the author's standing decision, not re-flagged).
- Only trained checkpoint in the repo: `checkpoints/franka_threading_v2/multi_nut_z20mm/ForgeTg2.pth` (134-byte LFS pointer); no training logs for the retained Sep-10 run are present, so env count and wall-clock cannot be confirmed from code.
