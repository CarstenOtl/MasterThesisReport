HUMANIZER REVIEW OF thesis/source (suggestions only, no repository file was edited)

Scope: abstract, chapter01-06, acknowledgments, appendix, appendix_controller, read from the working tree.
Line numbers are source lines. Most paragraphs are one source line, so `file:line` identifies the paragraph.
All counts are case-insensitive ERE matches over the ten files with LaTeX comment lines removed.


1. OVERALL VERDICT

The thesis does not sound machine-written at the word level. It has no em dashes, no "crucial/pivotal/delve/landscape" vocabulary (four weak hits in total), no promotional adjectives and almost no vague attribution. The tells are structural, and a careful reader will notice them mainly in chapter03 (worst), chapter05, the motivation of chapter01, and the acknowledgments. chapter04, chapter02 and appendix A read as normal technical prose. Appendix B is not AI-sounding but reads as a lab notebook, which collides with the author's own standing rules (see section 5).

The four patterns that recur most:
- Announced, counted lists ("Three properties make ... First, ... Second, ...", "The first gap is ..."): about 40 announcements (42 count-noun hits, 23 sentence-initial "First,/Second,/Third,", 18 "The first/second/... is").
- The reveal colon, a short claim followed by ": " and its explanation: 77 lowercase-colon-lowercase constructions, roughly 35 of them reveals (21 in chapter03 alone).
- Contrast by negation ("X, not Y", "rather than", "it is not A, it is not B"): 23 "rather than", 17 "instead (of)", 11 ", not ".
- Closing-inference connectives and aphoristic paragraph closers: 37 "therefore", 14 "thus", 2 "thereby", with "thus" marking the interpretive sentence of four results paragraphs in chapter04.
A fifth pattern is not a classic AI tell but reads as machine-assembled: the same set-piece sentence reused verbatim in two to four chapters (section 3).


HUMANIZER SKILL VERSUS thesis/notes/writing_guidelines.md (guidelines win)

- Personality, opinions, first person, "let some mess in": not applied. Guidelines demand "formal but plain".
- Rhythm variation: the guidelines demand "one idea per sentence", which produces the short declarative runs the skill calls soulless. I only flag runs where several sentences are fragments of one thought, and the rewrites join them with a comma or a subordinate clause.
- Em dashes: the skill replaces them with commas, periods or parentheses and sometimes with semicolons. The guidelines forbid dashes and semicolons. The thesis has no em dash and two prose semicolons (appendix_controller.tex:72 and :430). No rewrite below uses either.
- Signposting and formulaic openers and closers: the skill removes them. The guidelines require a chapter opener, a chapter handover and a forward link per paragraph. Chapter-level roadmaps and handover sentences are therefore left alone. Only section-level inventories that duplicate a roadmap, and slogans, are flagged.
- Title-case headings: flagged by the skill, kept here because the AIR template and both reference theses use them.
- Hyphenated word pairs: contact-rich, long-horizon, zero-shot and similar are terms of art and are not flagged.
- Hedging: the guidelines allow hedges where evidence is uncertain. "is meant to" and "are designed to" in chapter05:16 and chapter06:11 are kept, because the thesis does not isolate those factors.
- Rule of three: most triples are real enumerations (three nut sizes, three hand joints). Only decorative ones are flagged.


2. FINDINGS PER FILE (ordered by importance within each file)

---------------------------------------------------------------------
abstract.tex (reads fine, three small items; the German arm at line 18 mirrors each and needs the same change)
---------------------------------------------------------------------

A1. abstract.tex:11 | slogan with reveal colon (fourth copy of the same slogan in the thesis)
  Original: "This thesis therefore follows one principle: decompose during data generation, unify at deployment."
  Rewrite: "This thesis therefore decomposes the task during data generation and unifies it at deployment."
  German (line 18): "Diese Arbeit zerlegt die Aufgabe daher bei der Datenerzeugung und vereint sie beim Einsatz."

A2. abstract.tex:11 | tailing "which makes" clause twice in three sentences
  Original: "A single reinforcement-learning (RL) policy for all phases needs a reward that covers every phase and every transition, which makes long-horizon reward shaping difficult."
  Rewrite: "A single reinforcement-learning (RL) policy for all phases needs a reward that covers every phase and every transition, and such a reward is difficult to shape over a long horizon."

A3. abstract.tex:11 | four-word punch sentence before the result
  Original: "Generalization depends on geometry. The student also completes all ten cycles on the octagonal and round profiles, but it fails on the rectangular profile, whose face topology conflicts with the learned re-grasp."
  Rewrite: "Among the unseen profiles, the student also completes all ten cycles on the octagonal and round nuts, but it fails on the rectangular profile, whose face topology conflicts with the learned re-grasp."

---------------------------------------------------------------------
chapter01.tex
---------------------------------------------------------------------

1.1 chapter01.tex:10 | reveal colon plus imperative mini-narrative (casual register)
  Original: "For a person the process is intuitive: pick up the screw, find the hole, seat the screwdriver, and turn. If the screw does not bite, back off, straighten it in the hole, and turn again."
  Rewrite: "A person fastens a screw without deliberate planning. The person picks up the screw, finds the hole, seats the screwdriver, and turns. If the screw does not bite, the person backs off, straightens it in the hole, and turns again."

1.2 chapter01.tex:15 | punchy antithesis with anaphora ("It stops working ... It also stops working") and a quip
  Original: "This setup pays off in high-volume production. It stops working where parts vary, where the cell is not built around one product, and where batches are small. It also stops working in maintenance and disassembly, where the hole is wherever the part happens to be."
  Rewrite: "This setup pays off in high-volume production. It is not available where parts vary, where the cell is not built around one product, or where batches are small, and it is not available in maintenance and disassembly, where the pose of the part is not fixed in advance."

1.3 chapter01.tex:11 and :13 | short teaser sentences that only set up the next sentence
  Original (11): "Industry solves the same task differently. In industrial production, turning the fastener along the thread is done by dedicated equipment."
  Rewrite: "In industrial production, dedicated equipment turns the fastener along the thread."
  Original (13): "None of these machines has to find the hole. A fixture clamps the part in a known pose, so the hole is always at the same place."
  Rewrite: "These machines do not have to find the hole, because a fixture clamps the part in a known pose."

1.4 chapter01.tex:58 | near-verbatim duplicate of chapter02.tex:125, and a stronger claim than its twin
  Original: "The four difficulties are addressed separately in prior work. Simulation-based assembly learning makes thread contact tractable ... No prior work threads a nut over many grasp-and-release cycles with a dexterous hand, and none does so with a policy trained on simulated data alone. Chapter~\ref{ch:sota} reviews this work in detail. The gap raises the research questions of the next section."
  Rewrite: "Prior work addresses these difficulties separately, in simulation-based assembly learning with parallel-jaw grippers~\cite{Narang2022,Noseworthy2025,Tang2023industreal}, in learned dexterous screwing~\cite{Hsieh2026,Lum2026}, in policy chaining~\cite{Lee2022,Chen2023}, and in teacher--student distillation of single skills~\cite{Lum2024,Singh2025}. None of the reviewed works threads a nut over many grasp-and-release cycles with a dexterous hand, and none does so with a policy trained on simulated data alone (Section~\ref{sec:related-gap}). This gap raises the research questions of the next section."
  Note: "No prior work" becomes "None of the reviewed works", which is the wording chapter02.tex:125 already uses. That is a claim-strength choice for the author.

1.5 chapter01.tex:54 | ordinal scaffold ("in three places. The first is ... The second is ... The third is ..."), the second such scaffold in two consecutive subsections
  Original: "... threading widens the gap between the two in three places. The first is contact. Any thread model ... The second is perception. A deployed policy ... The third is actuation. The simulated arm and hand omit ..."
  Rewrite: "A skill that is learned in simulation has to survive the transfer to hardware, and threading widens the gap between the two in contact, perception, and actuation. Any thread model that is cheap enough for parallel \ac{RL} simplifies the thread, so the simulated nut resists, slips, and jams differently from the physical one. A deployed policy has to perceive the nut through a camera, and rendered images differ from real ones in lighting, texture, and depth noise~\cite{Tobin2017,Handa2024}. The simulated arm and hand omit friction, backlash, and latency of the physical drives, so the same command moves the two systems differently."

