# Thesis fact check, 2026-11-22

Scope: `thesis/source/` working tree (abstract, chapters 1–6, appendix A, appendix B).
Checked against: `additional/NUTS.md`, `~/code/forgeUltra` (branch `return-phase-clip`, ab34bc7),
`~/code/inspirehand-franka-ros2-ws-` (WS), the exp_20 teacher run artifacts, the thesis student's
`flow_config.json` / `run_provenance.json`, and the primary literature (arXiv HTML, publisher abstracts).
Nothing in any repository was edited.

Abbreviations: FU = forgeUltra, WS = inspirehand-franka-ros2-ws-.
Thesis student run = `WS/apps/policy_rollout/checkpoints/m24-dp3-exp20r01-proprio-friction-returndz7.5-tclip-smooth-clock-force-nohv-da-s0-20261111-173541-799500-.../` (config, provenance, tensorboard, one sim evaluation).
Teacher run (exp_20 run01) params and tensorboard: only copy found is in the desktop Trash,
`~/.local/share/Trash/files/m24-fr3v2-exp20-run01-hwfit-extended-2026-11-09_23-43-16-.../`. Restore it before it is purged.

## 1. Results provenance (critical)

All student results in Chapter 4 are copied from the paper, and they describe a different student
(old teacher with 512 envs, 20 demonstrations / 19,486 frames, 300 epochs), not the exp_20 student of Chapter 3.

| Thesis | Paper source | Problem |
|---|---|---|
| Table 4.2 real world (e) full method: 10.0 ± 0.0, −4.21 ± 1.20, −42.10 ± 4.37 | Table I(b) row (f) "Ours" | "Ours" is trained with human-corrected real-world data. The paper's simulated-data-only row (e) is 2.1 ± 1.4 cycles, −10.05 ± 4.08° |
| Table 4.3, all twelve nuts | Table II, "Ours" | same human-corrected student |
| Sec. 4.4.4 stress, 15–22 cycles | Sec. V-B | same |
| Table 4.2 simulation (e): 10.0, −1.77 ± 1.02, −17.7 ± 3.23 | Table I(a) row (e) | sim-only, but the old student |
| Table 4.2 simulation and real (a)–(d) | Table I rows (a)–(d) | paper trained these on the real-world-augmented data |
| Pose probe 8 / 8.6 mm, 15.16° / 31.20° | Sec. IV-D | encoders of the old, mixed-data students |

What exists for the actual thesis student:
- Simulation: `evaluation/returndz7.5-ret15x10/evaluation_report.json` in the student run folder: 47 of 48 runs complete ten cycles (0.979), 477 completed cycles, 0 transition failures, DR off, fixed 15 mm / 10° return gate. No cyclic-error statistic in the summary.
- Hardware (WS logs, 2026-11-12): nine recorded runs with `completed_cycles: 0`, one unrecorded run noted as "cycle 1 done, cycle 2 slipped". Six ros-sim rehearsals on 2026-11-11 also 0 cycles.
- Best hardware result of any student on this machine: 6 cycles, twice (earlier "rollback3" student, joint-space re-homing, M24 hex only, release on a 30° wrist-yaw proxy, no nut angle logged).
- No ten-cycle hardware trial, no nut-angle readings, nothing for M30/M36 or non-hex nuts on this machine.

Ablation implementations in FU: (b) ResNet encoder exists but no agent config wires it to the offline flow trainer; (c) the 512 LSTM head exists, no offline regression trainer with the DP3 encoder; (d) ACT-style regression: no implementation.

Affected text: abstract (EN + DE), ch1 contributions 2 and 3, ch4 Sec. 4.3.2–4.5, ch5 RQ1–RQ3 and Sec. 5.3, ch6 conclusion and RQ list.

## 2. Contradicted by code or data

