               NUTS: Learning Long-Horizon Cyclic Nut Threading via
                        Hybrid-Teacher Policy Distillation




Fig. 1. Overview of NUTS—decompose during data collection, unify at deployment. During data collection, an RL policy executes approach, grasp,
rotate, and goal reaching, while scripted controllers execute release and return&reset; together, they form a hybrid teacher for generating long-horizon
threading demonstrations. Human corrections augment real-world replays to address the sim-to-real gap. Policy distillation then unifies these demonstrations
into a single visuomotor policy that executes the complete cyclic task at deployment.


   Abstract— Learning controlled nut threading is one of the                    dependent: the policy completes all 10 cycles on the round and
most challenging problems in robotic assembly. Repetitive                       octagonal profiles with comparable errors, but barely succeeds on
phases—including grasping, turning, goal reaching, and release-                 rectangular profiles, indicating a limitation when test geometry
and-reset—must transition seamlessly to sustain consecutive                     does not support the learned grasping skill.
threading cycles, making the task long-horizon and sensitive
to errors at phase boundaries. We found that learning all                                                I. I NTRODUCTION
phases end to end with a single reinforcement-learning policy
makes long-horizon reward shaping and training difficult. We                      Threading a nut onto a bolt is among the most difficult
therefore present NUTS, which follows a simple principle:                      tasks in robotic assembly because threaded engagement is
decompose during data generation, unify during deployment. A
hybrid teacher combines a privileged RL policy for approach
                                                                               notoriously contact-rich. On the one hand, the engaged threads
through goal reaching with scripted release-and-reset behaviors                can produce more than 15,000 simultaneous contact points,
to generate complete multi-cycle demonstrations. Sparse human                  making faithful simulation prohibitively expensive for the
corrections augment real-world replays to reduce the sim-to-real               large number of parallel rollouts required for reinforcement
gap. We distill the combined data into a single conditional flow-              learning. Factory[1] directly addresses this computational
matching visuomotor student that predicts eight-step action
chunks from point-cloud features converted from RGB-D
                                                                               bottleneck through a combination of signed-distance-field
observations and executes the full task autonomously. We                       (SDF)[2] collision detection, contact reduction, and a Gauss–
evaluate the student policy in 10-cycle trials using in-distribution           Seidel solver, enabling 1,000 parallel nut–bolt assemblies to
M24, M30, and M36 hexagonal nuts and unseen rectangular,                       be simulated in real time on a single GPU.
octagonal, and round nut geometries. For all in-distribution nuts,                On the other hand, depending on the task, humans perform
the policy completes all 10 cycles, with mean cyclic tracking
errors below 6◦ in magnitude. Generalization is geometry                       nut threading in various ways. For simple spinning, a single
                                                                               finger is sufficient while the wrist remains fixed. A pinch
grasp is preferred for controlled threading, whereas a tripod            profiles.
or even a power grasp may be applied in high-resistance
scenarios.                                                                              II. R ELATED W ORK
   Prior work has typically approached the problem from                Robot Assembly with Dexterous Manipulation. Robot
the perspective of spinning. DexScrew[3] uses a dexterous           assembly requires precise motion and closed-loop contact
hand–arm setup similar to ours and replaces explicit thread         under geometric and dynamic uncertainty [6], with tasks in-
geometry with a revolute-joint proxy to learn a rotational          cluding peg-in-hole insertion, gear meshing, connector mating,
finger gait. The learned skill then assists teleoperation and       screwdriving, and nut–bolt fastening. Classical systems rely
supports the collection of real-world demonstrations for tactile    on fixtures or specialized tools, whereas multi-fingered hands
behavior cloning. However, its policy performs uncontrolled         offer greater versatility but introduce high-dimensional control
spinning without target conditioning or learned termination,        and complex contact dynamics. Learning-based systems
leaving goal-directed, cyclic nut threading unresolved.             include Factory[1] for scalable simulation, FORGE[7] for
   Play2Perfect[4] builds on the goal-conditioned object-           force-guided contact search, SimToolReal[5] for dexterous
manipulation policy introduced by SimToolReal[5]. It pre-           tool use, and Play2Perfect[4] for reusable manipulation priors.
trains this policy through play on diverse objects and goals,       Closest to our work, DexScrew[3] learns sustained rotation
then fine-tunes it for precise assembly tasks, including            of an already engaged fastener from simplified simulation. In
screwing a rod-like furniture leg. This formulation enables         contrast, NUTS performs controlled, multi-cycle nut threading
goal-directed screwing in a structured setting but does not         with coordinated turning and release-and-reset behavior across
address everyday threaded objects, such as nuts and bolts.          multiple nut sizes.
   We first attempted to approach the controlled threading             Policy Chaining in Long-Horizon Tasks. Training a single
problem for nuts and bolts by training a unified teacher            policy for a long-horizon task is challenging: small control
policy for the complete multi-cycle task. In practice, however,     errors can compound over time [8], while sequential fine-
designing rewards that capture both long-horizon progress           tuning on new subtasks can overwrite previously acquired
and precise transitions between phases proved exceedingly           behaviors and cause catastrophic forgetting [9]. Common
difficult.                                                          remedies include increasing network capacity, freezing or
   This motivates our central design principle: decompose           regularizing task-relevant parameters, and adopting archi-