1.6 chapter01.tex:18 | inflated framing ("The vision behind this thesis"), "trivial", reveal colon
  Original: "The vision behind this thesis is a dexterous robot that helps in manufacturing and assembly in a world built for humans. Threading a nut by hand is one of the basic skills such a robot needs. For humans the skill is trivial, but it is not for robots. This is an instance of Moravec's paradox: it is comparatively easy to make computers perform well on tasks that people find intellectually demanding, and difficult to give them the perception and mobility skills of a small child~\cite{Moravec1988}."
  Rewrite: "This thesis is motivated by dexterous robots that assist in manufacturing and assembly in environments built for humans. Threading a nut by hand is one of the basic skills such a robot needs, and it is easy for humans but hard for robots. Moravec's paradox describes this contrast. It is comparatively easy to make computers perform well on tasks that people find intellectually demanding, and difficult to give them the perception and mobility skills of a small child~\cite{Moravec1988}."

1.7 chapter01.tex:6 and :10 | sweeping uncited claim and two false ranges ("from X to Y")
  Original (6): "They appear in almost every industry. The halves of a cast engine housing are bolted together, ... Many valve and pipe connections consist of two threaded halves that are screwed together with a sealing material so that the fluid stays inside, from building plumbing to the cooling loop of a computer."
  Rewrite: "For example, the halves of a cast engine housing are bolted together, airplane seats are mounted with threaded bolts, and the injector of a rocket engine is bolted onto the combustion chamber. Many valve and pipe connections, in building plumbing as well as in the cooling loop of a computer, consist of two threaded halves that are screwed together with a sealing material so that the fluid stays inside."
  Original (10): "Threaded fasteners are also familiar from everyday life, from flat-pack furniture to household appliances."
  Rewrite: "Threaded fasteners are also familiar from everyday life, for example from flat-pack furniture and household appliances."

1.8 chapter01.tex:48 | aphorism ("moves the difficulty to"), used again at chapter02.tex:109, and "extra machinery"
  Original: "Chaining moves the difficulty to the transitions. The final state of one policy has to lie in the region where the next policy succeeds, which needs extra machinery that fine-tunes the sub-policies for their neighbors~\cite{Chen2023,Lee2022}, and several policies together with a switching logic have to be deployed."
  Rewrite: "In a chain, the final state of one policy has to lie in the region where the next policy succeeds. This requires additional mechanisms that fine-tune the sub-policies for their neighbors~\cite{Chen2023,Lee2022}, and several policies together with a switching logic have to be deployed."

1.9 chapter01.tex:30 | antithesis pair plus reveal colon, used three times in the thesis (also chapter02.tex:83, chapter03.tex:65)
  Original: "For large bodies this overlap is harmless. For threads it is not, because the thread geometry is small: the pitch is 3 to 4\,mm for the nuts used in this thesis."
  Rewrite: "This overlap is harmless for large bodies but not for threads, whose pitch is only 3 to 4\,mm for the nuts used in this thesis."

1.10 chapter01.tex:8 | setup sentence that says nothing on its own
  Original: "These applications have the same needs. The product has to be manufacturable in modules, assembled in a defined process, and opened again without damage for inspection, maintenance, repair, and development."
  Rewrite: "In all of these applications, the product has to be manufacturable in modules, assembled in a defined process, and opened again without damage for inspection, maintenance, repair, and development."

1.11 chapter01.tex:22 | meta signposting about the structure of the subsections
  Original: "The following subsections treat these difficulties in turn. Each states the difficulty, the reason it arises, and the requirement it places on the method."
  Rewrite: "The following subsections state each difficulty, the reason it arises, and the requirement it places on the method."

1.12 chapter01.tex:95 and :97, :101 | outline that lists the chapter titles, recaps the chapter just read, and repeats the roadmaps of chapter02.tex:4 and chapter04.tex:4 almost word for word
  Original (95): "This thesis comprises six chapters: Introduction, State of the Art, Methodology, Experiments, Discussion, and Conclusion and Future Work. This chapter motivated threading as a skill for dexterous robots, stated the four difficulties of learning it and the research questions that follow from them, and summarized the approach and the contributions."
  Rewrite: "The remainder of this thesis is organized as follows."
  Rewrite for 97: "Chapter~\ref{ch:sota} provides the theoretical background that the method builds on, reviews related work, and states the research gap."
  Rewrite for 101: "Chapter~\ref{ch:experiments} defines the evaluation metrics, the experimental setup, and the ablations, and it reports the results in simulation and on hardware, across nut sizes and geometries, and under long-horizon stress."

Lower priority: chapter01.tex:46 "..., rather than within a single phase." is a tailing negation on an uncited claim. Ending the sentence at "is made or broken." loses nothing.

---------------------------------------------------------------------
chapter02.tex (mostly reads as textbook prose)
---------------------------------------------------------------------

2.1 chapter02.tex:115 | "not as a switch" negation (same claim at chapter03.tex:12, :166, :196) and an aphoristic closer
  Original: "The phase enters the student only as a conditioning signal derived from physical events, not as a switch between networks, and the student predicts the transition actions itself (Section~\ref{sec:student}). The transitions are thus part of what the student learns rather than a problem to be solved between separate policies."
  Rewrite: "The phase enters the student as a conditioning signal derived from physical events, and the student predicts the transition actions itself (Section~\ref{sec:student}). The student therefore learns the transitions together with the phases."

2.2 chapter02.tex:39 | "X, not Y:" reveal
  Original: "Distillation changes the observation of the policy, not its action: the student imitates the action the teacher produced, in the teacher's action space, and the same controller executes it."
  Rewrite: "Distillation changes what the policy observes and leaves its action unchanged. The student imitates the teacher's action in the teacher's action space, and the same controller executes it."

2.3 chapter02.tex:61 | counted scaffold with three-word topic sentences ("First, training is simpler." "Second, sampling is faster."). This section has five counted lists (lines 41, 47, 47, 61, 103).
  Original: "First, training is simpler. The regression target is the difference of two samples, and the path fixes how noise and data are mixed over the flow time, so no noise schedule has to be designed. Second, sampling is faster. A straight path can be followed with a few large integration steps, whereas a curved path needs many small ones."
  Rewrite: "Training is simpler, because the regression target is the difference of two samples and the path fixes how noise and data are mixed over the flow time, so no noise schedule has to be designed. Sampling is faster, because a straight path can be followed with a few large integration steps, whereas a curved path needs many small ones."
  And: "Third, sampling is the deterministic integration of an \ac{ODE} from a given noise sample. The number of integration steps can therefore be chosen at run time, which trades accuracy against inference time without retraining."
  Rewrite: "Sampling is also the deterministic integration of an \ac{ODE} from a given noise sample, so the number of integration steps can be chosen at run time, which trades accuracy against inference time without retraining."

2.4 chapter02.tex:47 | counted scaffold that restates the paragraph before it (line 43 already explains sampling versus averaging)
  Original: "The generative action head has two advantages. First, when the demonstrations contain several valid actions for the same observation, a sample takes one of them rather than their average~\cite{Chi2024}. Second, the head can generate a whole action chunk (Section~\ref{sec:il-background}) as one sample, so that all actions of the chunk follow the same mode~\cite{Chi2024}."
  Rewrite: "When the demonstrations contain several valid actions for the same observation, a sample from the generative head takes one of them, whereas a regression head returns their average~\cite{Chi2024}. The head can also generate a whole action chunk (Section~\ref{sec:il-background}) as one sample, so that all actions of the chunk follow the same mode~\cite{Chi2024}."

2.5 chapter02.tex:97 | vague attribution opener ("According to a recent survey")
  Original: "According to a recent survey, analytical models of motion and contact have failed to provide practical solutions for in-hand manipulation because they cannot cope with complex environments and uncertainty, and research has therefore shifted to learning~\cite{Weinberg2024}."
  Rewrite: "Weinberg et al.~\cite{Weinberg2024} conclude in their survey that analytical models of motion and contact have failed to provide practical solutions for in-hand manipulation, because they cannot cope with complex environments and uncertainty, and that research has therefore shifted to learning."

2.6 chapter02.tex:99 | vague attribution ("Several works name") and "key challenge"
  Original: "Several works name the high-dimensional action space of the hand or of the hand--arm system as a key challenge of dexterous manipulation~\cite{Chen2021,Lum2024,Chen2023}."
  Rewrite: "Chen et al.~\cite{Chen2021}, Lum et al.~\cite{Lum2024}, and Chen et al.~\cite{Chen2023} each name the high-dimensional action space of the hand or of the hand--arm system as a main difficulty of dexterous manipulation."

