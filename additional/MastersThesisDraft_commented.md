# Chi's review comments on the thesis draft (MastersThesisDraft_commented.pdf)

Extracted from the PDF highlight annotations with PyMuPDF. The draft itself is the thesis at commit 26db6e6; the page text is not reproduced here.

## Comment 1 (page 7, by chi)

Highlighted: Abstract Threaded joints are central to assembly because they can be released again and because their threads are standardized. This thesis asks how a robot with a dexterous hand can learn to thread a

wording of the abstract needs to be treated carefully.

Proposed structure:
1- problem
2- we propose some thing( a conclusion), to address the problem in which way
3- how we did it(shortly)
4- most remarkable results
5- (optional) some limitations

about the problem:
threading is treated as one of the most difficult tasks in robot assembly tasks due to the complex contact conditions and its difficulty to simulate in virtual environments, as well as the huge sim2real gap to deploy an autonomous agent to the real world blabla...

## Comment 2 (page 9, by chi)

Highlighted: Motivation … . … . … . … . … . … . … . … . … . … . … . … Problem: How Can a Robot Learn Threading? … 1.2.1 Simulation … . … . … . … . … . … . … . … . … .

choose your wording more scientifically

also subtitle name should also be more scientific

something like: 

Explosion in simulation due to extensive contact points
Curse of dimensionality for a multi fingered robotic hands as an end effector
Compounding error in a long horizon cyclic task
sim to real transfer 
etc
etc

## Comment 3 (page 9, by chi)

Highlighted: Approach … . … . … . … . Research Questions … Contributions … . … . .

research questions should follow the problem

the logic is you analyze the current gap then you identify your questions

## Comment 4 (page 9, by chi)

Highlighted: 1.2.3 Threading Approach … Research Questions

approach should be with contribution, 

contribution should be like 3 max

you can describe how we did our contributions very shortly

## Comment 5 (page 9, by chi)

Highlighted: Teacher–Student and Visuomotor Summary and Research Gap

choose  your wording more carefully

## Comment 6 (page 9, by chi)

Highlighted: Imitation Learning Action Chunking Generative Action

why is this part a separate part?

## Comment 7 (page 9, by chi)

Highlighted: . … . … . … . … . Thread Geometry

anyway the theoretical background does not have to be that wide, you just need to express the key theories you used, the OSC is purely engineering side maybe you should drop it.

I think you should focus on the following.

RL for teacher policy
IL for student distillation
Conditional flow matching and its relation to Diffusion policy
(optional) simulator related, differential simulation etc etc, say why threading is super difficult to simulate

## Comment 8 (page 9, by chi)

Highlighted: Control … . … . … . … . … . … . … . … . and Threading .

the wordings are too naive

## Comment 9 (page 9, by chi)

Highlighted: Problem Formulation … . … . … . … . … . Simulated and Physical System … . … . 3.2.1 Platform … . … . … . … . … . … . … .

this thing should be in experiments

## Comment 10 (page 9, by chi)

Highlighted: 21 22

you really can take reference of our icra paper structure of the methodology and the sections to follow