during data generation, unify during deployment. Dur-               tectures with stronger temporal memory, such as recurrent
ing data generation, a learned policy handles approach,             networks or Transformers. An alternative is to decompose
grasp, rotate, and goal reaching, while scripted transition         the task into reusable skills and chain their policies. This
controllers handle release-and-reset behaviors. We refer            decomposition reduces the burden on each individual policy
to the composition of the learned RL skill and scripted             but introduces a transition problem: the terminal states
transition controllers as the hybrid teacher, while human           produced by one skill may fall outside the initial-state
intervention is used only during real-world replay to correct       distribution of the next, causing failures at skill boundaries.
teacher trajectories under sim-to-real discrepancies. During        Adversarial Skill Chaining[10] regularizes terminal states to
deployment, a student policy distills these heterogeneous           reduce this mismatch. Sequential Dexterity[11] addresses it
demonstrations into a single visuomotor policy that executes        using a learned transition-feasibility function that fine-tunes
the complete cyclic task without privileged state, scripted         adjacent dexterous policies, supports autonomous switching,
controllers, or human intervention. We evaluate threading           and enables recovery.
accuracy in both simulation and real-world experiments.                Sim-to-Real Adaptation with Human Intervention. The
   The main contributions of this work are:                         sim-to-real gap is a long-standing problem in robot learning:
   • A long-horizon cyclic nut-threading formulation and            policies trained in simulation encounter mismatches in
      hybrid teacher that combines an RL policy for approach,       perception, dynamics, contact, and control when deployed on
      grasp, rotation, and goal reaching with scripted release-     physical hardware. These discrepancies become increasingly
      and-reset behaviors, generating coherent long-horizon,        consequential for high-dimensional, contact-rich dexterous
      multi-cycle demonstrations without a monolithic RL            manipulation. Most approaches seek robust zero-shot transfer
      teacher.                                                      through domain randomization [12] or domain adaptation
   • A human-corrected sim-to-real demonstration strategy           through Adapt3R[13], while methods such as TRANSIC[14]
      that selectively replaces failure-prone segments during       use limited real-world data to adapt a simulation-trained
      real-world replay, adapting simulated behaviors to hard-      policy. DAgger[8] aggregates expert labels on states visited
      ware contact and perception discrepancies.                    by the learner, whereas SafeDAgger[15] reduces expert
   • A unified 3D flow-matching visuomotor student that dis-        queries by requesting supervision only when the learned
      tills heterogeneous demonstrations into complete cyclic       policy is predicted to be unsafe. Similarly, during real-
      behavior without privileged state, scripted controllers, or   world hybrid-teacher replay, we replace anticipated slip or
      human assistance at deployment. In real-world tests, it       misalignment failures with human corrections and add the
      completes every 10-cycle trial on all training sizes and      corrected trajectories to the student-distillation dataset.
      geometrically compatible unseen round and octagonal              Visuomotor Policy Distillation. Learning by Cheating[16]
      profiles, while exposing failure on the tested rectangular    demonstrates a practical route from policies trained with
Fig. 2. Detailed NUTS pipeline. An RL teacher is repeatedly rolled out with a scripted policy to construct cyclic threading demonstrations in simulation;
together, they form the hybrid teacher. During real-world replay, human corrections replace flawed trajectory segments from grasp through release, forming
a mixed simulation and real-world dataset. The conditional flow-matching student takes a 64-D visual feature extracted by a DP3 vision encoder from
RGB-D observations and a 256-D state feature comprising proprioception, timing, and phase encodings, and predicts an eight-step action chunk.



privileged simulator state to deployable policies that act                    angle upon completing the goal-reaching phase in cycle k.
from onboard sensing. In dexterous manipulation, DextrAH-                     We define the cycle and episodic tracking errors as
RGB[17] distills a privileged reinforcement-learning teacher                                    ek = ϕk − ϕk−1 − ∆ϕ∗ ,
into an end-to-end visual grasping policy, while UniGrasp-                                                                         K
Transformer[18] consolidates object-specific teacher policies                                                                      X
                                                                                                eep = ϕK − ϕ0 − K∆ϕ∗ =                   ek ,
into a unified student. For long-horizon tasks, predicting                                                                                            (2)
                                                                                                                                   k=1
action sequences improves temporal consistency, while                                                      K
generative models can represent multiple valid behaviors.                                              1   X
                                                                                             E(τ ) =             e2k + βe2ep .
Diffusion Policy[19] models multimodal action sequences                                                K
                                                                                                           k=1
through iterative denoising. Flow Matching[20] instead learns
                                                                               Positive (negative) errors indicate overshoot (lag); E squares
a continuous vector field for efficient ODE-based action
                                                                               them to prevent cancellation.
generation, as adopted by π0 [21]. These properties motivate
                                                                                  Our research problem is then to find the policy that chains
its use for distilling our hybrid-teacher and human-corrected
                                                                               all phases with maximum completion success and minimum
demonstrations.
                                                                               tracking error over the episode. Let ΠS denote the policies
        III. P ROBLEM S TATEMENT AND M ETHOD                                   that execute S in order in every cycle. We express the two
A. Problem Formulation                                                         priorities as
  We decompose cyclic nut threading into the ordered phase                             Πsucc = arg max Pr [C(τ ) = K] ,
                                                                                                       π∈ΠS τ ∼pπ
sequence                                                                                    ∗                                                         (3)
                                                                                           π = arg min Eτ ∼pπ [E(τ ) | C(τ ) = K] .
        S = approach, grasp, rotate, goal reaching,                                                    π∈Πsucc

                                                                              Here, C(τ ) counts completed cycles. Equation (3) first
            |                 {z                 }
                           MRL : πT
                                                                       (1)    maximizes K-cycle success and then minimizes tracking
            release, return&reset .
            |          {z       }                                             cost, with β weighting accumulated drift relative to cycle-
                        Mscript : κ
                                                                              wise accuracy. We set K = 10 and ∆ϕ∗ = 60◦ , and learn π ∗