### Chapter 3
- :118 "The teacher population was first qualified for one period only": leftover wording, there is one teacher.
- :120 "never write physics state": the thread-joint hold overwrites the joint state every physics substep (FU `forge_franka_env.py:1388-1416`).
- :125 caption "a return that times out rejects the episode": it is rolled back and retried first (FU `online_dagger_lstm.py:2066-2084`); contradicts :160.
- :131 "Twenty demonstrations": dataset has 36.
- :135 and ch4:71 "twelve different poses": 12 collected, 11 used in the fit. 9.7 mm / 0.98° is correct.
- :137 background-image replacement: never applied to the stored dataset (collector runs a `nut_pose_6d` student, recorder saves the raw image). Also appendix:478, :481, ch4:109, ch5:16.
- :137 "appearance is constant within a ten-cycle demonstration": true for table/nut/bolt materials only; shared dome light and floor are redrawn with p = 0.3 whenever any environment resets.
- :160 "An episode may last up to 200 s": the 200 s counter is zeroed at every release, so it bounds time since the last release.
- :160 list of fixed quantities incomplete: also arm armature and damping, bolt friction, nut-pose and bolt-frame observation noise.
- :162 "A sample holds the 35-D proprioception": file stores 29-D proprio plus separate force and torque arrays; the loader builds 35-D.
- :72-74 friction equation: code also caps the torque at the stopping torque (omission).
- :86 "critic observes clean values of the same quantities": critic gets absolute poses, not the actor's relative vectors.
- :98 "excess grip force" (also appendix:320, :351): the term penalizes the norm of the vector sum of the two pad forces, in which an opposing squeeze cancels. Grip force is bounded by the 0.5 N m effort limit.
- :100 termination list omits the joint-limit guard.
- :67 "With SDF mesh colliders ... not accurate enough to reproduce a mating thread": stated generally; FORGE (cited) threads nuts with SDF contacts. FU notes document the press-through exploit but one note rules out depenetration velocity as the cause of the loose thread (`docs/m10_collision_findings.md`). Scope the claim to this setup.

### Chapter 4
- :49 bench "60 cm by 80 cm", "5 cm pedestal": simulated top is 120 × 80 cm; bolt base is 50 mm above the robot base plane, 43.5 mm above the bench. No physical measurement on this machine.
- :75 "same action smoothing as in training": runner applies no EMA for this student (output already is the filtered target); only the temporal ensemble.
- :75 friction compensation 0.3 N m: default profile yes; whether it was on in the thesis student's hardware runs is not recorded, and the notes say the proprio-friction students are meant to run without it.
- :105 "11.7 ms on average and at most 12.0 ms": synthetic-frame benchmark of an older 26-D checkpoint (2026-10-15). Live passes of the thesis student: 17.8–36.7 ms, mean 22.5 ms.
- :125 caption: yellow bar spans z = 0 to the bolt base (below the bolt), side view shows only points within ±8 cm in y.
- :129 "the simulated arm has no gearbox friction": 0.2 N m × U(0.8, 2.0) per appendix:472 and appendix B :41.
- :129 "five hardware runs": appendix B lists six with the transition clip (run 6 ended in cycle 1); all with the earlier student.
- :152 slip fraction 0.063: last-ten-epoch mean is 0.061 (0.063 is epochs 190–199).
- :165 "Five students are trained on the simulated dataset of Section 3.4.4": see section 1.

### Chapter 5
- :8, :10, :12, :14, :16 all quote section-1 numbers.
- :16 "image-space color augmentation": none in the recipe (appendix:445 agrees).
- :21 "positions and velocities of the ten controlled joints": ten positions, seven arm velocities.
- :31 "the reward penalizes excess wrist force": no wrist-force term exists.
- :33 "People change the grasp as the resistance grows (Section 1.2.2)": that section does not say this.
- :35 "0.7 s per segment and 1.0 s": thesis dataset used 11/8/9/15/16 steps (0.73/0.53/0.60/1.00/1.07 s, 3.93 s total).
- :38 "The same hand also picks up a loose nut in simulation": only FR3 run grasps, lifts about 2 cm, drops; pick-up success 0.000. Contradicts ch6:22, :26.
- :42 calibration "measured but not deployment-validated": the deployed calibration file has status `validated`.

### Chapter 6
- :30 implies the teacher lacks axial coverage: teacher training already randomizes nut height 0–20 mm; the limit is in the demonstrations.
- :32 "depth-corruption model that the encoder pretraining already provides can then be applied": depth corruption is already applied in student training; the recipe has no pretraining.
- :36 "constraint that a chunk label must be produced by the teacher alone": never introduced.

