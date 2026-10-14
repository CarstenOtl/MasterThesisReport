TUM School of Engineering and Design
Technical University of Munich




In collaboration with Agile Robots SE




Semester Thesis


DAgger-Based Distillation of an RL-Trained
Privileged Grasping Policy for a Dexterous
Hand–Arm System: Towards Safer Training
DAgger-basierte Destillation einer RL-trainierten priv-
ilegierten Greifstrategie für ein geschicktes Hand-Arm-
System: Hin zu sichererem Training




Supervisor                 Prof. Dr.-Ing. habil. Alois C. Knoll

Advisor                    Chi Zhang, M.Sc.

Author                     Carsten Oertel

Date                       April 20, 2026 in Munich
Disclaimer


I confirm that this Semester Thesis is my own work and I have documented all sources and
material used.




Munich, April 20, 2026                                          (Carsten Oertel)
Acknowledgments


This thesis was conducted in collaboration with Agile Robots SE, Munich. The author was
employed at Agile Robots SE during the course of this work, and the research was carried
out using computational and hardware resources provided by Agile Robots SE, including
the Agile Hand dexterous manipulator and GPU infrastructure for reinforcement learning
training. The author gratefully acknowledges Agile Robots SE for their support, in particular
Antonio Gonzales Marin, M.Sc., for his supervision on the industry side.
Abstract

Dexterous multi-fingered hands are hardware-ready, yet there is no off-the-shelf recipe for
training grasping policies on a new hand–arm system that transfer from simulation to real
hardware without extensive retuning. This thesis presents a dexterous grasping pipeline for a
23-degree-of-freedom Agile Hand on a Franka Research 3 arm. A privileged teacher policy is
trained with Proximal Policy Optimization (PPO) under automatic domain randomization on
8 different objects, reaching 99.0 % grasp success at 12.2 % unsafe-episode rate. The teacher
is distilled into an RGB-based student using SafeDAgger. The resulting student reaches 97.0 %
grasp success, about 98 % of the teacher’s lifting performance. Benchmarked against two al-
ternative distillation baselines, behavioral cloning and DAgger, SafeDAgger achieves both
higher lift success (97.0 % vs. 87.8 % for Behavioral Cloning (BC) and 83.4 % for DAgger)
and the lowest unsafe-episode rate (38.3 % vs. 41.4 % for BC and 52.2 % for DAgger). To-
gether, these results establish a dexterous grasping pipeline in which safety-aware distillation
produces the best task performance and the safest student among the compared methods.




Kurzfassung

Mehrfingrige geschickte Roboterhände sind hardwareseitig einsatzbereit, doch es fehlt an
einem standardisierten Rezept, um Greifstrategien auf einem neuen Hand-Arm-System zu
trainieren, die ohne aufwändiges Nachjustieren vom Simulator auf reale Hardware übertrag-
bar sind. Diese Arbeit stellt eine Pipeline für geschicktes Greifen mit einer 23-Freiheitsgrad
Agile Hand auf einem Franka Research 3 Arm vor. Ein privilegierter Lehrer wird mit PPO
unter automatischer Domain-Randomization auf 8 verschiedenen Objekten trainiert und er-
reicht 99,0 % Greiferfolg bei 12,2 % unsicheren Episoden. Der Lehrer wird mittels SafeDAg-
ger in einen RGB-basierten Schüler destilliert. Der resultierende Schüler erreicht 97,0 %
Greiferfolg, rund 98 % der Hebeleistung des Lehrers. Im Vergleich zu zwei alternativen Des-
tillationsbaselines, Behavioral Cloning und DAgger, erzielt SafeDAgger sowohl den höheren
Greiferfolg (97,0 % gegenüber 87,8 % bei BC und 83,4 % bei DAgger) als auch die niedrigste
Rate unsicherer Episoden (38,3 % gegenüber 41,4 % bei BC und 52,2 % bei DAgger). Zusam-
men etablieren diese Ergebnisse eine Pipeline für geschicktes Greifen, in der sicherheitsbe-
wusste Destillation sowohl die beste Aufgabenleistung als auch den sichersten Schüler unter
den verglichenen Methoden liefert.
Contents


Acknowledgments                                                                                             v

List of Figures                                                                                           xii

List of Tables                                                                                            xiii

List of Abbreviations                                                                                      xv

1 Introduction                                                                                              1
  1.1 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      1
  1.2 Research Frontier . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       2
  1.3 Contributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       2
  1.4 Thesis Outline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      2

2 Related Work                                                                                              5
  2.1 Dexterous Grasping with Multi-Fingered Hands . . . . . . . . . . . . . . . . . . . .                  5
       2.1.1 Analytical and Data-Driven Grasp Synthesis . . . . . . . . . . . . . . . . .                   5
       2.1.2 Reinforcement Learning Based Grasping Policies . . . . . . . . . . . . . .                     6
  2.2 Privileged Policy Distillation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        6
       2.2.1 Imitation Learning and DAgger . . . . . . . . . . . . . . . . . . . . . . . . .                7
       2.2.2 Safety-Aware Distillation . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            7
  2.3 Sim-to-Real Transfer through Domain Randomization . . . . . . . . . . . . . . . .                     7

3 Methods                                                                                                  9
  3.1 Problem Formulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          9
  3.2 Privileged Teacher Training . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         10
      3.2.1 Asymmetric Actor–Critic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           10
      3.2.2 Reward Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          12
      3.2.3 Automatic Domain Randomization . . . . . . . . . . . . . . . . . . . . . . .                  12
  3.3 Policy Distillation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   13
      3.3.1 DAgger and SafeDAgger Based Distillation . . . . . . . . . . . . . . . . . .                  13
      3.3.2 RGB-Based Perception . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            15

4 Experiments and Results                                                                                 17
  4.1 Experimental Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        17
      4.1.1 Teacher Policy Training . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           17
      4.1.2 Student Policy Distillation . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         19
      4.1.3 Evaluation Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          19
  4.2 Ablation Studies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      20
      4.2.1 Safety Threshold Calibration . . . . . . . . . . . . . . . . . . . . . . . . . . .            21
      4.2.2 DAgger vs. SafeDAgger vs. Behavior Cloning . . . . . . . . . . . . . . . . .                  21
x                                                                                                    Contents



    4.3 Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   21
        4.3.1 Teacher Training Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          21
        4.3.2 Safety Threshold Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            22
        4.3.3 Distillation Method Comparison Results . . . . . . . . . . . . . . . . . . . .                24
    4.4 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     27

5 Discussion and Conclusion                                                                                 29
  5.1 Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      29
       5.1.1 Offline vs. Online Distillation . . . . . . . . . . . . . . . . . . . . . . . . . . .          29
       5.1.2 SafeDAgger Dominates BC and DAgger . . . . . . . . . . . . . . . . . . . .                     29
       5.1.3 Calibration and the Non-Monotonic Threshold-Performance Curve . . .                            30
  5.2 Limitations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     30
  5.3 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      31
  5.4 Future Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       31

A Training Configuration and Domain Randomization                                                           33
  A.1 PPO Hyperparameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           33
  A.2 Network Architecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          33
  A.3 Automatic Domain Randomization Parameters . . . . . . . . . . . . . . . . . . . .                     34
  A.4 Full Results Including Physics Instability . . . . . . . . . . . . . . . . . . . . . . . .            34
  A.5 Per-Object Failure Mode Breakdowns . . . . . . . . . . . . . . . . . . . . . . . . . .                35

Bibliography                                                                                                37
List of Figures


 2.1 Illustration of domain randomization. A single calibrated simulation (red cir-
     cle) may not match reality (green triangle), but a sufficiently wide distribution
     of randomized simulations (dashed ellipses) can encompass the real-world
     conditions, enabling zero-shot transfer. Figure from [21]. . . . . . . . . . . . . .           8

 3.1 Teacher training pipeline. A privileged teacher policy is trained using PPO with
     an asymmetric actor–critic architecture. The critic receives full privileged state
     information, while the actor observes only noisy proprioceptive observations
     processed through an LSTM-based recurrent network. The policy outputs joint
     position targets at 60 Hz, which are tracked by PD controllers running at the
     simulation frequency of 120 Hz. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
 3.2 Student distillation pipeline using SafeDAgger. The frozen teacher policy pro-
     vides teacher actions a T from noisy state observations, while the student pol-
     icy produces actions aS from stereo RGB images and proprioception. The
     safety policy evaluates the inverse-variance-weighted L2 action disagreement
     between teacher and student to determine whether the student may act au-
     tonomously or the teacher must intervene, controlled by the safety threshold δ. 14
 3.3 Stereo visual encoder used in the student policy, adapted from [5]. (a) Left and
     right camera frames are encoded by a shared ResNet-18 into token sequences,
     which are processed by a two-layer cross-view transformer; the output of the
     learnable [embed] token is projected into a 64-dimensional stereo embedding.
     (b) The cross-attention mask: the [embed] token attends to all tokens, while
     left-view and right-view tokens attend only to each other and the [embed]
     token. Intra-view attention is disabled. . . . . . . . . . . . . . . . . . . . . . . . . . 16

 4.1 Hardware platform: (a) the 16-DoF Agile Hand manufactured by Agile Robots
     SE, and (b) the combined FR3 arm–hand system as rendered in the Isaac Sim
     simulation environment. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   18
 4.2 The 8 training objects used for teacher and student policies. . . . . . . . . . . . .         18
 4.3 Teacher policy grasping rollout on the basketball shoe, showing the four phases
     produced by the policy: approach, contact, lift, and hold. . . . . . . . . . . . . .          22
 4.4 Weighted L2 action disagreement e t (eq. (3.7)) over training in the pure DAg-
     ger reference run. The blue trace shows the raw per-step values; the red line
     is a moving mean averaged over the preceding w = 100 iterations; the shaded
     curve shows the rolling 70th percentile (p70) averaged over the preceding
     w = 500 iterations, meaning 70 % of e t values in that averaging window fall
     below this boundary. The green band marks the resulting calibration range
     δ ∈ [2.0, 4.0] used for the threshold sweep. . . . . . . . . . . . . . . . . . . . . . .      23
 4.5 Observed SafeDAgger intervention rate β over training iterations for each
     swept threshold. Lower thresholds produce higher and more persistent in-
     tervention; higher thresholds decay quickly toward DAgger behaviour. . . . . .                23
xii                                                                                                List of Figures



      4.6 GSR and UER as a function of δ, with BC and DAgger as endpoints. The curve
          is non-monotonic: a lift peak at δ = 3.0 (97.0 %) and a secondary peak at
          δ = 3.4 are separated from the BC region by a dip at δ ∈ [1.0, 2.0]. δ = 3.0 is
          used for SafeDAgger in Section 4.3.3. . . . . . . . . . . . . . . . . . . . . . . . . . .            24
      4.7 SafeDAgger student grasping rollout on the basketball shoe across the four
          phases (approach, contact, lift, hold). Top row: third-person scene view. Bot-
          tom row: corresponding left stereo RGB frame passed to the student’s visual
          encoder. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   25
      4.8 Training curves for BC (green), SafeDAgger at δ = 3.0 (blue), and DAgger
          (orange) over 100k distillation iterations. (a) BC’s lift reflects the teacher’s
          performance since the teacher always acts; SafeDAgger and DAgger show the
          student’s own lift. (b) DAgger maintains the highest training-time unsafe rate;
          SafeDAgger reduces it through targeted intervention; BC’s rate reflects the
          teacher’s own unsafe rate. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         26
      4.9 Per-object standalone evaluation for all swept SafeDAgger thresholds, with BC
          and DAgger as endpoints. (a) Lift success varies by object geometry, with
          compact shapes performing reliably across all methods. (b) Unsafe-episode
          rate shows the largest method-dependent gaps on collision-prone objects. . . .                       27

      A.1 ADR parameter ranges. Blue bars indicate the full randomization range at
          maximum ADR level. Red diamonds mark the nominal start values. The thumb
          velocity limit spans the widest relative range, from 20 rad/s (simulation) to
          0.21 rad/s (hardware limit). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         34
      A.2 Per-object unsafe-episode rate across the threshold sweep (physics excluded).
          Each cell shows the UER for one object at one threshold. The basketball shoe
          and turtle candle holder exhibit the highest rates across most thresholds. . . .                     35
      A.3 Per-object unsafe-episode rate across the threshold sweep (physics included).
          Physics-instability events raise the overall rates but do not change the relative
          ordering across methods. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         36