2.7 chapter02.tex:109 and :111 | "moves the difficulty to" and "difficulties of its own" (same frame at :107 "each route has its own difficulties")
  Original (109): "Imitation avoids the reward problem but moves the difficulty to the data. One policy that imitates the whole task needs demonstrations of the whole task, and teleoperated demonstrations of forceful dexterous manipulation are hard to collect~\cite{Kedia2026}."
  Rewrite: "Imitation needs no reward. One policy that imitates the whole task, however, needs demonstrations of the whole task, and teleoperated demonstrations of forceful dexterous manipulation are hard to collect~\cite{Kedia2026}."
  Original (111): "Decomposing the task into skills shortens the horizon that each skill covers, but it creates difficulties of its own."
  Rewrite: "Decomposing the task into skills shortens the horizon that each skill covers, but it raises the problems of forgetting and of transitions between skills."

2.8 chapter02.tex:93 | double "rather than" in one sentence
  Original: "The \ac{RL} policy is rewarded for the angular velocity of the fastener rather than for reaching a target angle, its episodes end on failure or after a fixed time limit rather than on reaching a goal, and the nut is already installed on the bolt."
  Rewrite: "The \ac{RL} policy is rewarded for the angular velocity of the fastener, its episodes end on failure or after a fixed time limit, and the nut is already installed on the bolt. Neither the reward nor the termination refers to a target angle."

2.9 chapter02.tex:83 | second copy of the "harmless / it is not" pair
  Original: "Contact is therefore never strictly rigid. For large bodies the overlap is harmless. For threads it is not, because the flanks and crests of a thread with a pitch of a few millimeters are of the same order as the tolerated overlap."
  Rewrite: "Contact is therefore never strictly rigid. The overlap is harmless for large bodies, but the flanks and crests of a thread with a pitch of a few millimeters are of the same order as the tolerated overlap."

2.10 chapter02.tex:91 | the Factory sentence appears three times (chapter01.tex:28, chapter02.tex:79, :91), twice with the same wording inside this chapter
  Original: "Factory~\cite{Narang2022} combines signed-distance-field collision detection, contact reduction, and a Gauss--Seidel solver to simulate 1000 nut-and-bolt assemblies in real time on a single GPU, and it learns nut-and-bolt assembly with \ac{RL} through separate pick, place, and screw subpolicies."
  Rewrite: "Factory~\cite{Narang2022} makes nut-and-bolt contact tractable in simulation (Section~\ref{sec:thread-background}) and learns nut-and-bolt assembly with \ac{RL} through separate pick, place, and screw subpolicies."

2.11 chapter02.tex:37 | comma splice
  Original: "A policy in simulation satisfies this requirement, a recorded demonstration does not."
  Rewrite: "A policy in simulation satisfies this requirement, whereas a recorded demonstration does not."

---------------------------------------------------------------------
chapter03.tex (most AI-sounding chapter)
---------------------------------------------------------------------

3.1 chapter03.tex:196 | triple negative parallelism after "and nothing more:", the clearest tell in the thesis
  Original: "It is a monotonic clock for the complete behavior and nothing more: it is not a teacher-stage selector, it is not periodic, and it does not encode the cycle index."
  Rewrite: "It is a monotonic, non-periodic clock for the complete behavior and encodes neither the teacher stage nor the cycle index."
  Same paragraph, same pattern:
  Original: "The phase encoding is a synchronization aid: it does not switch networks or action contracts, and the student predicts the transition actions itself."
  Rewrite: "The phase encoding synchronizes the student with the cycle. One network with one action contract serves all phases, and the student predicts the transition actions itself."
  Note: the next sentence, "It tells the student how far into a nominally timed trial it is", repeats line 172 ("tells the student how far into the trial it is").

3.2 chapter03.tex:116 | "is what makes" cleft, inflated noun phrase, reveal colon with inverted negation
  Original: "This unified label space is what makes the demonstration a coherent supervision signal for one student: at no step does the label change meaning or units."
  Rewrite: "Because the label keeps its meaning and units at every step, one student can be supervised on the whole demonstration."

3.3 chapter03.tex:42, :46, :104, :166 (and chapter05.tex:8) | formula opener "X answers the Y difficulty of Section Z", five times
  Original (42): "The privileged teacher answers the dimensionality difficulty of Section~\ref{sec:difficulty-dexterity}. It learns to approach the nut, acquire the pinch grasp, keep it under load while turning, and stop at the target."
  Rewrite: "The privileged teacher learns to approach the nut, acquire the pinch grasp, keep it under load while turning, and stop at the target, which addresses the control problem of Section~\ref{sec:difficulty-dexterity}."
  Original (46): "The thread model answers the contact difficulty of Section~\ref{sec:difficulty-contact}: the skill is learned in simulation, so the simulated thread has to behave like a mating thread in each of the hundreds of parallel environments that \ac{PPO} needs."
  Rewrite: "Because the skill is learned in simulation, the simulated thread has to behave like a mating thread in each of the hundreds of parallel environments that \ac{PPO} needs (Section~\ref{sec:difficulty-contact})."
  Original (104): "The hybrid teacher answers the training side of the long-horizon difficulty of Section~\ref{sec:difficulty-horizon}: it chains the learned turn with scripted release and return, so that each phase is specified by the mechanism that specifies it most simply, and it rolls the chain out in simulation to produce complete multi-cycle demonstrations."
  Rewrite: "The hybrid teacher chains this turn with scripted release and return and rolls the chain out in simulation to produce complete multi-cycle demonstrations, so that each phase is specified by its simplest mechanism (Section~\ref{sec:difficulty-horizon})."
  Original (166): "The student answers the deployment side of the long-horizon difficulty of Section~\ref{sec:difficulty-horizon}. The hybrid teacher cannot be deployed, because both its learned policy and its scripted controllers act on privileged simulator state \eqref{eq:hybrid}. The student replaces it with one visuomotor policy that executes every phase of every cycle from sensor data, without a phase switch or separate networks."
  Rewrite: "The hybrid teacher cannot be deployed, because both its learned policy and its scripted controllers act on privileged simulator state \eqref{eq:hybrid}. The student replaces it with one visuomotor policy that executes every phase of every cycle from sensor data, which is the deployable policy that Section~\ref{sec:difficulty-horizon} requires."

3.4 chapter03.tex:120 | counted scaffold, two reveal colons, "X rather than Y:", and the informal "repairs nothing by teleporting"
  Original: "Two details of the coordinator matter for the quality of the labels. First, the scripted transitions never write physics state: a transition may request that the thread joint be held while the hand is away, but it repairs nothing by teleporting the nut, so every recorded frame is a physically consistent consequence of the recorded commands. Second, the release gate is physical rather than timed: release is decided from the measured nut rotation, and the return is validated against the reset frame, so the phase labels in the recording coincide with physical events."
  Rewrite: "The scripted transitions never write physics state. A transition may request that the thread joint be held while the hand is away, but it does not reposition the nut, so every recorded frame is a physically consistent consequence of the recorded commands. The transitions are also gated by physical events. Release is decided from the measured nut rotation, and the return is validated against the reset frame, so the phase labels in the recording coincide with physical events."

3.5 chapter03.tex:12 | "only:" reveal with a zeugma ("receives neither the phase label as a switch nor separate networks")
  Original: "The split is a property of the data-generation stage only: the deployed student receives neither the phase label as a switch nor separate networks per phase."
  Rewrite: "The split exists only during data generation. The deployed student is one network for all phases."
  Note: the "no switch, no separate networks" claim appears four times (chapter02.tex:115, chapter03.tex:12, :166, :196). Stating it once at :196, where the phase encoding is defined, is enough.

3.6 chapter03.tex:118 | unexplained jargon followed by an "X, not Y" contrast
  Original: "The teacher population was first qualified for one period only. Repeated cycles are a property of the hybrid rollout, not of the \ac{RL} teacher alone."
  Rewrite: "The \ac{RL} teacher is trained on a single turn, and the repeated cycles come from the hybrid rollout."
  Flag: "teacher population" and "one period" are defined nowhere, so the rewrite assumes "period" means one cycle. The author has to confirm the technical content.

3.7 chapter03.tex:67 | the same point three times in three sentences (and again at chapter02.tex:83 and chapter05.tex:8)
  Original: "A policy rewarded for axial progress can learn this shortcut, which fails on hardware. A kinematic coupling instead makes axial progress a consequence of rotation alone, so that progress can only be earned by turning. The thread model used for teacher training therefore replaces the thread contact by a kinematic coupling, illustrated in Figure~\ref{fig:thread-model}."
  Rewrite: "A policy rewarded for axial progress can learn this shortcut, which fails on hardware. The thread model used for teacher training therefore replaces the thread contact by a kinematic coupling, illustrated in Figure~\ref{fig:thread-model}, in which axial progress follows from rotation alone."