### Appendix A
- :24 "(hand drives otherwise 20 N m)": pinch joints 0.5, other proximal joints 1.864, distal followers 50.
- :27 "identified FR3": friction/armature/damping are Menagerie class values.
- :51 smoothing "same" on hardware: see ch4:75.
- :60 physical torque limit "robot torque-rate limit": also per-joint clamp 87/12 N m, as appendix B :28 says.
- :70 "Force channels (teacher only)": student observes them, also on hardware.
- :156 palm translation (1.2, 4.5, 1.4): stored (1.150, 4.456, 1.349), third rounds to 1.3.
- :164/:172/:180-181/:200 "vendor" register maps for the thumb are the driver's own earlier camera calibration.
- :168 "distal thumb coupling is the weakest fit, residual 0.031": index residual is 0.034 (thumb weakest by R² only).
- :212 "through closed and back to open": closed stop not among the six panels.
- :225 "Most of the 6.9 mm index error ... comes from its register map": map-only 3.1 mm, coupling-only 2.6 mm. "changes only the couplings": vendor variant is also clamped to vendor limits; unclamped vendor thumb error is 4.0/3.5 mm, so the reported thumb gain comes from the clamp.
- :229 held-out sweep ran at abduction register 266 and to the closed pinch target; fitted model is driven by feedback registers, not commanded ones.
- Table A.4: fitted maps leave the fitted limits (thumb flexion 0.394 > 0.38; abduction 0.246 < 0.25).
- :292 critic "previous filtered action": roll and pitch masked for the critic too.
- :306-325 Table A.6 omits table pose randomization (±5 cm x, ±10 cm y, ±2.5° yaw) and the random sign flip of the fingertip quaternion.
- :361 proper-grasp definition omits: both forces > 0.1 N, opposing (cos < −0.3), pinch line perpendicular to the nut axis. Termination list omits no-contact > 150 steps, joint-velocity reflex, thread numerical failure (all 0.000 in the last ten epochs).
- :374-375 segment durations: see ch5:35.
- :376 "accepted after 2.5 s of settling inside the upper limits": code accepts after waiting N steps if currently inside the maximum.
- :438 vs :468: 1473 steps vs 1474 frames (both right, different units; say so).
- :478, :481 background: see ch3:137.

### Appendix B
- :56 "Two terms were added" vs :430 "three measures".
- :132 "Its first hardware run": it was the last of about twelve attempts that morning.
- :161 "98.5–119.5 mm" after the slip: table says 98.5–104.6 mm; 119.5 is the contact window.
- :219 "The sweep was not run in ros-sim with a dead zone": started twice, neither completed.
- :258 viscous term "2.4–4.1 N": own table gives 2.4–4.3 N; the 0.27 ratio at :260 fits neither end.
- :422 "0.3 N m lies below the fitted friction on j1–j5": j3 is 0.29 on day 2.

## 3. Cross-chapter contradictions (not already above)
- ch1:91 "The acknowledgments state this attribution": they do not.
- ch1:58 "No prior work" vs ch2:125 "None of the reviewed works".
- "head camera" (ch3:154, :160, :172, appendix:475) vs fixed D415 on a stand (ch4).
- Return-gate tolerances: appendix A 5–15 mm / 5–10°; appendix B 30 mm / 25°, 3 mm / 2°, 15–20 mm / 10°; ch3:120 "same tolerances" on hardware. Hardware CLI defaults are 5 mm / 5° or 30 mm / 25° with re-homing.
- Figure captions list three or four learned phases inconsistently (ch3:36, :125 vs eq. 3.1).
- ch2:81 attributes the capped separating velocity to "PhysX and MuJoCo"; the cap is PhysX-specific.
- ch4:109 "rests entirely on four properties" omits depth augmentation, camera-pose and joint-friction randomization, which ch3 presents as transfer measures.
- ch4:219 rectangular M30/M36 "complete none" while "the fingers turn the nut by 60°": by the thesis's own cycle definition that would be one completed cycle (inherited from the paper).