Thus, the active phase satisfies mt ∈ M = MRL ∪ Mscript .                     from fixed hybrid-teacher demonstrations rather than through
The RL-learned teacher πT executes the four phases in MRL ,                   on-hardware optimization.
whereas scripted controllers κ execute the release-and-reset
phases in Mscript .                                                            B. Overview of the Distillation Pipeline
   Let K be the predefined cycle count, ∆ϕ∗ the desired                           The proposed pipeline, illustrated in Fig. 2, comprises three
clockwise rotation per cycle, and ϕk the unwrapped nut                         stages. First, we train a privileged RL policy for approach,
                                                                         span 128 control steps. The actor parameterizes a diagonal
                                                                         Gaussian over the normalized action at ∈ [−1, 1]9 .
                                                                           We use a 9-D action space comprising a 6-D Cartesian
                                                                         controller target native to the Franka arm and three finger-
                                                                         control dimensions.
                                                                           The resulting recurrent policy πT (a | zπ , h) is optimized
                                                                         with PPO using the shaped reward
                                                                                  X              X p
                                                                            rt =      wir Ri,t −    wj Pj,t ,
                                                                                  i∈R            j∈P
Fig. 3.   Coupled revolute–prismatic thread model, with k = −ρ/(2π) in                                                                  (5)
                                                                            R = {center, face, grasp, turn, target},
(4).
                                                                            P = {mag, ∆a, align, force, settle, clear, contact}.

grasp, rotate, and goal reaching and combine it with scripted            The reward follows three stages. During approach, Rtcenter
release-and-reset controllers to construct a hybrid teacher.             rewards motion toward the nut center and Rtface rewards
Second, we use the hybrid teacher to generate complete                   alignment with the designated opposing faces. Rtgrasp marks
cyclic demonstrations in simulation and replay the resulting             acquisition of a stable, proper grasp. During turning, Rtturn
trajectories on the real system. A human operator intervenes             rewards grip-maintaining progress toward the fixed helical
whenever a grasp failure is anticipated. We consolidate the              target. At completion, Rttarget rewards holding the target
simulated and human-corrected real-world demonstrations                  stably. The approach and turning rewards pay only new-
into a fixed offline dataset. Third, we convert the student’s            best progress, preventing repeated motion from accumulating
RGB-D observations into point clouds, encode them with                   reward.
the proprioceptive observations, and use conditional flow                   The penalties discourage large commands (Ptmag ), abrupt
matching to distill the demonstrated action-chunk distribution           action changes (Pt∆a ), hand–nut misalignment (Ptalign ), ex-
into a single visuomotor policy.                                         cess wrist force (Ptforce ), residual rotation near the target
                                                                         (Ptsettle ), insufficient table clearance (Ptclear ), and arm–table
C. Privileged Teacher Policy Training                                    contact (Ptcontact ).
    1) Simplified Thread Simulation: Our simplified thread                  We randomize the nut’s initial rotation and axial height
model couples a passive revolute joint to a coaxial, position-           and the controller settings to improve teacher robustness.
controlled prismatic joint, avoiding explicit thread contacts, as
illustrated in Fig. 3. With prismatic coordinate dt , unwrapped          D. Mixed-Dataset Construction with Human-Corrected Real-
direction-corrected revolute coordinate θt , thread pitch ρ, and         World Augmentation
turn-start index bk , the prismatic target is                               1) Cyclic Teacher Rollout in Simulation: In simulation,
                                 ρ                                       we combine the learned RL policy for MRL with scripted
                  d∗t − dbk = −     (θt − θbk ) ,             (4)
                                2π                                       controllers for Mscript . Let mt ∈ M denote the active
so one revolution produces one thread pitch of axial travel.             phase, xt the full simulator state, and zπt = gπ (xt , ξt ) the
Finger–nut contact forces remain active, while the revolute–             actor observation obtained by selecting the actor-visible state
prismatic mechanism constrains lateral motion and keeps the              components and applying observation noise ξt ; ht is the
nut near the commanded helix. The finite axial-drive stiffness           actor’s recurrent hidden state. During rollout, we use the
permits small deviations from this path. For revolute-joint              deterministic mean action of the Gaussian teacher policy,
velocity ωt , smoothed Coulomb and viscous friction give                 π̄T (zπt , ht ) = Ea∼πT (·|zπt ,ht ) [a]. The hybrid teacher is
τ̄f,t = −τc tanh(ωt /ωs ) − cv ωt , where τc is the Coulomb                                         (
friction torque, cv is the viscous damping coefficient, and ωs                                         π̄T (zπt , ht ), mt ∈ MRL ,
                                                                                  πHT (xt , mt ) =                                       (6)
is the smoothing speed.                                                                                κmt (xt ),       mt ∈ Mscript ,
    2) PPO Training: We train the privileged teacher using an
asymmetric recurrent actor–critic. The actor input contains              where κmt is the scripted controller for the active transition
noisy fingertip pose, fingertip velocity, nut-relative grasp             phase; both branches use the same filtered, bolt-relative
state, turning-target error, a grasp-phase flag, the previous            Cartesian controller action space.
action, and a nut-size one-hot code. The critic follows the                 Release is triggered when the rotation lies within ±5◦ of
same task and history structure using clean simulator values,            ϕtar (60◦ in our experiments), while a valid opposed-finger
and extends it with arm-joint positions, complete nut–bolt               grasp is maintained for a short dwell period. The fingers
geometry, controller state, and wrist and fingertip contact              then open to a safe clearance, after which scripted arm–hand
state. The one-hot code conditions a single teacher on M24,              waypoints return to the initial grasp pose and re-engage the
M30, and M36 hexagonal nuts. The actor and central critic                nut, completing the release-and-reset behavior. The turning
each use a two-layer LSTM with 1024 hidden units per layer,              reference is then updated, but the physical nut pose is not
followed by a 512–128–64 ELU MLP; recurrent sequences                    reset, producing complete multi-cycle demonstrations.
   2) Data Augmentation under Human Intervention: We                  Algorithm 1 Offline flow distillation with human intervention