List of Tables


 3.1 Observation components for the asymmetric actor–critic. The actor receives
     only information available on the real robot; the critic additionally receives
     privileged simulation state. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     11
 3.2 Reward terms for teacher policy training. d denotes hand-to-object distance,
     θ the palm alignment angle, nc the number of finger contacts, mc a binary
     contact mask, ∆a the action delta, and q̇ joint velocities. Weights marked ⋆
     are ADR-modulated; ranges give the endpoints. . . . . . . . . . . . . . . . . . . .              12
 3.3 Automatic Domain Randomization parameters. All parameters share a single
     increment counter. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   13

 4.1 Episode termination conditions. All early terminations mark the state as un-
     safe; penalty-eligible conditions additionally trigger rterm when they occur be-
     fore any object contact. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
 4.2 Teacher policy per-object evaluation (200 episodes per object, ADR-0 physics). 22
 4.3 Safety threshold sweep (100k iters, 32 envs, 640 eval eps). Best in bold. . . . . 23
 4.4 BC vs. DAgger vs. SafeDAgger standalone evaluation (640 episodes, 32 envi-
     ronments). SafeDAgger uses the best threshold δ = 3.0 from Section 4.3.2.
     UER excludes physics-instability events; Section A.4 reports the full breakdown. 24
 4.5 BC checkpoint sweep (640 episodes per checkpoint, 32 environments). Lift
     success peaks at 50k iterations and degrades thereafter, while UER remains
     consistently high. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26

 A.1 PPO hyperparameters for teacher training. . . . . . . . . . . . . . . . . . . . . . . .          33
 A.2 Automatic Domain Randomization parameters. . . . . . . . . . . . . . . . . . . . .               34
 A.3 Teacher policy per-object evaluation including physics instability (200 episodes
     per object, ADR-0 physics). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      35
List of Abbreviations


RL      Reinforcement Learning
DRL     Deep Reinforcement Learning
BC      Behavioral Cloning
PPO     Proximal Policy Optimization
MDP     Markov Decision Process
POMDP Partially Observable Markov Decision Process
DR      Domain Randomization
ADR     Automatic Domain Randomization
DoF     Degree of Freedom
FR3     Franka Research 3
GWS     Grasp Wrench Space
GSR     Grasp Success Rate
UER     Unsafe Episode Rate
MLP     Multilayer Perceptron
LSTM    Long Short-Term Memory
USD     Universal Scene Description
Chapter 1

Introduction


This chapter motivates the problem of dexterous robotic grasping, states the specific chal-
lenges addressed in this work, summarizes the contributions, and outlines the structure of
this thesis.



1.1   Motivation

Multi-fingered dexterous hands offer robots the potential to interact with the world in a
manner approaching human versatility. Unlike parallel-jaw grippers, which are limited to
a narrow set of grasp geometries, anthropomorphic hands can conform to arbitrary object
shapes, reorient objects in-hand, and wield tools [1]. Despite this potential, high Degree
of Freedom (DoF) hands remain largely confined to research laboratories. The core bottle-
neck is not hardware, as several capable platforms exist, including the Allegro Hand, the
Shadow Dexterous Hand, and the Agile Hand used in this work, but rather the difficulty of
synthesizing reliable control policies for contact-rich tasks.
    Traditional analytic approaches to grasp planning rely on known object models and pre-
cise contact modeling, assumptions that rarely hold in unstructured environments [2]. Learning-
based methods, particularly Deep Reinforcement Learning (DRL), have recently demon-
strated impressive dexterous manipulation capabilities in simulation [3, 4]. However, trans-
ferring these policies to real hardware introduces a fundamental challenge: during training,
RL agents have access to privileged information (exact object poses, contact forces, full state
vectors) that is unavailable at deployment time, where the robot must rely on noisy sensory
observations such as camera images.
    The dominant strategy to bridge this gap is policy distillation, in which a privileged teacher
policy is trained in simulation with full state access and its behavior is then distilled into a
student policy that operates from realistic sensor inputs [5, 6]. The DAgger algorithm [7]
is widely used for this distillation step, as it addresses the distribution shift between teacher
demonstrations and student-induced trajectories through iterative data aggregation. Yet DAg-
ger is agnostic to safety: it queries the teacher uniformly, including in states where the student
already performs well, and does not prevent the student from visiting dangerous states during
training. For dexterous hands, where unsafe actions can cause hardware damage (e.g., jam-
ming or overloading finger joints) or lead to unstable contact configurations, a safety-aware
distillation procedure is desirable.
2                                                                                1 Introduction



1.2    Research Frontier

From the situation outlined above, a general problem emerges: dexterous multi-fingered
hands are hardware-ready, yet no scalable recipe exists for obtaining grasping policies that
are simultaneously deployable on real hardware (i.e., driven by realistic sensor inputs rather
than privileged state) and safe to train, in the sense that the training procedure itself does
not rely on repeatedly visiting states that would damage the hand or the object on a physical
system.
    The currently dominant pipeline, in which a privileged Reinforcement Learning (RL)
teacher is trained in simulation and subsequently distilled into a sensor-based student, ad-
dresses the first requirement but not the second. Standard distillation algorithms treat the
student purely as an imitation target and provide no mechanism to avoid unsafe states en-
countered during the student’s own rollouts. As dexterous grasping moves closer to real-
world deployment, this gap becomes the limiting factor: the cost of an unsafe episode is
no longer a reset in simulation but potential hardware damage, and the question of how a
student policy is trained becomes as important as the final task performance it achieves.
    This thesis therefore addresses the problem of distilling a privileged dexterous grasping
teacher into a vision-based student in a way that is both effective in terms of grasp success
and explicit about training-time safety, and asks under what conditions such a safety-aware
distillation can match or improve upon the standard approach.



1.3    Contributions

The main contributions of this semester thesis are:

    1. Dexterous grasping environment in Isaac Lab: An RL environment in Isaac Lab for
       training arm-hand grasping policies with the Agile Hand and Franka Research 3 (FR3).

    2. Privileged teacher policy: A trained RL teacher policy that achieves robust dexterous
       grasping of diverse objects in simulation using privileged state information.

    3. SafeDAgger-based distillation: A comparative study of DAgger versus SafeDAgger for
       distilling the privileged teacher into a vision-based student, evaluating both task per-
       formance (Grasp Success Rate (GSR)) and training safety (number of unsafe episodes).



1.4    Thesis Outline

The remainder of this thesis is structured as follows:

Chapter 2 reviews related work on dexterous grasping, policy distillation methods (DAgger,
    SafeDAgger), and sim-to-real transfer for manipulation.

Chapter 3 formalizes the problem as a Partially Observable Markov Decision Process (POMDP),
    derives the privileged teacher training objective, and presents the mathematical frame-
    work for DAgger and SafeDAgger distillation.

Chapter 4 describes the experimental setup, presents teacher training results, and compares
    three distillation methods: BC, DAgger, and SafeDAgger.
1.4 Thesis Outline                                                                         3



Chapter 5 discusses the findings, limitations, and directions for future work in the master’s
    thesis.
Chapter 2

Related Work


This chapter reviews prior work along the three axes most relevant to this thesis: dexterous
grasping with multi-fingered hands, privileged policy distillation, and sim-to-real transfer
through domain randomization. Each section traces how the field evolved, highlights the
strengths and limitations of each paradigm, and motivates the choices made in this work.



2.1     Dexterous Grasping with Multi-Fingered Hands

Dexterous grasping with anthropomorphic hands has been studied for decades, but only re-
cently have learned policies begun to outperform classical pipelines on unstructured object
sets. This section contrasts analytical and learning-based paradigms, tracing how the limita-
tions of the former motivated the shift to the latter.


2.1.1   Analytical and Data-Driven Grasp Synthesis

Classical robotic grasping formulates the problem as finding contact points on a known object
surface that satisfy force closure, meaning that the contact wrenches alone can resist arbitrary
external loads [8, 9]. Given a 3D object model and friction parameters, analytical planners
search for contact configurations that maximize a quality metric such as the largest wrench
ball inscribable in the Grasp Wrench Space (GWS) [9]. For parallel-jaw grippers in structured
industrial settings, these methods have been highly successful. In practice, classical dexterous
systems organize perception, grasp planning, trajectory generation, and post-grasp manipula-
tion as independent pipeline stages with hand-tuned parameters per robot and object set [8,
10].
    Later work replaced the combinatorial search with data-driven methods while retaining
the analytical grasp-quality objective. DexGraspNet [11] generated 1.32 million grasps for
over 5,000 objects using a differentiable force-closure estimator, and Wu et al. [2] demon-
strated 86.7 % grasp success on novel objects with a learned generative model.
    The principal advantage of analytical and data-driven planning is interpretability: grasp
quality can be verified against well-understood physical criteria before execution. However,
these methods share two fundamental limitations. First, the search space grows to SE(3)×Rnh
for an nh -jointed hand, making exhaustive planning intractable for multi-fingered hands [8].
Second, all variants produce static grasp configurations that are executed by a separate con-
troller and cannot adapt if conditions differ from the assumed model; whenever the object
geometry, contact physics, or robot kinematics are wrong, as is unavoidable for novel objects,
deformable materials, or worn hardware, the planned grasp fails [1]. Errors compound across
the pipeline, and the absence of online adaptation prevents recovery from perturbations.
6                                                                               2 Related Work



2.1.2   Reinforcement Learning Based Grasping Policies

The static, non-adaptive nature and model dependence of analytical methods motivate a
fundamentally different paradigm: RL, which jointly learns perception, grasp strategy, and
reactive control from interaction [1]. Instead of relying on pre-specified grasp taxonomies,
the policy discovers contact strategies through trial and error in simulation, producing closed-
loop controllers that can react to perturbations at every time step.
    Kumar et al. [12] were among the first to demonstrate model-based RL for contact-rich
manipulation on a 24-DoF hand. Andrychowicz et al. [13] then showed that a Shadow Dex-
terous Hand could learn to solve a Rubik’s Cube through massive-scale RL in simulation fol-
lowed by sim-to-real transfer, establishing the viability of learned dexterous manipulation on
real hardware. DeXtreme [3] combined vectorized Automatic Domain Randomization (ADR)
with a vision-based pose estimator for robust in-hand cube reorientation on a real Allegro
Hand. DexPBT [14] applied population-based training to discover reward weights and hy-
perparameters automatically. UniDexGrasp++ [15] decomposed the problem into a learned
grasp proposal stage followed by goal-conditioned RL execution, achieving generalization to
novel objects.
    While much of this work targets in-hand manipulation with a fixed wrist, real applications
require coordinated arm-hand control: reaching, grasping, and transporting an object as a
single behavior. DextrAH-G [6] addressed this with a 23-motor arm-hand system, combin-
ing geometric fabrics [16] as a structured low-level control layer with an RL policy on top,
achieving fast and safe dexterous grasping from depth images. DextrAH-RGB [5] extended
this to RGB input and demonstrated the first successful sim-to-real transfer of an RGB-based
dexterous grasping policy.
    The key advantage of learned policies is closed-loop reactivity and the ability to handle
novel objects without explicit models. The key limitation is the sim-to-real gap: policies
trained with privileged simulation state (object poses, contact forces) do not directly transfer
to a real robot that observes only camera images and joint encoders. This gap motivates the
privileged teacher–student distillation paradigm discussed in the next section. This thesis
builds on DextrAH-RGB but trains the teacher as a standard RL policy without geometric
fabrics, accepting a less constrained controller in exchange for a simpler training stack and
the ability to use a custom hand asset (the Agile Hand on a Franka Research 3).



2.2     Privileged Policy Distillation

The sim-to-real gap identified in the previous section means that the most effective simulation-
trained policies, which rely on privileged state such as object poses and contact forces, cannot
be deployed directly. Bridging this gap requires transferring the teacher’s behavior to a stu-
dent that observes only what is available on the real robot.
    Knowledge distillation, introduced by Hinton et al. [17], was originally developed to com-
press a large teacher network into a smaller student network with minimal loss in accuracy.
The core idea is to train the student to reproduce the teacher’s output distribution rather than
the ground-truth labels alone, so that the student inherits not only the teacher’s decisions but
also its uncertainty structure. An alternative is the Mixture of Experts (MoE) paradigm, which
combines multiple specialist sub-networks through a learned gating mechanism rather than
consolidating knowledge into a single student.
    Privileged teacher–student distillation in robotics adapts the distillation framework to a
different problem: not model compression, but modality transfer. The teacher operates on
privileged simulation state (object poses, contact forces), while the student must produce
2.3 Sim-to-Real Transfer through Domain Randomization                                           7



the same behavior from deployable observations such as RGB images and proprioception [5,
6]. Because teacher and student observe fundamentally different inputs, the student cannot
simply copy the teacher’s internal representations; instead, it must learn a new perception
front-end while imitating the teacher’s actions. This makes the distillation step an imitation-
learning problem, and the quality of the transfer depends critically on how the training data
is collected. The following subsections discuss the imitation-learning algorithms used for this
purpose.


2.2.1   Imitation Learning and DAgger

BC fits a policy by supervised regression on a fixed dataset of teacher state–action pairs [18].
It is straightforward but brittle: small deviations from the teacher’s state distribution lead the
student into states the dataset never covered, compounding errors cause the policy to drift
off-distribution, and performance degrades [7].
     DAgger [7] addresses this by iteratively rolling out the current student policy, querying