3.8 chapter03.tex:75 | two reveal colons, "deliberate"
  Original: "The finger--nut contact forces remain fully simulated: the policy must physically grip and turn the nut."
  Rewrite: "The finger--nut contact forces remain fully simulated, so the policy must grip and turn the nut."
  Original: "The model has one deliberate simplification beyond contact: the nut is initialized already engaged with the bolt."
  Rewrite: "Beyond the contact simplification, the nut is initialized already engaged with the bolt."

3.9 chapter03.tex:48 and :65 | third copy of the depenetration explanation and of the "harmless / it is not" pair (chapter01.tex:30, chapter02.tex:81-83)
  Original (65): "For large bodies this tolerance is harmless. For threads it is not, because the pitch of the nuts used in this thesis is only 3 to 4\,mm and the flanks and crests are smaller still."
  Rewrite: "This tolerance matters for threads, because the pitch of the nuts used in this thesis is only 3 to 4\,mm and the flanks and crests are smaller still."
  Suggestion for 48: open with "PhysX resolves contact through interpenetration (Section~\ref{sec:thread-background}, Figure~\ref{fig:depenetration})." and drop the closing two sentences "Contact is therefore never strictly rigid. It tolerates a small overlap, and the repulsive response grows with that overlap.", which chapter02.tex:83 already states.

3.10 chapter03.tex:135 | elliptical antithesis whose antecedent is two sentences back ("Appearance and depth quality do not")
  Original: "Camera geometry and field of view therefore agree between the two domains up to calibration error. The collection covers this error: at every reset, the pose of the simulated camera is shifted by a uniform offset of up to $\pm11.2$\,mm per axis and rotated by up to $\pm1.13\degree$ per axis, sized from the residual of the hand--eye fit (Table~\ref{tab:datasets}). Appearance and depth quality do not, because a rendered scene has one clean appearance and a rendered depth image contains no sensor noise."
  Rewrite: "Camera geometry and field of view therefore agree between the two domains up to calibration error. To cover this error, the pose of the simulated camera is shifted at every reset by a uniform offset of up to $\pm11.2$\,mm per axis and rotated by up to $\pm1.13\degree$ per axis, sized from the residual of the hand--eye fit (Table~\ref{tab:datasets}). Appearance and depth quality differ between the two domains, because a rendered scene has one clean appearance and a rendered depth image contains no sensor noise."

3.11 chapter03.tex:100 | "which makes X a hard constraint rather than a shaped term" (repeated at chapter05.tex:8)
  Original: "It terminates early when the nut leaves the bolt, tilts, or releases the thread, or when the latched grasp is lost, which makes grasp retention a hard constraint rather than a shaped term."
  Rewrite: "It terminates early when the nut leaves the bolt, tilts, or releases the thread, or when the latched grasp is lost. Grasp retention is thereby a hard constraint."

3.12 chapter03.tex:131 | redundant sentence pair with jargon ("materialization", "explicitly successful")
  Original: "Demonstrations in which the teacher fails to complete all cycles are rejected before materialization. The retained set consists only of explicitly successful episodes."
  Rewrite: "Demonstrations in which the teacher fails to complete all cycles are rejected, so the dataset contains only successful episodes."

3.13 chapter03.tex:42, :104, :170 (also chapter04.tex:27, :133) | section-level inventories directly above the subsection headings they list
  Original (42): "This section first describes the simplified thread model on which the teacher's training depends, and then the training of the teacher with \ac{PPO}."
  Original (104): "This section describes the cyclic rollout, the disturbance augmentation, the vision data collection, and the dataset format."
  Original (170): "This section states what the head is trained to generate and which signals it is conditioned on."
  Suggestion: delete all three. The chapter opener at line 4 already gives the roadmap, which is what the guidelines ask for.

---------------------------------------------------------------------
chapter04.tex (reads mostly fine)
---------------------------------------------------------------------

4.1 chapter04.tex:251 | therefore, thus, therefore in five sentences, purpose stated twice, tailing negation ("but not indefinitely")
  Original: "The student is run on hardware for as many cycles as it sustains, to measure how far its horizon extends beyond the ten cycles of the demonstrations. Every revolution advances the nut by one pitch down the bolt. After enough cycles, the nut therefore leaves the axial range that the ten-cycle demonstrations cover. The stress trials thus measure how far the learned behavior reaches along the bolt. The student sustains between 15 and 22 cycles before it fails, depending on nut size, profile, and test conditions. It therefore extends the demonstrated horizon by at least half, but not indefinitely."
  Rewrite: "The student is run on hardware for as many cycles as it sustains. Every revolution advances the nut by one pitch down the bolt, so after enough cycles the nut leaves the axial range that the ten-cycle demonstrations cover. The stress trials measure how far the learned behavior reaches beyond this range. The student sustains between 15 and 22 cycles before it fails, depending on nut size, profile, and test conditions, which extends the demonstrated horizon by at least half."

4.2 chapter04.tex:219 | "thus" closer built as a symmetric antithesis that generalizes from three profiles
  Original: "Transfer thus holds when an unseen profile preserves re-grasp configurations compatible with the hexagon, and it breaks when the face topology conflicts with the learned re-grasp."
  Rewrite: "The octagonal and round profiles offer re-grasp configurations compatible with the hexagon, whereas the face topology of the rectangular profile conflicts with the learned re-grasp."
  Also line 219: "The rectangular profile fails." is a four-word punch sentence. Merge: "On the rectangular profile, the M24 nut completes $3.0\pm1.2$ cycles, and the M30 and M36 nuts complete none."

4.3 chapter04.tex:109 | "rests entirely on", announced count followed by four disconnected sentences, decorative triple ("images, trajectories, or corrections")
  Original: "No real-world images, trajectories, or corrections enter its training, and it is not fine-tuned on the robot. The transfer therefore rests entirely on four properties of the pipeline. The calibrated camera described above is the one that rendered the demonstrations. The point-cloud crop box removes the physical background before encoding. The demonstrations were rendered under lighting, texture, and background randomization. The Cartesian targets are executed by the impedance controller described above."
  Rewrite: "No real-world data enter its training, and it is not fine-tuned on the robot. The transfer therefore depends on four properties of the pipeline: the calibrated camera described above is the one that rendered the demonstrations, the point-cloud crop box removes the physical background before encoding, the demonstrations were rendered under lighting, texture, and background randomization, and the impedance controller described above executes the Cartesian targets."
  Note: dropping "corrections" also keeps the text clear of the human-correction topic.

4.4 chapter04.tex:19 | colon list that continues as separate sentences, "neither ... nor" closer, "which is the regime that motivates"
  Original: "It establishes neither controller correctness nor closed-loop success."
  Rewrite: "Controller correctness and closed-loop success are tested by the next two modes."
  Original: "The two diagnostic modes are used in that order to localize a failure before expensive retraining: a bad offline fit points to capacity, normalization, or alignment. A good fit with bad teacher-forced execution points to the command contract. Good teacher-forced execution with a bad closed loop points to distribution shift and recovery, which is the regime that motivates online labels or disturbance augmentation."
  Rewrite: "The two diagnostic modes are used in that order to localize a failure before expensive retraining. A bad offline fit points to capacity, normalization, or alignment. A good fit with bad teacher-forced execution points to the command contract. Good teacher-forced execution with a bad closed loop points to distribution shift and recovery, which online labels or disturbance augmentation address."

4.5 chapter04.tex:133, :137, :165 | the same justification twice within five lines, generic opener, and the five ablations described once in prose and again in the list
  Original (137): "The teacher of Section~\ref{sec:teacher} is the starting point of the pipeline, so its result is reported before the students. Table~\ref{tab:teacher-results} summarizes the last ten of its 200 training epochs."
  Rewrite: "Table~\ref{tab:teacher-results} summarizes the last ten of the 200 training epochs of the teacher of Section~\ref{sec:teacher}."
  Original (165): "To investigate the contribution of individual components, the ablation study focuses on three aspects."
  Rewrite: "The ablation study addresses three questions."
  Suggestion for 165: delete "Ablation (a) replaces the training data and addresses RQ1. Ablation (b) replaces ... These three address RQ2. Ablation (e) is the full method.", because the list (a) to (e) follows immediately and the RQ mapping is given two sentences earlier.