replay simulated trajectories on the real system through the          Require: Hybrid teacher πHT , human operator πH , horizon
same Cartesian controller. When slip or misalignment is                   H
anticipated, an operator replaces the affected teacher-action          1: Collect simulated rollouts Dsim using πHT
segment from grasp through release, recovering stable contact          2: Replay them in the real world, overwriting failure-prone
and completing the turn. These human actions overwrite                    grasp-to-release segments with πH to obtain Dreal
the corresponding teacher actions in the trajectory, and the           3: Form H-step chunks from D = Dsim ∪ Dreal
resulting corrected trajectory is recorded as a real-world             4: repeat
demonstration.                                                         5:   Sample (yt , UD                0
                                                                                            t ) ∼ D, Ut ∼ N (0, I), and λ ∼
   Before training, we combine simulated rollouts and human-                U[0, 1]
corrected replays into a fixed offline dataset of RGB-D                6:   Encode the point cloud and fuse it with the condition-
observations, proprioception, normalized task progress, phase               ing inputs to obtain ct
encodings, and executed commands. We mask chunks that                  7:   Update θ by minimizing (7)
cross physical resets, retain phase boundaries, and pad                8:   Update EMA parameters θ̄ ← αθ̄ + (1 − α)θ
terminal chunks with the final valid command.                          9: until convergence
                                                                      10: return Student velocity field vθ̄
E. Student Policy Distillation
   Student learning is posed as supervised imitation from
the fixed dataset of simulated hybrid-teacher and human-                    a) Mean Completed Cycle Count: For trial i, Ci ∈
corrected demonstrations, D = Dsim ∪ Dreal . At time t, the           {0, 1, . . . , 10} counts completed cycles before failure or
student observes yt = (ORGBD       , st , pt , emt ) and learns the
                             t
                                                                             P incomplete cycles are excluded. We report C̄ =
                                                                      timeout;
distribution of the executed H-step action chunk, where emt           N −1 i Ci ; higher is better.
is the one-hot encoding of the active phase mt ∈ M from                     b) Cyclic Tracking Error: For completed cycle k in trial
(1).                                                                  i, the angular error is ei,k = ∆ϕi,k − 60◦ , where ∆ϕi,k =
   Following DP3[22], we transform each RGB-D observation
                                                                      Pi,k − ϕi,k−1 is the clockwise nut rotation. Over
                                                                      ϕ                                                       all M =
into a point cloud Pt for further processing. A compact                                                                    −1
                                                                                                                              P
                                                                           C
                                                                         i i    completed   cycles,  we  report µ cyc = M        i,k ei,k
PointNet with 64–128–256 pointwise layers and global max              and standard deviation σcyc . Negative values indicate lag and
pooling encodes Pt into a 64-D feature vt , which is fused            positive values overshoot; a mean closer to zero and a smaller
with proprioception, task progress, and phase information. A          deviation are better. If M = 0, both cyclic-error statistics are
128–128 ELU MLP encodes proprioception, and fusion yields             reported as “–.”
the 320-D condition ct . With H = 8, a four-layer non-causal                c) Ten-Cycle Tracking Error: Let I10 = {i : Ci = 10}
Transformer (512-D width, eight heads, and a 2048-D GELU              denote the trials that complete all P   ten cycles. For each i ∈
MLP) predicts velocities for the eight 9-D action tokens,                                                       10                ◦
                                                                      I10 , the ten-cycle error   is e 10,i =   k=1 ∆ϕi,k − 600 . We
conditioned on ct and a sinusoidal flow-time embedding.                                    −1
                                                                                              P
                                                                      report µ10 = |I10 |        i∈I10 e10,i and its standard deviation
During distillation, we follow DEXTRAH-RGB[17]-style                  over completed ten-cycle trials. Trials with fewer than ten
lighting and texture randomization to improve robustness and          completed cycles are excluded; if I10 is empty, the ten-cycle
reduce the sim-to-real gap.                                           error is reported as “–.” All errors are in degrees and use the
   The supervision target is the executed action chunk UD      t =    sign convention above.
[ut , . . . , uD
   D
               t+H−1 ] ∈ R
                          H×9
                               . We formulate its distillation as
conditional flow matching:                                            B. Experimental Setup
                           
                                                        2
                                                                        We simulate a seven-DoF Franka Research 3 (FR3) arm
            ∗                       λ                 λ
          θ = arg min E vθ (Ut , λ | ct ) − U̇t             ,         equipped with an Inspire Hand RH56DFX using Isaac
                    θ                           2
                                                               (7)    Sim 5.1.0 and Isaac Lab 2.2.1. The 9-D action space
                             λ          0    D
                   s.t.   Ut = (1 − λ)Ut + λUt ,                      encodes a six-DoF Cartesian-controller target and three
                          U̇λt = UD    0
                                  t − Ut .
                                                                      index–thumb joint commands. At 15 Hz, the student converts
                                                                      each RGB-D observation into a point cloud for further
The expectation is over (yt , UD             0
                                 t ) ∼ D, Ut ∼ N (0, I), and          processing and fuses a 64-dimensional DP3 feature with
