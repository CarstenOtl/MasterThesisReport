# Thesis outline and storyline

Working document for the logic of the thesis, top to bottom. Each section has a short summary and, where it matters, what it hands to the next section. Items marked **[open]** are decisions or gaps to settle. Questions the report must answer are collected in [questions.md](questions.md).

## 0. The story in six sentences

1. Threaded joints are central to assembly, because they can be released again for disassembly, maintenance, and adjustment, and because their threads are standardized.
2. Fastening a nut is still largely done by people or by specialized tools, and dexterous robots that operate with human tools and parts could one day take over such assembly work in a world built for humans.
3. Teaching a robot to thread raises three difficulties at once: the skill has to be learned in simulation and transferred to hardware although thread contact is very hard to simulate, a dexterous hand has a high-dimensional action space with countless ways to solve the task, and threading is a long-horizon cyclic task.
4. A single RL policy cannot be trained on the whole cyclic task, because reward shaping over many phases and the transitions between them breaks down.
5. This thesis decomposes during data generation (a privileged RL turning skill chained with scripted release and return) and unifies at deployment (one visuomotor student distilled by conditional flow matching).
6. The student is trained on simulated data only, sustains consecutive threading cycles in simulation, and is transferred zero-shot to a physical dexterous hand-arm system.

**Framing rule:** the thesis is about robotic threading. Long-horizon learning, dexterity, and sim-to-real transfer are the difficulties that threading poses, and each part of the method answers one of them.

**Level-of-detail rule:** the Introduction stays at the level of the problem and the approach. Implementation numbers (turn angle per cycle, cycle count, nut sizes, rates) first appear in Chapter 3. The specific hardware (robot, hand, camera) first appears in Chapter 5.

## 1. Introduction

Goal: lead a reader with an engineering background from "why threading matters" to "why it is hard for a robot" to "how this thesis solves it". This chapter sets the tone for all later reasoning.

### 1.1 Motivation: threaded joints in assembly

What a threaded joint is and why it matters in assembly: it can be released again (field assembly, disassembly, maintenance, adjustment), its threads are standardized, and the thread turns a large rotation into a small axial travel, so assembling the joint means turning the nut along the thread. Kept to one paragraph, using only the verified claims in [threading_sources.md](threading_sources.md).

Then: how threading is automated today (nutrunners, screwdriving spindles, fixtures, parts presented in a fixed pose) and where that stops working (varying parts, unstructured cells, small batches, maintenance and disassembly). This leads to the vision: dexterous hands that use the same parts and tools as people, so that robots can help in manufacturing and assembly in a world built for humans.

Handover: if a dexterous robot should thread, it has to learn the skill. How?

Sources: Niemann et al. (Maschinenelemente 1, Ch. 10) and Shigley (Ch. 8). Only verified claims are used; see [threading_sources.md](threading_sources.md).
Figure placeholder instead of a statistic: one figure with three or four examples of how threading is automated today (for example a handheld or stationary nutrunner, a multi-spindle station, a robot with a screwdriving end effector, a fixture that presents the part in a fixed pose). In the .tex: a `\fbox` filler per panel and a `% TODO(figure)` note. Images need a license or a citable source; manufacturer press images usually allow this with attribution.

### 1.2 Problem: how can a robot learn threading?

Three difficulties, each in its own short subsection or paragraph group. Each ends with the requirement it puts on the method.

**(a) Learning in simulation and transferring zero-shot.**
Learning on hardware is slow and unsafe, so the skill is learned in simulation. Thread contact is among the hardest things to simulate: engaged threads produce thousands of simultaneous contacts, and faithful simulation is too expensive for the parallel rollouts that RL needs. Any simplification opens a gap in contact and perception that the transfer has to close.
Requirement: a tractable thread model and a transfer recipe that needs no real data.

**(b) Threading with a dexterous hand.**
A multi-fingered hand on an arm has a high-dimensional action space, and the task has a huge solution space: people thread with a single finger, a pinch, or a multifingered grasp depending on resistance. Exploration and reward design become hard, and the grasp has to be acquired, kept under load, and released, which parallel-jaw systems with a pre-grasped nut avoid.
Requirement: a learned policy that controls the hand, with the solution space narrowed to one grasp strategy (pinch).