the teacher at each visited state, and aggregating the new labels into the training set. After
N iterations, DAgger provably finds a policy whose performance is bounded by εN + O(1/N ),
where εN is the best achievable loss on the aggregated dataset. Because the student drives
data collection, the dataset gradually covers the states the student actually visits, and the
compounding-error problem of BC is largely eliminated. DAgger is the distillation method
used in DextrAH-G [6] and DextrAH-RGB [5], which form the basis of the present work.


2.2.2   Safety-Aware Distillation

DAgger has two practical drawbacks for dexterous manipulation. First, it queries the teacher
at every visited state, including states where the student already acts correctly, which is query-
inefficient. Second, it offers no mechanism to prevent the student from visiting dangerous
states during its own rollouts; the student is allowed to fail freely as long as the teacher label
is recorded afterwards. For dexterous hands, where unsafe actions can damage finger joints
or destroy the manipulated object, this is unsatisfactory.
    SafeDAgger [19] addresses both issues with a safety-dependent gating mechanism that
decides, at every time step, whether the student or the teacher should execute the next action.
Whenever the student’s proposed action deviates too far from the teacher’s, the system hands
control to the teacher, intercepting dangerous actions before execution. This mixed-control
scheme reduces both the number of teacher queries and the number of unsafe states visited
during training. The result is an implicit curriculum: early in training the teacher drives most
of the trajectory, while later the student takes over in regions it has mastered.
    This thesis directly compares DAgger and SafeDAgger as the distillation algorithm
for a privileged dexterous grasping teacher. To the best of the author’s knowledge, no prior
work has reported a head-to-head comparison of DAgger and SafeDAgger for arm-hand dex-
terous grasping with a vision-based student.



2.3     Sim-to-Real Transfer through Domain Randomization

Training entirely in simulation avoids the cost and risk of real-world data collection but in-
troduces the sim-to-real gap, referring to discrepancies between simulated and real physics,
perception, and actuation. Domain Randomization (DR) is the dominant strategy for closing
8                                                                                               2 Related Work



this gap: simulation parameters are varied across training episodes so that the policy learns
to be robust to a wide distribution of conditions [20]. The underlying hypothesis, illustrated
in Figure 2.1, is that if the real world falls within the distribution of randomized simulations,
the policy will generalize at deployment time without fine-tuning.




Figure 2.1: Illustration of domain randomization. A single calibrated simulation (red circle) may not match reality
(green triangle), but a sufficiently wide distribution of randomized simulations (dashed ellipses) can encompass
the real-world conditions, enabling zero-shot transfer. Figure from [21].


    In dexterous manipulation, the most commonly randomized parameters are object prop-
erties (mass, friction, scale), actuator characteristics (joint stiffness, damping, effort limits),
kinematic perturbations (link masses, center-of-mass offsets), and sensor noise (observation
delays, measurement variance) [3, 13, 22]. For contact-rich tasks such as grasping, fric-
tion and actuator gains are particularly influential because they directly determine whether
a grasp is stable or slips.
    Peng et al. [22] demonstrated zero-shot sim-to-real transfer of locomotion and manip-
ulation policies through dynamics randomization, and the same idea underlies the in-hand
reorientation results of Andrychowicz et al. [13]. A drawback of manually selected random-
ization ranges is that they are difficult to calibrate: too narrow, and the real world falls
outside the training distribution; too wide, and the task becomes so hard that learning fails.
ADR [23] automates this trade-off by gradually widening the parameter ranges based on
policy performance, producing an emergent curriculum from easy to hard. Handa et al. [3]
showed in DeXtreme that vectorized ADR on top of GPU-accelerated simulation is sufficient
to transfer in-hand manipulation policies trained purely in simulation to a real Allegro Hand
without any motion-capture system.
    ADR is the strategy adopted for the teacher policy in this thesis (Chapter 4), with a cur-
riculum schedule custom-designed for the Agile Hand and FR3 hardware.
Chapter 3

Methods


This chapter formalizes the dexterous grasping problem and presents the mathematical frame-
work underlying the two-stage privileged teacher–student pipeline. Section 3.1 states the
problem as a partially observable decision process and gives the optimization objective. Sec-
tion 3.2 presents the privileged teacher training, including the asymmetric actor–critic that
exploits privileged state information. Section 3.3 introduces the distillation framework: DAg-
ger and its safety-aware variant SafeDAgger, and the visual encoder architecture used for
RGB-based student policies.



3.1    Problem Formulation

Reinforcement learning problems are typically formalized as a Markov Decision Process (MDP),
a mathematical model of sequential decision making under uncertainty [24]. An MDP is de-
fined by the tuple (S , A, P, R, γ), where S is the set of possible states of the world, A is the
set of actions the agent can take, P : S × A → ∆(S ) is the transition function that gives the
probability distribution over the next state given the current state and action, R : S × A → R
is the reward function that scores how good a state–action pair is, and γ ∈ [0, 1) is a discount
factor that determines how much future rewards are valued relative to immediate ones. The
defining property of an MDP is the Markov property: the next state depends only on the cur-
rent state and action, not on the full history of past states; in other words, the current state is
a sufficient summary of everything the agent needs to know about the past in order to make
an optimal decision. At each time step t , the agent observes the current state s t , selects an
action a t according to its policy π(a t | s t ), receives a reward R(s t , a t ), and transitions to a new
state s t+1 ∼ P(· | s t , a t ). The agent’s task is to find a policy that maximizes the expected sum
of discounted rewards collected over time.
    The dexterous grasping task studied in this thesis does not fit the standard MDP model,
because at deployment the robot cannot directly measure the full state of the world. It only
sees noisy and incomplete sensory measurements: joint encoders and camera images, but
not, for example, the exact pose of the object or the contact forces at each fingertip. Such
problems are described by a POMDP, which extends the MDP with an explicit observation
channel that mediates between the underlying state and what the agent actually perceives.
A POMDP is defined by the tuple

                                       M = (S , A, O, P, O, R, γ),                                 (3.1)

which adds, on top of the MDP elements, an observation space O and an observation function
O : S → ∆(O) that returns the distribution over possible observations given the true (hidden)
state. The full state s t ∈ S contains the joint configuration and velocities of the arm–hand
10                                                                                                     3 Methods



system, the object pose, velocity, and physical properties, and contact information. At de-
ployment, the agent does not have access to s t directly; instead, it receives an observation
o t ∼ O(· | s t ) consisting of proprioceptive measurements and camera images, and must choose
its action based on this partial view alone.
     The objective is to find a policy π : O → ∆(A) that maximizes the expected discounted
return                                            T                
                                                  X
                                                      t
                                       J(π) = Eπ     γ R(s t , a t ) .                    (3.2)
                                                       t=0
Solving eq. (3.2) directly under partial observability is difficult because the policy must si-
multaneously learn what to do (the manipulation skill) and how to perceive (extracting task-
relevant information from raw sensor data). The privileged teacher–student paradigm de-
couples these two challenges by training the teacher policy π∗ on an information-complete
observation function Opriv that is only available in simulation, and subsequently distilling π∗
into a student policy π̂ that operates on the realistic observation function Opartial available at
deployment. The remainder of this chapter formalizes both stages.



3.2     Privileged Teacher Training

The teacher is trained via PPO on an asymmetric actor–critic architecture that exploits privi-
leged state information at training time while keeping the actor restricted to the observations
that will be available at distillation time. Figure 3.1 illustrates the overall teacher training
pipeline.




Figure 3.1: Teacher training pipeline. A privileged teacher policy is trained using PPO with an asymmetric actor–
critic architecture. The critic receives full privileged state information, while the actor observes only noisy pro-
prioceptive observations processed through an LSTM-based recurrent network. The policy outputs joint position
targets at 60 Hz, which are tracked by PD controllers running at the simulation frequency of 120 Hz.




3.2.1   Asymmetric Actor–Critic

In an asymmetric actor–critic [25], the actor (policy) and critic (value function) receive dif-
ferent observation vectors. Let oactor
                                 t     denote the teacher’s actor observation and ocritic
                                                                                      t    the
3.2 Privileged Teacher Training                                                                              11



critic observation, where ocritic
                           t      contains additional privileged information beyond oactor
                                                                                     t     , such
as object velocities and contact forces. The actor parameterizes a Gaussian policy

                               πθ (a t | oactor              actor      2
                                                                          
                                          t     ) = N µ θ (o t     ), σ θ ,                 (3.3)

while the critic estimates the state–value function
                                            T −t                        
                                            X
                                  critic           k
                            Vφ (o t ) ≈ Eπ        γ R(s t+k , a t+k ) s t .                               (3.4)
                                                   k=0

This asymmetry allows the critic to use richer information for more accurate value estimates
during training, while the actor learns a policy that depends only on the subset of state that
will subsequently be available to the student through distillation. In effect, the privileged in-
formation is consumed by the critic to shape gradients but never directly enters the deployed
policy.
    In the dexterous grasping scenario studied in this thesis, the asymmetry is particularly
pronounced. Table 3.1 summarizes the observation components for actor and critic. The
critic observes the full simulation state, including per-body positions and velocities for the
palm and all five fingertips (54D), object linear and angular velocity (6D), aggregate contact
forces (3D), and measured joint torques for all 28 DOFs including coupled joints (23 actuated
+ 5 mimic), none of which are available on the real robot. The actor, by contrast, receives
only the palm center position and velocity (6D), proprioceptive joint measurements, and a
scalar object identifier, which are the same inputs that the student will later receive alongside
its RGB images. Because the critic is discarded after training, the privileged information it
consumes does not affect the deployed policy [25]. The teacher’s actor therefore already
operates on the same proprioceptive interface that will be available on the real robot, and
distillation only needs to add visual perception on top.

Table 3.1: Observation components for the asymmetric actor–critic. The actor receives only information available
on the real robot; the critic additionally receives privileged simulation state.

       Component                                 Description                            Actor    Critic
       Joint positions and velocities            All 23 actuated joints                   46       46
       Hand body positions                       Palm + 5 fingertip positions              6       18
       Hand body velocities                      Linear + angular per body                 –       36
       Previous action                                                                    23       23
       Object position and orientation           Position (3D) + quaternion (4D)           7        7
       Object goal position and scale                                                      4        4
       Scalar object identifier                                                            1        1
       Object velocity (privileged)              Linear (3D) + angular (3D)                –       6
       Contact forces (privileged)               Aggregate fingertip forces                –        3
       Measured joint torques (privileged)       All 28 DOFs (incl. coupled)               –       28
       Total                                                                              87      172


    The action space is 23-dimensional, consisting of joint position targets for all 7 arm joints
and 16 hand joints. Actions are scaled from the policy’s normalized output a t ∈ [−1, 1]23 to
absolute joint position targets using per-joint scaling factors. The policy directly commands
joint positions without geometric fabrics or motion primitives, which distinguishes this work
from the FGP-based approach in DextrAH-RGB [5].
12                                                                                                       3 Methods



3.2.2   Reward Structure

The reward function decomposes as a signed, weighted sum of K terms,

                                      K
                                      X
                    R(s t , a t ) =         signi ·w i · ri (s t , a t ),   signi ∈ {+1, −1}, w i > 0,       (3.5)
                                      i=1


where each ri ≥ 0 is a non-negative per-term reward and signi determines whether the term
acts as an incentive (+) or a penalty (−). Positive terms encourage desired behavior, while
negative terms penalize undesirable behavior. Table 3.2 summarizes the reward and penalty
terms used in this thesis, including their functional forms and weights. The lift and goal terms
are gated by a contact mask mc , ensuring the policy only receives reward for lifting when
actually grasping the object rather than accidentally launching it. Hand joints are penalized
1.5× more than arm joints for action rate and 3× more for joint velocity, encouraging smooth
finger motions.

Table 3.2: Reward terms for teacher policy training. d denotes hand-to-object distance, θ the palm alignment
angle, nc the number of finger contacts, mc a binary contact mask, ∆a the action delta, and q̇ joint velocities.
Weights marked ⋆ are ADR-modulated; ranges give the endpoints.

                   Term        Purpose                            Form                       Weight
                    rhand      Hand-to-object ap-                  w·e   −αd
                                                                                               +4.0
                               proach
                    rpalm      Palm alignment                     −w · θ 2                     +0.7
                    rcurl      Finger curl penalty                −w · ∥q − qref ∥2         0.3 → 0.8⋆
                    rcontact   Hand-object con-                    w · nc                      +3.0
                               tact
                    rgrasp     Thumb + finger in                   w · 1[thumb ∧ finger]       +3.0
                               contact
                    rlift      Lift after stable                   w · e−α|z−z g | · mc     40 → 30⋆
                               contact
                    rgoal      Object-to-goal dis-                 w · e−αd g · mc            +40.0
                               tance
                    rtime      Proximity      time                 w · 1[d < 0.2]            +0.005
                               bonus
                    rsuccess   Goal region bonus                   w · 1[at goal]             +20.0
                                                                                2
                    raction    Action rate penalty                −w · ∥∆a∥                    0.01
                    rvel       Joint       velocity               −w · ∥q̇∥2                  5·10−4
                               penalty
                    rterm      Early termination                  −w · 1[no contact]           1.0
                               penalty




