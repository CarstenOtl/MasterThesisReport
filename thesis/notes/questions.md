# Questions the report must answer

Running list. Add questions as they come up. For each one, note where the report answers it and whether the answer is backed (citation, number, or result). Status: `todo`, `drafted`, `done`.

## Motivation: threading and assembly

| # | Question | Where | Status | Notes |
|---|----------|-------|--------|-------|
| M1 | What is a threaded joint, and why does it matter in assembly? | 1.1 | drafted | Niemann Ch. 10 and Shigley Ch. 8; see [threading_sources.md](threading_sources.md). "Most widely used" dropped as unverified. |
| M2 | Which properties of threaded joints are worth stating? | 1.1 | drafted | Keep only verified ones: releasable, standardized, the thread turns rotation into axial travel. |
| M3 | How is threading automated in industry today, and where does that stop working? | 1.1 | todo | Nutrunners, fixtures, fixed part poses. |
| M4 | Why use a dexterous hand instead of a nutrunner or a parallel gripper? | 1.1, 6.4 | todo | An engineering reader will ask this first. |
| M5 | What does "robots in a world built for humans" mean for assembly? | 1.1 | todo | |

## Problem: how can a robot learn threading?

| # | Question | Where | Status | Notes |
|---|----------|-------|--------|-------|
| P1 | Why learn the skill in simulation instead of on hardware? | 1.2a | todo | |
| P2 | Why is thread contact so hard to simulate? | 1.2a, 3.2 | todo | Factory: thousands of contacts. |
| P3 | Is the kinematic thread model a valid simplification, and what does it leave out? | 3.2, 6.5 | todo | |
| P4 | What causes the sim-to-real gap here (contact, perception, control)? | 1.2a, 3.4 | todo | |
| P5 | Why does a dexterous hand make the problem hard (action dimension, solution space)? | 1.2b | todo | |
| P6 | How do humans thread a nut, and why does this thesis use the pinch grasp? | 1.2b | todo | Check whether Feix 2016 actually supports the grasp claims. |
| P7 | Why are only three hand DoF commanded? | 3.2 | todo | |
| P8 | What is a long-horizon cyclic task? | 1.2c | todo | Needs a definition and examples. |
| P9 | Why are long-horizon cyclic tasks relevant beyond threading? | 1.2c | todo | |
| P10 | What makes long-horizon tasks difficult (compounding error, transitions, reward shaping, credit assignment)? | 1.2c | todo | Citations. |
| P11 | Was a single end-to-end RL policy for the full cyclic task tried, and why did it fail? | 1.2c, 3.3 | todo | NUTS says reward design proved too hard. Report concretely if there is evidence. |
| P12 | Why not policy chaining at deployment? | 1.2c, 2.2 | todo | |

## Method

| # | Question | Where | Status | Notes |
|---|----------|-------|--------|-------|
| X1 | Why a 60 degree turn per cycle and ten cycles per trial? | 3.1 | todo | One hex face per cycle. |
| X2 | Why does the trial start with the nut already engaged? | 3.2, 6.5 | todo | |
| X3 | Why are release and return scripted instead of learned? | 3.4 | todo | |
| X4 | Why distill into one student instead of deploying the hybrid teacher? | 3.4, 3.5 | todo | The teacher needs privileged state. |
| X5 | Why flow matching instead of regression or diffusion? | 3.5 | todo | |
| X6 | Why offline distillation instead of DAgger, when DAgger was the original plan? | 3.5, 4.5, 6.2 | todo | |
| X7 | Why a point cloud instead of RGB images? | 3.5, 4.3 | todo | |
| X8 | Why the Cartesian action contract instead of joint space? | 3.2, 4.4 | todo | |
| X9 | What do the progress scalar and the phase encoding do, and are they a form of cheating? | 3.5, 4.4 | todo | Phase comes from physical events at deployment. |
| X10 | Why the Franka arm instead of the Tiangong 2 the project started on? | 3.2 | todo | |

## Results and discussion

| # | Question | Where | Status | Notes |
|---|----------|-------|--------|-------|
| R1 | Does the multi-cycle student beat the single-cycle student? | 4.3 | todo | Ablation (a) pending. |
| R2 | Does flow matching beat the regression heads? | 4.3 | todo | Ablations (c), (d) pending. |
| R3 | Does the point cloud beat the ResNet encoder? | 4.3 | todo | Ablation (b) and pose probe pending. |
| R4 | Does the student transfer zero-shot, and on which nut sizes and geometries? | 5 | todo | Hardware pending. |
| R5 | How far is the result from industrial threading (tightening torque, cycle time, loose-nut start)? | 6.4 | todo | |
| R6 | How sensitive is the student to camera calibration error? | 6.5 | todo | Not quantified yet. |