4.6 chapter04.tex:180 | "thus" inference with a vague tail, and interpretation inside a results sentence
  Original: "The student thus lags the $60\degree$ target by less than two degrees per cycle, and the lag accumulates over the trial without its spread drifting."
  Rewrite: "The student lags the $60\degree$ target by less than two degrees per cycle, and the lag accumulates over the trial."
  Flag: "without its spread drifting" names no number. Either cite the value that supports it or drop it.
  Original: "The Transformer regression student (d) completes $1.4\pm0.8$ cycles with an overshoot of $+124.21\pm18.50\degree$, so it fails from the same compounding error after a short delay."
  Rewrite: "The Transformer regression student (d) completes $1.4\pm0.8$ cycles with an overshoot of $+124.21\pm18.50\degree$."
  Note: the cause is an interpretation, and chapter05.tex:14 discusses it.

4.7 chapter04.tex:207 | emphatic "exactly", and a closing sentence that chapter05.tex:12 repeats almost verbatim
  Original: "A re-grasp needs exactly the orientation of the nut faces relative to the fingers, so the probe tests whether a representation carries the quantity on which the closed loop depends."
  Rewrite: "A re-grasp depends on the orientation of the nut faces relative to the fingers, so the probe tests whether a representation carries this quantity."
  Original: "The image-space feature thus preserves the nut position but loses much of the face orientation on which the re-grasp depends, which is consistent with the early failure of (b) in closed loop."
  Suggestion: keep this sentence in only one of the two chapters. The guidelines place interpretation in the discussion.

4.8 chapter04.tex:212 | "which shows that" claims more than an observed failure mode can show (chapter05.tex:10 words the same point as "the failure expected from")
  Original: "In its typical failure, the fingers slip off the edge of the nut after a few cycles, which shows that the student has learned the turning skill but does not follow the axial advance of the nut."
  Rewrite: "In its typical failure, the fingers slip off the edge of the nut after a few cycles, which is consistent with a student that has learned the turning skill but does not follow the axial advance of the nut."

4.9 chapter04.tex:75 | figurative verb ("meet the stiffness")
  Original: "The student's commands therefore meet the stiffness under which the teacher acquired its contact behavior."
  Rewrite: "The student's commands are therefore executed with the stiffness under which the teacher learned its contact behavior."

---------------------------------------------------------------------
chapter05.tex (second most AI-sounding chapter)
---------------------------------------------------------------------

5.1 chapter05.tex:38 | rhetorical pivot ("These gaps do not erase what the result shows."), mixed tense, and a closer that reappears at chapter06.tex:22
  Original: "These gaps do not erase what the result shows. In simulation, a learned policy controlled a dexterous hand through ten cycles of grasp, turn, release, and return, and it re-grasped the nut at the angle and height that the previous cycle left it. It perceives the nut from one fixed camera, and it is trained without any real data. ... Whether this versatility outweighs the speed of a dedicated tool depends on the application, and the remaining gaps define the work that separates the two (Chapter~\ref{ch:conclusion})."
  Rewrite: "Within these limits, in simulation, a learned policy controlled a dexterous hand through ten cycles of grasp, turn, release, and return, and it re-grasped the nut at the angle and height at which the previous cycle left it. It perceived the nut from one fixed camera, and it was trained without any real data. ... Whether this versatility outweighs the speed of a dedicated tool depends on the application. Chapter~\ref{ch:conclusion} turns the remaining gaps into future work."
  See section 4 for the sentence "The same hand also picks up a loose nut in simulation.", which is left untouched here.

5.2 chapter05.tex:19 and :4 | aphoristic "lesson" in prescriptive voice with a "therefore" that no experiment supports
  Original (19): "A student should therefore imitate the action the teacher produced, in the units the teacher produced it, and let the controller do the conversion it was designed for."
  Rewrite: "The student therefore imitates the teacher's action in the teacher's units and leaves the conversion to the controller."
  Original (4): "Section~\ref{sec:disc-contracts} draws the lesson of the action and observation contracts."
  Rewrite: "Section~\ref{sec:disc-contracts} discusses the action and observation contracts."

5.3 chapter05.tex:12 | run of ten short declaratives without connectives, with a "does not need X. ... What the student needs is Y" pseudo-cleft
  Original: "On the representation side, the student does not need to localize the nut to sub-millimeter accuracy. The engagement of the nut on the bolt and the compliance of the impedance controller absorb lateral error. What the student needs is the orientation of the nut faces for the re-grasp and the height of the nut for the approach."
  Rewrite: "On the representation side, sub-millimeter localization of the nut is unnecessary, because the engagement of the nut on the bolt and the compliance of the impedance controller absorb lateral error. The student needs the orientation of the nut faces for the re-grasp and the height of the nut for the approach."
  Original: "The point-cloud encoder consumes the metric geometry of nut, bolt, and hand directly. It has about 60\,000 parameters and no pretrained image backbone."
  Rewrite: "The point-cloud encoder consumes the metric geometry of nut, bolt, and hand directly, with about 60\,000 parameters and no pretrained image backbone."
  Original: "The probe is consistent with an orientation deficit. The two features locate the nut with similar position errors of 8\,mm and 8.6\,mm, but ..."
  Rewrite: delete the first sentence. The numbers that follow make the point, and the final sentence of the paragraph states it again.

5.4 chapter05.tex:25 to :35 and chapter06.tex:26 to :36 | rigid ordinal template over ten consecutive paragraphs ("The first gap is ...", "The second gap is ...", "The first extension is ...", "The fifth extension concerns ...", "The last extension completes ...")
  Original (25): "Measured against an industrial fastening step, the demonstrated skill covers the run-down of an engaged nut and leaves four gaps."
  Rewrite: "Measured against an industrial fastening step, the demonstrated skill covers the run-down of an engaged nut and leaves gaps at the start of the task, at its end, in the grasp, and in cycle time."
  Original (27): "The first gap is the start of the task. Every trial starts with the nut already engaged on the bolt (Section~\ref{sec:thread-model}). ... Engagement is therefore not covered by the demonstrated skill."
  Rewrite: "Every trial starts with the nut already engaged on the bolt (Section~\ref{sec:thread-model}). In assembly the nut arrives loose and has to be seated on the thread first, which is a separate skill with a narrow entry configuration."
  Original (29): "The second gap is the end of the task. A trial ends after ten turns of $60\degree$, ..."
  Rewrite: "A trial ends after ten turns of $60\degree$, ..."
  Original (33): "The third gap is the grasp. The student executes one strategy, ..."
  Rewrite: "The student executes one grasp strategy, ..."
  Original (35): "The fourth gap is cycle time. In the demonstrations, release and return take ..."
  Rewrite: "In the demonstrations, release and return take ..."
  The chapter06 rewrites are under 6.4.

5.5 chapter05.tex:10 | teaser sentence and a "thus ... the principle that ..., rather than ..., yields" closer
  Original: "The content of the data is the likely reason. In a single-cycle demonstration the nut is always grasped at its reset height, so a student trained on it never has to read the height from the point cloud."
  Rewrite: "The likely reason is that a single-cycle demonstration always shows the nut at its reset height, so a student trained on it never has to read the height from the point cloud."
  Original: "The result thus supports the principle that unifying the complete cyclic behavior in one dataset, rather than invoking a per-cycle policy repeatedly, yields a policy that sustains consecutive cycles."
  Rewrite: "A student trained on the complete cyclic behavior thus sustains consecutive cycles, whereas a per-cycle policy invoked repeatedly does not."

5.6 chapter05.tex:14 | counted scaffold, punch sentence, and a negation wedged into the main clause
  Original: "Two mechanisms could favor the flow head. The first is multimodality of the labels. ... The second is the structure of the prediction."
  Rewrite: "Two mechanisms could favor the flow head, the multimodality of the labels and the structure of the prediction. For near-identical observations, the dataset contains ... The flow head also predicts a velocity from a noisy chunk toward the data, ..."
  Original: "Both regression heads fail first. The \ac{LSTM} student (c) diverges before it completes the first cycle, and ..."
  Rewrite: delete "Both regression heads fail first." It repeats chapter04.tex:180.
  Original: "Because (d) differs from (e) only in the objective, the generative objective, and not the backbone or the chunking, separates the full method from this failure."
  Rewrite: "Because (d) differs from (e) only in the objective, the generative objective accounts for the difference between this failure and the full method."