3.2.3   Automatic Domain Randomization

To produce a teacher that transfers across varying physical conditions, the training environ-
ment applies ADR [23]. Let ξ ∈ Ξ denote the vector of randomizable simulation parameters
such as friction, mass, and actuator gains. ADR maintains an interval [ξlo     hi
                                                                          i , ξi ] for each pa-
                                lo hi
rameter and samples ξi ∼ U (ξi , ξi ) at every episode reset. Whenever the policy’s rolling
success rate exceeds a threshold τADR , a shared increment counter n is advanced and each
3.3 Policy Distillation                                                                                    13



interval is interpolated from its initial range toward its maximum range,

                                        start, lo/hi        n  max, lo/hi    start, lo/hi
                                                                                           
                          ξlo/hi
                           i
                                 (n) = ξi              +       ξi          − ξi              ,       (3.6)
                                                           Nmax

yielding an emergent curriculum from near-nominal physics to progressively more chal-
lenging conditions. The curriculum uses Nmax = 50 increments and a success threshold
τADR = 0.4. Table 3.3 lists the key randomized parameters and their start/max ranges. The
maximum ranges for finger joint stiffness and damping correspond to values measured on
the real Agile Hand hardware, and the thumb rotation velocity limit is ramped toward the
hardware limit of approximately 12 deg/s (≈ 0.21 rad/s).
    In addition to physics-parameter randomization, ADR controls an external wrench per-
turbation applied to the grasped object. Whenever the hand is within a proximity threshold
of the object, random forces and torques are applied at each perturbation interval, with mag-
nitudes scaled by the object mass. The maximum linear acceleration is ramped from 0 to
10 m/s2 over the ADR schedule, forcing the teacher to develop robust force-closure grasps
that resist progressively stronger perturbations.

  Table 3.3: Automatic Domain Randomization parameters. All parameters share a single increment counter.


                 Parameter                                   Start Range           Max Range
                 Object mass scale                             [1.0, 1.0]            [0.5, 2.0]
                 Object friction (static)                      [1.0, 1.0]            [0.5, 1.5]
                 Robot restitution                             [1.0, 1.0]            [0.8, 1.0]
                 Arm stiffness scale                           [1.0, 1.0]            [0.5, 2.0]
                 Arm damping scale                             [1.0, 1.0]            [0.5, 2.0]
                 Finger MCP pitch stiffness                    [1.0, 1.0]           [0.17, 1.0]
                 Finger MCP pitch damping                      [1.0, 1.0]          [0.083, 1.0]
                 Finger MCP yaw stiffness                      [1.0, 1.0]          [0.025, 1.0]
                 Finger PIP stiffness                          [1.0, 1.0]           [0.02, 1.0]
                 Thumb rotation velocity limit                [20.0, 20.0]      [0.21, 20.0] rad/s
                 Object wrench max. accel.                       [0, 0]            [0, 10] m/s2




3.3     Policy Distillation

Given a trained teacher π∗ operating on privileged observations, the goal of distillation is to
train a student policy π̂θ : Opartial → A that imitates π∗ using only the partial observations
available at deployment. This section presents the distillation algorithms (DAgger and its
safety-aware variant SafeDAgger) and the visual encoder architecture used when the student
operates on RGB images. Figure 3.2 illustrates the overall student distillation pipeline.


3.3.1   DAgger and SafeDAgger Based Distillation

BC on a fixed dataset of teacher trajectories suffers from compounding errors: small devi-
ations from the teacher’s state distribution lead the student into unvisited states, causing
the policy to drift and fail [7]. DAgger [7] addresses this by iteratively collecting data un-
der the student’s own policy while labelling it with the teacher’s actions. However, DAgger
14                                                                                                   3 Methods




Figure 3.2: Student distillation pipeline using SafeDAgger. The frozen teacher policy provides teacher actions a T
from noisy state observations, while the student policy produces actions aS from stereo RGB images and proprio-
ception. The safety policy evaluates the inverse-variance-weighted L2 action disagreement between teacher and
student to determine whether the student may act autonomously or the teacher must intervene, controlled by the
safety threshold δ.



does not prevent the student from visiting dangerous states during data collection, which is
unsatisfactory for dexterous hands where unsafe actions can damage hardware.
   This thesis therefore adopts SafeDAgger [19], which augments DAgger with a safety gate.
Since the teacher is queried at every state to label the dataset, the learned safety classifier of
Zhang and Cho [19] is redundant; the action disagreement can be computed directly. Let

                                           dim
                                                                                        2
                                            XA       µθ ,i (ostudent
                                                             t       ) − µ∗i (oteacher
                                                                               t       )
                                   et =                                                                    (3.7)
                                            i=1               σ∗i 2 (oteacher
                                                                      t       )

denote the per-step inverse-variance-weighted L2 action disagreement, where µθ and µ∗ are
the mean actions of the student and teacher and σ∗i 2 is the teacher’s predicted variance for
action dimension i . This is the same per-step quantity used as the action imitation loss in
eq. (3.10), so SafeDAgger’s safety gate and the supervision signal share a single scale. The
executed action is selected by thresholding e t against a safety threshold δ > 0:
                               ¨
                                   π̂θ (ostudent )     if e t ≤ δ (student acts),
                        at =             t
                                                                                                           (3.8)
                                   π (oteacher
                                     ∗
                                       t       )       otherwise (teacher intervenes).

Setting δ → ∞ recovers vanilla DAgger; δ → 0 recovers pure BC. The threshold δ is cali-
brated empirically so that roughly 20–30 % of environments are flagged unsafe at the start
of distillation; the intervention rate then decays naturally as the student improves, providing
an implicit curriculum from teacher-guided to student-autonomous execution. The calibra-
tion procedure is detailed in Section 4.2.1. The complete procedure is given in Algorithm 1;
highlighted lines mark the safety-gating additions relative to vanilla DAgger.
3.3 Policy Distillation                                                                                       15



Algorithm 1 Online SafeDAgger with direct action-disagreement gating. Blue lines indicate
the safety-gating modifications that distinguish SafeDAgger from vanilla DAgger.
 1: Initialize student π̂θ , safety threshold δ > 0
 2: for each time step t in rollout do
 3:    Query teacher: a∗t = π∗ (oteacher
                                       t     )
 4:    Compute action disagreement e t as in eq. (3.7)
 5:    if e t ≤ δ then
 6:         Execute a t = π̂θ (ostudent
                                t        )                                                         ▷ Student acts
 7:    else
 8:         Execute a t = a∗t                                                                ▷ Teacher intervenes
 9:    end if
10:    Update π̂θ on (ostudent
                          t      , a∗t ) using eq. (3.9)
11: end for
12: return π̂θ



    Unlike classical DAgger, which accumulates an aggregated dataset across iterations and
retrains the student on the full history, the implementation used here updates the student
online using only the current-step teacher label, without maintaining a replay buffer.
    The student is optimized under a combined loss

                                  L(θ ) = Laction (θ ) + λaux Laux (θ ),                                    (3.9)

consisting of an action imitation term and an auxiliary regularization term. The action loss is
the inverse-variance-weighted L2 loss from DextrAH-RGB [5], in which each action dimension
i is rescaled by the teacher’s per-dimension variance σ∗i 2 :

                                           dim
                                                                                    2
                                            XA   µθ ,i (ostudent
                                                         t       ) − µ∗i (oteacher
                                                                           t       )
                          Laction (θ ) =                                                 ,                (3.10)
                                           i=1            σ∗i 2 (oteacher
                                                                  t       )

where µθ and µ∗ are the mean actions of the student and teacher. Dimensions in which the
teacher is confident (small σ∗ ) contribute more strongly, while uncertain dimensions con-
tribute less, yielding an automatic weighting that does not require hand-tuning arm-versus-
hand action scales. The auxiliary loss Laux = ∥x̂obj − xobj ∥22 regresses the ground-truth object
position from the visual encoder’s representation, providing an additional learning signal that
regularizes the encoder toward spatially meaningful features.


3.3.2   RGB-Based Perception

The student replaces the teacher’s privileged object state with stereo RGB images. This thesis
reuses the visual encoder architecture from DextrAH-RGB [5].
    A stereo pair is used rather than a single camera because the student must infer the 3D
position of the object without access to the privileged pose that the teacher saw; a stereo
pair encodes parallax, which resolves the metric depth ambiguity of monocular images. The
left and right RGB frames are passed through a shared (Siamese) ResNet-18 [26] backbone,
producing 128 tokens of dimension 128 per view. These tokens, together with a learnable
[embed] token, are fed into a two-layer transformer with a cross-attention mask that permits
attention only between views, forcing the network to learn implicit stereo correspondences
without explicit depth supervision (Figure 3.3). The output of the [embed] token is pro-
jected by an Multilayer Perceptron (MLP) into a 64-dimensional stereo embedding, which
16                                                                                                      3 Methods



is concatenated with proprioception and fed into an Long Short-Term Memory (LSTM) (512
hidden units) that provides temporal context across time steps. The entire stack is optimized
jointly under the inverse-variance-weighted L2 loss (eq. (3.10)).




      Ileft




     Iright


              (a) Stereo encoder architecture.                              (b) Cross-attention mask.

Figure 3.3: Stereo visual encoder used in the student policy, adapted from [5]. (a) Left and right camera frames are
encoded by a shared ResNet-18 into token sequences, which are processed by a two-layer cross-view transformer;
the output of the learnable [embed] token is projected into a 64-dimensional stereo embedding. (b) The cross-
attention mask: the [embed] token attends to all tokens, while left-view and right-view tokens attend only to each
other and the [embed] token. Intra-view attention is disabled.


   In addition to the dynamics gap addressed by ADR, the sim-to-real gap acquires a visual
component when the student operates on camera images. Following DextrAH-RGB [5], visual
domain randomization is applied during distillation to mitigate this: at each episode reset,
dome-light HDRI backgrounds, material properties (albedo, roughness, metallic constant) of
the robot, table, and object, as well as object and table textures are randomized. Additional
data augmentations include color jitter and motion blur.
Chapter 4

Experiments and Results


This chapter describes the experimental realization of the methods introduced in Chapter 3.
Section 4.1 presents the experimental setup, covering teacher policy training (Section 4.1.1),
student policy distillation (Section 4.1.2), and the evaluation metrics (Section 4.1.3). Sec-
tion 4.2 describes the ablation studies and their rationale. Section 4.3 reports the results for
both teacher training and distillation.



4.1     Experimental Setup

All experiments are conducted in Isaac Lab 2.1.0 [27] (Isaac Sim 5.1.0) on a single NVIDIA
RTX 4090 GPU. The simulation runs at 120 Hz with a policy control frequency of 60 Hz.
The robotic platform consists of a FR3 7-DoF arm equipped with a 16-DoF Agile Hand (Agile
Robots SE), forming a 23-DoF arm–hand system controlled via joint position targets with sim-
ulated PD controllers (Figure 4.1). The arm and hand are combined into a single articulated
Universal Scene Description (USD) asset with convex-hull collision meshes. The observation,
action, and reward design are defined in Sections 3.2.1 and 3.2.2.


4.1.1   Teacher Policy Training

The teacher is trained with PPO on 1,024 parallel environments with ADR following the
formulation in Section 3.2.3. The teacher is trained on a set of 8 different objects (Figure 4.2),
spanning compact graspable shapes (teddy bear, closed fist) to thin and irregular objects
(toy excavator, basketball shoe). At episode reset, each environment is assigned one object
uniformly at random, and the object’s mass, friction, and scale are randomized within the
ADR ranges. Each episode lasts up to 10 s (600 steps) and terminates early if any unsafe
condition from Table 4.1 is triggered. These termination conditions are reused as unsafe-
event signals for SafeDAgger’s intervention logic during distillation. An episode is considered
successful if the object is lifted above the table and held for at least 0.5 s (30 steps). When the
rolling success rate across all environments exceeds the ADR threshold τADR = 0.4 (40 %), the
randomization ranges are widened by one increment, progressively increasing the difficulty
of the training distribution.
    To encourage robust force closure, random external wrenches (forces and torques) are
applied to the object whenever the hand is within 0.3 m. New perturbation directions are
sampled every 120 steps (∼1 s), with magnitudes scaled by the object mass. The maximum
linear acceleration is ramped by ADR from 0 to 10 m/s2 , exposing the teacher to progres-
sively stronger perturbations as training advances. During distillation and evaluation, ADR
18                                                                                        4 Experiments and Results




            (a) The physical Agile Hand.                                    (b) FR3 + Agile Hand in Isaac Sim.

Figure 4.1: Hardware platform: (a) the 16-DoF Agile Hand manufactured by Agile Robots SE, and (b) the com-
bined FR3 arm–hand system as rendered in the Isaac Sim simulation environment.