**(c) Threading as a long-horizon cyclic task.**
What a long-horizon cyclic task is: a fixed sequence of phases repeated many times while the task state advances (here approach, grasp, turn, release, return, while the nut rises by a fraction of a pitch each cycle). Why such tasks are relevant: much of assembly and everyday manipulation is repetitive (threading, screwing, cranking, winding, wiping). Why they are difficult: errors compound across cycles, transitions between phases are where failures occur, reward shaping and credit assignment over the whole horizon break down for a single RL policy, and policy chaining moves the problem to the transitions and leaves several policies at deployment.
Requirement: a training signal that is easy to specify per phase, and one deployable policy that sustains many cycles.

Handover to 1.3: the three requirements together point to one approach, decomposing the task into a hybrid privileged teacher for data generation and unifying it in one student for deployment. No hardware and no implementation numbers (robot model, turn angle, cycle count) appear here.

**[open]** Second alternative to policy chaining to name in (c). Citations for each claim; search `library.bib` first.

### 1.3 Approach

The three requirements lead to the method in one paragraph and the teaser figure: a simplified kinematic thread model makes PPO feasible; a privileged RL teacher learns the pinch-grasp turn; scripted release and return chain it into multi-cycle demonstrations (decompose during data generation); one flow-matching student distills them and runs the whole cycle from RGB-D (unify at deployment); a calibrated camera model, a metric point cloud, and visual randomization carry it to hardware without real data.

### 1.4 Research Questions

Three questions, aligned with the ablation questions of the NUTS paper (Sec. IV.C):

- RQ1 (long horizon): Does one student distilled from complete multi-cycle demonstrations sustain consecutive threading cycles better than a single-cycle policy invoked repeatedly? (NUTS Q1)
- RQ2 (student design): Which student design distills the hybrid-teacher demonstrations into a policy that sustains the cyclic task: a flow-matching action head compared with deterministic regression (LSTM, Transformer), and a point-cloud encoder compared with an image-space encoder? (NUTS Q2 and Q3 merged)
- RQ3 (sim-to-real): Can a student trained on simulated demonstrations only transfer zero-shot to the physical system? (Replaces NUTS Q4)

No mention of the exposé.

**Deliberate divergence from NUTS on RQ3.** NUTS closes the sim-to-real gap with human-corrected real-world replays (its Q4). The thesis instead asks whether the gap can be closed without any real data. The thesis has to deal with the paper's evidence: there, the sim-only student (ablation e) completed only 2.1 ± 1.4 cycles on hardware. Chapter 3.4 must state what changed in the sim-only pipeline since then (camera calibration, visual randomization, metric crop, encoder pretraining), and Chapter 5 must report the new zero-shot trials against that baseline, whatever the outcome.

**[open]** All NUTS ablation numbers for (a) to (d) used the real-world-augmented data set and must be rerun on the sim-only data before they can answer RQ1 and RQ2 (already a TODO in Chapter 4).

### 1.5 Contributions

1. A formulation of cyclic nut threading as a phase sequence with cyclic and episodic tracking errors, and a hybrid teacher that generates multi-cycle demonstrations with physically gated phase boundaries.
2. A unified visuomotor student distilled by conditional flow matching, with a systematic ablation of its components.
3. A zero-shot sim-to-real recipe: calibrated camera model, metric point cloud, visual randomization, shared Cartesian action path.
4. An evaluation in simulation and on hardware across nut sizes and geometries.

Plus attribution to the semester thesis and the advisor.

### 1.6 Outline

One paragraph per chapter.

Handover: the reader knows why threading matters, the three difficulties, the approach, and the questions.

## 2. State of the Art

Goal: background needed for the method, and the related work ordered along the three difficulties.

### 2.1 Theoretical Background

- Threaded joints and the thread geometry needed later (pitch, axial advance per revolution, self-locking friction). Short, only what the thread model uses.
- RL with privileged information: PPO, asymmetric actor-critic.
- Imitation learning and compounding error: behavior cloning, DAgger.
- Generative action heads: diffusion and conditional flow matching.
- Visual representations for manipulation: point clouds versus image encoders; the DP3 point-cloud encoder (`Ze2024`).
- Operational-space control: the impedance law of the action path, from the textbooks: Modern Robotics, Ch. 11.4 "Motion Control with Torque or Force Inputs" (`Lynch2017`), and the Springer Handbook of Robotics, Ch. 8 "Motion Control" (`Chung2016`) and Ch. 9 "Force Control" (`Villani2016`); null space projections (`Dietrich2015`). This also grounds the difference between the dynamically consistent projector in simulation and the damped pseudoinverse projector on the real robot (Chapter 5).