λ ∼ U [0, 1]. The condition yt contains RGB-D, propriocep-            proprioception, progress, and phase; physics runs at 120 Hz.
tion, task progress, and phase information and is encoded as          For the retained M24 run, we train the PPO teacher for
ct . The learned velocity field transports Gaussian noise to          200 epochs in 512 environments. Using only 20 successful
the conditional action distribution pθ (Ut | yt ).                    ten-cycle demonstrations (19,486 frames) collected from 32
                        IV. E XPERIMENTS                              environments, we increase trajectory diversity by applying
                                                                      30 random arm impulses to each demonstration. On a single
A. Evaluation Metrics                                                 NVIDIA GeForce RTX 5090, training one teacher policy
   We evaluate each condition over N = 10 trials, with up to          takes approximately 10 hours, while student-policy training
ten cycles per trial. Each cycle consists of a 60◦ clockwise          takes approximately 30 minutes.
turn followed by the release-and-reset behavior.
                                                                                 (d) DP3 Vision + Transformer Distillation. Inspired by
                                                                                 the Transformer-based action-chunking design of ACT[23],
                                                                                 we use a deterministic variant without the CVAE objective.
                                                                                 It has four layers, eight attention heads, a 512-D hidden
                                                                                 representation, 2048-D feed-forward layers, and eight learned
                                                                                 action queries that predict an eight-step action chunk.
Fig. 4. Teacher policy training in Isaac Sim (left) and rollouts with lighting
and texture randomization (right).
                                                                                 (e) Ours with Only Simulated Data. We train the multi-cycle
                                                                                 student using only simulated hybrid-teacher demonstrations,
                                                                                 excluding all human-corrected real-world data.
   For real-world augmentation, 12 of the 20 replays (60%)                       (f) Ours. We train one flow-matching student on complete
contain at least one human correction. Human-overwritten                         multi-cycle hybrid-teacher demonstrations augmented with
grasp-to-release segments comprise only 6.48% of replay                          human-corrected real-world data.
frames; the remaining 93.52% retain hybrid-teacher actions,
                                                                                 D. Results
showing that intervention is temporally sparse. We train the
flow-matching student for 300 epochs using eight-step action                     TABLE I: Simulation and real-world ablations on the M24 hexagonal nut
chunks.                                                                          over 10 trials. Each defined entry reports the mean ± standard deviation.
   The physical platform comprises the same FR3 arm and                          Completed-cycle count is averaged across trials, cyclic-error statistics use
                                                                                 successful cycles only, and ten-cycle error compares accumulated rotation
Inspire Hand RH56DFX. An Intel RealSense D415 supplies                           with the 600◦ target. Ten-cycle error is reported as “–” when no trial
the RGB-D observations, which are converted into point                           completes all 10 cycles. Errors are signed in degrees: negative denotes
clouds before student inference. Robot commands use the                          lagging and positive denotes overshooting.
same Cartesian controller as in simulation. In real-world                                                      (a) Simulation
deployment, the flow-matching policy uses a prediction                                          Completed          Cyclic tracking         10-cycle tracking
horizon of eight and 16 ODE integration steps. Teacher and                       Ablation        cycles ↑            error → 0                error → 0
student training use only hexagonal nuts. We test M24, M30,                      (a)            5.5 ± 0.8          −4.16 ± 3.21                 –
and M36 hexagonal nuts in distribution and hold out the                          (b)            2.3 ± 0.9          +20.17 ± 7.80                –
octagonal, rectangular, and round geometries of each size for                    (c)            0.0 ± 0.0               –                       –
out-of-distribution evaluation.                                                  (d)            1.4 ± 0.8         +124.21 ± 18.50               –
                                                                                 (e)            10.0 ± 0.0         −1.77 ± 1.02            −17.7 ± 3.23
C. Ablations                                                                     (f) Ours       10.0 ± 0.0         −2.13 ± 1.10            −21.30 ± 3.48
   To investigate the contribution of individual components
                                                                                                              (b) Real World
in our framework, we conduct ablation studies focusing on
four key aspects: (Q1) whether a unified multi-cycle student                                     Completed          Cyclic tracking        10-cycle tracking
                                                                                 Ablation         cycles ↑            error → 0               error → 0
outperforms repeated execution of a single-cycle policy,
(Q2) the contribution of the DP3 point-cloud encoder, (Q3)                       (a)             5.2 ± 1.2         −4.56 ± 5.55                 –
the effectiveness of flow matching relative to deterministic                     (b)             1.1 ± 0.9         +24.09 ± 9.94                –
                                                                                 (e)             2.1 ± 1.4         −10.05 ± 4.08                –
behavior cloning with LSTM and Transformer backbones,
                                                                                 (f) Ours        10.0 ± 0.0        −4.21 ± 1.20            −42.10 ± 4.37
and (Q4) the benefit of augmenting simulation demonstrations
with human-corrected real-world trajectories during student
distillation. Results are averaged over 10 trials on the M24                        To address Q1, we compare the single-cycle student (a)
hexagonal nut and reported in Table I.                                           with our multi-cycle student (f). Our full method completes
   We compare six ablations under matched training and                           all 10 cycles in both simulation and the real world, whereas