is disabled and the wrench magnitude is zero, so the student never experiences external
perturbations. Training hyperparameters are listed in Section A.1.




        (a) Mario                      (b) Milk pot            (c) Turtle candle holder          (d) Toy excavator




      (e) Teddy bear                  (f) Closed fist            (g) Basketball shoe              (h) Elephant toy

                       Figure 4.2: The 8 training objects used for teacher and student policies.
4.1 Experimental Setup                                                                                          19



Table 4.1: Episode termination conditions. All early terminations mark the state as unsafe; penalty-eligible condi-
tions additionally trigger rterm when they occur before any object contact.

        Condition                     Trigger                                                    Penalty
        object_escape_xy              Object’s XY position leaves a ±0.25 m × ±0.4 m                ✓
                                      area centered on the table surface
        object_too_low                Object falls more than 5 cm below the table sur-              ✓
                                      face
        hand_too_far                  Hand workspace body leaves the table footprint                ✓
                                      inflated by 0.35 m, or rises more than 1.35 m
                                      above the table surface
        hand_too_close                Any fingertip or palm comes within 1 cm of the                 –
                                      table surface
        palm_flip                     Palm direction deviates more than 108◦ from the               ✓
                                      target down-direction
        arm_table_contact             Arm contacts the table                                         –
        hand_vel_explosion            Any finger joint velocity exceeds 50 rad/s                     –
        robot_unstable                NaN or Inf detected in joint positions or velocities           –
        timeout                       Episode reaches Tmax = 10 s (600 steps at 60 Hz)               –


4.1.2   Student Policy Distillation

The student replaces the teacher’s privileged object state with stereo RGB images (320×240 at
30 fps) while retaining the proprioceptive inputs (joint positions/velocities, hand pose, goal
position, previous action). The student does not receive the object position, orientation, scale,
or contact information; these must be inferred from the visual input. The visual encoder,
cross-attention fusion, and LSTM policy head are described in Section 3.3.2.
    Distillation follows the SafeDAgger procedure from Algorithm 1 (Section 3.3.1), using
Adam with a learning rate of 1 × 10−4 and the combined loss from eq. (3.9). The teacher in-
tervenes whenever the per-environment weighted L2 action disagreement exceeds the safety
threshold δ. Training runs for 100,000 iterations across 32 parallel environments (4 environ-
ments per object), which produces stable per-object gradients during online distillation.


4.1.3   Evaluation Metrics

Three metrics are used to evaluate both teacher and student policies. Let τ ∈ {1, . . . , N }
index evaluation episodes and t ∈ {0, . . . , Tτ } index time steps within an episode. Evaluation
episodes use a horizon of 10 s and each configuration is evaluated over N = 640 episodes (80
per object).

Lift success (grasp with hold). Let hτt denote the object height above the table at time step
t of episode τ, and let H be a lift threshold. An episode is considered successful if the object
remains above H for at least Nhold consecutive steps:
                        Iτlift = I ∃ t : ∀ k ∈ {0, . . . , Nhold − 1}, hτt+k > H .
                                                                               
                                                                                           (4.1)
In this work, H = 0.15 m above the table surface and Nhold = 30 (0.5 s at 60 Hz). The hold
requirement prevents counting accidental upward launches as successful grasps. The GSR is
the primary task metric:
                                               N
                                            1 X τ
                                    GSR =         I .                                (4.2)
                                            N τ=1 lift
20                                                                      4 Experiments and Results



Unsafe episode rate.     An episode may terminate early due to one of four hardware-relevant
failure modes:
     • Harmful collision (m = coll): any fingertip or palm body frame drops within 1 cm of
       the table top, or any arm link contacts the table.

     • Object out of bounds (m = obj): the object’s XY position leaves the ±0.25 m × ±0.4 m
       area centered on the table surface, or the object falls more than 5 cm below the table
       surface.

     • Palm flipped (m = flip): the palm direction deviates more than 108◦ from the downward-
       facing target direction.

     • Hand too far (m = hf): the hand workspace body leaves the table footprint inflated by
       0.35 m, or rises more than 1.35 m above the table surface.

Let M = {coll, obj, flip, hf} denote this set of termination modes, and let Iτm ∈ {0, 1} indicate
whether mode m ∈ M occurs in episode τ. An episode is unsafe if any mode is triggered:
                                                          
                                      τ               τ
                                                  _
                                     Iunsafe = I     Im = 1 .                               (4.3)
                                                  m∈M

The Unsafe Episode Rate (UER) quantifies training-time safety:
                                                   N
                                              1 X τ
                                      UER =        I       .                               (4.4)
                                              N τ=1 unsafe

This definition excludes physics_instability events (NaN joint states, velocity explo-
sions), which are simulation-only artifacts that cannot occur on physical hardware. All UER
values reported in this thesis refer to this hardware-relevant definition unless stated other-
wise. Full results including physics instability are provided in Section A.4.

Failure-mode decomposition. Each episode is assigned a single terminal mode mτ ∈ M ∪
{timeout, success}. When multiple unsafe conditions trigger in the same time step, the first
condition (by a fixed priority order) is recorded. Per-mode rates are reported as:
                                              N
                                        1 X
                          FailRate(m) =       I[mτ = m],       m ∈ M.                      (4.5)
                                        N τ=1

This decomposition identifies which failure categories each distillation method is most prone
to.



4.2     Ablation Studies

The following ablation studies are conducted to justify the pipeline design. The first abla-
tion (Section 4.2.1) identifies a suitable SafeDAgger safety threshold δ via a sweep over the
weighted L2 action-disagreement distribution (eq. (3.7)) of an uncorrected DAgger student,
determining the operating point used as the SafeDAgger configuration in the subsequent
comparison. The second ablation (Section 4.2.2) compares the three distillation variants
BC, DAgger, and SafeDAgger at this threshold. All three variants use the same teacher, stu-
dent architecture, loss function, and training budget; only the data-collection strategy dif-
fers. The variants are evaluated in terms of lift-success growth, unsafe-episode rate, and
4.3 Results                                                                                  21



intervention
       P T −1 rate (defined as the fraction of time steps in which teacher takeover occurs,
β = T1 t=0 I[g t = 1], averaged over evaluation episodes) during training. Since the UER
is the primary safety metric, not only the average rate across all test objects is reported but
also a per-object, failure-mode decomposition to assess each method under different failure
conditions.


4.2.1   Safety Threshold Calibration

SafeDAgger’s behavior depends on the safety threshold δ, which controls how often the
teacher is allowed to override the student’s action. Zhang and Cho [19] selected a single
value from the error distribution of an initial supervised policy, targeting approximately 20–
30 % early intervention. Faithfully adapting this recipe to dexterous grasping requires the
distribution of the per-step disagreement e t (eq. (3.7)) measured on a student trained with-
out interventions. If the reference distribution of e t is taken from a SafeDAgger run instead,
the largest values are missing from it, because those are exactly the moments at which the
teacher had already overridden the student. This work therefore uses a pure DAgger baseline
(δ → ∞, no interventions) as the reference distribution on which the sweep range is defined.
    The DAgger run yields the empirical distribution of e t across training, which is used in
two stages. First, the averages of this distribution at different training phases define a mean-
ingful range of candidate thresholds. Thresholds well below the late-training average are
exceeded by e t at almost every step throughout training, so the teacher overrides the stu-
dent nearly always and SafeDAgger collapses toward BC behavior. Thresholds well above
the early-training average are essentially never exceeded, even at the start of training when
student-teacher disagreement is largest, so the teacher rarely intervenes and SafeDAgger be-
comes indistinguishable from DAgger. Second, within this range the threshold is swept in
fine increments to identify the best operating point empirically. A few low-end anchors and
the δ → ∞ DAgger endpoint are added to characterize the boundary regimes. The resulting
operating point is used for SafeDAgger in the method comparison of Section 4.2.2; the sweep
results are reported in Section 4.3.2.


4.2.2   DAgger vs. SafeDAgger vs. Behavior Cloning

The central experiment compares the three distillation methods at the best SafeDAgger thresh-
old identified from the sweep (Section 4.2.1). BC trains on teacher rollouts with the teacher
always driving the environment, DAgger collects data under the student’s own policy with
no intervention, and SafeDAgger adds safety-aware gating (Algorithm 1). All three use the
same teacher, student architecture, training budget, and evaluation protocol; only the data-
collection strategy differs.



4.3     Results

4.3.1   Teacher Training Results

The teacher policy was trained on the 8 objects shown in Figure 4.2 using 1,024 parallel
environments with a sim-to-real-aware ADR curriculum. Training reached ADR level 14 after
approximately 20,000 epochs and continued for 33,000 epochs total without further ADR
22                                                                               4 Experiments and Results



progression. The resulting teacher achieves 99.0 % GSR and 12.2 % UER at nominal (ADR-
0) physics, demonstrating reliable multi-object grasping with the hardware-realistic actuator
constraints. Table 4.2 reports the full per-object evaluation breakdown. Figure 4.3 shows
a representative grasping rollout, illustrating the four phases that the policy produces: ap-
proach, contact, lift, and hold. This teacher is used for all distillation experiments reported
below.




        (a) Approach                (b) Contact                   (c) Lift                    (d) Hold

Figure 4.3: Teacher policy grasping rollout on the basketball shoe, showing the four phases produced by the
policy: approach, contact, lift, and hold.



           Table 4.2: Teacher policy per-object evaluation (200 episodes per object, ADR-0 physics).

           Object                   Lift (%)      UER (%)    Coll. (%)       OOB (%)     Palm (%)
           basketball shoe              99.0         28.0            7.0         21.0           0.0
           closed fist                 100.0          9.0            0.0          9.0           0.0
           elephant toy                100.0          3.0            2.0          0.5           0.5
           mario                        98.0          2.0            0.0          1.0           0.0
           milk pot                     96.5          5.5            0.5          5.0           0.0
           teddy bear                   99.5         15.0            0.5         14.5           0.0
           toy excavator                99.0         10.5            2.0          7.5           1.0
           turtle candle holder        100.0         24.5            0.0         24.0           0.0
           Average (8 objects)          99.0         12.2           1.5          10.3           0.2




4.3.2    Safety Threshold Results

The weighted L2 action-disagreement distribution (eq. (3.7)) extracted from the DAgger
baseline (Figure 4.4) sets the sweep range. The distribution decays from an early-training
mean of ∼3.2 to a late-training mean of ∼1.9, with percentiles bracketing a meaningful sweep
range of δ ∈ [2.0, 4.0]. At each threshold in this range, the observed SafeDAgger intervention
rate β (Figure 4.5) confirms the relative ordering from the disagreement distribution: lower
δ produces higher and more persistent intervention, higher δ decays quickly toward DAgger
behavior.
    Table 4.3 and Figure 4.6 report the resulting lift success and unsafe-episode rate as a
function of δ, with BC (δ → 0) and DAgger (δ → ∞) as continuous-axis endpoints. The
response is non-monotonic. The curve exhibits multiple local peaks and dips across the swept
range, with the best GSR at δ = 3.0 (97.0 %). Given the noisy nature of the training pipeline,
the specific locations of these peaks and dips are likely sensitive to individual training seeds
and should not be over-interpreted as systematic effects of the threshold.
    The best SafeDAgger configuration is δ = 3.0, reaching 97.0 % GSR at 38.3 % UER. δ =
3.0 is used for SafeDAgger in all subsequent distillation experiments.
4.3 Results                                                                                                                                              23




                                                                         DAgger L2 over training
                        8
                                                                                                         Calibration range (2.0 4.0)
                                                                                                         Moving mean (w=100)
                        7                                                                                Rolling p70 (w=500)

                        6

                        5
              L2 loss




                        4

                        3

                        2

                        1

                        00            20                                     40               60                 80                 100
                                                                             Iteration (×103 )
Figure 4.4: Weighted L2 action disagreement e t (eq. (3.7)) over training in the pure DAgger reference run. The
blue trace shows the raw per-step values; the red line is a moving mean averaged over the preceding w =
100 iterations; the shaded curve shows the rolling 70th percentile (p70) averaged over the preceding w = 500
iterations, meaning 70 % of e t values in that averaging window fall below this boundary. The green band marks
the resulting calibration range δ ∈ [2.0, 4.0] used for the threshold sweep.




Table 4.3: Safety threshold sweep                                                 SafeDagger intervention rate across threshold sweep
(100k iters, 32 envs, 640 eval eps).                                                                                                       BC
Best in bold.
                                                                   1.0                                                                             4.0
                                                                                                                                                   3.8
                                                                                                                                                   3.6
                                                                                                                                                   3.4
   δ                    GSR    UER                                 0.8                                                                             3.2
                                           Intervention rate (β)




                                                                                                                                                   3.0
   → 0 (BC)             87.8   41.4                                                                                                                2.8
                                                                                                                                                     Safety Threshold δ



   0.5                  90.9   38.6                                0.6                                                                             2.6
   1.0                  79.4   37.9                                                                                                                2.4
                                                                                                                                                   2.2
   2.0                  79.2   37.5                                                                                                                2.0
   2.2                  90.8   47.4                                0.4
   2.4                  87.3   69.4
   2.6                  88.8   35.0
                                                                   0.2
   2.8                  82.0   42.0                                                                                                                1.0
   3.0                  97.0   38.3
   3.2                  89.5   42.0                                0.0                                                                  DAgger
                                                                                                                                                   0.5
   3.4                  95.3   39.0
   3.6                  90.6   41.0                                      0            20            40           60            80            100
   3.8                  85.9   40.0                                                                Iteration (×103 )
   4.0                  94.7   35.0
                                               Figure 4.5: Observed SafeDAgger intervention rate β over training itera-
   → ∞ (D.)             83.4   52.2
                                               tions for each swept threshold. Lower thresholds produce higher and more
                                               persistent intervention; higher thresholds decay quickly toward DAgger be-
                                               haviour.
