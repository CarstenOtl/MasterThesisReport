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

Goal: lead a reader with an engineering background from "why threading matters" to "why it is hard for a robot" to the research questions, and only then to the approach. Structure after the advisor's review (November 2026): problem, then research questions, then approach and contributions together.

### 1.1 Motivation

Threaded joints in assembly, how threading is automated today and where that stops working, the vision of dexterous robots in a world built for humans, Moravec's paradox. Formal register, no colloquial examples.

### 1.2 Problem Statement

Four difficulties with scientific subsection titles. Each ends with the requirement it puts on the method.

- 1.2.1 Contact Explosion in Thread Simulation: thousands of contacts, SDF contact (Factory), penetration-based solvers, exploitable shortcut through the flanks. Requirement: a cheap, non-exploitable thread model.
- 1.2.2 Curse of Dimensionality of a Multi-Fingered Hand: action-space dimension, solution space of grasp strategies, grasp acquisition and release that parallel-jaw systems avoid. Requirement: one learned hand-arm policy narrowed to the pinch.
- 1.2.3 Compounding Error in a Long-Horizon Cyclic Task: definition, relevance, compounding error, transitions, reward shaping and credit assignment, policy chaining and whole-task imitation as the two answers. Requirement: a per-phase training signal and one deployable policy.
- 1.2.4 Sim-to-Real Transfer without Real-World Data: contact, perception, and actuation gaps, cost of real data. Requirement: a transfer recipe without real data.

Closes with the research gap (no prior work threads over many grasp-and-release cycles with a dexterous hand from simulated data alone).

### 1.3 Research Questions

RQ1 (long horizon), RQ2 (policy design), RQ3 (sim-to-real), each tied to the difficulty it follows from. Phrased at the level of the problem, not of the method.

### 1.4 Approach and Contributions

One paragraph on decompose-during-data-generation, unify-at-deployment, mapped to the four difficulties, plus the teaser figure. Exactly three contributions, each with a one-clause "how": (1) hybrid teacher for cyclic threading, (2) unified flow-matching student with ablations, (3) zero-shot sim-to-real recipe and hardware evaluation. Attribution to the advisor.

### 1.5 Outline

## 2. State of the Art

Goal: only the theories the method uses, then related work along the four difficulties. Operational-space control is engineering and lives in Appendix A (`sec:app-osc`); the impedance law itself is stated in 3.3.2.

### 2.1 Theoretical Background

- 2.1.1 Reinforcement Learning for the Privileged Teacher: MDP, policy gradient, actor-critic, GAE, asymmetric critic, PPO, reward shaping.
- 2.1.2 Imitation Learning and Policy Distillation: BC, compounding error, DAgger, teacher-student distillation (offline vs online), action chunking and temporal ensembling, multimodality.
- 2.1.3 Conditional Flow Matching and Its Relation to Diffusion Policy: generative heads, Diffusion Policy, flow-matching objective, straight vs curved paths, head on a backbone.
- 2.1.4 Simulation of Threaded Contact: pitch and axial advance, contact count, SDF contact, penetration-based resolution, hand-over to the kinematic thread model of 3.3.1.

### 2.2 Related Work

- 2.2.1 Learning-Based Robotic Assembly and Fastening
- 2.2.2 Dexterous Manipulation with Multi-Fingered Hands
- 2.2.3 Visual Representations for Visuomotor Policies
- 2.2.4 Policy Chaining in Long-Horizon Tasks
- 2.2.5 Distillation of Privileged Teachers into Visuomotor Policies
- 2.2.6 Research Gap

## 3. Methodology

Mirrors the NUTS paper (Sec. III). No hardware description here; the platform is in 4.2.

- 3.1 Problem Formulation: phase sequence, cyclic and episodic tracking errors, objective, POMDP.
- 3.2 Overview of the Distillation Pipeline: the three steps and the pipeline figure.
- 3.3 Privileged Teacher Policy Training: 3.3.1 Simplified Thread Simulation, 3.3.2 Action Contract and Controller (impedance law `eq:osc`, derivation in Appendix A), 3.3.3 Observations, Reward, and Training.
- 3.4 Dataset Construction with the Hybrid Teacher: cyclic rollout, disturbance augmentation, vision data collection, dataset format.
- 3.5 Student Policy Distillation by Conditional Flow Matching: objective, architecture, offline training.

## 4. Experiments

Mirrors the NUTS paper (Sec. IV).

- 4.1 Evaluation Metrics: evaluation ladder, metrics.
- 4.2 Experimental Setup: hand-arm platform, perception and calibration, deployment controller, test objects and angle measurement, training and inference hardware, zero-shot transfer protocol.
- 4.3 Ablations: teacher and demonstrations, ablated students (a)-(e).
- 4.4 Results: ablations in simulation, zero-shot transfer on the training nut, generalization across nut sizes and geometries, long-horizon stress.
- 4.5 Summary.

## 5. Discussion

- 5.1 Interpretation per RQ.
- 5.2 Action and observation contracts.
- 5.3 What this means for robotic assembly.
- 5.4 Limitations.

## 6. Conclusion and Future Work

Conclusion returns to the assembly motivation: what a dexterous robot can now do in threading and what is missing. Future work: autonomous engagement of a loose nut, tightening to a preload with force feedback, longer horizon with learned phase inference, measured sensor randomization, other grasp topologies.

## Coherence checks

1. Each difficulty of Section 1.2 has one method component that answers it, one experiment that tests it, and one paragraph in the Discussion.
2. Every RQ is tested in Chapter 4 or 5 and answered in the Conclusion.
3. Every contribution is backed by a named experiment.
4. The Conclusion closes the loop to the assembly motivation of Section 1.1.
5. Pending results do not change the storyline.