evaluation budgets, changing only the component specified                        the single-cycle student completes only 5.5 and 5.2 cycles
by each ablation.                                                                on average, respectively. A typical failure mode is that the
(a) Single-Cycle Student. We train on real-world-augmented                       single-cycle-trained student slips off the edge of the nut after
single-cycle demonstrations and invoke the resulting policy                      a few cycles, showing that (a) learns the basic threading skill
ten times, resetting its temporal context after each cycle.                      but fails to follow the axial motion of the nut (Table I).
(b) Ours + ResNet Visual Encoder. We replace DP3 with a                             For Q2, we perform an ablation on the vision encoder
one-branch, ImageNet-pretrained ResNet-18 stage-2 encoder                        using both DP3 and ResNet-18 backbones, while holding the
that fuses RGB, log depth, validity, and calibrated XYZ                          policy, objective, data, and training budget fixed. A shared
geometry into a 64-D feature, while keeping the policy,                          decoder is used to evaluate the prediction error of the two
objective, data, and training budget fixed.                                      encoded features. The DP3 encoder achieves a positional
(c) DP3 Vision + LSTM Distillation. Using the same                               error of 8 mm and a rotational error of 15.16◦ in simulation,
real-world-augmented dataset as ours, we replace the flow-                       while ResNet-18 achieves a similar positional error of 8.6 mm
matching Transformer with the DEXTRAH-RGB[17]-style                              but a notably higher rotational error of 31.20◦ . Real-world
backbone—a layer-normalized 512-unit LSTM followed by                            conditions further amplify the difference, with ablation (f)
a 512–512–256 ELU MLP—trained using deterministic                                completing all 10 cycles while ablation (b) completes only
supervised action regression.                                                    1.1 cycles on average. The substantially larger rotational
                                                                                M24, M30, and M36 hexagonal nuts, as well as the out-of-
                                                                                distribution octagonal, rectangular, and round nuts, to charac-
                                                                                terize geometry-dependent transfer. Our method completes
                                                                                the task on the in-distribution training objects. The M30 nut
                                                                                achieves the smallest lag, with an average of 3.7◦ per cycle
                                                                                and 37◦ over the ten-cycle trial. The M36 hexagonal nut has
                                                                                the largest lag among the in-distribution sizes. We hypothesize
                                                                                that its larger geometry increases sensitivity to simulation-
Fig. 5. Real-world setup (left) and test-object family (right), comprising      model errors, including penetration-depth mismatch; however,
M24, M30, and M36 hexagonal, octagonal, rectangular, and round nuts with        our experiments do not isolate this factor.
corresponding bolts and holders.
                                                                                   Interestingly, among the tested out-of-distribution nut
                                                                                shapes, the round nut achieves the best performance, followed
                                                                                by the octagonal nut, in terms of both mean cyclic tracking
prediction error of the ResNet representation suggests that
                                                                                error and ten-cycle tracking error. Because we do not ablate
image-space features are less effective at preserving the
                                                                                individual geometry factors, we do not attribute this ranking
geometry required for repeated re-grasping under viewpoint
                                                                                to a specific geometric property.
and axial changes (Table I).
                                                                                   In contrast, the current policy performs poorly on the
   Results from ablations (c), (d), and (f) show that the choice
                                                                                rectangular nut. A common failure mode occurs after the nut
of student action backbone makes a substantial difference
                                                                                is turned 60◦ clockwise: in the next cycle, the fingers fail
in this long-horizon task, answering Q3. While the LSTM
                                                                                to establish contact with the next pair of faces, leaving the
backbone fails completely in simulation, diverging before
                                                                                nut stuck at the first 60◦ position. A smaller nut such as the
completing even the first cycle, the Transformer backbone
                                                                                M24 can escape this failure mode by chance, but it survives
survives slightly longer and completes 1.4 cycles on average,
                                                                                for only another two cycles before the mismatched policy
but soon faces the same compounding-error problem. Neither
                                                                                completely fails. Together, these results suggest that transfer
ablation (c) nor (d) advances to real-world testing (Table I).
                                                                                is strong when an unseen profile preserves cyclic re-grasp
   The comparison between ablations (e) and (f) provides                        configurations compatible with training, but degrades sharply
strong evidence for Q4. As shown in Table I, the student                        when its face topology conflicts with the learned re-grasp
policy distilled using only simulation data performs perfectly                  strategy.
in Isaac Sim, completing all 10 cycles and even achieving a
lower cyclic tracking error and standard deviation than our                               V. C ONCLUSION AND F UTURE W ORK
full method. However, when deployed in the real world, the                      A. Conclusion
hardware sim-to-real gap greatly affects its threading success
                                                                                   We presented NUTS, a framework for learning long-
rate, leaving ablation (e) able to complete only 2.1 cycles
                                                                                horizon cyclic nut threading with dexterous hands. Rather than
on average, with a cyclic tracking error of −10.05◦ and
                                                                                learning the entire task with a monolithic policy, NUTS de-
a standard deviation of 4.08◦ . In contrast, our full method
                                                                                composes demonstration generation into an RL-learned, goal-
maintains consistent performance in both simulation and real-
                                                                                conditioned turning skill and scripted transition behaviors,
world tests, completing all 10 cycles. In the real world, it
                                                                                while distilling the resulting long-horizon trajectories into a
achieves a cyclic tracking error of −4.21◦ with a standard
                                                                                unified visuomotor policy for deployment. Human corrections
deviation of 1.20◦ , slightly higher than in simulation.
                                                                                during real-world replay further adapt the demonstration