24                                                                                                                                       4 Experiments and Results



                                                     Run 14         Threshold sweep: lift vs. unsafe rate
                                                       Lift                                                                              Unsafe
                                                                                                          80
                        100 88 91         91 87 89
                                                          97
                                                              90
                                                                  95
                                                                      91
                                                                          86
                                                                              95                                                    69
     Lift success (%)




                                                                                        Unsafe rate (%)
                                                      82                          83
                         80
                                  79 79
                                                                                                          60                                                               52
                                                                                                                               47
                         60                                                                               40
                                                                                                               42
                                                                                                                    39 38 38
                                                                                                                                         35
                                                                                                                                              42
                                                                                                                                                   39 39 41 40   38
                                                                                                                                                                      35

                         40
                                                                                                          20
                         20
                          0 0 0.5 1.0 2.0 2.2 2.4 2.6 2.8 3.0 3.2 3.4 3.6 3.8 4.0 ∞                        0 0 0.5 1.0 2.0 2.2 2.4 2.6 2.8 3.0 3.2 3.4 3.6 3.8 4.0 ∞
                                       Safety Threshold δ                                                               Safety Threshold δ
Figure 4.6: GSR and UER as a function of δ, with BC and DAgger as endpoints. The curve is non-monotonic:
a lift peak at δ = 3.0 (97.0 %) and a secondary peak at δ = 3.4 are separated from the BC region by a dip at
δ ∈ [1.0, 2.0]. δ = 3.0 is used for SafeDAgger in Section 4.3.3.


4.3.3              Distillation Method Comparison Results

All distillation experiments share the same teacher (99.0 % GSR, 12.2 % UER), the same stu-
dent architecture (ResNet-18 + cross-attention + LSTM-512), and the same loss (eq. (3.9)).
The primary three-way comparison uses 100,000 distillation iterations at 32 parallel environ-
ments (4 per object). SafeDAgger uses the best threshold δ = 3.0 identified in Section 4.3.2.


DAgger vs. SafeDAgger vs. Behavior Cloning

Table 4.4 reports the evaluation metrics for BC, DAgger, and SafeDAgger at δ = 3.0.

Table 4.4: BC vs. DAgger vs. SafeDAgger standalone evaluation (640 episodes, 32 environments). SafeDAgger
uses the best threshold δ = 3.0 from Section 4.3.2. UER excludes physics-instability events; Section A.4 reports
the full breakdown.


              Metric                                                   BC        DAgger                        SafeDAgger (δ = 3.0)                         Teacher
              GSR (%)                                                87.8              83.4                                    97.0                              99.0
              UER (%)                                                41.4              52.2                                    38.3                              12.2
                Harmful collision (%)                                19.3              15.3                                    15.0                               1.5
                Object out of bounds (%)                             21.1              35.0                                    20.0                              10.3
                Palm flipped (%)                                      1.3               1.8                                     3.3                               0.2

    SafeDAgger at δ = 3.0 is the strongest student on both axes. It achieves 97.0 % GSR,
within 2 percentage points of the teacher ceiling (99.0 %), and a lower UER (38.3 %) than
both BC (41.4 %) and DAgger (52.2 %). The three methods exhibit qualitatively different
failure profiles that reflect their training-time data-collection strategy.
    Since the lift-success metric requires the object to be held above the threshold for at least
0.5 s (30 consecutive steps), all reported GSR values reflect genuinely sustained grasps, not
brief accidental lifts. BC achieves 87.8 % GSR but the highest UER (41.4 %), consistent with
the covariate-shift failure described in Section 3.3.
    DAgger lets the student drive the environment with no teacher intervention, producing
fully student-distributed training data but also exposing the student to dangerous trajectories
that it has no incentive to avoid. Its UER is the highest of the three methods (52.2 %), dom-
4.3 Results                                                                                                    25



inated by object-out-of-bounds terminations (35.0 % of all episodes), reflecting aggressive
grasping without recovery behaviour.
    SafeDAgger sits between these two regimes: the teacher intervenes on states where the
student’s action disagreement exceeds δ, keeping the training-time state distribution close to
the teacher’s while still allowing the student to practice autonomously elsewhere. At δ = 3.0,
intervention is sparse but targeted at the states where it matters, yielding the best-of-both-
worlds outcome: near-teacher task performance and the lowest unsafe-episode rate among
the three distillation methods.
    SafeDAgger reaches the highest GSR (97.0 %), recovering about 98 % of the teacher ceil-
ing, while DAgger reaches 83.4 %. The largest per-category safety gap is in the object out-of-
bounds rate, where DAgger’s unrestricted exploration produces a 35.0 % failure rate versus
20.0 % for SafeDAgger. Figure 4.7 shows a representative SafeDAgger rollout across the ap-
proach, contact, lift, and hold phases together with the corresponding left stereo RGB frames
that the student sees as input.




       (a) Approach                  (b) Contact                    (c) Lift                    (d) Hold

Figure 4.7: SafeDAgger student grasping rollout on the basketball shoe across the four phases (approach, con-
tact, lift, hold). Top row: third-person scene view. Bottom row: corresponding left stereo RGB frame passed to the
student’s visual encoder.


    Figure 4.8 shows the training-time lift success and unsafe-episode rate for all three meth-
ods. BC’s lift curve starts at the teacher level and stays there throughout training, because the
teacher drives the environment at every step and the metric reflects the teacher’s performance
rather than the student’s. SafeDAgger converges quickly to near-teacher lift, while DAgger
exhibits more variability as the student drives the environment without intervention. The
unsafe-episode rate (Figure 4.8b) reveals the safety gap during training: DAgger maintains
∼25–35 %, SafeDAgger settles at ∼10–20 %, and BC tracks slightly below SafeDAgger at a
level close to the teacher’s own UER, because the teacher acts at every step and the training
metric reflects the teacher’s safety rather than the student’s. Notably, the training-time UER is
substantially lower than the standalone evaluation UER for all methods. For SafeDAgger this
is partly expected, as the teacher still rescues high-disagreement steps during training. The
remaining gap, which also affects DAgger where no teacher intervention occurs, is not fully
explained; one contributing factor may be the training metric’s 100-episode rolling window,
which could smooth over per-object variability that the 640-episode standalone evaluation
captures uniformly.
    A checkpoint sweep (Table 4.5) confirms that BC overfits: lift success peaks at 95.6 %
after 50k iterations, then degrades to 85.6 % at 100k. The UER remains consistently high
(35–49 %) across all checkpoints, confirming that BC cannot learn safety behavior regardless
   26                                                                                                                                                          4 Experiments and Results


                          Hold-gated lift success during training   BC vs. SafeDagger vs. DAgger                                      Unsafe episode rate during training   BC vs. SafeDagger vs. DAgger
                   100                                                                                                         100
                                                                                                                                                                                            BC
                                                                                                                                                                                            SafeDagger ( =3.0)
                                                                                                                                                                                            DAgger
                    80                                                                                                          80
Lift success (%)




                                                                                                             Unsafe rate (%)
                    60                                                                                                          60


                    40                                                                                                          40


                    20                                                                                                          20
                                                                                   BC
                                                                                   SafeDagger ( =3.0)
                                                                                   DAgger
                     00             20              40              60             80               100                          00           20              40              60             80              100
                                                    Iteration (×103 )                                                                                         Iteration (×103 )
                                   (a) Lift success during training.                                                                  (b) Unsafe-episode rate during training.

   Figure 4.8: Training curves for BC (green), SafeDAgger at δ = 3.0 (blue), and DAgger (orange) over 100k
   distillation iterations. (a) BC’s lift reflects the teacher’s performance since the teacher always acts; SafeDAgger
   and DAgger show the student’s own lift. (b) DAgger maintains the highest training-time unsafe rate; SafeDAgger
   reduces it through targeted intervention; BC’s rate reflects the teacher’s own unsafe rate.


   of training duration.

   Table 4.5: BC checkpoint sweep (640 episodes per checkpoint, 32 environments). Lift success peaks at 50k
   iterations and degrades thereafter, while UER remains consistently high.


                                            Iter          Lift (%)             UER (%)                    Coll. (%)                    OOB (%)                   Palm (%)
                                           10k                71.9                  49.4                    13.4                             12.5                     23.4
                                           25k                86.9                  47.2                    13.9                             23.4                     9.8
                                           50k                95.6                  39.1                    19.4                             16.6                     3.1
                                           75k                95.2                  35.8                    14.4                             14.8                     6.6
                                          100k                85.6                  40.1                    20.6                             18.0                     1.6



   Failure Mode Decomposition

   The three-way comparison reveals a clear ranking between task performance and training-
   time safety. DAgger lets the student visit dangerous states freely and pays the highest eval-
   uation UER (52.2 %). BC maximizes in-distribution action accuracy but still produces an
   evaluation UER of 41.4 %, because the student never practices recovery from its own mis-
   takes during training. SafeDAgger at δ = 3.0 achieves the lowest evaluation UER (38.3 %)
   while simultaneously reaching the highest GSR, by intercepting the few high-disagreement
   actions that would otherwise push the student off-distribution. The observed intervention
   rate is sparse throughout training (Figure 4.5), so the student acts autonomously in the vast
   majority of environments while the teacher rescues only the most misaligned ones.
       Beyond the best operating point, the threshold sweep (Table 4.3 and fig. 4.6) shows that
   SafeDAgger produces policies with a lower UER than DAgger across the majority of swept
   thresholds. This indicates that safety-aware gating yields safer student policies on average,
   not only at a single well-chosen threshold.
       Figure 4.9 reports the per-object lift-success and unsafe-episode rates across the thresh-
   old sweep. The safety advantage of SafeDAgger is uneven across objects: the largest margins
   appear on collision-prone shapes (basketball shoe, toy excavator), where the teacher’s in-
   terventions most often replace an overly aggressive student action, while compact objects
4.4 Summary                                                                                                                                            27



(closed fist, mario) show a narrower method gap because all three methods already lift them
reliably. Per-object training dynamics and full failure-mode decompositions are provided in
Section A.5.
                                     Run 14       Per-object lift across threshold sweep (vs. Teacher 11)
                          100
                                                                                                                                  Object
                                                                                                                               basketball shoe
                                                                                                                               closed fist
                           80                                                                                                  elephant toy
       Lift success (%)



                                                                                                                               mario
                                                                                                                               milk pot
                                                                                                                               teddy bear
                           60                                                                                                  toy bagger
                                                                                                                               tutle candle holder


                           40

                           20                                                                                                  Teacher 11 (priv.)
                                                                                                                               Avg over 8 objects
                                                                                                                               Top-2 lift thresholds

                            0   Teacher 0   0.5 1.0 2.0 2.2 2.4 2.6 2.8 3.0 3.2 3.4 3.6 3.8 4.0                            ∞

                                                                Safety Threshold δ
                                                  (a) Per-object lift success across the threshold sweep.

                                 Run 14      Per-object unsafe rate across threshold sweep (vs. Teacher 11)
                          100
                                                                                                                                    Object
                                                                                                                                basketball shoe
                                                                                                                                closed fist
                           80                                                                                                   elephant toy
       Unsafe rate (%)




                                                                                                                                mario
                                                                                                                                milk pot
                                                                                                                                teddy bear
                           60                                                                                                   toy bagger
                                                                                                                                tutle candle holder


                           40

                           20                                                                                                   Teacher 11 (priv.)
                                                                                                                                Avg over 8 objects

                            0   Teacher 0   0.5    1.0   2.0   2.2   2.4   2.6   2.8   3.0   3.2   3.4   3.6   3.8   4.0   ∞

                                                                Safety Threshold δ
                                            (b) Per-object unsafe-episode rate across the threshold sweep.

Figure 4.9: Per-object standalone evaluation for all swept SafeDAgger thresholds, with BC and DAgger as end-
points. (a) Lift success varies by object geometry, with compact shapes performing reliably across all methods.
(b) Unsafe-episode rate shows the largest method-dependent gaps on collision-prone objects.




4.4    Summary