### 2.2 Related Work

- Robotic assembly and threading: classical automation, Factory, FORGE, IndustReal, dexterous threading and screwing (DexScrew, Play2Perfect).
- Dexterous manipulation with learned policies.
- Sim-to-real transfer for contact-rich manipulation.
- Long-horizon tasks and policy chaining.
- Teacher-student and visuomotor distillation.

Handover: no prior work threads a nut over many cycles with learned grasping and re-grasping on a dexterous hand.

## 3. Methodology

Goal: present the method so that each part visibly answers one difficulty of Section 1.2.

### 3.1 Problem Formulation

Phase sequence, cyclic and episodic tracking errors, objective, partial observability.

### 3.2 System

Hand-arm platform; simplified thread simulation (answers difficulty a); shared action contract and impedance controller.

**[open]** The simulation uses a model of the real robot. Under the level-of-detail rule, either describe it generically here (seven-DoF arm, five-fingered hand, three commanded pinch DoF) and name the products in 5.1, or accept naming them here as part of the simulated system.

### 3.3 Privileged Teacher

Asymmetric recurrent PPO for the pinch-grasp turn: observations, reward, domain randomization, curriculum (answers difficulty b).

### 3.4 Hybrid Teacher and Demonstration Generation

Cyclic rollout with scripted release and return, physical phase gating, disturbance augmentation, dataset (answers difficulty c, data side). Sim-to-real design choices: camera model, metric representation, visual randomization, shared action path (answers difficulty a, transfer side).

### 3.5 Student Distillation by Conditional Flow Matching

Why offline distillation, flow-matching objective, architecture (point-cloud encoder, fusion, progress and phase conditioning, Transformer velocity network, chunking, temporal ensembling), offline training, online DAgger variant, baselines (answers difficulty c, deployment side).

**[open]** Online DAgger here or only in the experiments.

### 3.6 Evaluation Protocol

Evaluation ladder and metrics.

Handover: every component is defined; Chapter 4 tests them.

## 4. Experiments in Simulation

- 4.1 Setup: data set, budgets.
- 4.2 Teacher training: turn teachers, hybrid rollout (32 of 32 ten-cycle runs).
- 4.3 Main ablations (RQ1 and RQ2): single-cycle, ResNet, LSTM regression, Transformer regression, full method (10.0 cycles, cyclic error -1.77 degrees). Results (a) to (d) pending.
- 4.4 Design ablations: action contract, progress and phase conditioning, encoder and pretraining, sweeps, robustness.
- 4.5 Offline versus online distillation.

Handover: the method works in simulation; does it transfer?

**[open]** Single-seed design ablations: main text, appendix, or rerun. Ablation inventory to the appendix.

## 5. Experiments on Real Hardware (RQ3)

- 5.1 Hardware setup: robot, camera calibration, controller, angle measurement, test objects.
- 5.2 Zero-shot transfer protocol.
- 5.3 Training nut sizes: M24, M30, M36 hexagonal.
- 5.4 Unseen geometries: octagonal, rectangular, round.
- 5.5 Long-horizon stress.

All results pending.

## 6. Discussion

- 6.1 Interpretation per RQ.
- 6.2 Offline flow distillation versus online DAgger.
- 6.3 Action and observation contracts.
- 6.4 What this means for robotic assembly: how far the result is from industrial threading (engaged start, no tightening torque, one grasp strategy, cycle time).
- 6.5 Limitations.

Drop the "Answers to the Questions of the Exposé" section.

## 7. Conclusion and Future Work

Conclusion returns to the assembly motivation: what a dexterous robot can now do in threading and what is missing. Future work: autonomous engagement of a loose nut, tightening to a preload with force feedback, longer horizon with learned phase inference, measured sensor randomization, other grasp topologies.

## Coherence checks

1. Each difficulty of Section 1.2 has one method component that answers it, one experiment that tests it, and one paragraph in the Discussion.
2. Every RQ is tested in Chapter 4 or 5 and answered in the Conclusion.
3. Every contribution is backed by a named experiment.
4. The Conclusion closes the loop to the assembly motivation of Section 1.1.
5. Pending results do not change the storyline.