5.7 chapter05.tex:33 | anaphora on "carries" (three times), punch sentence
  Original: "The held-out octagonal, rectangular, and round profiles of Section~\ref{sec:geometry} test how far the single strategy carries. It carries to the octagonal and round profiles, on which the student completes all ten cycles in every trial at all three sizes, and the round nut shows the smallest lag at every size. It does not carry to the rectangular profile. The student completes $3.0\pm1.2$ cycles on the M24 rectangular nut and none on the M30 and M36 rectangular nuts (Table~\ref{tab:geometry})."
  Rewrite: "The held-out octagonal, rectangular, and round profiles of Section~\ref{sec:geometry} test how far the single strategy generalizes. On the octagonal and round profiles, the student completes all ten cycles in every trial at all three sizes, and the round nut shows the smallest lag at every size. On the rectangular profile, it completes $3.0\pm1.2$ cycles on the M24 nut and none on the M30 and M36 nuts (Table~\ref{tab:geometry})."

5.8 chapter05.tex:8 | "well posed:" reveal, fifth "answers the ... difficulty", fourth "can only be earned by turning", tense slip
  Original: "The kinematic constraint makes the learning problem well posed: it ties axial progress to rotation, so the progress reward can only be earned by turning. The teacher also answers the dimensionality difficulty of Section~\ref{sec:difficulty-dexterity}: with the hand restricted to three commanded pinch degrees of freedom, it acquires the pinch grasp and keeps it under the turning load, and losing the grasp after it has latched ends the episode, which makes grasp retention a hard constraint (Section~\ref{sec:teacher})."
  Rewrite: "The kinematic constraint ties axial progress to rotation, so the policy earns the progress reward only by turning. With the hand restricted to three commanded pinch degrees of freedom (Section~\ref{sec:difficulty-dexterity}), the teacher acquires the pinch grasp and keeps it under the turning load. Losing the grasp after it has latched ends the episode, so grasp retention is a hard constraint (Section~\ref{sec:teacher})."
  Original: "The \ac{RL} teacher solves one turn, and the hybrid rollout extended it to ten consecutive cycles."
  Rewrite: "The \ac{RL} teacher solves one turn, and the hybrid rollout extends it to ten consecutive cycles."

5.9 chapter05.tex:16 | convoluted "since ... is also what ... differs from", "The same geometric property ... matters here:" reveal
  Original: "RQ3 asks whether a student trained on simulated data only transfers zero-shot to the physical system, and it tests the transfer difficulty of Section~\ref{sec:difficulty-transfer} together with the contact difficulty of Section~\ref{sec:difficulty-contact}, since the thread model that makes training feasible is also what the physical thread differs from."
  Rewrite: "RQ3 asks whether a student trained on simulated data only transfers zero-shot to the physical system. It tests the transfer difficulty of Section~\ref{sec:difficulty-transfer} together with the contact difficulty of Section~\ref{sec:difficulty-contact}, because the simplified thread model differs from the physical thread."
  Original: "The same geometric property that RQ2 relies on matters here: inside the crop box the point geometry is identical in both domains up to depth noise and calibration error, whereas an image-space encoder faces the appearance gap of the full image."
  Rewrite: "Inside the crop box, the point geometry is identical in both domains up to depth noise and calibration error, whereas an image-space encoder faces the appearance gap of the full image."

5.10 chapter05.tex:42 | limitations as one block of unlinked short sentences, section-level signposting, opaque phrase
  Original: "Section~\ref{sec:disc-assembly} described the task-level gaps to industrial threading. This section states the limitations of the method and of the evidence."
  Rewrite: "Beyond the task-level gaps of Section~\ref{sec:disc-assembly}, the method and the evidence have the following limitations."
  Original: "It is measured but not deployment-validated, and the dependence of the student on calibration error has not been quantified."
  Rewrite: "The dependence of the student on this calibration error has not been quantified."
  Flag: "measured but not deployment-validated" is opaque. If it carries a fact, state the fact. The paragraph would also read better split into method limits (grasp, axial range, thread model) and evidence limits (randomization ranges, calibration, ten trials).

5.11 chapter05.tex:21 | filler link ("follows the same logic") that the next sentence does not bear out
  Original: "The observation contract follows the same logic. The student receives the previous filtered action, which the teacher also observes, ..."
  Rewrite: "The student receives the previous filtered action, which the teacher also observes, ..."

---------------------------------------------------------------------
chapter06.tex
---------------------------------------------------------------------

6.1 chapter06.tex:22 | participial opener with colon, "can now" followed by "What it cannot yet do is" pseudo-cleft, slogan closer
  Original: "Returning to the motivation of Section~\ref{sec:motivation}: in simulation, a dexterous hand can now thread a nut over ten consecutive cycles with a learned policy, re-grasping it in every cycle from camera data at the angle and height that the previous cycle left it, and the policy is trained without real data. It does so zero-shot on the physical system as well, on hexagonal nuts of three sizes and on unseen octagonal and round profiles (RQ3). What it cannot yet do is start from a loose nut, tighten the joint, choose a different grasp when the resistance grows, or match the speed of a dedicated tool (Section~\ref{sec:disc-assembly}). These gaps define the future work."
  Rewrite: "With respect to the motivation of Section~\ref{sec:motivation}, a dexterous hand can thread a nut in simulation over ten consecutive cycles with a learned policy that is trained without real data. The policy re-grasps the nut in every cycle from camera data at the angle and height at which the previous cycle left it. It does so zero-shot on the physical system as well, on hexagonal nuts of three sizes and on unseen octagonal and round profiles (RQ3). It cannot yet start from a loose nut, tighten the joint, choose a different grasp when the resistance grows, or match the speed of a dedicated tool (Section~\ref{sec:disc-assembly}). Section~\ref{sec:future-work} addresses these gaps."

6.2 chapter06.tex:13 | empty bridging verdict
  Original: "The evidence is consistent with the principle. In simulation, the distilled student completes all ten cycles ..."
  Rewrite: "In simulation, the distilled student completes all ten cycles ..."

6.3 chapter06.tex:11 | fourth copy of the slogan with reveal colon
  Original: "The thesis answers these difficulties with one principle: decompose during data generation, unify at deployment. During data generation the cycle is decomposed into a turning skill and scripted transitions."
  Rewrite: "The thesis answers these difficulties by decomposing the task during data generation and unifying it at deployment. During data generation the cycle is decomposed into a turning skill and scripted transitions."

6.4 chapter06.tex:26 to :36 | ordinal template (see 5.4), with the vague verb "concerns" twice and "completes" once
  Original (26): "The first extension is autonomous engagement of a loose nut. It requires grasping the loose nut, transporting it to the bolt, and chaining these steps with threading."
  Rewrite: "Autonomous engagement of a loose nut requires grasping the nut, transporting it to the bolt, and chaining these steps with threading."
  Original (28): "The second extension is tightening to a preload. A threading cycle that ends with the nut tight needs ..."
  Rewrite: "Tightening to a preload needs a thread model whose resistance rises when the nut seats, a grasp that transmits the resulting torque, and a policy that senses when the joint is tight."
  Original (32): "The fourth extension concerns the transfer. The randomization ranges of the simulated camera should be fitted ..."
  Rewrite: "For the transfer, the randomization ranges of the simulated camera should be fitted ..."
  Original (34): "The fifth extension concerns the grasp. Training on more than one face topology would extend ..."
  Rewrite: "Training on more than one face topology would extend ..."
  Original (36): "The last extension completes the distillation study. The online flow-matching student is implemented and remains to be evaluated."
  Rewrite: "The distillation study can be completed with the online flow-matching student, which is implemented and remains to be evaluated."

6.5 chapter06.tex:26 and :28 | the same force-channel sentence closes two consecutive paragraphs, with a stacked noun phrase and "natural"
  Original (26): "It will most likely require fingertip-force and tactile feedback, and the hardware-equivalent fingertip-force and joint-torque observation channels that are implemented for teacher and student are the starting point."
  Rewrite: "It will most likely require fingertip-force and tactile feedback, for which the fingertip-force and joint-torque observations of teacher and student are a starting point."
  Original (28): "The force channels that the teacher and the student already observe are the natural inputs for such a policy."
  Rewrite: "The same force observations can serve as inputs for such a policy."

6.6 chapter06.tex:8 | two unrelated clauses joined by "and" where the sense is contrast
  Original: "Threaded joints can be released again and their threads are standardized~\cite{Budynas2020}, and fastening a nut is still largely left to people and specialized tools."
  Rewrite: "Threaded joints can be released again and their threads are standardized~\cite{Budynas2020}, yet fastening a nut is still largely left to people and specialized tools."

---------------------------------------------------------------------
acknowledgments.tex (stock gratitude phrases, the one file with classic AI vocabulary)
---------------------------------------------------------------------