The key experimental findings are:

   1. SafeDAgger produces the best student. At δ = 3.0, SafeDAgger reaches 97.0 % GSR
      (about 98 % of the teacher ceiling of 99.0 %) and a 38.3 % evaluation UER. It out-
      performs both BC (87.8 %, 41.4 %) and DAgger (83.4 %, 52.2 %) on task performance
      and safety simultaneously. Moreover, SafeDAgger produces lower UER than DAgger
      across the majority of swept thresholds, indicating that safety-aware gating yields safer
      policies on average, not only at a single operating point.
28                                                                     4 Experiments and Results



     2. The threshold-performance curve is non-monotonic and noisy. The sweep exhibits
        multiple local peaks and dips whose locations are likely sensitive to individual training
        seeds. The optimal threshold cannot be determined analytically from the disagreement
        distribution alone; an empirical sweep is necessary.

     3. The three methods produce qualitatively distinct failure profiles. BC produces the
        highest collision and object-out-of-bounds rates at evaluation; DAgger visits dangerous
        states freely and accumulates the highest object-out-of-bounds rate (35.0 %); SafeDAg-
        ger at δ = 3.0 sits between them with sparse, targeted intervention and the lowest UER
        overall.

   Additional implementation findings related to physics stability and teacher–student ob-
servation mapping are discussed in Section 5.1.3.
Chapter 5

Discussion and Conclusion


This chapter interprets the experimental results of Chapter 4, discusses the limitations of the
present study, and outlines directions for future work.



5.1     Discussion

5.1.1   Offline vs. Online Distillation

The three-way comparison between BC, DAgger, and SafeDAgger contrasts offline distilla-
tion, where the student trains exclusively on teacher-generated data, with online distillation,
where the student acts in the environment during training. BC achieves a respectable 87.8 %
grasp success rate but produces an evaluation UER of 41.4 %, because the student never
practices recovery from its own mistakes. The checkpoint sweep further reveals that BC
overfits after 50k iterations, with lift success peaking at 95.6 % before degrading to 85.6 %
at 100k. These results confirm that training exclusively on the teacher’s state distribution
yields high in-distribution accuracy but fails to produce robust behavior when the student
acts autonomously.


5.1.2   SafeDAgger Dominates BC and DAgger

Once a suitable safety threshold is identified from the DAgger action-disagreement distribu-
tion, SafeDAgger at δ = 3.0 reaches 97.0 % grasp success, about 98 % of the teacher ceiling,
and simultaneously produces the lowest evaluation UER of the three methods (38.3 % vs.
41.4 % for BC and 52.2 % for DAgger). Safety-aware distillation is thus Pareto-dominant
over both alternative baselines on both axes.
    The mechanism is visible in the failure-mode profile of each method. DAgger lets the stu-
dent explore freely and accumulates object-out-of-bounds terminations (35.0 % of all episodes)
as the student learns an aggressive grasp motion but not when to stop. BC drives every step
with the teacher and produces an in-distribution student that fails the moment it encounters
a state the teacher never visited. SafeDAgger at δ = 3.0 rescues the student only on the few
steps where its action most sharply disagrees with the teacher; the remaining steps proceed
under the student’s own actions, which gives the student the self-distribution practice DAgger
provides without the unchecked exploration that makes DAgger unsafe.
    A notable pattern across all three methods is that object-out-of-bounds is the dominant
failure mode despite high lift success. The teacher is trained with external wrench perturba-
tions that ramp up via ADR, which forces it to develop robust force-closure grasps. During
30                                                                   5 Discussion and Conclusion



distillation and evaluation, however, the wrench magnitude is zero. The student therefore
never needs to resist external perturbations, yet it still drops objects after initially lifting
them. This suggests that the distilled student does not fully reproduce the teacher’s finger
coordination for maintaining force closure: the student learns where to grasp but not how
tightly to hold, resulting in fragile grasps that fail under the object’s own inertia during the
lifting motion. Training the student under ADR conditions closer to those of the teacher, in-
cluding the external wrench perturbations, could force the student to develop more robust
grasps during distillation and reduce the object-out-of-bounds failure rate.


5.1.3   Calibration and the Non-Monotonic Threshold-Performance Curve

The threshold sweep (Section 4.3.2) reveals that the relationship between δ and performance
is neither smooth nor monotonic. The curve exhibits multiple local peaks and dips whose
positions are likely sensitive to individual training seeds rather than systematic properties
of the threshold. Using the DAgger distribution to scope the sweep range places meaning-
ful threshold candidates in [2.0, 4.0]. This principle of deriving the sweep range from an
intervention-free reference is expected to transfer to other action spaces, though the specific
optimum is platform-dependent.



5.2     Limitations

The present study has several limitations that constrain the generality of its conclusions and
that motivate future work.
    All teacher and student policies were trained and evaluated in simulation only; no real-
robot rollouts were performed and no system identification was carried out on the physical
Agile Hand or the FR3. Although the sim-to-real-aware ADR schedule is designed to narrow
the sim-to-real gap, the actual gap on the physical platform is unknown, and the unsafe-
episode rates reported in Section 4.3.3 are simulator-defined and should not be interpreted
as predictions of hardware damage rates.
    All experiments use a single hand–arm combination (Agile Hand on FR3) and target a
single task (top-down grasping of rigid objects from a flat surface), so the conclusions about
SafeDAgger’s safety advantage may not transfer to other hands (e.g., the Allegro or Shadow
hands), other arms, or tasks that involve in-hand reorientation or regrasping. The training
and evaluation set consists of only 8 objects; a substantially larger and more diverse object set
would be needed to produce a generalizable grasping policy and to draw statistically robust
conclusions about distillation method performance.
    The SafeDAgger variant used in this thesis gates teacher intervention on the inverse-
variance-weighted L2 distance between the student’s and teacher’s actions, rather than on
a learned binary safety classifier as in the original Zhang and Cho formulation [19]. The
safety signal is therefore purely action-based and does not incorporate value-based failure
prediction, which may limit its ability to distinguish genuinely dangerous states from benign
action disagreements.
    The original DextrAH-RGB pipeline relies on fabric-guided policies to produce smooth,
kinematically consistent action targets, which was deliberately omitted in this work because
of its implementation complexity. Adding fabrics would likely improve the smoothness of the
teacher’s action distribution and indirectly improve distillation quality.
5.3 Conclusion                                                                             31



5.3   Conclusion

This semester thesis presented a privileged teacher–student distillation pipeline for dexter-
ous grasping with a custom 23-degree-of-freedom Agile Hand and Franka Research 3 plat-
form. Through a three-way comparison of BC, DAgger, and SafeDAgger at a suitable safety
threshold, we show that safety-aware distillation produces the strongest student on both
axes: 97.0 % grasp success (about 98 % of the teacher ceiling) and the lowest evaluation
unsafe-episode rate among the three methods. The task-performance gap to the teacher is
now small (2 percentage points); the remaining gap is on safety, where the student’s 38.3 %
unsafe-episode rate is still roughly 3× the teacher’s 12.2 %. Closing this safety gap, rather
than further improving raw task performance, is the main direction for future work.



5.4   Future Work

Real-robot validation. The most important next step is to evaluate the SafeDAgger stu-
dent on the physical FR3 and Agile Hand, both to measure the true sim-to-real gap and to
test whether the in-training unsafe-episode reduction observed in simulation translates into
fewer hardware-damaging events on the real platform. This step also requires a basic system
identification of the Agile Hand actuators, which was deliberately deferred in the semester
thesis.

Improving teacher quality through low-level control. The teacher policy in this work
reaches ADR level 14 before training stalls, whereas DextrAH-RGB and DextrAH-G report
substantially higher ADR progression. A likely explanation is that these systems use Fabric-
Guided Policies (FGPs), which offload collision avoidance and palm-alignment constraints to
a geometric-fabrics controller rather than learning them through reward shaping. The RL
policy then operates in a reduced, kinematically consistent action space rather than com-
manding raw joint positions. DextrAH-RGB further reduces the hand’s action space through
Hand-PCA components derived from teleoperation data, which constrains the Allegro Hand
to anthropomorphic synergies and simplifies exploration. Integrating an FGP or similar struc-
tured low-level controller for the Agile Hand is a promising direction for improving ADR
consistency and teacher quality, and would make the reward terms for collision avoidance
and palm alignment ( rpalm , raction ) redundant. The student already recovers about 98 % of
the teacher’s lift success, so the immediate benefit of a stronger teacher is not raising the
student’s task ceiling but distilling at higher ADR levels, which DextrAH-RGB reports as the
key ingredient for robust zero-shot sim-to-real transfer, a property that the current pipeline
does not yet achieve.

Scaling the distillation pipeline. DextrAH-RGB achieves stronger distillation results in part
through longer training schedules, more parallel environments, and a multi-GPU setup. The
current pipeline is limited to a single RTX 4090, which constrains both the number of envi-
ronments and the RGB rendering resolution (320 × 240 at 30 fps). Higher-resolution images
may improve the student’s object localization and grasp accuracy, but would require substan-
tially more GPU memory. Exploring multi-GPU distillation or more memory-efficient render-
ing backends could unlock this trade-off. On the architecture side, the ResNet-18 backbone
with two removed layers and the two-layer cross-attention transformer were adopted from
DextrAH-RGB without modification. Ablations on the vision backbone (e.g., stronger fea-
ture extractors, different layer cutoffs), transformer depth, and hidden dimensions may yield
32                                                                   5 Discussion and Conclusion



better visual representations, particularly for the auxiliary object-position prediction task.

Stronger safety signals. The action-disagreement gate used in this thesis is the simplest
reasonable implementation of safety-aware distillation, and the threshold sweep reveals that
the optimal operating point is sensitive to training noise and cannot be determined analyti-
cally. A natural extension is replacing the fixed-threshold weighted L2 gate with a learned risk
predictor, such as the binary safety classifier from the original SafeDAgger formulation [19],
which could adapt to the evolving student distribution rather than relying on a static thresh-
old. More generally, coupling the safety decision to the privileged teacher’s value estimate
could provide a richer signal for identifying genuinely unsafe states.

Weighted action disagreement. The current disagreement metric treats all 23 action di-
mensions equally through the teacher’s inverse-variance weighting. However, the 16 hand
joints operate over substantially smaller ranges of motion than the 7 arm joints, so hand-level
disagreements are numerically smaller and may be diluted when averaged with arm-level dis-
agreements. Since grasp stability depends primarily on finger coordination, explicitly weight-
ing hand-joint disagreements more heavily in the safety gate could make the intervention
more sensitive to the subtle finger-action errors that lead to object-out-of-bounds failures.
Appendix A

Training Configuration and Domain Randomization


A.1   PPO Hyperparameters

Table A.1 lists the PPO hyperparameters used for teacher policy training.

                        Table A.1: PPO hyperparameters for teacher training.


                            Hyperparameter                    Value
                            Learning rate                    1 × 10−4
                            Clip parameter ε                     0.2
                            Mini-epochs per update                4
                            Horizon length                   16 steps
                            Minibatch size                     2048
                            Discount factor γ                   0.99
                            GAE λ                               0.95
                            Number of environments             1,024
                            Max training epochs               33,000




A.2   Network Architecture

The teacher policy uses an LSTM-based recurrent network implemented in rl_games. The
actor consists of an MLP encoder followed by an LSTM layer with 1024 hidden units, followed
by an output head mapping to the 23-dimensional action space. The critic has an identical
architecture but receives the larger critic observation (Table 3.1).
   The student uses a vision–proprioception fusion architecture:

  1. Visual encoder: A ResNet-18 backbone processes each stereo image independently,
     producing a 32-dimensional feature vector per image.

  2. Cross-attention fusion: A cross-attention transformer module fuses the two stereo
     features into a single 64-dimensional visual embedding.

  3. Policy head: The visual embedding is concatenated with the proprioceptive state vec-
     tor and fed into an LSTM with 512 hidden units, followed by a linear output layer
     producing the 23-dimensional action.
34                                                   A Training Configuration and Domain Randomization



A.3     Automatic Domain Randomization Parameters

Table A.2 lists the key randomized parameters and their start/max ranges. The maximum
ranges for finger joint stiffness and damping correspond to values measured on the real Agile
Hand hardware using an Isaac Lab gain tuner. The thumb rotation velocity limit is ramped
down toward the real hardware limit of approximately 12 deg/s (≈ 0.21 rad/s). All ADR
parameters share a single increment counter (Nmax = 50, success threshold τADR = 0.4),
meaning all parameters progress together.

                             Table A.2: Automatic Domain Randomization parameters.


                 Parameter                             Start Range          Max Range
                 Object mass scale                       [1.0, 1.0]            [0.5, 2.0]
                 Object friction (static)                [1.0, 1.0]            [0.5, 1.5]
                 Robot restitution                       [1.0, 1.0]            [0.8, 1.0]
                 Arm stiffness scale                     [1.0, 1.0]            [0.5, 2.0]
                 Arm damping scale                       [1.0, 1.0]            [0.5, 2.0]
                 Finger MCP pitch stiffness              [1.0, 1.0]           [0.17, 1.0]
                 Finger MCP pitch damping                [1.0, 1.0]          [0.083, 1.0]
                 Finger MCP yaw stiffness                [1.0, 1.0]          [0.025, 1.0]
                 Finger PIP stiffness                    [1.0, 1.0]           [0.02, 1.0]
                 Thumb rotation velocity limit          [20.0, 20.0]      [0.21, 20.0] rad/s


                                            ADR Parameter Ranges (start → max)
                  Thumb vel. limit                                                Max ADR range
                          (rad/s)                                                 Start value
               Finger PIP stiffness

              Finger MCP stiffness

                     Arm stiffness

                    Object friction

                      Object mass
                                      2.5     5.0    7.5    10.0   12.5    15.0    17.5    20.0
                                              Parameter value (or scale factor)
