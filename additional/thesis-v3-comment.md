# Chi's review comments on thesis v3 (thesis-v3-comment.pdf)

Extracted from the PDF highlight annotations with mutool. The page text is not reproduced here.

## Page 7 [Highlight] by chi
Highlighted: s in the demonstrations, and on unseen octagonal, rectangular, and round profiles of each size. In simulation, the student completes all ten cycles on the M24 nut in every trial with a mean cyclic tracking error of −1.77◦, and every ablated student fails earlier. On hardware, it completes all ten cycles in every trial on all three hexagonal nuts, with mean cyclic tracking errors below 6◦ in magnitude. Generalization depends on geometry. The student also completes all ten cycles on the octagonal and round profiles, but it fails on the rectangular profile, whose face topology conflicts with the learned re-grasp. All trials start from a nut already engaged on the thread, and tightening is not addressed.

this is more of an experimental design, not the result. you should say we can achieve * results in simulation, ** results on seen objects in real system, *** results on unseen results in real system blabla

## Page 9 [Highlight] by chi
Highlighted: 1.2.3 Zero-Shot Sim-to-Real Transfer . . . . . . . . . . . . . . . . . . . . . . . . . 4 1.3 Research Questions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

zero shot sim to real transfer for visuomotor policies

## Page 9 [Highlight] by chi
Highlighted: 3.2.2 PPO Training . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25 3.3 Dataset Construction with the Hybrid Teacher . . . . . . . . . . . . . . . . . . . . .

PPO training and reward shaping

## Page 25 [Highlight] by chi
Highlighted: RQ1 (long horizon). Does one policy learned from complete multi-cycle demonstrations sustain consecutive threading cycles better than a single-cycle policy that is invoked repeatedly? RQ2 (policy design). Which visuomotor policy design, in its visual representation and in its action head, turns such demonstrations into a policy that sustains the cyclic task? RQ3 (sim-to-real). Can a policy trained on simulated demonstrations only transfer zero-shot to a physical dexterous hand–arm system?

you should choose the wording for these three question more scientifically.

e.g. RQ2: (something like that)

in visuomotor policy distillation, is our current choice of point cloud encoder best condense scene information and is our conditional flow matching backbone best supports the skill transfer? 

RQ3: is the well known sim2real gap be mitigated by our proposed method to enable zero-shot deployment to the physical dexterous hand-ar

RQ1: in consecutive long horizon tasks such as our nut threading scenario, does our distillation approach from complete multi cycle demonstrations outperform a simpler single-cycle policy that is invoked repeatedly?

in the following sections, you should first criticize the alternative approaches then list the advantages of our approach, provide data to support our claim, so on so on.

## Page 58 [Highlight] by chi
Highlighted: The student of Chapter 3 rests on three design choices. It is distilled from complete multi- cycle demonstrations, it perceives the scene through a point-cloud encoder, and it predicts action chunks with a flow-matching head. Each choice has a simpler or more common al-

bullet point them

## Page 58 [Highlight] by chi
Highlighted: Ablation Studies Ablation Studies

questions are questions, ablation design are ablation design, don't mix them.

e.g. you should formulate the 4.3 section as follows.

we design the ablation studies to answer the following questions"
(i) is the long horizon distillation needed at all? blabla
(ii) is the point cloud encoder necessary? blabla
(iii) is the cfm back bone a good choice for the visuomotor student?

Therefore we designed the four ablation experiments to justify our design choices:
(a) single cycle student: how do you design the experiments
(b) resnet vision head: definition
(c) ...
(d) ...
(e) ...

then you show the results
then you compare ablations and draw conclusion

## Page 65 [Highlight] by chi
Highlighted: Interpretation per Research Question

here you should recall the original question for the convenience of the readers

## Page 67 [Highlight] by chi
Highlighted: Limitations

in my opinion, you should bullet point these

## Page 79 [Highlight] by chi
Highlighted: Table A.9: Demonstration data of the M24 ten-cycle collection used for the reported students.

unify table font size and optimize table placements

## Page 85 [Highlight] by chi
Highlighted: Figure B.1: Thumb abduction sweep on the physical hand, six stops from open (top left, register 979) to fully abducted (bottom right, register 242). Magenta outlines show the vendor model and cyan outlines the fitted model at the register of each stop, both projected into the camera image. Each label gives the fingertip distance of the vendor and the fitted model from the camera fit. Mean over the stops: 18.3 mm for the vendor model, 3.7 mm for the fitted model.

these page wide pics you should squeeze a bit and don't leave too much blank