K1. acknowledgments.tex:18 | "heartfelt", "this entire journey", tacked-on -ing clause
  Original: "I wish to convey my heartfelt thanks to my family and friends, who supported me throughout this entire journey and patiently listened while I explained what I was working on, often learning about it along the way."
  Rewrite: "I thank my family and friends, who supported me throughout this thesis and listened patiently whenever I explained what I was working on."

K2. acknowledgments.tex:22 | generic closer with a triple ("support, guidance, and encouragement")
  Original: "This work would not have been possible without the support, guidance, and encouragement of all these people and institutions. Thank you."
  Rewrite: delete the paragraph. Every person and institution has already been thanked individually.

K3. acknowledgments.tex:8 | "express my sincere gratitude", triple "for ..., for ..., and for generously ..."
  Original: "I would like to express my sincere gratitude to my advisor, Chi Zhang, M.Sc., for guiding me through this thesis, for teaching me how to conduct research, and for generously sharing his expertise with me."
  Rewrite: "I thank my advisor, Chi Zhang, M.Sc., for guiding me through this thesis and for teaching me how to conduct research."
  See section 4: chapter01.tex:91 says the acknowledgments state the advisor's contributions, and this sentence does not.

K4. acknowledgments.tex:16 | triple
  Original: "I further thank all my colleagues in the team for their support, their insights and advice, and their many contributions to this work."
  Rewrite: "I further thank my colleagues in the team for their advice and their contributions to this work."

K5. acknowledgments.tex:12 and :20 | "deeply grateful", and "the opportunity to conduct (this/my) research" twice (lines 14 and 20)
  Original (12): "I am deeply grateful to Agile Robots SE, where this work was carried out."
  Rewrite: "I thank Agile Robots SE, where this work was carried out."
  Original (20): "Finally, I thank the Technical University of Munich for providing me with the opportunity to conduct this research."
  Rewrite: "Finally, I thank the Technical University of Munich for making this research possible."

---------------------------------------------------------------------
appendix.tex (prose reads fine)
---------------------------------------------------------------------

P1. appendix.tex:89 and :101 | the same sentence twice in one appendix
  Original (89): "The policy thus regulates contact forces by placing targets rather than by commanding forces, and an unexpected contact does not produce the large forces of a stiff position controller."
  Original (101): "The policy thus regulates contact forces by placing targets, without commanding forces directly."
  Rewrite for 89: "Section~\ref{sec:app-osc} explains how the policy uses this behavior to regulate contact forces."

P2. appendix.tex:101 | "second reason" without a first reason named as such
  Original: "Impedance is the second reason for this choice."
  Rewrite: "The operational-space controller is also chosen for its impedance behavior."

P3. appendix.tex:79 | stray comma (typo, not style)
  Original: "A fixed action decoder, maps each action to a Cartesian target for the hand's grasp frame and three pinch-joint targets."
  Rewrite: "A fixed action decoder maps each action to a Cartesian target for the hand's grasp frame and three pinch-joint targets."

---------------------------------------------------------------------
appendix_controller.tex (terse lab-report prose, not AI-sounding; see section 5 for the rule conflicts)
---------------------------------------------------------------------

Q1. appendix_controller.tex:430 | semicolon-separated list (forbidden by the guidelines)
  Original: "The deployment controller therefore adds three measures: joint friction compensation on hardware, which reduces the hysteresis by 38\,\% and the accuracy error by 25\,\% (Section~\ref{sec:app-ctrl-repeat}); the training dead zone as an option in ros-sim; and the wider transition clip, which fixed the orientation stall of the return (Section~\ref{sec:app-ctrl-tclip})."
  Rewrite: "The deployment controller therefore adds three measures. Joint friction compensation on hardware reduces the hysteresis by 38\,\% and the accuracy error by 25\,\% (Section~\ref{sec:app-ctrl-repeat}). The training dead zone is available as an option in ros-sim. The wider transition clip fixed the orientation stall of the return (Section~\ref{sec:app-ctrl-tclip})."

Q2. appendix_controller.tex:72 | semicolon joining two clauses
  Original: "One of them used friction compensation; for the other, the setting was not recorded."
  Rewrite: "One of them used friction compensation. For the other, the setting was not recorded."

Q3. appendix_controller.tex:165, :205, :262, :291, :386 | verbless fragments in the "Limitations" paragraphs
  Original (165): "One hardware run and three ros-sim runs, all within the first 99 steps of a single cycle."
  Rewrite: "The comparison covers one hardware run and three ros-sim runs, all within the first 99 steps of a single cycle."
  Original (205): "Two poses, one probe speed, and one session per condition."
  Rewrite: "The probe covers two poses, one probe speed, and one session per condition."
  Original (291): "Two stalls at one return pose."
  Rewrite: "The analysis covers two stalls at one return pose."
  Lines 262 and 386 follow the same pattern.

Q4. appendix_controller.tex:52 and :126 | informal metaphors ("a hole in the stiffness", "the hand floats", "sticky")
  Original (52): "On a gravity-free arm, the dead zone is a hole in the stiffness: inside the band no task wrench acts, and the hand floats."
  Rewrite: "On a gravity-free arm, the dead zone removes the stiffness inside the band, so no task wrench acts there and the hand is free to move."
  Original (126): "the dead zone makes free-space motion sticky but leaves the arm compliant against contact forces."
  Rewrite: "the dead zone leaves small free-space errors uncorrected but leaves the arm compliant against contact forces."


3. REPO-WIDE PATTERNS (better fixed by search than sentence by sentence)

Counts are over the ten files, comment lines excluded, `grep -oiE`.

Structural tells
- Counted announcements: 42. Pattern: `\b(two|three|four|five) (properties|advantages|difficulties|gaps|mechanisms|details|places|stages|steps|limits|measures|aspects|kinds|parts|contributions|research questions|families|respects|further changes|checks|quantities|sessions|recipes)`. Per file: c1 7, c2 7, c3 5, c4 5, c5 7, c6 2, appendix 4, appendix_controller 5.
- Sentence-initial ordinals: 23, `\b(First|Second|Third|Fourth),`. Ordinal topic sentences: 18, `The (first|second|third|fourth|fifth|last) (is|gap|extension|check)` (c5 6, c6 6).
- Reveal colon: 77, `[a-z]: [a-z]` (c3 21, appendix_controller 15, c4 14, c1 9). Roughly 35 are "claim: explanation" and the rest introduce lists or caption parts.
- "rather than": 23, `\brather than\b` (c2 9, appendix_controller 5). "instead": 17, `\binstead\b`. ", not ": 11.
- "therefore": 37, "thus": 14, "thereby": 2. "thus" marks the interpretive sentence of chapter04.tex:180, :207, :219, :251.
- "so that": 25, of which 13 in chapter03.
- "X answers the Y difficulty": 5, `answers? the [a-z -]+ difficulty` (chapter03.tex:42, :46, :104, :166, chapter05.tex:8).
- "at the cost of": 4 (chapter01.tex:46, :58, chapter02.tex:27, :125). "moves the difficulty to": 2.

Set-piece sentences reused verbatim
- "decompose during data generation, unify at deployment": 4 in English (abstract.tex:11, chapter01.tex:79 caption, chapter03.tex:31, chapter06.tex:11) plus the German arm. Keep it once as a named principle, at most twice.
- "For large bodies ... harmless. For threads it is not": 3 pairs, `For (large bodies|threads)` (chapter01.tex:30, chapter02.tex:83, chapter03.tex:65).
- "never strictly rigid": chapter02.tex:83, chapter03.tex:48.
- "1000 nut-and-bolt assemblies in real time on one/a single GPU": 3 (chapter01.tex:28, chapter02.tex:79, :91).
- "can only be earned by turning": 3 (chapter02.tex:83, chapter03.tex:67, chapter05.tex:8).
- "a separate skill with a narrow entry configuration": 3 (chapter03.tex:75, chapter05.tex:27, chapter06.tex:26).
- "teleoperated demonstrations of forceful dexterous manipulation are hard to collect": chapter01.tex:48, chapter02.tex:109, paraphrased again at chapter02.tex:113.
- "nominal action/motion in one demonstration and a recovery in another": chapter02.tex:43, chapter03.tex:180, chapter05.tex:14.
- "sustains consecutive cycles better than a single-cycle policy (that is) invoked repeatedly": chapter01.tex:65, chapter02.tex:115, chapter03.tex:166.
- No switch, no separate networks: chapter02.tex:115, chapter03.tex:12, :166, :196.
- "deduced from twelve different poses of a calibrated AprilTag observed by the camera": chapter03.tex:135, chapter04.tex:71.
- "The transfer (therefore) rests (entirely) on four properties of the pipeline": chapter04.tex:109, chapter05.tex:16.
- "fingers slip off the edge of the nut after a few cycles": chapter04.tex:212, chapter05.tex:10. The rectangular-failure sentence ("In the typical failure, the fingers turn the nut by $60\degree$ but do not establish contact with the next pair of faces in the following cycle") is identical at chapter04.tex:219 and chapter05.tex:33.
- "loses much of the face orientation": chapter04.tex:207, chapter05.tex:12. "fail first": chapter04.tex:180, chapter05.tex:14.
- "all ten cycles": 20, "in every trial": 15. These are results and must stay, but three occurrences in the abstract and four in chapter06 are noticeable.
- The gap paragraph: chapter01.tex:58 and chapter02.tex:125 share four sentences.