TABLE II: Geometry-dependent real-world transfer across nut sizes and           distribution to contact and perception discrepancies that are
profiles over 10 trials per nut. Values are mean ± standard deviation; shaded   difficult to capture in simulation.
rows denote out-of-distribution geometries.                                        Experiments show that the distilled policy reliably com-
                     Completed Cyclic tracking 10-cycle tracking                pletes 10 consecutive threading cycles on all training-
      Size Type       cycles ↑   error → 0        error → 0                     distribution nut sizes and transfers to unseen round and octag-
          Hex.  10.0 ± 0.0 −4.21 ± 1.20              −42.10 ± 4.37              onal profiles, while rectangular profiles expose a limitation
          Oct.  10.0 ± 0.0 −4.10 ± 1.16              −41.00 ± 4.20              of the learned re-grasp strategy. These results suggest that
      M24
          Rect. 3.0 ± 1.2 +30.30 ± 4.50                   –
          Round 10.0 ± 0.0 −2.33 ± 0.91              −23.30 ± 3.58
                                                                                structured behavior generation followed by unified policy
                                                                                distillation provides an effective approach to long-horizon,
             Hex.  10.0 ± 0.0      −3.70 ± 0.77      −37.00 ± 2.37
             Oct.  10.0 ± 0.0      −3.66 ± 0.58      −36.60 ± 1.74
                                                                                contact-rich dexterous manipulation.
      M30
             Rect. 0.0 ± 0.0            –                 –
             Round 10.0 ± 0.0      −2.45 ± 0.49      −24.50 ± 1.43              B. Future Work
          Hex.  10.0 ± 0.0         −5.52 ± 1.34      −55.20 ± 5.44                Long-horizon stress tests reveal a clear limitation: the
          Oct.  10.0 ± 0.0         −5.48 ± 1.22      −54.80 ± 4.75              current student policy eventually fails after 15–22 cycles,
      M36
          Rect. 0.0 ± 0.0               –                 –                     depending on nut size, geometry, and test conditions. This
          Round 10.0 ± 0.0         −4.78 ± 1.02      −47.80 ± 2.36
                                                                                degradation appears to be largely due to limited domain
                                                                                randomization along the z-axis, which inadequately covers the
   In Table II, we provide test data for the in-distribution                    axial drift accumulated over many cycles. An important next
step is therefore to introduce a curriculum that progressively                         on Intelligent Robots and Systems (IROS), 2017, pp. 23–30. [Online].
expands the axial variation encountered during training,                               Available: https://ieeexplore.ieee.org/document/8202133
                                                                                  [13] A. Wilcox, M. Ghanem, M. Moghani, P. Barroso, B. Joffe, and
improving the long-horizon capability of the RL teacher and,                           A. Garg, “Adapt3R: Adaptive 3D scene representation for domain
consequently, the distilled student.                                                   transfer in imitation learning,” in Proceedings of the 9th Conference
   To simplify the task, we deliberately initialize the nut                            on Robot Learning, ser. Proceedings of Machine Learning Research,
                                                                                       vol. 305. PMLR, 2025, pp. 1486–1514. [Online]. Available:
already engaged with the bolt. We adopted this setting after                           https://proceedings.mlr.press/v305/wilcox25a.html
unsuccessful attempts to learn or demonstrate nut engagement                      [14] Y. Jiang, C. Wang, R. Zhang, J. Wu, and L. Fei-Fei, “TRANSIC:
using reinforcement learning, teleoperation, and imitation                             Sim-to-real policy transfer by learning from online correction,” in
                                                                                       Proceedings of the 8th Conference on Robot Learning, ser. Proceedings
learning. We attribute much of the difficulty to the rigid                             of Machine Learning Research, vol. 270. PMLR, 2025, pp. 1691–1729.
nut and the helical thread constraint, which admit only a                              [Online]. Available: https://proceedings.mlr.press/v270/jiang25a.html
narrow entry configuration for successful engagement. Future                      [15] J. Zhang and K. Cho, “Query-efficient imitation learning for end-to-end
                                                                                       autonomous driving,” arXiv preprint arXiv:1605.06450, 2016. [Online].