Figure A.1: ADR parameter ranges. Blue bars indicate the full randomization range at maximum ADR level. Red
diamonds mark the nominal start values. The thumb velocity limit spans the widest relative range, from 20 rad/s
(simulation) to 0.21 rad/s (hardware limit).




A.4     Full Results Including Physics Instability

The results in Chapter 4 exclude physics instability events (NaN joint states, velocity explo-
sions), which are simulation-only artifacts that cannot occur on physical hardware. This
section reports the full evaluation data including physics instability for completeness.
A.5 Per-Object Failure Mode Breakdowns                                                                                           35



Table A.3: Teacher policy per-object evaluation including physics instability (200 episodes per object, ADR-0
physics).

   Object                        Lift (%)     UER (%)            Coll. (%)     OOB (%)            Palm (%)      Phys. (%)
   basketball shoe                     99.0         32.0                 7.0         21.0                 0.0         4.0
   closed fist                        100.0         19.5                 0.0          9.0                 0.0        10.5
   elephant toy                       100.0         22.0                 2.0          0.5                 0.5        19.0
   mario                               98.0          8.5                 0.0          1.0                 0.0         6.5
   milk pot                            96.5         15.0                 0.5          5.0                 0.0         9.5
   teddy bear                          99.5         21.5                 0.5         14.5                 0.0         6.5
   toy excavator                       99.0         25.5                 2.0          7.5                 1.0        15.0
   turtle candle holder               100.0         35.0                 0.0         24.0                 0.0        10.5
   Average (8 objects)                 99.0         22.4                 1.5         10.3                 0.2        10.2


A.5     Per-Object Failure Mode Breakdowns

Figures A.2 and A.3 show the per-object unsafe-episode rate across all swept SafeDAgger
thresholds, with BC (δ → 0) and DAgger (δ → ∞) as endpoints. Figure A.2 excludes physics-
instability events; Figure A.3 includes them for completeness.

                                              Run 14       Per-object unsafe rate
   basketball shoe    36   44    44     53    54    79     39      30     36   34    44     39      41     50   61    100
        closed fist   32   25    26     20    45    52     24      38     20   30    38     36      36     16   32
                                                                                                                      80
      elephant toy    34   30    35     28    40    74     31      55     32   45    30     41      26     38   35




                                                                                                                           Unsafe rate (%)
             mario    38   41    29     32    42    69     31      48     34   36    31     26      32     20   31    60

          milk pot    55   46    51     48    46    68     40      49     39   34    46     42      35     37   49
                                                                                                                      40
        teddy bear    48   41    45     42    48    58     36      40     39   40    40     52      39     34   78
                                                                                                                      20
        toy bagger    44   38    38     33    50    72     42      34     55   48    54     46      45     44   62

tutle candle holder   48   44    36     43    54    84     36      41     55   42    48     34      45     38   69    0
                      0    0.5   1.0    2.0   2.2   2.4    2.6     2.8   3.0   3.2   3.4    3.6     3.8   4.0   ∞

                                                    Safety Threshold δ
Figure A.2: Per-object unsafe-episode rate across the threshold sweep (physics excluded). Each cell shows the
UER for one object at one threshold. The basketball shoe and turtle candle holder exhibit the highest rates across
most thresholds.
36                                                              A Training Configuration and Domain Randomization




                                         Run 14        Per-object unsafe rate (incl. physics)
     basketball shoe    99   95    86      83     96     99   95    94    95    98    98    94    96    100   70   100
          closed fist   86   72    65      52     76     76   86    91    69    81    65    79    70    66    48
                                                                                                                   80




                                                                                                                        total (%)
        elephant toy    84   72    76      57     76     84   75    86    60    84    61    75    65    78    54

              mario     88   81    51      62     76     89   68    81    62    79    68    68    66    56    55   60




                                                                                                                        Unsafe rate
            milk pot    91   95    76      75     66     86   95    82    72    78    79    84    61    92    69
                                                                                                                   40
         teddy bear     86   88    79      62     79     72   84    69    71    70    74    82    66    90    85
                                                                                                                   20
         toy bagger     98   94    89      63     89     92   99    99    88    95    90    94    80    95    85

tutle candle holder     95   94    74      63     82     95   92    94    85    89    80    81    68    78    81   0
                        0    0.5   1.0    2.0   2.2     2.4   2.6   2.8   3.0   3.2   3.4   3.6   3.8   4.0   ∞

                                                        Safety Threshold δ
Figure A.3: Per-object unsafe-episode rate across the threshold sweep (physics included). Physics-instability
events raise the overall rates but do not change the relative ordering across methods.
Bibliography


 [1]   Tang, C., Abbatematteo, B., Hu, J., Chandra, R., Martín-Martín, R., and Stone, P. “Deep
       Reinforcement Learning for Robotics: A Survey of Real-World Successes”. In: (Sept.
       2024).
 [2]   Wu, A., Guo, M., and Liu, C. K. “Learning Diverse and Physically Feasible Dexterous
       Grasps with Generative Model and Bilevel Optimization”. In: (Dec. 2022).
 [3]   Handa, A., Allshire, A., Makoviychuk, V., Petrenko, A., Singh, R., Liu, J., Makoviichuk,
       D., Wyk, K. V., Zhurkevich, A., Sundaralingam, B., Narang, Y., Lafleche, J.-F., Fox, D.,
       and State, G. “DeXtreme: Transfer of Agile In-hand Manipulation from Simulation to
       Reality”. In: (Jan. 2024). URL: https://arxiv.org/pdf/2210.13702.
 [4]   Lin, T., Sachdev, K., Fan, L., Malik, J., and Zhu, Y. “Sim-to-Real Reinforcement Learning
       for Vision-Based Dexterous Manipulation on Humanoids”. In: (Sept. 2025).
 [5]   Singh, R., Allshire, A., Handa, A., Ratliff, N., and Wyk, K. V. “DextrAH-RGB: Visuomo-
       tor Policies to Grasp Anything with Dexterous Hands”. In: (Feb. 2025).
 [6]   Lum, T. G. W., Matak, M., Makoviychuk, V., Handa, A., Allshire, A., Hermans, T.,
       Ratliff, N. D., and Wyk, K. V. “DextrAH-G: Pixels-to-Action Dexterous Arm-Hand Grasp-
       ing with Geometric Fabrics”. In: (Oct. 2024).
 [7]   Ross, S., Gordon, G. J., and Bagnell, J. A. “A Reduction of Imitation Learning and
       Structured Prediction to No-Regret Online Learning”. In: (Mar. 2011).
 [8]   Bicchi, A. and Kumar, V. “Robotic grasping and contact: a review”. In: Proceedings
       2000 ICRA. Millennium Conference. IEEE International Conference on Robotics and Au-
       tomation. Symposia Proceedings (Cat. No.00CH37065). IEEE, 2000, pp. 348–353. ISBN:
       0-7803-5886-4. DOI: 10.1109/ROBOT.2000.844081.
 [9]   Ferrari, C. and Canny, J. F. “Planning optimal grasps”. In: Proceedings 1992 IEEE Inter-
       national Conference on Robotics and Automation (ICRA). IEEE, 1992, pp. 2290–2295.
       DOI : 10.1109/ROBOT.1992.219918.

[10]   Siciliano, B., Sciavicco, L., Villani, L., and Oriolo, G. Robotics: Modelling, Planning and
       Control. Springer, 2009. ISBN: 978-1-84628-641-4.
[11]   Wang, R., Zhang, J., Chen, J., Xu, Y., Li, P., Liu, T., and Wang, H. “DexGraspNet: A
       Large-Scale Robotic Dexterous Grasp Dataset for General Objects Based on Simula-
       tion”. In: (Mar. 2023).
[12]   Kumar, V., Todorov, E., and Levine, S. “Optimal control with learned local models:
       Application to dexterous manipulation”. In: 2016 IEEE International Conference on
       Robotics and Automation (ICRA). IEEE, May 2016, pp. 378–383. ISBN: 978-1-4673-
       8026-3. DOI: 10.1109/ICRA.2016.7487156.
38                                                                                   Bibliography



[13]   Andrychowicz, M., Baker, B., Chociej, M., Jozefowicz, R., McGrew, B., Pachocki, J.,
       Petron, A., Plappert, M., Powell, G., Ray, A., Schneider, J., Sidor, S., Tobin, J., Welin-
       der, P., Weng, L., and Zaremba, W. “Learning Dexterous In-Hand Manipulation”. In:
       The International Journal of Robotics Research 39.1 (2020), pp. 3–20. DOI: 10.1177/
       0278364919887447.
[14]   Petrenko, A., Allshire, A., State, G., Handa, A., and Makoviychuk, V. “DexPBT: Scaling
       up Dexterous Manipulation for Hand-Arm Systems with Population Based Training”.
       In: (May 2023).
[15]   Wan, W., Geng, H., Liu, Y., Shan, Z., Yang, Y., Yi, L., and Wang, H. “UniDexGrasp++:
       Improving Dexterous Grasping Policy Learning via Geometry-aware Curriculum and
       Iterative Generalist-Specialist Learning”. In: (Apr. 2023).
[16]   Ratliff, N. and Wyk, K. V. “Fabrics: A Foundationally Stable Medium for Encoding Prior
       Experience”. In: (Sept. 2023).
[17]   Hinton, G., Vinyals, O., and Dean, J. “Distilling the Knowledge in a Neural Network”.
       In: (Mar. 2015).
[18]   Pomerleau, D. A. “ALVINN: An Autonomous Land Vehicle in a Neural Network”. In:
       Advances in Neural Information Processing Systems 1 (1988).
[19]   Zhang, J. and Cho, K. “Query-Efficient Imitation Learning for End-to-End Autonomous
       Driving”. In: (May 2016).
[20]   Tobin, J., Fong, R., Ray, A., Schneider, J., Zaremba, W., and Abbeel, P. “Domain Ran-
       domization for Transferring Deep Neural Networks from Simulation to the Real World”.
       In: 2017 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS).
       IEEE, 2017, pp. 23–30. DOI: 10.1109/IROS.2017.8202133.
[21]   Weng, L. Domain Randomization for Sim2Real Transfer. May 2019. URL: https : / /
       lilianweng.github.io/posts/2019-05-05-domain-randomization/ (visited on 04/09/2026).
[22]   Peng, X. B., Andrychowicz, M., Zaremba, W., and Abbeel, P. “Sim-to-Real Transfer of
       Robotic Control with Dynamics Randomization”. In: 2018 IEEE International Confer-
       ence on Robotics and Automation (ICRA). IEEE, 2018, pp. 3803–3810. DOI: 10.1109/
       ICRA.2018.8460528.
[23]   OpenAI, Akkaya, I., Andrychowicz, M., Chociej, M., Litwin, M., McGrew, B., Petron,
       A., Paino, A., Plappert, M., Powell, G., Ribas, R., Schneider, J., Tezak, N., Tworek, J.,
       Welinder, P., Weng, L., Yuan, Q., Zaremba, W., and Zhang, L. “Solving Rubik’s Cube
       with a Robot Hand”. In: The International Journal of Robotics Research 39.1 (2020),
       pp. 34–65. DOI: 10.1177/0278364919887447.
[24]   Sutton, R. S. and Barto, A. G. Reinforcement Learning: An Introduction. 2nd. MIT Press,
       2018. ISBN: 978-0-262-03924-6.
[25]   Pinto, L., Andrychowicz, M., Welinder, P., Zaremba, W., and Abbeel, P. “Asymmetric
       Actor Critic for Image-Based Robot Learning”. In: Robotics: Science and Systems (RSS).
       2018.
[26]   He, K., Zhang, X., Ren, S., and Sun, J. “Deep Residual Learning for Image Recognition”.
       In: IEEE Conference on Computer Vision and Pattern Recognition (CVPR). 2016.
[27]   Mittal, M., Yu, C., Yu, Q., Liu, J., Rudin, N., Hoeller, D., Yuan, J. L., Singh, R., Guo,
       Y., Mazhar, H., Mandlekar, A., Babich, B., State, G., Hutter, M., and Garg, A. “Orbit: A
       Unified Simulation Framework for Interactive Robot Learning Environments”. In: IEEE
       Robotics and Automation Letters 8.6 (2023), pp. 3740–3747. DOI: 10.1109/LRA.2023.
       3270034.