Terminology drift (guideline: one term per concept)
- Progress signal, five names in 13 hits, `progress (scalar|clock)|trajectory progress|task progress|global progress`: "normalized task progress" (chapter03.tex:162, :172), "global trajectory progress" (chapter03.tex:188, :196), "normalized global progress" (chapter03.tex:36), "global progress scalar" and "progress scalar" (chapter04.tex:109, chapter05.tex:10, :21), "global progress clock" (chapter05.tex:42, chapter06.tex:30).
- "re-grasp" 14 versus "regrasp" 3 (chapter02.tex:21, :97, :125).
- Transition names, 18 hits over three variants, `release-and-reset|return and reset|release and return`: "release and return" (most), "release-and-reset" (chapter01.tex:79), "release and reset" (chapter03.tex:36), "return and reset" (chapter03.tex:10).
- Learned phases: "approach, grasp, rotate, goal reaching" (chapter03.tex:10), "approach, grasp, turn, and hold" (chapter03.tex:125), "grasp, rotation, and goal reaching" without approach (chapter03.tex:36).
- "cyclic tracking error" versus "cyclic error", "ten-cycle tracking error" versus "ten-cycle error" versus "episodic tracking error" (chapter03.tex:14).
- "RQ2 (policy design)" (chapter01.tex:66) versus "RQ2 (student design)" (chapter04.tex:165, :180).
- "the full method" versus "the student" versus "the distilled student" for ablation (e).
- British "centre" once (chapter04.tex:125), "center" elsewhere.

Punctuation rule
- Prose semicolons: 2 (appendix_controller.tex:72, :430). The other 36 `;` hits are math spacing or table cells. Em dashes: 0.


4. POSSIBLE FACTUAL INCONSISTENCIES (listed only, not resolved)

1. Number of demonstrations. chapter03.tex:131 "Twenty demonstrations contain too little variation ..." versus 36 demonstrations at chapter04.tex:109, chapter04.tex:161 and appendix.tex:429, :467.
2. Impulses per demonstration. chapter03.tex:131 "one impulse ... of every policy, waypoint, and return segment of every cycle, which gives 30 impulses per ten-cycle demonstration" versus chapter03.tex:118 and appendix.tex:374 (four release waypoints plus one return segment per cycle, which with one policy segment gives six segments per cycle).
3. Forward reference to the acknowledgments. chapter01.tex:91 "The acknowledgments state this attribution." versus acknowledgments.tex:8, which thanks the advisor for guidance and does not mention the hybrid teacher, the distillation stack or the hardware experiments.
4. Colour augmentation. chapter05.tex:16 "together with image-space color augmentation" versus appendix.tex:445 "RGB augmentation & none".
5. Encoder pretraining and depth corruption. chapter06.tex:32 "The depth-corruption model that the encoder pretraining already provides can then be applied to the student's training data as well" versus chapter03.tex:194 "The encoder has no pretrained backbone", appendix.tex:436 "trained from scratch", and chapter03.tex:139, where depth augmentation is already applied during student training.
6. Loose nut. chapter05.tex:38 "The same hand also picks up a loose nut in simulation." versus chapter06.tex:22 ("What it cannot yet do is start from a loose nut") and chapter06.tex:26 (grasping the loose nut listed as future work). No experiment in chapter04 reports it.
7. Joint velocities in the student observation. chapter05.tex:21 "the positions and velocities of the ten controlled joints" versus chapter03.tex:192 "the ten controlled joint positions, the seven arm joint velocities ... The hand joint velocities are omitted."
8. Force channels. appendix.tex:70 "Force channels (teacher only)" versus chapter03.tex:172, :192 and chapter05.tex:8, where the student also observes the fingertip forces and joint torques.
9. Integration steps at deployment. chapter04.tex:105 and :109 (sixteen steps on a GPU) versus appendix.tex:448 "N=16 steps (online training: 8; CPU deployment: 2)" and chapter03.tex:178 "with $N=16$ in simulation (Table~\ref{tab:flow} lists the deployment setting)".
10. Camera. "head camera" at chapter03.tex:154 (twice), :160, :172 and appendix.tex:475 versus "A fixed Intel RealSense D415 on a stand" at chapter04.tex:65, :71 and "one fixed camera" at chapter05.tex:38.
11. Cross-reference without support. chapter05.tex:33 "People change the grasp as the resistance grows (Section~\ref{sec:difficulty-dexterity})" versus chapter01.tex:36, which says a nut can be held with many grasp types and says nothing about changing the grasp with resistance.
12. Penalised force. chapter05.tex:31 "the reward penalizes excess wrist force" versus chapter03.tex:98 "excess grip force" and appendix.tex:351 (pad contact force) and :353 (thread wrench).
13. Number of transfer properties. Three in abstract.tex:11 and chapter01.tex:88 ("a calibrated camera model, visual randomization, and a Cartesian action path") versus four in chapter04.tex:109, chapter05.tex:16 and chapter06.tex:11 (crop box added).
14. Number of learned phases in the figure captions. chapter03.tex:36 (grasp, rotation, goal reaching) and chapter03.tex:125 (approach, grasp, turn, hold) versus the four phases of chapter03.tex:10 and :31.
15. Controller additions. appendix_controller.tex:56 "Two terms were added to it for deployment" versus appendix_controller.tex:430 "adds three measures".
16. Return gate and timeout. appendix.tex:376 (tolerance drawn between 5 and 15 mm and between 5 and 10 degrees) and chapter04.tex:23, appendix.tex:379 (16 s timeout) versus appendix_controller.tex:78 caption (30 mm and 25 degrees), :266 (3 mm and 2 degrees, 16.9 s), :299 (15 mm then 20 mm and 10 degrees). These may be different runs, but the text does not say which gate applies to the results of chapter04.
17. Median demonstration length. appendix.tex:438 "98.2\,s (1473 steps)" versus appendix.tex:468 median 1474 frames.
18. Difficulties versus related-work topics. chapter02.tex:4 "reviews related work along the four difficulties" followed by five topics.
19. Undefined constraint. chapter06.tex:36 "without violating the constraint that a chunk label must be produced by the teacher alone". No earlier chapter introduces this constraint.
20. Claim strength. chapter01.tex:58 "No prior work threads a nut ..." versus chapter02.tex:125 "None of the reviewed works threads a nut ...".


5. OUTSIDE THE STYLE BRIEF: CONFLICTS WITH THE AUTHOR'S STANDING RULES

Not AI tells, and not rewritten, but visible while reading.
- Code and tool names in typeset text: "ros-sim" 64 times (chapter04.tex:129 and appendix_controller throughout), "ros2\_control plugin" (appendix_controller.tex:56), "libfranka" and "\texttt{tau\_ext\_hat\_filtered}" (chapter04.tex:75, appendix.tex:36, :71), "rl\_games" (appendix.tex:389), "fr3\_v2 model of MuJoCo Menagerie" and "\texttt{franka\_description}" (appendix.tex:140).
- Provenance narration: appendix_controller.tex:66 "According to the notes kept with the controller settings" and "The same notes report", :128 "the assignment of the six ros-sim runs to the two conditions is inferred from the order in which they were run", :58 and :64 unit-test counts.
- Narrated failures: appendix_controller.tex:74 (five of six runs ended with a re-home failure), :179 (three of six sessions ended with an error), :219 (two sessions ended early), :336 and :354 (rejected and interrupted attempts).
- Human-correction topic: chapter01.tex:54 "or by correcting replayed demonstrations by hand" and chapter04.tex:109 "or corrections".
- Source comments that name the conference paper: chapter04.tex:172, :181, :208, :213, :220, :252. They are not typeset, but they are in the committed source.
- Open TODO comments remain at chapter01.tex:7, :12, :14, :16, chapter02.tex:76, :82, chapter04.tex:101, :172, chapter05.tex:30, :36, chapter06.tex:9.