work will therefore focus on autonomous nut engagement,                                Available: https://arxiv.org/abs/1605.06450
which we anticipate will require fine-grained fingertip-force                     [16] D. Chen, B. Zhou, V. Koltun, and P. Krähenbühl, “Learning by
feedback and tactile sensing.                                                          cheating,” in Proceedings of the Conference on Robot Learning, ser.
                                                                                       Proceedings of Machine Learning Research, vol. 100. PMLR, 2020,
                                                                                       pp. 66–75. [Online]. Available: https://proceedings.mlr.press/v100/
                              R EFERENCES                                              chen20a.html
                                                                                  [17] R. Singh, A. Allshire, A. Handa, N. Ratliff, and K. V. Wyk,
 [1] Y. Narang, K. Storey, I. Akinola, M. Macklin, P. Reist, L. Wawrzyniak,
                                                                                       “DextrAH-RGB: Visuomotor policies to grasp anything with dexterous
     Y. Guo, A. Moravanszky, G. State, M. Lu, A. Handa, and D. Fox,
                                                                                       hands,” arXiv preprint arXiv:2412.01791, 2024. [Online]. Available:
     “Factory: Fast contact for robotic assembly,” in Proceedings of Robotics:
                                                                                       https://arxiv.org/abs/2412.01791
     Science and Systems, New York City, NY, USA, June 2022. [Online].
                                                                                  [18] W. Wang, F. Wei, L. Zhou, X. Chen, L. Luo, X. Yi, Y. Zhang,
     Available: https://www.roboticsproceedings.org/rss18/p035.html
                                                                                       Y. Liang, C. Xu, Y. Lu, J. Yang, and B. Guo, “UniGraspTransformer:
 [2] M. Macklin, K. Erleben, M. Müller, N. Chentanez, S. Jeschke, and
                                                                                       Simplified policy distillation for scalable dexterous robotic grasping,”
     Z. Corse, “Local optimization for robust signed distance field collision,”
                                                                                       in Proceedings of the IEEE/CVF Conference on Computer Vision and
     Proceedings of the ACM on Computer Graphics and Interactive
                                                                                       Pattern Recognition (CVPR), June 2025, pp. 12 199–12 208. [Online].
     Techniques, vol. 3, no. 1, pp. 8:1–8:17, May 2020.
                                                                                       Available: https://dexhand.github.io/UniGraspTransformer/
 [3] E. Hsieh, W.-H. Hsieh, Y.-J. Wang, T. Lin, J. Malik, K. Sreenath,
                                                                                  [19] C. Chi, S. Feng, Y. Du, Z. Xu, E. Cousineau, B. C. M.
     and H. Qi, “Learning dexterous manipulation skills from imperfect
                                                                                       Burchfiel, and S. Song, “Diffusion policy: Visuomotor policy learning
     simulations,” in IEEE International Conference on Robotics and
                                                                                       via action diffusion,” in Proceedings of Robotics: Science and
     Automation (ICRA), 2026, arXiv:2512.02011. [Online]. Available:
                                                                                       Systems, Daegu, Republic of Korea, July 2023. [Online]. Available:
     https://dexscrew.github.io/
                                                                                       https://www.roboticsproceedings.org/rss19/p026.html
 [4] T. G. W. Lum, K. Kedia, C. K. Liu, and J. Bohg, “Play2Perfect:
                                                                                  [20] Y. Lipman, R. T. Q. Chen, H. Ben-Hamu, M. Nickel, and M. Le,
     What matters in dexterous play pretraining for precise assembly?”
                                                                                       “Flow matching for generative modeling,” in International Conference
     arXiv preprint arXiv:2606.26428, 2026. [Online]. Available: https:
                                                                                       on Learning Representations (ICLR), 2023. [Online]. Available:
     //arxiv.org/abs/2606.26428
                                                                                       https://openreview.net/forum?id=PqvMRDCJT9t
 [5] K. Kedia, T. G. W. Lum, J. Bohg, and C. K. Liu, “SimToolReal:
                                                                                  [21] K. Black, N. Brown, D. Driess, A. Esmail, M. R. Equi, C. Finn,
     An object-centric policy for zero-shot dexterous tool manipulation,”
                                                                                       N. Fusai, L. Groom, K. Hausman, B. Ichter, S. Jakubczak, T. Jones,
     arXiv preprint arXiv:2602.16863, 2026. [Online]. Available: https:
                                                                                       L. Ke, S. Levine, A. Li-Bell, M. Mothukuri, S. Nair, K. Pertsch,
     //arxiv.org/abs/2602.16863
                                                                                       L. X. Shi, L. Smith, J. Tanner, Q. Vuong, A. Walling, H. Wang,
 [6] B. Siciliano and O. Khatib, Eds., Springer Handbook of Robotics,
                                                                                       and U. Zhilinsky, “π0 : A vision-language-action flow model for
     2nd ed. Cham, Switzerland: Springer, 2016.
                                                                                       general robot control,” in Proceedings of Robotics: Science and
 [7] M. Noseworthy, B. Tang, B. Wen, A. Handa, C. C. Kessens, N. Roy,                  Systems, Los Angeles, CA, USA, June 2025. [Online]. Available:
     D. Fox, F. Ramos, Y. Narang, and I. Akinola, “FORGE: Force-guided                 https://www.roboticsproceedings.org/rss21/p010.html
     exploration for robust contact-rich manipulation under uncertainty,”         [22] Y. Ze, G. Zhang, K. Zhang, C. Hu, M. Wang, and H. Xu,
     IEEE Robotics and Automation Letters, vol. 10, no. 5, pp. 4436–4443,              “3D diffusion policy: Generalizable visuomotor policy learning via
     2025.                                                                             simple 3D representations,” in Proceedings of Robotics: Science
 [8] S. Ross, G. J. Gordon, and J. A. Bagnell, “A reduction of imitation               and Systems, Delft, Netherlands, July 2024. [Online]. Available:
     learning and structured prediction to no-regret online learning,” in              https://www.roboticsproceedings.org/rss20/p067.html
     Proceedings of the Fourteenth International Conference on Artificial         [23] T. Z. Zhao, V. Kumar, S. Levine, and C. Finn, “Learning fine-grained
     Intelligence and Statistics, ser. Proceedings of Machine Learning                 bimanual manipulation with low-cost hardware,” in Proceedings of
     Research, vol. 15. PMLR, 2011, pp. 627–635. [Online]. Available:                  Robotics: Science and Systems, Daegu, Republic of Korea, July 2023.
     https://proceedings.mlr.press/v15/ross11a.html
 [9] J. Kirkpatrick, R. Pascanu, N. Rabinowitz, J. Veness, G. Desjardins,
     A. A. Rusu, K. Milan, J. Quan, T. Ramalho, A. Grabska-Barwinska,
     D. Hassabis, C. Clopath, D. Kumaran, and R. Hadsell, “Overcoming
     catastrophic forgetting in neural networks,” Proceedings of the National
     Academy of Sciences, vol. 114, no. 13, pp. 3521–3526, 2017.
[10] Y. Lee, J. J. Lim, A. Anandkumar, and Y. Zhu, “Adversarial
     skill chaining for long-horizon robot manipulation via terminal
     state regularization,” in Proceedings of the 5th Conference on
     Robot Learning, ser. Proceedings of Machine Learning Research,
     vol. 164. PMLR, 2022, pp. 406–416. [Online]. Available:
     https://proceedings.mlr.press/v164/lee22a.html
[11] Y. Chen, C. Wang, L. Fei-Fei, and C. K. Liu, “Sequential dexterity:
     Chaining dexterous policies for long-horizon manipulation,” in
     Proceedings of the 7th Conference on Robot Learning, ser. Proceedings
     of Machine Learning Research, vol. 229. PMLR, 2023, pp. 3809–3829.
     [Online]. Available: https://proceedings.mlr.press/v229/chen23e.html
[12] J. Tobin, R. Fong, A. Ray, J. Schneider, W. Zaremba, and P. Abbeel,
     “Domain randomization for transferring deep neural networks from
     simulation to the real world,” in IEEE/RSJ International Conference