## 4. Literature and bibliography
No cited claim is contradicted. Needs rewording or another source:
- ch2:113 π0 demonstrations "collected by teleoperation": the paper says "robot operators", never teleoperation.
- ch2:119 Lin et al. "per-object RL specialists": paper says sub-task specialists; its best variant groups objects.
- ch2:93 Manyar "industrial screwdriving tool": abstract says mobile manipulator, no "industrial". ch2:91 fixtures sentence unverified (closed access).
- ch2:41 chunking with H and H_e attributed to ACT: ACT has one chunk size k.
- ch1:28 "thousands of simultaneous contacts": Factory gives about 16k per pair before reduction, about 300 after.

Bibliography (`literature.bib`):
- 20 entries print with no venue. Published venues: Black2026 RSS 2025; Chen2021 CoRL 2021 (PMLR 164:297-307); Chen2023 CoRL 2023 (PMLR 229:3809-3829); Chi2024 IJRR 44(10-11):1684-1704; Handa2024 ICRA 2023 pp. 5977-5984; Kedia2026 RSS 2026; Koczy2025 IROS 2025 pp. 121-127; Lin2024 CoRL 2024 (PMLR 270:5220-5235); Lin2025 CoRL 2025 (PMLR 305:4926-4940); Lipman2023 ICLR 2023; Lum2024 CoRL 2024 (PMLR 270:3182-3211); Narang2022 RSS 2022; Noseworthy2025 RA-L 10(5):4436-4443; Petrenko2023 RSS 2023; Ross2011 AISTATS 2011 (PMLR 15:627-635); Singh2025 ICRA 2026 pp. 5086-5093; Tang2023industreal RSS 2023; Ze2024 RSS 2024. arXiv only: Lipman2024 (2412.06264), Zhang2026 (2610.13354).
- Wrong years: Black2026 (2025), Handa2024 (2023), Singh2025 (2026).
- Never cited: Huang2025, Luo2025, Zhang2016, IntlAirTool, Hochreiter1997, Jiang2025transic, Siciliano2016, Rombach2022, Black2025.
- All cited keys resolve; `main.log` has no undefined references or citations.

## 5. Not verifiable on this machine
- Dataset statistics beyond 36 episodes / 53,408 frames / median 1474: 16 envs, 6400 steps, seed 1, 14 envs contributing, 20 episodes with retries, 40 retries, 10,136 rows dropped, 1341 / 1838 min / max, "at most 3" retries (dataset manifest and recipe JSON are absent).
- Transition clip 0.05 m / 0.25 rad, dead zone 1 N m, lower gate bounds 5 mm / 5°.
- Depth figure 21.4 % → 47.3 %.
- Vendor-model teacher 0.82 "same recipe and seed"; pad-force replay 43/38, 27/21, 12/7 N; reset-probe numbers (only in the exp_20 doc).
- Isaac Lab 2.3.2 (lock pins a commit, not a tag); RTX 4090 for training (paper says RTX 5090).
- Runner flags and friction-compensation state of the thesis student's hardware runs.
- Crop-box 40 mm margin under the current calibration.
- Several appendix B single numbers not in stored summaries.

## 6. Confirmed
About 250 individual claims: thread model and its parameters, all PPO hyperparameters, 46-D / 76-D observations with every row, reward weights (15 terms), every DR range listed, action decoder and OSC law, teacher results table (recomputed from tensorboard), student architecture and training recipe line by line against the run config (incl. 59,648 encoder parameters, 30 impulses per demonstration, camera-pose ±11.2 mm / ±1.13°, all depth-augmentation parameters), deployment controller gains / projector / step limit / no Coriolis, perception chain (640×480 → 640×360 → 320×180, raw aligned depth, 0.01–5 m), and nearly every appendix B table reproduced from stored JSON summaries.

## 7. Housekeeping
- Source comments name the paper at ch4:172, :181, :208, :213, :220, :252.
- Open TODO comments: ch1:7, :12, :14, :16; ch2:76, :82; ch4:101, :172; ch5:30, :36; ch6:9.
- `thesis/TODO_draft.md` is stale relative to the current chapters.
