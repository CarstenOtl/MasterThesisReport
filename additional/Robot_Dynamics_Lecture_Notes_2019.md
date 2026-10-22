Robot Dynamics Lecture Notes

   Robotic Systems Lab, ETH Zurich

              HS 2019
Contents

1   Introduction                                                                     1
    1.1 Nomenclature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     2
    1.2 Operators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    3

2   Kinematics                                                                        5
    2.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    5
    2.2 Position . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    6
        2.2.1 Representation of Positions . . . . . . . . . . . . . . . . . .         6
                Cartesian coordinates . . . . . . . . . . . . . . . . . . . . . .     6
                Cylindrical coordinates . . . . . . . . . . . . . . . . . . . . .     7
                Spherical coordinates . . . . . . . . . . . . . . . . . . . . . .     7
    2.3 Linear Velocity . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     7
        2.3.1 Representation of Linear Velocities . . . . . . . . . . . . . .         7
                Cartesian Coordinates . . . . . . . . . . . . . . . . . . . . .       8
                Cylindrical Coordinates . . . . . . . . . . . . . . . . . . . .       8
                Spherical Coordinates . . . . . . . . . . . . . . . . . . . . .       8
    2.4 Rotation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    9
        2.4.1 Rotation Matrices . . . . . . . . . . . . . . . . . . . . . . . .       9
        2.4.2 Active vs. Passive Rotation . . . . . . . . . . . . . . . . . . .      11
                Passive Rotation . . . . . . . . . . . . . . . . . . . . . . . .     11
                Active Rotation . . . . . . . . . . . . . . . . . . . . . . . . .    11
        2.4.3 Elementary Rotations . . . . . . . . . . . . . . . . . . . . . .       12
        2.4.4 Composition of Rotations . . . . . . . . . . . . . . . . . . .         12
        2.4.5 Representation of Rotations . . . . . . . . . . . . . . . . . .        13
                Euler Angles . . . . . . . . . . . . . . . . . . . . . . . . . .     13
                Angle Axis . . . . . . . . . . . . . . . . . . . . . . . . . . .     18
                Unit Quaternions . . . . . . . . . . . . . . . . . . . . . . . .     19
    2.5 Angular Velocity . . . . . . . . . . . . . . . . . . . . . . . . . . . .     21
        2.5.1 Time Derivatives of Rotation Parameterizations . . . . . . . .         22
                Time Derivatives of Euler Angles ZYX ⇔ Angular Velocity .            23
                Time Derivatives of Euler Angles XYZ ⇔ Angular Velocity .            24
                Time Derivatives of Euler Angles ZYZ ⇔ Angular Velocity .            24
                Time Derivatives of Euler Angles ZXZ ⇔ Angular Velocity .            24
                Time Derivative of Rotation Quaternion ⇔ Angular Velocity .          24
                Time Derivative of Angle Axis ⇔ Angular Velocity . . . . . .         25
                Time Derivative of Rotation Vector ⇔ Angular Velocity . . .          25
    2.6 Transformation . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     26
    2.7 Velocity in Moving Bodies . . . . . . . . . . . . . . . . . . . . . . .      28

                                           i
                 Some Notes on Vector Differentiation . . . . . . . . . . . . . 29
    2.8  Kinematics of Systems of Bodies . . . . . . . . . . . . . . . . . . . . 30
         2.8.1 Generalized Coordinates and Joint Configuration . . . . . . . 30
         2.8.2 Task-Space Coordinates . . . . . . . . . . . . . . . . . . . . 31
                 End-Effector Configuration Parameters . . . . . . . . . . . . 31
                 Operational Space Coordinates . . . . . . . . . . . . . . . . . 32
         2.8.3 Forward Kinematics . . . . . . . . . . . . . . . . . . . . . . 33
         2.8.4 Differential Kinematics and Analytical Jacobian . . . . . . . 34
                 Position and Rotation Jacobian . . . . . . . . . . . . . . . . . 35
                 Dependency on Parameterization . . . . . . . . . . . . . . . . 35
         2.8.5 Geometric or Basic Jacobian . . . . . . . . . . . . . . . . . . 37
                 Addition and Subtraction of Geometric Jacobians . . . . . . . 37
                 Calculation of geometric Jacobian using Rigid Body Formulation 38
         2.8.6 Relation between Geometric and Analytic Jacobian Matrix . . 41
    2.9 Kinematic Control Methods . . . . . . . . . . . . . . . . . . . . . . 42
         2.9.1 Inverse Differential Kinematics . . . . . . . . . . . . . . . . 42
                 Singularities . . . . . . . . . . . . . . . . . . . . . . . . . . 42
                 Redundancy . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
         2.9.2 Multi-task Inverse Differential Kinematics Control . . . . . . 43
                 Multi-task with Equal Priority . . . . . . . . . . . . . . . . . 43
                 Multi-task with Prioritization . . . . . . . . . . . . . . . . . . 44
         2.9.3 Inverse Kinematics . . . . . . . . . . . . . . . . . . . . . . . 47
                 Analytical Solution . . . . . . . . . . . . . . . . . . . . . . . 47
                 Numerical Solution . . . . . . . . . . . . . . . . . . . . . . . 47
                 Appropriate Rotation Error . . . . . . . . . . . . . . . . . . . 50
         2.9.4 Trajectory Control . . . . . . . . . . . . . . . . . . . . . . . 53
                 Position Trajectory Control . . . . . . . . . . . . . . . . . . . 53
                 Orientation Trajectory Control . . . . . . . . . . . . . . . . . 53
    2.10 Floating Base Kinematics . . . . . . . . . . . . . . . . . . . . . . . . 54
         2.10.1 Generalized Velocity and Acceleration . . . . . . . . . . . . . 54
         2.10.2 Forward Kinematics . . . . . . . . . . . . . . . . . . . . . . 55
         2.10.3 Differential Kinematics of Floating Base Systems . . . . . . . 55
         2.10.4 Contacts and Constraints . . . . . . . . . . . . . . . . . . . . 56
                 Point Contacts - Quadruped . . . . . . . . . . . . . . . . . . 57
                 Extended Contacts - Humanoid . . . . . . . . . . . . . . . . 57
         2.10.5 Support Consistent Inverse Kinematics . . . . . . . . . . . . 57

3   Dynamics                                                                         59
    3.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   59
    3.2 Foundations from Classical Mechanics . . . . . . . . . . . . . . . . .       60
        3.2.1 Newton’s Law for Particles . . . . . . . . . . . . . . . . . . .       60
        3.2.2 Virtual Displacements . . . . . . . . . . . . . . . . . . . . .        61
        3.2.3 Virtual Displacement of Single Rigid Bodies . . . . . . . . .          61
        3.2.4 Virtual Displacement of Multi-Body Systems . . . . . . . . .           62
        3.2.5 Principle of Virtual Work . . . . . . . . . . . . . . . . . . . .      62
    3.3 Newton-Euler Method . . . . . . . . . . . . . . . . . . . . . . . . .        63
        3.3.1 Newton-Euler for Single Bodies . . . . . . . . . . . . . . . .         63
        3.3.2 Newton-Euler for Multi-Body Systems . . . . . . . . . . . .            64
    3.4 Lagrange Method . . . . . . . . . . . . . . . . . . . . . . . . . . . .      65
        3.4.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . .     65

                                           ii
        3.4.2 Kinetic Energy . . . . . . . . . . . . . . . . . . . . . . . . .     66
        3.4.3 Potential Energy . . . . . . . . . . . . . . . . . . . . . . . .     67
        3.4.4 External Forces . . . . . . . . . . . . . . . . . . . . . . . . .    67
        3.4.5 Additional Constraints . . . . . . . . . . . . . . . . . . . . .     67
   3.5 Projected Newton-Euler Method . . . . . . . . . . . . . . . . . . . .       68
        3.5.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . .   68
        3.5.2 Deriving Generalized Equations of Motion . . . . . . . . . .         69
        3.5.3 External Forces & Actuation . . . . . . . . . . . . . . . . . .      70
   3.6 Summary and Relation between Methods . . . . . . . . . . . . . . .          71
   3.7 Dynamics of Floating Base Systems . . . . . . . . . . . . . . . . . .       71
        3.7.1 Contact Forces . . . . . . . . . . . . . . . . . . . . . . . . .     72
                Soft Contact Model . . . . . . . . . . . . . . . . . . . . . . .   72
                Contact Forces from Constraints . . . . . . . . . . . . . . . .    73
        3.7.2 Constraint Consistent Dynamics . . . . . . . . . . . . . . . .       73
        3.7.3 Contact Switches and Impact Collisions . . . . . . . . . . . .       73
                Impulse Transfer . . . . . . . . . . . . . . . . . . . . . . . .   74
                Energy Loss . . . . . . . . . . . . . . . . . . . . . . . . . .    74
   3.8 Joint-space Dynamic Control . . . . . . . . . . . . . . . . . . . . . .     75
        3.8.1 Joint Impedance Regulation . . . . . . . . . . . . . . . . . .       75
                Gravity Compensation . . . . . . . . . . . . . . . . . . . . .     75
                Inverse Dynamics Control . . . . . . . . . . . . . . . . . . .     75
   3.9 Task-space Dynamics Control . . . . . . . . . . . . . . . . . . . . .       76
        3.9.1 Multi-task Decomposition . . . . . . . . . . . . . . . . . . .       76
        3.9.2 End-effector Dynamics . . . . . . . . . . . . . . . . . . . . .      77
        3.9.3 End-efector Motion Control . . . . . . . . . . . . . . . . . .       77
                Alternative Notation . . . . . . . . . . . . . . . . . . . . . .   77
        3.9.4 Operational Space Control . . . . . . . . . . . . . . . . . . .      78
   3.10 Inverse Dynamics for Floating-Base Systems . . . . . . . . . . . . .       79
        3.10.1 Quadratic Problems . . . . . . . . . . . . . . . . . . . . . . .    79
        3.10.2 Iterative Null-Space Projection . . . . . . . . . . . . . . . . .   79
        3.10.3 Sequence of Constrained Optimization . . . . . . . . . . . .        80
        3.10.4 Task-Space Control for Floating Base Systems as QP . . . . .        81
   3.11 Quasi-static (Virtual Model) Control . . . . . . . . . . . . . . . . . .   81

A Matlab Code for Examples                                                         85
  A.1 Multi-task Control . . . . . . . . . . . . . . . . . . . . . . . . . . .     85
  A.2 Inverse Kinematics for Rotations . . . . . . . . . . . . . . . . . . . .     86

B Matlab Code for 3D rotations                                                     91
  B.1 Euler angles to rotation matrix . . . . . . . . . . . . . . . . . . . . .    91
  B.2 Rotation matrix to Euler angles . . . . . . . . . . . . . . . . . . . . .    92




                                         iii
iv
Chapter 1

Introduction

The course ”Robot Dynamics” provides an overview on how to model robotic sys-
tems and gives a first insight in how to use these models in order to control the sys-
tems. It tries to foster the understanding of the similarities between different types of
robots, such as robot arms, legged and wheeled machines, or flying systems, that can be
modeled using the same techniques. In fact, most robots can be described (accurately
enough) by a single body or a set of bodies on which different forces act. However,
these forces can come from different sources. A robot arm moving in free space is
driven by the actuator forces acting on the joints, while a legged robot additionally
encounters interaction forces at its feet and flying vehicles are kept in the air due to
aerodynamic forces.
    In general, we need to distinguish between two categories of robots, namely fixed
base and floating base systems. The former category includes all kinds of robotic ma-
chines that are rigidly bolted to the ground. The classical example are industrial robot
arms. Such systems mostly feature an actuator in every joint, which means that the
degree of freedom (DOF) is equal to the number of actuators in the systems. The latter
category encompasses mobile systems, i.e. robots that have a moving base. In contrast
to the robot arm example, the motion of the floating base can typically not directly be
controlled through actuators but only through external forces acting on the system such
as contact or aerodynamic forces.

    This lecture script gives a compact overview about the underlying theory. As the
course is still in development, this script is neither complete nor extensive. As general
readings for people interested in this topic, we refer to two great books that are available
through SpringerLink (free access from ETH), namely


    • Handbook of Robotics (Siciliano, Khatib) [7]
      http://link.springer.com/referencework/10.1007/978-3-540-30301-5


    • Robotics – Modelling, Planning and Control (Siciliano, Sciavicco, Villani, Ori-
      olo) [8]
      http://link.springer.com/book/10.1007%2F978-1-84628-642-1

                                             1
1.1       Nomenclature
The following list holds as reference table for the entire script. While almost every
textbook uses a different nomenclature, we try to stick here to the IEEE standards for
the style and use index parameter to ensure a complete description

 r                   vector (bold small letter)
 B                   matrix (bold capital letter)
 eA      A
   x , ey , ez
                A
                     unitary basis vectors of coordinate frame A
 A                   coordinate frame A (caligraph letter)
 A                   origin of coordinate system A
 eIx , eIy , eIz     global / inertial / world coordinate system (never moves)
 A rAP               position vector of point P w.r.t. the origin of frame A expressed in
                     frame A
 φAB                 describes the orientation of frame B w.r.t. A, which is ∈ SO(3)
 χP                  stacked parameters of position representation
 χR                  stacked parameters of orientation representation
 χP,0                minimal-dimensional stacked parameters of position representation
 χR,0                minimum-dimensional stacked parameters of orientation representa-
                     tion
 vP                  (absolute) velocity of point P w.r.t. inertial frame
 aP                  (absolute) acceleration of point P w.r.t. inertial frame
 ωAB                 angular velocity of frame B w.r.t. A
 ΩB = I ωIB          absolute angular velocity of frame B
 ΨB = Ω̇B            absolute angular acceleration of frame B
 nq                  total number of generalized coordinates, respectively velocities
 nj                  number of joints
 nl                  number of links
 nτ                  number of actuated joints
 nb                  number of base coordinates
 nc                  number of contact points
 m                   number of end-effector configuration parameters
 m0                  number of operational space coordinates
                     = minimal number of end-effector configuration parameters
                    machine precision
 x∗                  the star stands for a desired value
 q                   generalized coordinates
 J                   Jacobian matrix
 JA                  analytical Jacobian matrix
 J0                  basic Jacobian matrix
 N = N (J)           null-space projector matrix




                                          2
1.2    Operators
There exist a number of special operators such as
                                                                              
                                           a1     b1          0         −a3   a2     b1
 Cross product/skew/unskew a × b = a2  × b2  = [a]× b =  a3         0    −a1  b2 
                                           a3     b3         −a2        a1     0     b3
                                   √            p
 Euclidean norm            kak =       aT a =       a21 + . . . + a2n
                                                              
 Absolute vector           |a| = |a1 |      ...          |an |

 Null space projector      N (J)




                                       3
4
Chapter 2

Kinematics

2.1     Introduction
Kinematics is the description of the motion of points, bodies, and systems of bodies. It
does only describe how things are moving, but not why. To describe the kinematics of
a moving point, we will refer to position vectors, which are generically defined in R3 ,
and their derivatives. For an extended body, we need to additionally take into account
rotations φ ∈ SO(3) to completely define its configuration.
    In the following, we will first discuss the basics of kinematics by describing the
motion of points and single bodies before moving on to serial systems of bodies in
section 2.8.




                                           5
                                 eA
                                  z




                                                            B
                                            φ rAB
                                                    r       z       eA
                                                                     y
                                    A
                                                        ρ       x
                                        θ
                               eA            y
                                x


Figure 2.1: Representation of positions using Cartesian, cylindrical, or spherical coor-
dinates.


2.2     Position
The position of a point B relative to point A can be written as

                                            rAB .                                   (2.1)

For points in the three dimensional space, positions are represented by vectors r ∈ R3 .
In order to numerically express the components of a vector, it is necessary to define a
reference frame A and to express the vector in this frame:

                                      A rAB .                                       (2.2)
                       A A
                             
The unit vectors eA                                                     3
                  x , ey , ez of frame A form an ortho-normal basis of R .



2.2.1    Representation of Positions
Representing a position in the three dimensional space requires three parameters.

Cartesian coordinates
The most common approach is to work with Cartesian coordinates and hence parame-
terize the position by
                                        
                                         x
                                χP c = y  ,                               (2.3)
                                         z
which implies that a position vector is simply given by
                                                        
                                                        x
                                   A       A
                          A r = xex + yey + zez =
                                                  A    y                          (2.4)
                                                        z

                                             6
Cylindrical coordinates
A second approach is to work with cylindrical coordinates
                                           
                                             ρ
                                  χP z = θ  ,                                                       (2.5)
                                             z
which implies that a position vector is given by
                                                   
                                            ρ cos θ
                                  Ar =
                                          ρ sin θ  .                                                (2.6)
                                               z

Spherical coordinates
A third method is to use spherical coordinates 1
                                             
                                              r
                                    χP s =  θ  ,                                                    (2.7)
                                              φ
which implies that a position vector is given by
                                                      
                                         r cos θ sin φ
                               Ar =
                                       r sin θ sin φ  .                                             (2.8)
                                            r cos φ
    Note: All the previously introduced parameterizations require three parameters to
describe a position in 3D space, meaning that they are at the same time also minimal
representations. This will be different for rotations as shown in section 2.4.5. In most
of the cases, people work with Cartesian coordinates due to the simple properties for
vector calculus.


2.3       Linear Velocity
The velocity of point B relative to point A is given by
                                                  ṙAB .                                              (2.9)
For three dimensional space, velocities are represented by vectors ṙ ∈ R3 . For per-
forming vector algebra, the same rules as introduced for the positions need to hold.

2.3.1      Representation of Linear Velocities
There exists a linear mapping EP (χ) between velocities ṙ and the derivatives of the
representation χ̇P :
                                            ṙ = EP (χP ) χ̇P                                       (2.10)
                                         χ̇P = E−1
                                                P (χP ) ṙ                                          (2.11)
   1 What is drawn in Fig. 2.1 is the azimuthal angle θ, and polar angle φ.     This is often referred to as
”mathematical notation”, whereby we use φ instead of ϕ in order to limit conflicts with other use of ϕ in
this lecture notes. The common notation in physics (which is also the ISO standard) uses ϕ for the azimuthal
angle and θ for the polar angle. Be also careful when using Matlab as it outputs typically elevation angle
instead of azimuthal angle.


                                                     7
Cartesian Coordinates
For Cartesian coordinates, the mapping is simply the identity:

                            EP c (χP c ) = E−1
                                            P c (χP c ) = I                    (2.12)

Cylindrical Coordinates
For cylindrical coordinates we get
                                                            
                                        ρ̇ cos θ − ρθ̇ sin θ
                          ṙ (χP z ) = ρ̇ sin θ + ρθ̇ cos θ ,                (2.13)
                                                  ż

which can be solved for
                                                               
           ρ̇           ẋ cos θ + ẏ sin θ      cos θ     sin θ 0   ẋ
 χ̇P z = θ̇  = −ẋ sin θ/ρ + ẏ cos θ/ρ = − sin θ/ρ cos θ/ρ 0 ẏ  .
           ż                    ż                0         0   1   ż
                                              |         {z         }
                                                                  E−1
                                                                   Pz
                                                                               (2.14)
The inverse is
                                                                        
                                            cos θ       −ρ sin θ        0
                                ∂r (χP z ) 
                 EP z (χP z ) =           = sin θ       ρ cos θ         0 .   (2.15)
                                 ∂χP z
                                              0            0            1

Spherical Coordinates
Using the same approach for spherical coordinates results in:
                                                               
                     cos θ sin φ −r sin φ sin θ r cos φ cos θ
             EP s =  sin φ sin θ r cos θ sin φ r cos φ sin θ  ,              (2.16)
                         cos φ           0           −r sin φ
                                                                   
                          cos θ sin φ      sin φ sin θ        cos φ
             E−1                                                   .
              P s = − sin θ/(r sin φ) cos θ/(r sin φ)           0              (2.17)
                       (cos φ cos θ)/r (cos φ sin θ)/r − sin φ/r




                                           8
                                        eA
                                         z
                                                        P

                       eB
                        z
                                                            eB
                                                             y




                                        A=B                      eA
                                                                  y




                        eA
                         x            eB
                                       x

            Figure 2.2: Generic 3D rotation between two frames A and B.


2.4     Rotation
While the configuration of a point is fully described by a position, bodies additionally
require a rotation to define their pose. As theoretical abstraction of rotations,

                                     φAB ∈ SO(3)                                    (2.18)

is often used to indicate the orientation of body fixed frame B with respect to a reference
frame A. It is important to understand that, since φAB lives in SO(3), there is no
numerical equivalent to a position such as ”angular position”. Instead, the orientation
φAB can be parametrized in several ways. For a better understanding, we will start
by defining the mapping between coordinate frames by means of rotation matrices and
then show how these relate to different parameterizations.

2.4.1    Rotation Matrices
Consider the situation depicted in Fig. 2.2 with a reference frame A. The position
vector of a point P which is fixed in this frame is written as
                                                     
                                              A rAP x
                                 A rAP =
                                            A rAP y  .                    (2.19)
                                              A rAP z

Consider now a reference frame B which is rotated w.r.t. A. The origin B of frame
B coincides with the origin A of frame A. The position vector of point P, this time
expressed in frame B, is                         
                                          B rAP x
                                B rAP =
                                        B rAP y  .                             (2.20)
                                            r
                                          B AP z
                                                                             
By writing the unit vectors of B expressed in frame A as A eB        B      B
                                                              x , A ey , A ez , we can
write the mapping between the two position vectors A rAP and B rAP as
                           B                B                B
                A rAP = A ex · B rAP x + A ey · B rAP y + A ez · B rAP z .          (2.21)

                                             9
The mapping shown in (2.21) can be rewritten in compact form as
                                B         B      B
                                                    
                      A rAP = A ex     A ey    A ez · B rAP
                                                                                (2.22)
                               = CAB · B rAP .

The term CAB is a 3 × 3 matrix called rotation matrix. Since the columns of CAB are
orthogonal unit vectors, CAB is orthogonal, meaning that

                                  CTAB · CAB = I3                               (2.23)

A consequence of (2.23) is that CBA = C−1           T
                                           AB = CAB . The rotation matrix CAB belongs
to the special orthogonal group SO(3). This requires to apply a special type of algebra
that is different from classical R3 vector algebra.




                                          10
                                                       v
                                     eA
                                      z

                                          eB
                                           z                      u




                                                                eA
                                                                 y

                  eB
                   x
                                                        eB
                                                         y

                          eA
                           x


Figure 2.3: A passive rotation can be interpreted as the rotation of a coordinate frame,
and an active rotation as the rotation of an object u which yields v.


2.4.2    Active vs. Passive Rotation
Rotations can have two different interpretations, which lead to the definition of the
so-called active and passive rotations.

Passive Rotation
Passive rotations, also known as rotation transformations, correspond to a mapping
between coordinate frames as shown in (2.21). A passive rotation CAB maps the same
object u from frame B to frame A:

                                   A u = CAB · B u                               (2.24)

Active Rotation
An active rotation, often indicated with a 3 × 3 matrix R, is an operator that rotates a
vector A u to a vector A v in the same reference frame A:

                                    A v = R ·A u.                                (2.25)

Active rotations are not very relevant in robot dynamics and are hence not used in the
course of this lecture.




                                          11
2.4.3       Elementary Rotations
The most simple and at the same time most often appearing rotations are elementary
rotations, i.e. rotations around one of the basis vectors eA     A    A
                                                           x , ey or ez . Given a rotation
angle ϕ, the three elementary rotations are:
               eA
      eB
       z
                 z

                            eB                                             
                             y                          1      0       0
                             ϕ    CAB = Cx (ϕ) = 0 cos ϕ − sin ϕ (2.26)
                           eA                           0 sin ϕ cos ϕ
                            y
        eA    B
         x = ex
              ϕ
                   eA
                    z
        eB
         z
                                                                 
                                                    cos ϕ 0 sin ϕ
                                   CAB = Cy (ϕ) =  0      1   0               (2.27)
                        eA    B                    − sin ϕ 0 cos ϕ
                         y = ey
     eA
      x       eB
               x

                  eA    B
                   z = ez

                                                                 
                            eB
                             y
                                                   cos ϕ − sin ϕ 0
                                   CAB = Cz (ϕ) =  sin ϕ cos ϕ 0              (2.28)
                            eA
                             y                        0     0    1
     eA
      x
             eB
              x
        ϕ


2.4.4       Composition of Rotations
Consider three reference frames A, B and C. The coordinates of vector u can be
mapped from B to A by writing

                                     A u = CAB · B u.                              (2.29)

We can also write
                                     B u = CBC · C u.                              (2.30)
By combining the last two equations, we can write

                                  A u = CAB · (CBC · C u)
                                                                                   (2.31)
                                     = CAC · C u.

The resulting rotation matrix CAC = CAB · CBC can be interpreted as the rotation
obtained by rotating frame A until it coincides with frame B, and then rotating frame
B until it coincides with frame C.




                                            12
2.4.5    Representation of Rotations
As discussed in the previous sections, generic rotations in the three-dimensional space
are represented by 3 × 3 rotation matrices, i.e. by means of 9 parameters. These
parameters, however, are not independent, but constrained by the orthogonality condi-
tions shown in (2.23). Hence, only three independent parameters such as Euler angles
are needed to obtain a minimal representation of rotations in space. Other non-minimal
representations can be derived, namely the angle-axis and the unit quaternion represen-
tation. We will briefly discuss advantages and disadvantages of each parameterization,
as well as derive the mapping from one implementation to the other. For a more de-
tailed analysis of three dimensional rotations (which goes beyond the scope of this
lecture), the reader is referred to [2].

Euler Angles
A rotation in space can be understood as a sequence of three elementary rotations
defined in (2.26) to (2.28). To fully describe all possible orientations, two successive
rotations should not be made around parallel axes. When the first and third rotations are
made around the same axis, the parameterization is called proper Euler angles. When
all three angles are different, we typically refer to Tait–Bryan, Cardan or roll-pitch-yaw
angles. The latter ones are often used in robotics.
     Note: Please note again that there applies a different type of algebra to rotations
than what we know from typical position vectors. Hence, never add, subtract or simply
multiply Euler angles, angle-axis, or quaternions.




                                           13
Figure 2.4: ZYZ Euler Angles as three successive rotations around z, y, and z axes.
Rotation from A-frame to D-frame: (z–y’–z”) – (yaw–pitch–yaw)


ZYZ Euler Angles ZYZ Euler Angles are also known as proper Euler Angles. The
rotation angles can be collected in a parameter vector
                                                 
                                                  z1
                                χR,eulerZY Z =  y  .                (2.32)
                                                  z2

The resulting rotation matrix is obtained by a concatenation of elementary rotations
(see Fig.2.4) given by

    CAD = CAB (z1 )CBC (y)CCD (z2 ) ⇒ A r = CAD D r
                                                                           
           cos z1 − sin z1 0        cos y 0 sin y cos z2           − sin z2   0
        =  sin z1    cos z1 0 0            1     0  sin z2     cos z2    0
              0         0      1 − sin y 0 cos y            0         0       1
                                                            
           cy cz1 cz2 − sz1 sz2 −cz2 sz1 − cy cz1 sz2 cz1 sy
        = cz1 sz2 + cy cz2 sz1 cz1 cz2 − cy sz1 sz2 sy sz1  .
                  −cz2 sy              sy sz2           cy
                                                                               (2.33)
Analyzing (2.33) allows to find the solution of the inverse problem. Given a rotation
matrix                                               
                                       c11 c12 c13
                             CAD = c21 c22 c23  ,                            (2.34)
                                       c31 c32 c33
the ZYZ Euler angles are given by
                                                             
                             z1          atan2
                                           p (c23 , c13 ) 
                                                               
             χR,eulerZY Z =  y  = atan2    c213 + c223 , c33  .            (2.35)
                             z2         atan2 (c32 , −c31 )




                                         14
Figure 2.5: ZXZ Euler Angles as three successive rotations around z, x, and z axes.
Rotation from A-frame to D-frame: (z–x’–z”) – (yaw–roll–yaw)


ZXZ Euler Angles ZXZ Euler Angles are also known as proper Euler Angles. The
rotation angles can be collected in a parameter vector
                                                 
                                                  z1
                               χR,eulerZXZ =  x  .                  (2.36)
                                                  z2

The resulting rotation matrix is obtained by a concatenation of elementary rotations
(Fig.2.5) given by

    CAD = CAB (z1 )CBC (x)CCD (z2 ) ⇒ A r = CAD D r
                                                                           
           cos z1 − sin z1 0 1            0        0    cos z2 − sin z2       0
        =  sin z1     cos z1 00 cos x − sin x sin z2        cos z2       0
              0           0    1 0 sin x cos x             0       0          1
                                                            
           cz1 cz2 − cx sz1 sz2 −cz1 sz2 − cx cz2 sz1 sx sz1
        = cz2 sz1 + cx cz1 sz2 cx cz1 cz2 − sz1 sz2 −cz1 sx  .
                   sx sz2               cz2 sx          cx
                                                                               (2.37)
Analyzing (2.37) allows to find the solution of the inverse problem. Given a rotation
matrix                                               
                                       c11 c12 c13
                             CAD = c21 c22 c23  ,                            (2.38)
                                       c31 c32 c33
the Euler Angles are given by
                                                            
                            z1            p(c13 , −c23 ) 
                                       atan2
                                                              
             χR,eulerZXZ =  x  = atan2    c213 + c223 , c33  .             (2.39)
                            z2          atan2 (c31 , c32 )




                                         15
Figure 2.6: ZYX Euler Angles as three successive rotations around z, y, and x. Rotation
from A-frame to D-frame: (z–y’–x”) – (yaw–pitch–roll)


ZYX Euler Angles ZYX Euler Angles, also known as Tait-Bryan angles, are often
used for flying vehicles and called yaw-pitch-roll. The rotation angles can be collected
in a parameter vector                             
                                                    z
                                χR,eulerZY X = y  .                             (2.40)
                                                    x
The resulting rotation matrix is obtained by a concatenation of elementary rotations
given by

   CAD = CAB (z)CBC (y)CCD (x) ⇒ A r = CAD D r
                                                              
          cos z − sin z 0        cos y 0 sin y 1        0      0
       =  sin z  cos z 0 0             1     0 0 cos x − sin x
             0       0       1 − sin y 0 cos y 0 sin x cos x                     (2.41)
                                                  
           cy cz cz sx sy − cx sz sx sz + cx cz sy
       = cy sz cx cz + sx sy sz cx sy sz − cz sx  .
           −sy         cy sx            cx cy

Given a rotation matrix as in (2.38), the inverse solution is
                                              atan2   (c21 , c11 )
                                                                        
                                  z                       p          
                                                                       
              χR,eulerZY X = y  = atan2 −c31 , c232 + c233  .                (2.42)
                                 x               atan2 (c32 , c33 )




                                          16
Figure 2.7: XYZ Euler Angles as three successive rotations around x, y, and z. Rotation
from A-frame to D-frame: (x–y’–z”) – (roll–pitch–yaw)


XYZ Euler Angles XYZ Euler Angles are also known as Cardan angles. The rota-
tion angles can be collected in a parameter vector
                                                  
                                                   x
                                χR,eulerXY Z = y  .                (2.43)
                                                   z

The resulting rotation matrix is obtained by a concatenation of elementary rotations
(see Fig.2.7) given by

   CAD = CAB (x)CBC (y)CCD (z) ⇒ A r = CAD D r
                                                                          
          1      0        0       cos y 0 sin y cos z             − sin z    0
       = 0 cos x − sin x 0              1  0  sin z           cos z     0
          0 sin x cos x          − sin y 0 cos y       0             0       1     (2.44)
                                                  
                cy cz           −cy sz       sy
       = cx sz + cz sx sy cx cz − sx sy sz −cy sx  .
          sx sz − cx cz sy cz sx + cx sy sz cx cy

Given a rotation matrix as in (2.38), the inverse solution is
                                             atan2
                                                                         
                                  x                 (−c p  23 , c33 ) 
                                                                        
               χR,eulerXY Z = y  = atan2 c13 , c211 + c212  .                  (2.45)
                                  z             atan2 (−c12 , c11 )




                                           17
Figure 2.8: The angle-axis representation defines the orientation of two coordinate
frames as a rotation of an angle θ around an axis n.


Angle Axis
The angle-axis is a non-minimal implementation of rotations which is defined by an
angle θ and an axis n. The vector n ∈ R3 defines the direction around which the
rotation is made, while the scalar θ ∈ R defines the rotation magnitude:
                                                   
                                                    θ
                                 χR,AngleAxis =                              (2.46)
                                                    n
This representation features four parameters and the unitary length constraint knk = 1.
It is possible to combine these two quantities to obtain a rotation vector, or Euler
vector, defined as
                                    ϕ = θ · n ∈ R3 .                             (2.47)
It is important to note that, although ϕ belongs to R3 , the sum operation is in general
non-commutative, i.e. ϕ1 + ϕ2 6= ϕ2 + ϕ1 .

   With angle axis parameters ϕAB , the rotation matrix results to
                                                                                     
              n2x (1 − cθ ) + cθ     nx ny (1 − cθ ) − nz sθ nx nz (1 − cθ ) + ny sθ
 CAB = nx ny (1 − cθ ) + nz sθ         n2y (1 − cθ ) + cθ    ny nz (1 − cθ ) − nx sθ  .
           nx nz (1 − cθ ) − ny sθ ny nz (1 − cθ ) + nx sθ       n2z (1 − cθ ) + cθ
                                                                                    (2.48)
Given a rotation matrix as in (2.38), the angle axis parameters are:
                                                            
                                  −1    c11 + c22 + c33 − 1
                          θ = cos                              ,                    (2.49)
                                                  2
                                                            
                                                   c32 − c23
                                           1     c13 − c31  .
                                  n=                                                (2.50)
                                       2sin(θ)
                                                   c21 − c12
As it can be seen from (2.50), this representation encounters a problem for θ = 0 and
θ = π since sin(θ) = 0, meaning that the rotation vector is not defined. For θ = 0 it
can have any direction, for θ = π it can point in two opposite directions.

                                           18
Unit Quaternions

A non-minimal representation of rotations which does not suffer from the disadvantage
encountered with the angle axis is provided by unit quaternions, also known as Euler
parameters. Considering a rotational vector ϕ ∈ R3 , a unit quaternion ξ is defined by

                                             
                                             ξ
                               χR,quat = ξ = 0 ∈ H,                                   (2.51)
                                             ξ̌

where
                                           
                                  kϕk        θ
                    ξ0 = cos          = cos
                                   2         2
                                                         
                                                     ξ1                           (2.52)
                                kϕk    ϕ         θ
                     ξ̌ = sin             = sin     n = ξ2  .
                                 2    kϕk        2
                                                         ξ3


The first parameter ξ0 is called the real part of the quaternion, the latter ξ̌ the imaginary
part. The unit quaternion fulfills the constraint


                                  ξ02 + ξ12 + ξ22 + ξ32 = 1.                          (2.53)


Similarly to the angle axis, the rotation matrix calculated from quaternions is

                               2                             
   CAD = I3×3 + 2ξ0 ξ̌ × + 2 ξ̌ × = 2ξ02 − 1 I3×3 + 2ξ0 ξ̌ × + 2ξ̌ ξ̌ T
          2                                                                 
           ξ0 + ξ12 − ξ22 − ξ32     2ξ1 ξ2 − 2ξ0 ξ3       2ξ0 ξ2 + 2ξ1 ξ3             (2.54)
       =  2ξ0 ξ3 + 2ξ1 ξ2       ξ02 − ξ12 + ξ22 − ξ32    2ξ2 ξ3 − 2ξ0 ξ1  .
             2ξ1 ξ3 − 2ξ0 ξ2        2ξ0 ξ1 + 2ξ2 ξ3    ξ02 − ξ12 − ξ22 + ξ32

Given a rotation matrix as in (2.38), the corresponding quaternions are

                                           √                   
                                     c11 +√c22 + c33 + 1
                           sgn(c32 − c23 ) c11 − c22 − c33 + 1
        χR,quat = ξAD = 12                √                    
                           sgn(c13 − c31 ) c22 − c33 − c11 + 1 .                    (2.55)
                                           √
                            sgn(c21 − c12 ) c33 − c11 − c22 + 1

When working with quaternions, there exists a special algebra that allows to directly
work with the quaternion paramterization (and not only the rotation matrices). The in-
terested reader should have a look at [9], which provides a very complete, yet compact
and well understandable introduction to quaternions. In short, the following rules are
important. For inversion with ξ −1 parameterizing C−1 = CT it holds that:

                                                                       
                             ξ       inverse                         ξ
                       ξ=               →        ξ −1 = ξ T =                         (2.56)
                             ξ̌                                     −ξ̌

                                                19
If ξAB and ξBC represent the quaternions corresponding to CAB and CBC , their multi-
plication associated with CAC = CAB CBC is
                                                      T
                                                                          
                                     ξ0,AB · ξ0,BC − ξ̌AB · ξ̌BC 
            ξAB ⊗ ξBC =                                                        (2.57)
                            ξ0,AB · ξ̌BC + ξ0,BC · ξ̌AB + ξ̌AB × · ξ̌BC
                                                      
                                                    ξ0
                            ξ0         −ξ̌T        ξ1 
                        =                                                    (2.58)
                            ξ̌     ξ0 I + ξ̌ ×       ξ2 
                                                AB
                          |           {z          } ξ3
                                  Ml (ξAB )                BC
                                                    
                            ξ0 −ξ1 −ξ2 −ξ3                 ξ0
                          ξ1 ξ0 −ξ3 ξ2  ξ1 
                        =                            ,                     (2.59)
                          ξ2 ξ3         ξ0 −ξ1  ξ2 
                            ξ3 −ξ2 ξ1           ξ0 AB ξ3 BC

whereby Ml (ξ) represents the left matrix of a quaternion. The same quaternion mul-
tiplication can also be written using the right quaternion, which gives:
                                                       
                                                     ξ0
                              ξ0           −ξ̌T     ξ1 
                ξAB ⊗ ξBC =                                                  (2.60)
                              ξ̌       ξ0 I − ξ̌ ×    ξ2 
                                                   BC
                            |             {z         } ξ3
                                       Mr (ξBC )           AB
                                                       
                              ξ0     −ξ1 −ξ2 −ξ3           ξ0
                             ξ1      ξ0     ξ3 −ξ2      ξ1 
                            =
                             ξ2
                                                         ,                  (2.61)
                                     −ξ3 ξ0        ξ1  ξ2 
                              ξ3     ξ2 −ξ1 ξ0 BC ξ3 AB

Using the special algebra for quaternions can be directly used to rotate vectors. The
pure (imaginary) quaternion of a coordinate vector B r expressed in frame B is given
by
                                             
                                              0
                                  p (B r) =       .                             (2.62)
                                             Br


Given the unit quaternion ξAB representing the orientation of A w.r.t. B, one can show
that [9]:

                                                  T
                       p (A r) = ξAB ⊗ p (B r) ⊗ ξAB                           (2.63)
                                                 T
                                                    
                               = Ml (ξAB ) Mr ξAB     p (B r)                  (2.64)


   Example 2.4.1: Rotation with quaternion multiplication
                          
                           0
   Given a vector A r = 1 in frame A. What is the vector expressed in frame
                           0
   B, which is rotated by θ = π/3 w.r.t. A around the x-axis?


                                         20
    The quaternion corresponding to the rotation from B to A is
                                                    √ 
                                                    3
                                  cos θ2         1  1 
                        ξAB =                 ,=        .                     (2.65)
                                 sin θ2 n         2   0 
                                                      0

    Hence, the quaternion corresponding to the inverse rotation is
                                                √ 
                                                    3
                                             1   −1  
                                      T
                              ξBA = ξAB   =    
                                                      
                                                                                (2.66)
                                             2    0
                                                  0

    In order to express vector r in B we can apply the following calculation:
                                T
    p (B r) = ξBA ⊗ p (A r) ⊗ ξBA                                                (2.67)
                              T
                                  
            = Ml (ξBA ) Mr ξBA      p (B r)                                  (2.68)
                √                      √                                       
                   3 √1      0      0          3     −1
                                                     √       0     0    0        0
              1                                                 0              
            = 
                 −1      3 √0             1
                                    0   1            3    √0        0 =  01 
              2 0      0     3 √1  2  0           0        3       1           
                                                                  √1             2√
                                                                                    3
                  0     0 −1         3        0      0      −1      3   0       − 2
                                                                             (2.69)



2.5     Angular Velocity
Consider a frame B which is moving with respect to a fixed frame A. The angular
velocity A ωAB , which describes the rotational motion of B w.r.t. A, is defined by the
limit
                                              A ϕB(t)B(t+)
                              A ωAB = lim                    .                        (2.70)
                                         →0        
As discussed in the last section, a rotational vector ϕ is, in general, not a proper vector.
However, for  → 0, the angular velocity is defined as the ratio of a proper vector
A ϕB(t)B(t+) and a scalar. Hence, angular velocities can be summed according to the
rules of vector summation. Consequently, the relative rotation of A w.r.t. B is

                                     ωAB = −ωBA .                                    (2.71)

It can be shown that the relationship between the angular velocity vector A ωAB and a
time varying rotation matrix CAB (t) is defined by

                                [A ωAB ]× = ĊAB · CTAB ,                            (2.72)

with [A ωAB ]× being the skew symmetric matrix of A ωAB :
                                                            
                             0   −ωz ωy                       ωx
             [A ωAB ]× =  ωz     0     −ωx  ,      A ωAB =
                                                             ωy  .                 (2.73)
                           −ωy ωx        0                    ωz

                                            21
Angular velocities can be transformed like other vectors:

                                 B ωAB = CBA · A ωAB .                               (2.74)

The corresponding cross-product matrix [ω]× is transformed by

                          [B ωAB ]× = CBA · [A ωAB ]× · CAB .                        (2.75)

The angular velocity of consecutive coordinate systems is given by

                                D ωAC = D ωAB + D ωBC                                (2.76)

Similarly to the vector addition used before, it is important that all vectors are expressed
in the same reference system D.

    Example 2.5.1: Angular velocity from rotation matrix

    Determine the angular velocity of B with respect to A in case of an elementary
    rotation with α (t) around eA
                                x using the corresponding rotation matrix:
                                                              
                                  1        0            0
                      CAB (t) = 0 cos (α(t)) − sin (α(t))                 (2.77)
                                  0 sin (α(t)) cos (α(t))



        [A ωAB ]× = ĊAB CTAB                                                    (2.78)
                                                                       
                      0     0        0       1               0         0
                  = 0 −α̇ sin α −α̇ cos α 0             cos α     sin α      (2.79)
                      0 α̇ cos α −α̇ sin α   0            − sin α    cos α
                               
                      0 0     0
                  = 0 0 −α̇                                                    (2.80)
                      0 α̇ 0

    Un-skewing this matrix results in:
                                             
                                             α̇
                                      ω
                                     A AB =  0 .                               (2.81)
                                              0




2.5.1    Time Derivatives of Rotation Parameterizations
As introduced in section 2.4.5, there exist different parameterizations for a rotation.
Similarly to what we have seen for linear velocity, their derivatives can be mapped to
angular velocity:
                                A ωAB = ER (χR ) · χ̇R .                             (2.82)

In the following, these mappings will be derived and discussed.

                                            22
Time Derivatives of Euler Angles ZYX ⇔ Angular Velocity
                                                                T
Given a set of ZYX Euler angles χR,eulerZY X = z y x and their time deriva-
                                  T
tives χ̇R,eulerZY X = ż ẏ ẋ , we wish to find the mapping ER,eulerZY X =
ER (χR,eulerZY X ) ∈ R3×3 that maps χ̇ to A ωAB . The columns of E(χR,eulerZY X )
are the components of the unit vectors around which the angular velocities are applied
expressed in a fixed frame A. These are obtained by selecting the columns of a rotation
matrix which is built up by successive elementary rotations specified by the Euler angle
parameterization.
    Starting from the reference frame A, the first rotation will be an elementary rotation
around A eAz , which is simply given by
                                              
                                              0         0
                                  A           
                               A ez = I3×3 0 = 0 .                                  (2.83)
                                              1         1
                                                           0
After an elementary rotation around A eA                 A
                                       z , the y axis A ey will be expressed by
                                                                 
        0
                     0   cos(z) − sin(z)              0 0       − sin(z)
      A               
   A ey = CAA0 (z) · 1 = sin(z)  cos(z)               0 1 =  cos(z)  .           (2.84)
                     0      0       0                 1 0           0
                                           0                   00
After an elementary rotation around A eA                 A
                                       y , the x axis A ex will be expressed by
                                             
             00
                                             1
           A
        A ex      = CAA0 (z) · CA0A00 (y) · 0
                                             0
                                                              
                     cos(z) − sin(z) 0          cos(y) 0 sin(y)   1
                  =  sin(z) cos(z) 0  0             1    0  0                   (2.85)
                         0        0       1 − sin(y) 0 cos(y) 0
                                   
                     cos(y) cos(z)
                  =  cos(y) sin(z)  .
                        − sin(y)

Finally, the mapping E(χR ) will be computed as:
                                                                                 
                    A                         0 − sin(z)           cos(y) cos(z)
                               0       00 
  ER,eulerZY X = A ez A eA   y    A eA
                                     x      = 0 cos(z)             cos(y) sin(z)  . (2.86)
                                               1     0                − sin(y)

It is easy to find that det(ER,eulerZY X ) = − cos(y). The mapping then becomes
singular when y = π/2 + kπ, ∀k ∈ Z. This means that although we can always de-
scribe an angular velocity using Euler Angle time derivatives, the inverse is not always
possible. The inverse mapping is given by:
                                                                     
                                   cos(z) sin(y) sin(y) sin(z)
                                  cos(y)                           1
                                                     cos(y)          
                  −1             
                 ER,eulerZY X =  − sin(z)            cos(z)        0.           (2.87)
                                  cos(z)             sin(z)          
                                                                    0
                                      cos(y)          cos(y)

                                               23
Time Derivatives of Euler Angles XYZ ⇔ Angular Velocity

Analog to the previous derivation, the projection matrix for XYZ Euler Angles and its
inverse are
                                                             
                                1       0          sin(y)
              ER,eulerXY Z = 0 cos(x) − cos(y) sin(x) ,                      (2.88)
                                0 sin(x) cos(x) cos(y)
                                                                   
                                     sin(x) sin(y) − cos(x) sin(y)
                               1        cos(y)           cos(y)    
                                                                   
                −1
              ER,eulerXY Z = 0         cos(x)           sin(x)    .         (2.89)
                                                                    
                                      − sin(x)           cos(x)    
                                0
                                         cos(y)           cos(y)


Time Derivatives of Euler Angles ZYZ ⇔ Angular Velocity

The projection matrix for ZYZ Euler angles and its inverse are
                                                     
                         0 − sin(z1 ) cos(z1 ) sin(y)
         ER,eulerZY Z = 0 cos(z1 ) sin(z1 ) sin(y)  ,                        (2.90)
                         1        0         cos(y)
                                                                     
                          − cos(y) cos(z1 ) − cos(y) sin(z1 )
                                                                    1
                              sin(y)             sin(y)              
         E−1          =     −  sin(z  )         cos(z 1)            0
          R,eulerZY Z               1                                .       (2.91)
                             cos(z1 )           sin(z1 )             
                                                                     0
                               sin(y)             sin(y)


Time Derivatives of Euler Angles ZXZ ⇔ Angular Velocity

The projection matrix for ZXZ Euler angles and its inverse are
                                                           
                            0 cos(z1 )     sin(z1 ) sin(x)
             ER,eulerZXZ = 0 sin(z1 ) − cos(z1 ) sin(x) ,                    (2.92)
                            1       0          cos(x)
                                                                      
                             − cos(x) sin(z1 ) cos(x) cos(z1 )
                                                                     1
                                 sin(x)              sin(x)           
             E−1         =      cos(z   )           sin(z 1)         0
              R,eulerZXZ              1                               .      (2.93)
                                sin(z1 )          − cos(z1 )          
                                                                      0
                                  sin(x)              sin(x)


Time Derivative of Rotation Quaternion ⇔ Angular Velocity

For quaternions it can be shown that the following relations hold:

                    I ωIB = 2H(ξIB )ξ̇IB = ER,quat χ̇R,quat                    (2.94)
                           1
                     ξ̇IB = H(ξIB )T I ωIB = E−1
                                              R,quat χ̇R,quat ,                (2.95)
                           2

                                          24
with
                             h                        i
                      H(ξ) = −ξ̌         ξ̌ × + ξ0 I3×3 ∈ R3×4                    (2.96)
                                                         
                               −ξ1     ξ0 −ξ3 ξ2
                           = −ξ2      ξ3     ξ0 −ξ1  .                          (2.97)
                               −ξ3     −ξ2 ξ1         ξ0

Hence, the mapping matrix ER and its inverse for a quaternion representation (2.51)
are

                                 ER,quat = 2H(ξ),                                 (2.98)
                                           1
                                 E−1
                                  R,quat = H(ξ) .
                                                 T
                                                                                  (2.99)
                                           2

Time Derivative of Angle Axis ⇔ Angular Velocity
For angle axis it can be shown that the following relations hold:

  I ωIB = nθ̇ + ṅ sin θ + [n]× ṅ(1 − cos θ)                                    (2.100)
                                                
                           1 sin θ       2  1
  θ̇ = nT I ωIB ,   ṅ = −            [n]× − [n]× I ωIB             ∀θ ∈ R\{0} (2.101)
                           2 1 − cosθ       2

Hence, the mapping matrix ER and its inverse for the angle axis (2.46) are
                                                                    
               ER,angleaxis = n         sin θI3×3 + (1 − cos θ) [n]×             (2.102)
                                                           
                                             nT
               E−1          =                   2                                (2.103)
                R,angleaxis     − 21 1−cosθ
                                      sin θ
                                             [n]× − 12 [n]×

Time Derivative of Rotation Vector ⇔ Angular Velocity
For a rotation vector it can be shown that the following relations hold:
                                                                
                           1 − cos kϕk          2   kϕk − sin kϕk
 ω
I IB  =   I 3×3 + [ϕ] ×                  +  [ϕ] ×                      ϕ̇    ∀kϕk ∈ R\{0}
                              kϕk2                      kϕk3
                                                                                 (2.104)
                                                
           1          2  1         kϕk sin kϕk
ϕ̇ = I3×3 − [ϕ]× + [ϕ]×        1 −                   I ωIB                  ∀kϕk ∈ R\{0}
           2            kϕk2        2 1 − cos kϕk
                                                                                 (2.105)

Hence, the mapping matrix ER and its inverse for the rotation vector (2.47) are
                                                                             
                                      1 − cos kϕk           2   kϕk − sin kϕk
  ER,rotationvector = I3×3 + [ϕ]×                     + [ϕ] ×
                                         kϕk2                        kϕk3
                                                                               (2.106)
                                                                            
                             1              2    1          kϕk sin kϕk
  E−1
   R,rotationvector = I3×3 −   [ϕ]× + [ϕ]×             1−
                             2                kϕk2            2 1 − cos kϕk
                                                                               (2.107)




                                          25
2.6     Transformation




                                                                  P


                                                              rBP

                                  rAP               eB
                                                     y                eB
                                                                       x
                    eA
                     z
                                                              B

                     A                      rAB          eB
                                                          z
                eA
                 x                 eA
                                    y



                    Figure 2.9: Single body with body fixed frame B.


    In the most general case, two reference frames have a position offset and relative
rotation (see Fig. 2.9). As a result, a point P can be transformed from one frame to
another using a homogeneous transformation matrix T which is a combined translation
and rotation:


                         rAP = rAB + rBP                                      (2.108)
                     A rAP = A rAB + A rBP = A rAB + CAB · B rBP              (2.109)
                                                  
                    A rAP           CAB A rAB    B rBP
                                =                                             (2.110)
                      1             01×3    1       1
                                  |      {z   }
                                         TAB



The inverse of the homogeneous transformation can be calculated as

                                                    B rBA
                                                              
                                                  z    }|   {
                                T−1   T          −CTAB A rAB  .
                                 AB = CAB                                     (2.111)
                                      01×3              1


Consecutive homogeneous transformations are given by


                                        TAC = TAB TBC .                       (2.112)




                                               26
Example 2.6.1: Homogeneous transformation
                                                         B
                                         P             0   ey
                                             B rBP =  1 
                                                       1

            eA
             z        A rAP =?


                                                eB
                                                 z


                                                             B
                                               0          eB
                                                           x
              A                      A rAB =  3 
                               eA
                                y              1

         eA
          x

What is the homogeneous transformation matrix TAB and the position vector
A rAP ?


The homogeneous transformation matrix is
                                               
                                1 0 0          0
                              0 0 −1          3
                                                .
                       TAB =                                      (2.113)
                              0 1 0           1
                                0 0 0          1

Correspondingly, the position vector can be calculated as:
                                               
                            1 0 0 0            0         0
                 A rAP
                             0 0 −1 3 1 2
                          =                    
                    1        0 1 0 1 1 = 2 .                 (2.114)
                              0 0 0 1            1         1




                                    27
                                                                        ΩB


                                                               vP       ΨB
                                                    P
                                                              aP
                                                    rBP
                              rAP
                                          eB
                                           y             eB
                                                          x
               eA
                z
                                     vB
                                                    B
                                    rAB                  aB
                  A                         eB
                                             z
             eA             eA
                             y
              x


                Figure 2.10: Rigid body with velocity and acceleration.


2.7     Velocity in Moving Bodies
Figure 2.10 depicts the velocities of a single body. Assuming A being in inertial fixed
frame, we have:
    • vP : the absolute velocity of P
    • aP = v̇P : the absolute acceleration of P
    • ΩB = ωAB : (absolute) angular velocity of body B
    • ΨB = Ω̇B : (absolute) angular acceleration of body B
At this point it is important to understand the difference between the velocity, i.e. the
absolute time variation of a position, expressed in a frame C:
                                                 
                                           d
                            C (ṙAP ) =C      rAP   =C vAP ,                    (2.115)
                                           dt
and the time differentiation of the coordinates of a position vector:
                                                ·       d
                            (C ṙAP ) = (C rAP ) =         (C rAP ) .            (2.116)
                                                        dt
They are only equal in case C is selected as an inertial frame. Following the transfor-
mation introduced before, we can write the position of P as:

                    A rAP = A rAB + A rBP = A rAB + CAB · B rBP .                (2.117)
Differentiating with respect to time results in

                      A ṙAP = A ṙAB + CAB · B ṙBP + ĊAB · B rBP              (2.118)
Since P is a point on the rigid body B, the relative velocity B ṙBP = 0. Furthermore,
from (2.72) it can be seen that ĊAB = [A ωAB ]× · CAB , yielding

                        A ṙAP = A ṙAB + [A ωAB ]× · CAB · B rBP                (2.119)
                              = A ṙAB + A ωAB × A rBP                           (2.120)

                                           28
This is the very famous rigid body formulation for velocities, also known as velocity
composition rule. It can be reformulated to

                                  vP = vB + Ω × rBP .                            (2.121)

Applying the same calculation rules for accelerations results in

                         aP = aB + Ψ × rBP + Ω × (Ω × rBP ) .                    (2.122)

Some Notes on Vector Differentiation
Be careful with vector differentiation in moving coordinate systems. In particular, it is
not true that the velocity generally equals the time derivative of the position:

                                        vP 6= ṙAP                               (2.123)

Equality only holds if the differentiation is done in non-moving systems represented
by A:
                                     A vP = A ṙAP                           (2.124)
In case a moving system B is used for representation, the Euler differentiation rule
must be applied

                              d
           B vP = CBA ·          (CAB · B rAP )                                  (2.125)
                             dt                         
                = CBA · CAB · B ṙAP + ĊAB · B rAP                              (2.126)
                                                                     
                = CBA · CAB · B ṙAP + [A ωAB ]× · CAB · B rAP                   (2.127)
                = B ṙAP + CBA · [A ωAB ]× · CAB · B rAP                         (2.128)
                (2.75)
                 =       B ṙAP + B ωAB × B rAP                                  (2.129)




                                             29
                    (a) ABB IRB 120            (b) Atlas   Humanoid
                    6DOF robot arm.            robot.

              Figure 2.11: Fixed base (a) and floating base (b) systems.


2.8     Kinematics of Systems of Bodies
Most robotic systems can be modeled as open kinematic structures composed of nl =
nj + 1 links connected by nj joints (prismatic or revolute) with one degree of freedom
each. Since there is a single joint with displacement qi between two successive bodies,
a simple transformation relates both bodies:

                               TBi−1 Bi = TBi−1 Bi (qi )                        (2.130)

There are two different types, namely fixed base and floating base systems whereby
the root link is either connected to the ground or freely moving. In the following
when discussing general aspects of multi-body kinematics we will focus on fixed base
systems such as manipulators. Floating base systems will be specifically covered in
section 2.10. When dealing with fixed base systems, the frame attached to the root link
is often selected to be identical with the world fixed (inertial) frame.


2.8.1    Generalized Coordinates and Joint Configuration
The configuration of a robot such as a manipulator can be described by the generalized
coordinate vector                         
                                            q1
                                          .. 
                                     q =  . .                                (2.131)
                                            qn
This set of scalar values must completely describe the configuration of the system,
i.e. for constant values of q, the robot cannot move anymore. In most cases, one
chooses coordinates that are independent, which implies that the number of generalized
coordinates corresponds to the number of degrees of freedom. For a fixed base system
without additional kinematic constraints, this minimal set of generalized coordinates
are then called minimal coordinates. It is important to understand that the choice of
generalized coordinates is not unique. However, in most applications the generalized
coordinates correspond to the degrees of freedom of the robot: For revolute joints, the
single degree of freedom qi corresponds to the rotation angle of the joint. In case of a
prismatic joint, qi represents the linear displacement.

                                          30
                                                eB
                                                 y
                                                              eB
                                                               x
                                                          B

                                                     eB
                                                      z




                                                re



                              eA
                               z



                                A
                           eA
                            x               eA
                                             y


Figure 2.12: Example of task space coordinates corresponding to the end-effector of a
manipulator.


    Example 2.8.1: Generalized Coordinates and Joint Configuration

                                            The generalized coordinates of a
                                            SCARA robot arm are:
                                                                 T
                                               q= α β γ ζ ,            (2.132)

                                            with the rotation angles α, β, and γ
                                            around the global vertical axis and the
                                            linear displacement ζ.



2.8.2    Task-Space Coordinates
The configuration of the end-effector of a robot arm as depicted in Fig. 2.12 can be
described by its relative position and orientation w.r.t. a reference frame. The reference
frame is often selected as the inertial or root frame.

End-Effector Configuration Parameters
As we have seen in section 2.2.1 and section 2.4.5, the position re ∈ R3 and rotation
φe ∈ SO(3) of a frame with respect to a base can be parameterized by χP respectively
χR . Hence, the combined position and orientation (of the end-effector) is given by
                                     
                                       re
                               xe =         ∈ SE(3),                           (2.133)
                                      φe

                                           31
which can be parameterized by

                                                  
                                                χ1
                                        χeP       .. 
                                  χe =         =  .  ∈ Rm .                                       (2.134)
                                         χeR
                                                  χm

The number m varies depending on the parameterization. Please remember at this
point that the rotation φe is only a theoretical abstraction of the orientation, for which
no numerical equivalent such as ”angular position” exists (see section 2.4).

    Example 2.8.2: End-effector Configuration

    To describe the end-effector in 3D space using Cartesian position parameters
    (3) as well as Euler Angles (3), gives a total of m = 6 parameters. In case one
    uses spherical position parameters (3) and all elements of the direction cosine
    matrix associated with the rotation (9), m = 12 parameters will be necessary.




Operational Space Coordinates

The end-effector of a manipulator operates in the so-called operational space, which
depends on the geometry and structure of the arm. The operational space can be de-
scribed by
                                                                  
                                                             χ1
                                                 χoP              
                                     χo =                  =  ...  ,                              (2.135)
                                                 χoR
                                                                 χm0


whereby χ1 , χ2 , . . . , χm0 are independent operational space coordinates2 . Hence, they
can be understood as a minimal selection of end-effector configuration parameters.
Note that m0 ≤ nj since the degree of mobility at the end-effector is certainly not
larger than the number of joints in the system.

    Example 2.8.3: Operational Space Coordinates 1

    To describe the end-effector in the most general case of a six-dimensional op-
    erational space requires m0 = 6 parameters. Hence, only Euler Angles are a
    valid parameterization while the choice of quaternions or rotation matrix is not
    possible.




   2 Please note that there are different definitions for operational space coordinates in literature and some

use them as equivalent to end-effector coordinates. We introduce this here as minimal representation to
properly define things like e.g. singularities.


                                                       32
   Example 2.8.4: Operational Space Coordinates 2

                                           For a SCARA robot arm as depicted on
                                           the left, the operational space is only
                                           4DOF, namely the three positions and
                                           the rotation around the vertical axis.
                                                            
                                                              x
                                                           y 
                                                      χo = 
                                                           z 
                                                                           (2.136)
                                                              ϕ
   Note: In the example for the SCARA robot arm it is relatively simple to define
   four operational space coordinates for a 4DOF arm. However, in case of an arm
   with four non co-linear rotation axes, it can be impossible to select four oper-
   ational space coordinates. In such an example, operational space coordinates
   remain a rather theoretical concept.


    In the following, we will not work with operational space coordinates but focus on
the more generic concept of end-effector configuration parameters.




2.8.3    Forward Kinematics

Forward kinematics describes the mapping between joint (generalized) coordinates q
and the end-effector configuration χe :


                                      χe = χe (q) .                              (2.137)


This relation can be obtained through the evaluation of (2.130) from the base to the
end-effector. For a serial linkage system with nj joints, this is

                      nj
                                       !                                  
                      Y                               CIE (q)     I rIE (q)
  TIE (q) = TI0 ·           Tk−1,k (qk )   · Tnj E =                           . (2.138)
                                                       01×3           1
                      k=1



    When talking about fixed base robots, the first coordinate frame of the robot 0 is
not moving with respect to an inertial frame such that TI0 is a constant transformation.
Furthermore, in most cases, an end-effector frame E is introduced, which is rigidly
connected to the last link but which does not have to be identical with the last body
coordinate frame. Hence, also Tnj E is constant.
    In order to create the representation in form of (2.137), it is necessary to trans-
form the rotation matrix CIE (q) and the position vector I rIE (q) into end-effector
parameters χe . While this is straight forward for the position, i.e. χeP (q) = I rIE ,
transferring the rotation matrix CIE (q) can be significantly more difficult depending
on the choice of parameterization (see section 2.5.1).

                                            33
    Example 2.8.5: Forward Kinematics



                                                        ϕ3 l3
                                                                     eE
                                            l2          e3z           z
                                          ϕ2
                                            e2z                 eE
                                                  e3x            x

                             l1
                           ϕ1              e2x
                              e1z


                                    e1x
                      l0    e0z = eIz


                             e0x = eIx
    Find the forward kinematics for a planar 3DOF robot arm.

    The generalized coordinates are
                                           
                                         q1      ϕ1
                                    q = q2  = ϕ2  .                        (2.139)
                                         q3      ϕ3

    With this we calculate the end-effector position and orientation:

                       
               χeP (q)
     χe (q) =                                                                 (2.140)
                χeR (q)
                                                                                   
               x           l1 sin (q1 ) + l2 sin (q1 + q2 ) + l3 sin (q1 + q2 + q3 )
    χeP (q) =      =
                z       l0 + l1 cos (q1 ) + l2 cos (q1 + q2 ) + l3 cos (q1 + q2 + q3 )
                                                                              (2.141)
    χeR (q) = χeR (q) = q1 + q2 + q3                                           (2.142)



2.8.4    Differential Kinematics and Analytical Jacobian
Very often, we are interested in local changes or local changes per time (i.e. velocities)
which is know as differential or instantaneous kinematics. A common approach is to
linearize the forward kinematics:
                                                        ∂χe (q)           
        χe + δχe = χe (q + δq) = χe (q) +                       δq + O δq2 ,      (2.143)
                                                          ∂q
which results in the first order approximation
                                      ∂χe (q)
                           δχe ≈              δq = JeA (q) δq,                    (2.144)
                                        ∂q

                                                  34
where                                          ∂χ1             ∂χ1 
                                                  ∂q1    ···    ∂qnj
                                       .                ..         .. 
                            JeA (q) = 
                                       ..                 .           
                                                                     .           (2.145)
                                                  ∂χm           ∂χm
                                                  ∂q1    ···    ∂qnj

is the m × nj analytical Jacobian matrix. The Jacobian matrix is very often used in
kinematics and dynamics of robotic systems. It relates differences from joint to config-
uration space. While it represents an approximation in the context of finite differences:

                                     ∆χe ≈ JeA (q) ∆q,                            (2.146)

it results in an exact relation between velocities:

                                          χ̇e = JeA (q) q̇.                       (2.147)

Position and Rotation Jacobian
Since the end-effector configuration (2.134) is parameterized by the stacked vector of
end-effector position χeP and orientation χeR , literature often talks about position and
rotation Jacobian:
                                           " ∂χeP #
                                      JeAP          ∂q
                             JeA =           = ∂χ         .                       (2.148)
                                      JeAR            eR
                                                               ∂q


Dependency on Parameterization
As we have seen in section 2.2.1 and section 2.4.5, this Jacobian strongly depends on
the selected parameterization. For example, when using Euler Angles the dimension
of JeAR is 3 × nj , in case of quaternions it is 4 × nj , and for the full rotation matrix
parameters 9 × nj .
    Example 2.8.6: Analytical Jacobian



                                                         ϕ3 l3
                                                                           eE
                                            l2           e3z                z
                                          ϕ2
                                            e2z                      eE
                                                   e3x                x

                             l1
                           ϕ1              e2x
                              e1z


                                    e1x
                      l0    e0z = eIz


                             e0x = eIx



                                                   35
Find the analytical position and rotation Jocobian for the end-effector of a pla-
nar 3DOF robot arm.

Differentiation of χeP (q) given in (2.141) with respect to the generalized co-
ordinates q given in (2.139) is:

             ∂χeP
JeAP (q) =
               ∂q
                                                                     
               l1 c1 + l2 c12 + l3 c123      l2 c12 + l3 c213 l3 c213
           =                                                            ∈ R2×3
              −l1 s1 − l2 s12 − l3 s123     −l2 s12 − l3 s213−l3 s213
                                                                         (2.149)
with c123 = cos(q1 + q2 + q3 ) and s123 = sin(q1 + q2 + q3 ).
Differentiation of χeR (q) given in (2.142) with respect to the generalized co-
ordinates q given in (2.139) is:

                                ∂χeR                
                  JeAR (q) =         = 1        1   1 ∈ R1×3             (2.150)
                                 ∂q




                                       36
                                                                      ωIk = Ωk
                                                                                  ωe = ΩE = ωIE
                                                        ekz          eky
                                 ωI(k−1) = Ω(k−1)                                 eEz
                          e2y                                       ṙIk                      eEy
                                                              ekx                eny
                                           (k−1)
                                          ey          r(k−1)k        enz                      ve = ṙIE
            e2z
                                   (k−1)                                                eEx
                                  ez                  ṙI(k−1)             enx
                        e2x
                                                  (k−1)
                                                 ex
            e1y


e1z
                  e1x
                                    eIy
        e0y

                  e0x                      eIx
                                  eIz
      e0z

                         Figure 2.13: Serial linkage arm with n moving links.


2.8.5        Geometric or Basic Jacobian
As we have seen in (2.147), a Jacobian maps generalized velocities (in joint space)
to time-derivatives of the end-effector configuration representation (which is not the
linear and angular velocity!). The associated partial differentiations of the end-effector
configuration JeA = ∂χ    e
                       ∂q depends on the selected parameterization, especially on the
parameterization of the rotation.
    However, as we have learned previously, a body has a unique linear velocity ve
and angular velocity ωe . Hence, there must exist a unique Jacobian that relates the
generalized velocity q̇ to the velocity of the end-effector (linear ve and angular ωe ):
                                       
                                        ve
                                we =          = Je0 (q) q̇.                       (2.151)
                                        ωe

Je0 is called the geometric (or basic) Jacobian and it has in the most general cases the
dimension 6 × nj . Please also note at this point that the geometric Jacobian has a basis
A as it maps generalized velocities to end-effector velocities represented in a specific
coordinate frame
                                  A we = A Je0 (q) q̇.                           (2.152)

Addition and Subtraction of Geometric Jacobians
From basic kinematics we know that the velocity of a point C can be calculated from
the velocity of a point B and the relative velocity between B and C:
                                      
                                       vC
                             wC =            = wB + wBC
                                       ωC                  .                 (2.153)
                            JC q̇ = JB q̇ + JBC q̇

                                                       37
From this we can identify that geometric Jacobians can be simply added
                                 A JC = A JB + A JBC ,                                    (2.154)
as long as they are represented with respect to the same reference frame.

Calculation of geometric Jacobian using Rigid Body Formulation
From the analysis of the velocities of points on moving bodies (c.f. (2.121)) applied to
the serial linkage depicted in Fig. 2.13, it follows that the velocity of linkage k is given
by
                          ṙIk = ṙI(k−1) + ωI(k−1) × r(k−1)k .                      (2.155)
Please keep again in mind that for numerical addition it is crucial that all the vectors
are expressed in same coordinate system. When denoting the base frame as 0 and the
end-effector frame as n + 1, the end-effector velocity can be written as
                                         n
                                         X
                               ṙIE =          ωIk × rk(k+1) .                            (2.156)
                                         k=1

Using nk to represent the rotation axis of joint k such that
                                     ω(k−1)k = nk q̇k                                     (2.157)
and recalling that
                              ωI(k) = ωI(k−1) + ω(k−1)k ,                                 (2.158)
the angular velocity of body k can be written as
                                                 k
                                                 X
                                     ωIk =             ni q̇i .                           (2.159)
                                                 i=1

Substituting this in (2.156) and rearranging terms results to
                                   n k
                                                                         !
                                   X X
                          ṙIE =                 (ni q̇i ) × rk(k+1)                      (2.160)
                                   k=1     i=1
                                   Xn                 n
                                                      X
                               =         nk q̇k ×           ri(i+1)                       (2.161)
                                   k=1                i=k
                                   Xn
                               =         nk q̇k × rk(n+1)                                 (2.162)
                                   k=1

Bringing this in matrix formulation yields the geometric Jacobian
                                                                             
                                                                              q̇1
                                                                               
                                                                             q̇2 
      ṙIE = n1 × r1(n+1)      n2 × r2(n+1)           ...     nn × rn(n+1)  .           (2.163)
            |                          {z                                 }  .. 
                                          Je0P
                                                                                    q̇n
Given (2.159), the rotation Jacobian is
                                                                           
                                                                            q̇1
                             n
                             X                                           q̇2 
                                                                          
                                                                                
                     ωIE =       ni q̇i = n1          n2      ...     nn  .             (2.164)
                                         |                  {z          } .
                                                                            .
                             i=1
                                                        Je0R
                                                                           q̇n

                                                 38
Combining these two expressions yields the combined geometric Jacobian:


                                                                                                  
                Je0P    n × r1(n+1)                          n2 × r2(n+1)     ...    nn × rn(n+1)
   Je0 =              = 1                                                                                 (2.165)
                Je0R       n1                                    n2           ...        nn


As stated at the beginning of this section, it is important that we need to define this
Jacobian with respect to a basis, e.g. I (or any other frame):


                                                                                                              
               I Je0P                I n1 × I r1(n+1)          I n2 × I r2(n+1)      ...      I nn × I rn(n+1)
 I Je0 =                    =                                                                                        .
               I Je0R                      I n1                        I n2          ...           I nn
                                                                                                          (2.166)
In this formulation, the rotation axis is given by



                                           I nk = CI(k−1) · (k−1) nk .                                    (2.167)




    Example 2.8.7: Basic Jacobian

                                                                                    ωe

                                                                      ϕ3 l3
                                                                                         eE
                                                        l2            e3z                 z
                                                      ϕ2
                                                                                     ve
                                                        e2z                    eE
                                                                e3x             x

                                         l1
                                       ϕ1              e2x
                                          e1z


                                                e1x
                                l0     e0z = eIz


                                         e0x = eIx
    Determine the basic Jacobian for this planar robot arm

    The generalized coordinates are
                                                       
                                                     q1      ϕ1
                                                q = q2  = ϕ2                                      (2.168)
                                                     q3      ϕ3


                                                               39
Step 1: determine the rotation matrices
                              
                  c1 0 s1
        CI1 =  0       1 0                                              (2.169)
                 −s1 0 c1
                                                
                         c2 0 s2         c12 0 s12
        CI2 = CI1 ·  0        1 0 =  0     1 0                        (2.170)
                        −s2 0 c2        −s12 0 c12
                                                  
                         c3 0 s3         c123 0 s123
        CI3 = CI2 ·  0        1 0 =  0      1 0 ,                     (2.171)
                        −s3 0 c3        −s123 0 c123

with s123 = sin (q1 + q2 + q3 ) and c123 = cos (q1 + q2 + q3 ) .
Step 2: determine the local rotation axis (k−1) nk :

                            0 n1 = 1 n2 = 2 n3 = ey                       (2.172)

Step 3: determine the rotation axis I nk = CI(k−1) · (k−1) nk :

                            I n1 = 0 n1 = ey                              (2.173)
                            I n2 = CI1 · 1 n2 = ey                        (2.174)
                            I n3 = CI2 · 2 n3 = ey                        (2.175)

Step 4: determine the position vectors from joint to end-effector:

                I r1E = I r12 + I r23 + I r3E                             (2.176)
                      = CI1 · 1 r12 + CI2 · 2 r23 + CI3 · 3 r3E           (2.177)
                                                       
                            sq1          s12          s123
                      = l1  0  + l2  0  + l3  0                     (2.178)
                            cq1          c12           c123
                I r2E = I r23 + I r3E                                     (2.179)
                      = CI2 · 2 r23 + CI3 · 3 r3E                         (2.180)
                                            
                            s12          s123
                      = l2  0  + l3  0                                (2.181)
                            c12          c123
                I r3E = I r3E                                             (2.182)
                      = CI3 · 3 r3E                                       (2.183)
                                 
                             s123
                      = l3  0                                           (2.184)
                             c123

Step 5a: determine the position Jacobian:
                                                           
  I Je0P = I n1 × I r1E       I n2 × I r2E    I n3 × I r3E                (2.185)
                                                                     
               l1 c1 + l2 c12 + l3 c123    l2 c12 + l3 c123   l3 c123
          =               0                       0             0       (2.186)
              −l1 s1 − l2 s12 − l3 s123 −l2 s12 − l3 s123 −l3 s123


                                        40
    Step 5b: determine the rotation Jacobian:
                                                              
                            I Je0R = I n1 I n2          I n3                 (2.187)
                                             
                                        0 0 0
                                    = 1 1 1                                (2.188)
                                        0 0 0



2.8.6    Relation between Geometric and Analytic Jacobian Matrix
As introduced in section 2.2.1 and section 2.5.1, there exists a mapping between the
differentials of the end-effector representation parameters χ̇e and the twist we consist-
ing of linear and angular velocities. This relationship also shows up in the mapping
of the representation dependent Jacobians given by a partial differentiation of position
and rotation with respect to generalized coordinates JeA = ∂χ     ∂q ∈ R
                                                                    e      m×nj
                                                                                 and the
                              6×nj
geometric Jacobian Je0 ∈ R          . Given that

          χ̇e = JeA (q) q̇    with JeA (q) ∈ Rme ×nj                             (2.189)
                                                 6×nj
          we = Je0 (q) q̇     with Je0 (q) ∈ R                                   (2.190)
                                                                  
                                                EP        0
          we = Ee (χe ) χ̇e    with Ee (χe ) =              ∈ Rme ×6             (2.191)
                                                 0       ER

the following mapping holds

                               Je0 (q) = Ee (χ) JeA (q)                          (2.192)

Please note that the parameterization dependent matrices E and E−1 were derived
earlier:
    • Cartesian coordinates (2.12)
    • Cylindrical coordinates (2.14) and (2.15)
    • Spherical coordinates (2.16) and (2.17)
    • Euler Angles
         – XYZ: (2.88) and (2.89)
         – ZYX: (2.86) and (2.87)
         – ZYZ: (2.90) and (2.91)
    • Quaternions (2.98) and (2.99)
    • Angle Axis (2.102) and (2.103)
    • Rotation Vector (2.106) and (2.107)


    Literature often does not distinguish between geometric and analytic Jacobian.
Mostly, when writing J it is referred to the geometric Jacobian. The same holds for
this course. For planar systems, the analytical and geometric Jacobian are identical.

                                           41
2.9     Kinematic Control Methods
The previously introduced relationship between end-effector and joint space configu-
ration respectively is often used for kinematic control.

2.9.1    Inverse Differential Kinematics
As we have seen, the Jacobian Je0 (q) performs a simple mapping between joint space
velocity q̇ and end-effector velocity we :

                                      we = Je0 q̇                                 (2.193)

However, in many cases and particularly in control, we are interested to solve the in-
verse problem. Given a (desired) end-effector velocity we∗ , what is the corresponding
joint velocity q̇? The obvious way to do this, is simply to invert the Jacobian or, more
general, to take the pseudo-inverse of the Jacobian
                                                ∗
                                      q̇ = J+
                                            e0 we .                               (2.194)

However, as we know, there exist different kinds of pseudo-inverse methods and the
solution is not unique but depending on the properties of Je0 .

Singularities
In case the robot is in a configuration qs such that the Jacobian Je0 (qs ) has rank <
m0 , with m0 being the number of operational space coordinates (number of con-
trollable end-effector DOFs), the configuration is called singular. A singularity im-
plies that for a desired end-effector velocity we∗ there exists no generalized velocity q̇
that fulfills we∗ = Je0 q̇. By taking the Moore-Penrose pseudo inverse, the solution
                                                              2
q̇ = J+     ∗                                      ∗
       e0 we minimizes the least square error kwe − Je0 q̇k .
    Unfortunately, if a robot is close to a singular configuration, Je0 becomes badly
conditioned with singular values close to 0. This implies that small desired velocities
we∗ in corresponding directions will lead to extremely high joint velocities q̇. This
behavior is particularly problematic for inverse kinematics algorithms as introduced in
section 2.9.3.
    Some of the singularities are obvious (e.g. in case the robot arm is at the limit of
its workspace) and hence simple to prevent. However, there can also be cases of end-
effector configurations that are perfectly within the workspace but where some joints
are in singular alignment. These situations are hard to prevent and require carefull
motion planning. This is particularly the case when working with a 6DOF arm and
controlling the same number of end-effector coordinates. A commonly used method
to prevent the robot from getting stuck in singularities while following desired end-
effector poses, is to use robot arms with 7DOF. Thereby, the redundancy of the system
can be used to keep the robot configuration away from singularities, while following
the same end-effector pose trajectory.

Damped Solution To cope with the problem of a badly conditioned Je0 close to
singularities, a common approach is to use a damped version of the Moore-Penrose
pseudo-inverse:
                                                   −1 ∗
                          q̇ = JTe0 Je0 JTe0 + λ2 I   we                 (2.195)

                                           42
with λ being a damping parameter. The larger the damping behavior, the more stable
the solution, but the slower the convergence. This inversion method minimizes the
                     2         2
error kwe∗ − Je0 q̇k + λ2 kq̇k . For more details, the interested reader is referred to
this manuscript [3].

Redundancy
In case the robot is in a configuration q∗ such that the Jacobian Je0 (q∗ ) has rank < n,
the configuration is called redundant. When taking the Moore-Penrose pseudo inverse,
as in the previous cases, the solution
                                                    −1 ∗
                                 q̇ = JTe0 Je0 JTe0     we                         (2.196)
minimizes kq̇k2 while satisfying we∗ = Je0 q̇. Redundancy in the system implies that
there exist an infinite number of solutions
                                            ∗
                                  q̇ = J+
                                        e0 we + Nq̇0 ,                            (2.197)
with N = N (Je0 ) being the null-space projection matrix of Je0 fulfilling Je0 N = 0.
This allows modifying the generalized velocity q̇ by an arbitrary choice of q̇0 without
changing the end-effector motion
                                   ∗
                                                   ∗
                         Je0 J+e0 we + Nq̇0 = we        ∀q̇0 .                  (2.198)
There are different methods to determine the null-space projection matrix. The simplest
projection is given by
                                   N = I − J+ e0 Je0 .                          (2.199)

2.9.2    Multi-task Inverse Differential Kinematics Control
For task- or operational space objectives such as following a certain trajectory, reaching
an end-effector orientation, ensuring kinematic constraints, etc., the task Jacobian and
desired task velocity are defined by:
                                  taski := {Ji , wi∗ } .                          (2.200)

Multi-task with Equal Priority
In case all nt tasks have the same priority, the generalized velocity is given by
                                      +  ∗ 
                                       J1         w1
                                      ..   .. 
                                q̇ =  .   .  .                                (2.201)
                                      J nt    wn∗
                                     | {z } | {zt }
                                         J̄        w̄

In case the row-rank of the stacked Jacobian matrix J̄ is larger than the column rank,
the tasks are only fulfilled in a least square optimal sense w̄ − J̄q̇ 2 . A way to weight
some tasks higher than others is to use a weighted pseudo inverse matrix
                                                   −1 T
                                 J̄+W = J̄T WJ̄        J̄ W                        (2.202)
with a weighting matrix W = diag (w1 , . . . , wm ). This corresponds to the minimiza-
tion of the error W1/2 w̄ − J̄q̇ 2 . Since W is a diagonal matrix, the Cholesky
factor 1/2 corresponds to element-wise square root.

                                              43
Multi-task with Prioritization
An approach in order to clearly prioritize certain tasks with respect to others is to use
consecutive null-space projection in oder to determine the solution. Assume that the
nt tasks have decreasing priority. As we have seen in (2.197), the solution to task1 is
                                                   ∗
                                          q̇ = J+
                                                1 w1 + N1 q̇0 .                                                 (2.203)

Hence, in order not to violate the first objective, it must hold that
                                                    ∗
                                                               
                          w2 = J2 q̇ = J2 J+    1 w1 + N1 q̇0 .                                                 (2.204)

This can be solved for q̇0
                                                       +                          
                                 q̇0 = (J2 N1 )             w2∗ − J2 J+  ∗
                                                                      1 w1                                      (2.205)

and back-substituted in (2.203) resulting in
                                  ∗                              +                    
                         q̇ = J+
                               1 w1 + N1 (J2 N1 )                      w2∗ − J2 J+  ∗
                                                                                 1 w1 .                         (2.206)

For nt tasks, the solution can be written in a recursive way as
              nt                                                                  i−1
                                                                                                  !
              X                                              +                   X
       q̇ =         N̄i q̇i ,   with q̇i = Ji N̄i                      wi∗ − Ji         N̄k q̇k       ,         (2.207)
              i=1                                                                 k=1

                                                                                                                        T
whereby N̄i is the null-space projection of the stacked Jacobian J̄i = JT1                                ...    JTi−1        .
    Example 2.9.1: Multi-task Control




                                                                  ϕ3 l3
                                                                                      eE
                                                 l2              e3z                   z
                                               ϕ2
                                                                                      ve
                                                 e2z                         eE
                                                           e3x                x

                                  l1
                                ϕ1              e2x
                                   e1z


                                         e1x
                           l0   e0z = eIz


                                  e0x = eIx
    This example discusses again the 3DOF planar robot arm which has unitary
    link lengths. Given is a desired end-effector velocity 0 ṙ∗E (t) defined in R2 .
    For numerical evaluation, we consider an instant t when the robot is in con-
                                       T
    figuration qt = π/6, π/3, π/3         and the desired end-effector velocity is


                                                           44
    ∗
                   T
0 ṙE,t =   1, 1        .



What is the analytical solution to this end-effector tracking problem?

The desired end-effector motion is:
                                          ∗
                                         wE = 0 ṙ∗E .                     (2.208)

Using JE given by the x and z row of the Jacobians calculated in Example 2.8.6
and 2.8.7, the generalized velocity can be calculated as:
                                                  ∗
                                         q̇ = J+
                                               E wE                        (2.209)


What is the numerical solution to this end-effector tracking problem?

The target velocity for this instant is
                                                          
                                     ∗                    1
                                    wE,t = 0 ṙ∗E,t =                      (2.210)
                                                          1
                                                  
Evaluation of the Jacobians for qt = π/6, π/3, π/3 gives
                                                         √     √ 
                                              1 0        − 3   − 3
                            JE,t = JE (qt ) =                              (2.211)
                                              2 −4        −3    −1

Taking the Moore-Penrose pseudo inverse results in
                                                  
                                             0.069
                   q̇single
                     t      = J+    ∗
                               E,t wE,t =
                                          −0.560 .                       (2.212)
                                            −0.595

As we can see, these generalized velocities yield the exact task space error
velocity                                   
                                 single     1        ∗
                   wE,t = JE,t q̇t      =       = wE,t               (2.213)
                                            1



Beside moving the end-effector with the desired velocity, we want that the first
and second joint velocity is zero. What is the general solution if all tasks should
be fulfilled with equal priority?

In addition to the previously defined task, we introduce an additional task to
keep all joint velocities equal:
                                                    
                                0             1 0 0
                       wj =       ,     Jj =                          (2.214)
                                0             0 1 0


                                              45
The stacked problem can now be solved for :
                                      +  ∗ 
                                      JE   wE
                              q̇ =                                         (2.215)
                                      Jj   wj∗



What is the numerical solution to the stacked problem?


                                           +  ∗ 
                                      JE,t      wE
                           q̇stack =                                       (2.216)
                             t         Jj,t     wj∗
                                              
                                       −0.133
                                   = −0.067                              (2.217)
                                       −1.132

We notice that this joint velocity results in
                                               
                                        1.039      ∗ 
                     JE,t stack          0.933 
                                                 6= w∗E
                            q̇t     =−0.133                             (2.218)
                     Jj,t                            w∆q̇
                                         −0.067

It is interesting to have a look at the errors on both tasks, which are
                         ∗
                       kwE,t − JE,t q̇stack
                                      t     k2 = 0.0059                    (2.219)
                           ∗
                         kwj,t − Jj,t q̇stack
                                        t     k2 = 0.0223.                 (2.220)

As we can see, both tasks will be equally violated and neither of them is ful-
filled. In comparison, the solution without joint velocity constraint (2.212)
yields
                         ∗
                       kwE,t − JE,t q̇single
                                      t      k2 = 0                        (2.221)
                           ∗
                         kwj,t − Jj,t q̇single
                                        t      k2 = 0.319.                 (2.222)

The error in the second task (2.227) is larger than the sum of errors of both tasks
(2.219) and (2.220) of the joint optimization. In other words, when optimizing
for both tasks, we sacrifice end-effector tracking performance in order to reduce
the velocity in joint 1 and 2.



What is the general solution if the end-effector tracking task has higher priority
than keeping the first two joint velocities to zero?

To this end we use the formalism given in (2.206)
                                          +                  
          q̇prio
            t    = J+  ∗
                    1 w1 + N1 (J2 N1 )        w2∗ − J2 J+  ∗
                                                        1 w1 .             (2.223)


                                        46
    with J1 = JE,t , J2 = Jj,t , w1∗ = wE,t
                                         ∗            ∗
                                            and w2 = wj,t . A possible null-space
    projector matrix is
                                                           
                                               1 −2 2
                                           1
                        N1 = I − J +1 J1 =    −2 4 −4                    (2.224)
                                           9
                                               2 −4 4

    Using N1 , which has rank = 1, the generalized velocity results in
                                                
                                         −0.169
                              q̇prio
                                t    = −0.085                               (2.225)
                                         −1.070

    Again, let us have a look at the errors
                              ∗
                            kwE,t − JE,t q̇prio
                                           t    k2 = 0                        (2.226)
                                ∗
                              kwj,t − Jj,t q̇prio
                                             t    k2 = 0.036                  (2.227)

    In comparison to the stacked solution, the total error is larger but the end-
    effector task is tracked accurately. When comparing to the single task opti-
    mization, it can be seen that the total error is reduced. In fact, the single di-
    mensional null-space was used in an optimal sense in order to reduce the joint
    velocities without changing end-effector tracking performance.



2.9.3    Inverse Kinematics
The goal of inverse kinematics is to find a joint configuration q as a function of a given
end-effector configuration χ∗e :
                                       q = q (χ∗e )                                (2.228)

Analytical Solution
There exist analytic solutions for a large class of mechanisms. In fact, many robot arms
are particularly designed such that inverse kinematics can be analytically solved. For
a classical 6DOF robot arm, the necessary condition for an analytical solution is that
three neighboring axes intersect. There exist two widely used approaches to solve an
inverse kinematics problem analytically. The geometric approach is to decompose the
spacial geometry of the manipulator into several plane problems and apply geometric
laws. The algebraic approach is to manipulate the transformation matrix to get the
angles. For more information, the interested reader is referred to [8].

Numerical Solution
With increasing computational power, numerical approaches are a common tool to
solve the inverse kinematics problem. As we have seen in section 2.8.4, differences
in joint space coordinates ∆q can be directly mapped to differences in end-effector
coordinates ∆χe using the analytical Jacobian:

                                    ∆χe = JeA ∆q.                                 (2.229)

                                              47
    This relationship can be used to iteratively solve the inverse kinematics problem
for a given desired end-effector configuration χ∗e and start configuration q0 (see al-
gorithm 1). The algorithm iterates through these steps until the target location q∗ is
reached with a certain tolerance on k∆χe k = kχ∗e − χe (q∗ )k < tol.



Algorithm 1 Numerical Inverse Kinematics
 1: q ← q0                                                         . Start configuration
 2: while kχ∗
            e − χe (q)k > tol do                     . While the solution is not reached
 3:    JeA ← JeA (q) = ∂χ∂q (q)
                           e
                                                              . Evaluate Jacobian for q
         +            +
 4:    JeA ← (JeA )                                      . Calculate the pseudo inverse
 5:    ∆χe ← χ∗e − χe (q)             . Find the end-effector configuration error vector
 6:    q ← q + J+
                eA ∆χe                            . Update the generalized coordinates
 7: end while




    Unfortunately, this approach has some problems. First, if the error between the
target and actual configuration ∆χie is getting large, the error linearization as imple-
mented by analytical Jacobian is not accurate enough. A simple way to deal with this
issue is to scale each update step:



                                 q ← q + kJ+
                                           eA ∆χe                                (2.230)



with 0 < k < 1 in order to remain within the validity region of the linearization
and avoid overshooting or divergence. However, this leads to a slower convergence
of the solution. When working with very small k gains, the solution follows the local
linearization represented by the analytical Jacobian until full convergence.

    Second, in case the target is close to a singularity position the Jacobian inversion
becomes a badly conditioned problem. As illustrated in section 2.9.1, one can for
example use the damped inverse in order to overcome this problem. Another approach,
for which a detailed explanation is given in [3], is to use the Jacobi-transposed method
to replace the update step 6 by



                                 q ← q + αJTeA ∆χe .                             (2.231)



When choosing the parameter α small enough, convergence of the problem can be
guaranteed. At the same time, there is no time-consuming inversion required.

    At this point it is important to understand that the choice of parameterization leads
to very different numerical behaviors as illustrated in Example 2.9.7.


                                           48
Example 2.9.7: Inverse Kinematics of Rotations




As an example to illustrate the effect of different parameterizations, we con-
sider an example with a simple robot arm that features three successive rota-
tional joints with rotation axis z, y, and x respectively:
                                          
                                            qz
                                    q = qy                           (2.232)
                                            qx

The selection of this set of generalized coordinates results in the rotation matrix
given in (2.41) with z = qz , y = qy , and x = qx . Following (2.164), the basic
Jacobian is
                                                            
                0                    0                            1
    Je0R = 0           Cz (qz ) 1       Cz (qz ) Cy (qy ) 0         (2.233)
                1                    0                            0
                                           
              0 − sin(z) cos(y) cos(z)
          = 0 cos(z) cos(y) sin(z)  .                                     (2.234)
              1        0         − sin(y)
                                                                   T
The initial conditions are selected as q0 = −0.7         0      1.5 . For this
configuration, the rotation of the end-effector expressed in Euler ZYX coor-
                                                             T
dinates corresponds to χR,eulerZY X = −0.7 0            1.5 indicated by the
blue coordinate frame aligned with the center of the unit sphere. Please note:
Since the Euler Angle parameterization has exactly the same order as joint ro-
tations, we have χR,eulerZY X = q. The target orientaiton of the end-effector
                                                       T
is selected as χR,eulerZY X = 0.7         1.5     −0.5 (red frame). For pa-
rameterization of the rotation we select:
                                                            T
    1. Euler angles ZYX: χR,eulerZY X = z          y      x
                                                            T
    2. Euler anlges XYZ: χR,eulerXY Z = x          y      z
                                                       T
    3. Rotation Vector: χrotvec = ϕx        ϕx      ϕz
For every parameterization, the following steps have to be applied:


                                        49
Figure 2.14: A 3D rotation from a start to a target coordinate system can be represented
by a rotation angle and a rotation vector



       1. Evaluate the rotation matrix Ci = C (q) for the actual generalized coor-
          dinates qi
       2. Transform Ci into end-effector parameters χiR using
             • Euler ZYX: (2.42)
             • Euler XYZ: (2.45)
             • Rotation vector: (2.47), (2.49) and (2.50)
       3. Evaluate the analytical Jacobian JieAR = EχR (χiR )−1 Je0R (qi ) with
          EχR given by
             • Euler ZYX: (2.86)
             • Euler XYZ: (2.89)
             • Rotation vector: (2.106)
       4. Calculate difference ∆χiR = χ∗R − χiR
       5. Update the generalized coordinates qi+1 = qi + kJ+              i
                                                                  eAR ∆χR , with k
          being a small scaling factor to follow always the local linearization.
   Depending on the robot kinematics and the choice of rotation parameterization
   (blue: Euler ZYX, red: Euler XYZ, black: rotation vector), the coordinate
   frame is rotated on different ways to the target system. The matlab code for
   this example can be found in appendix A.2



Appropriate Rotation Error
As we have seen in the previous example, the selection of rotation parameterization
changes the convergence from the start to the goal configuration. Ideally, we would
work with rotation errors and directions that allow for a rotation on a ”shortest path”.
In order to better understand rotation errors in 3D we can have a look at Fig. 2.14.

                                          50
As we already know from section 2.4.5, a possible rotation parameterization is angle
axis, i.e. an axis giving the direction of the rotation (black arrow) and an angle defining
the magnitude of the rotation. As the rotation axis remains constant throughout the
rotation, this can be understood as the ”closest possible rotation”. Hence, we choose
rotation error as
                                         ∆φ = ∆ϕ,                                   (2.235)
which parameterizes the relative rotation CGS from start CSI (ϕt ) to the goal CGI (ϕ∗ )
orientation given by
                          CGS (∆ϕ) = CGI (ϕ∗ )CTSI (ϕt ).                       (2.236)
∆ϕ is not ϕ∗ − ϕt but can be calculated from CGS using (2.47), (2.49) and (2.50).
Given the definition of the angular velocity in (2.70), we can change the update step 6
of algorithm 1 to
                                q ← q + k pR J +e0R ∆ϕ.                        (2.237)
In case kpR is taken very small, the algorithm will rotate on the ”shortest path” from
the start to the target configuration. Please note two things: First, this update step takes
the geometric instead of the analytical Jacobian. Second, in contrast to the previous
formulations, ∆ϕ is not equivalent to the difference in rotation vectors of start and
goal rotation, but rather represents the rotation vector of the ”difference rotation”.
    To better understand the concept of relative rotation between two frames, we can
relate the relative rotation between two frames with the linear relative position. Con-
sider two frames B and B ∗ with their origins B and B ∗ , representing the measured and
desired pose of a body with respect to the inertial frame I. The linear position error
can be defined as
                                 I rBB ∗ =I rIB ∗ −I rIB .                           (2.238)
Analogously, we can define the relative rotation between the two poses as

                                  CBB∗ = CTIB · CIB∗ .                              (2.239)

    Example 2.9.8: Inverse Kinematics using Rotation Vector




    This example considers the same problem as in example 2.9.7, but applies the
    inverse kinematics approach using a rotation vector description of the rotation
    error.
    Given the target rotation matrix C∗ , the following steps are applied:


                                            51
   1. Get the rotation matrix Ci = C (q) for the actual generalized coordi-
      nates qi .
   2. Calculate the relative rotation Crel = C∗ · CiT .
   3. Calculate the rotation vector for the relative rotation ∆ϕ using (2.47),
      (2.49) and (2.50).
   4. update the generalized coordinates qi+1 = qi + kJ+   e0R ∆ϕ, with k being
      a small scaling factor to follow always the local linearization.
As we can see, the solution follows the green path (= ”direct line”) from the
start to the goal location. The matlab code for this example can be found in
appendix A.2




                                      52
2.9.4    Trajectory Control
Pure inverse differential kinematics is often insufficient to follow a predefined tasks-
space trajectory, as the pose will drift away if no feedback is provided for position or
rotation. Hence, trajectory control can be achieved by stabilizing inverse differential
kinematics through a weighted tracking error feedback . This results in smooth and
drift-free motion.

Position Trajectory Control
For position tracking with a given pre-planned position r∗e (t) and velocity ṙ∗e (t), the
problem is trivial. The feedback control part should bring
                                                      
                               ∆rte = r∗e (t) − re qt                             (2.240)

to zero, which results in the following trajectory controller:
                                                             
                         q̇∗ = J+     t      ∗             t
                                e0P (q ) · ṙe (t) + kpP ∆re .                    (2.241)
Thereby, kpP represents the position feedback, defining how quickly the actual position
converges to the target position. If this algorithm is implemented as digital control
problem with fixed time step ∆t, one can provide stability boundaries for kpP by an
Eigenvalue analysis (see e.g. [8]).

Orientation Trajectory Control
Things are getting more complicated when tracking orientations χ∗R (t) and angular
velocities ω ∗ (t). As we have seen in the inverse kinematics example 2.9.7, the selection
of parameterization leads to different trajectories. The best approach is to follow the
shortest rotation approach, which is equivalent to the position tracking. With this we
can write:
                           q̇∗ = J+      t      ∗
                                  e0R (q ) · (ωe (t) + kpR ∆ϕ) ,                   (2.242)
whereby ∆ϕ is calculated as described in section 2.9.3. Please note that this formula-
tion does not require an analytical Jacobian.




                                           53
                                                                  e
                                                                 B z
                                                                       body frame B
                                                                        e
                                                                       B y
                                                                        B x e          HAA


    unactuated




                                                                                            actuated joint coordinates
                                                                                HFE


    base coordinates
                                                                                      KFE


                       e
                       I z

                             e
                             I y

                                   e constraint contact forces
                                   I x
  intertial frame I

                                         (a) Quadruped                                                                   (b) Humanoid


                                   Figure 2.15: Free-floating robots have an un-actuated base.

2.10                         Floating Base Kinematics
Free-floating robots like the quadruped and humanoid depicted in Fig. 2.15 are de-
scribed by nb un-actuated base coordinates qb and nj actuated joint coordinates qj :
                                          
                                           qb
                                     q=                                       (2.243)
                                           qj
The unactuated base is free in translation and rotation
                                         
                                     q bP
                            qb =            ∈ R3 × SO(3),                                                                               (2.244)
                                     qbR
whereby the position qbP and rotation qbR can be parameterized using different repre-
sentations as seen in sections 2.2.1 and 2.4.5, Hence, the dimension of the generalized
coordinate vector of a floating base system nb + nj depends on the parameterization
of the rotation, whereby the minimal number of generalized coordinates for the base is
nb0 = 6.
    There are several challenges linked with floating base systems. First, there are
typically no (onboard) sensors that allow to directly measure the base position and
orientation. To cope with this, some research areas use motion tracking systems, i.e.
external cameras and markers on the robot that allows measuring the pose of the base.
Otherwise, it is necessary to use sensor fusion algorithms in order to estimate the pose
from different other sensor information. Second, since the base is not directly actu-
ated, the motion of the system of bodies (i.e. the total linear and angular impulse) can
only be changed through additional external forces resulting from contacts (see also
section 2.10.4).

2.10.1                       Generalized Velocity and Acceleration
Since differentiation in SO(3) is different from R3 , people often introduce generalized
velocity and acceleration vectors
                                                          
                 I vB                                   I aB
             B ωIB                                B ψIB 
                                                          
              ϕ̇1                                         
        u=           ∈R   6+nj
                                   =R   nu
                                               u̇ =  ϕ̈1  ∈ R6+nj              (2.245)
              ..                                   .. 
              .                                    . 
                 ϕ̇nj                                   ϕ̈nj

                                                                                      54
     As shown in section 2.5.1, there exists a direct mapping from rotational velocity ω
to time derivatives of end-effector rotation coordinates q̇bR such that
                                                                      
                                                 I3×3    0        0
                 u = Ef b · q̇, with Ef b =  0         EχR       0             (2.246)
                                                   0     0     Inj ×nj

whereby the rotation parameterization dependent matrices EχR and its inverse E−1
                                                                              χR
are given in
    • Euler Angles
         – XYZ: (2.88) and (2.89)
         – ZYX: (2.86) and (2.87)
         – ZYZ: (2.90) and (2.91)
    • Quaternions (2.98) and (2.99)
    • Angle Axis (2.102) and (2.103)
    • Rotation Vector (2.106) and (2.107)
    Please note that many text-books write q̇, but implicitly mean u and not the time-
derivative of the parameterization. For fixed base systems, there is typically no differ-
ence. However, whenever working with floating base systems, you must be aware of
the difference. In these lecture notes we try to be consistent in this context and hence
always use u when specifically talking about floating base systems.

2.10.2     Forward Kinematics
We wish to derive the relationship between the generalized velocities u and the opera-
tional space velocities I vQ of a point Q, which is fixed at the end of a kinematic chain
that stems from a floating base B. The position vector I rIQ = I rIQ (q) of a point w.r.t.
the inertial frame I is given by:

                      I rIQ (q) = I rIB (q) + CIB (q) · B rBQ (q),                (2.247)

where the rotation matrix CIB (q) describes the orientation of the floating base B w.r.t.
the inertial frame I, I rIB (q) represents the position of the floating base B w.r.t. the
inertial frame I expressed in the inertial frame, B rBQ (q) represents the position of Q
w.r.t. the floating Base B expressed in frame B, and q = q(t) is a function of time t.

2.10.3     Differential Kinematics of Floating Base Systems
Time differentiation of the position vector (2.247) yields:


         I vQ = I vB + ĊIB · B rBQ + CIB · B ṙBQ
              = I vB + CIB · [B ωIB ]× · B rBQ + CIB · B ṙBQ
              = I vB − CIB · [B rBQ ]× · B ωIB + CIB · B ṙBQ                     (2.248)
              = I vB − CIB · [B rBQ ]× · B ωIB + CIB · B JPqj (qj ) · q̇j
                h                                                  i
              = I3×3     −CIB · [B rBQ ]×       CIB · B JPqj (qj ) · u

                                           55
   If we attach a frame at I rIQ , we can derive a similar mapping for angular velocities.
The orientation of frame Q w.r.t. the inertial frame I is described by:

                                       CIQ = CIB · CBQ                               (2.249)
Time differentiation of both sides of (2.249) yields:

    [I ωIQ ]× · CIQ = [I ωIB ]× · CIB · CBQ + CIB · [B ωBQ ]× · CBQ
                       = [I ωIB ]× · CIQ + CIB · CBI · [I ωBQ ]× · CTBI · CBQ        (2.250)
                       = [I ωIB ]× · CIQ + [I ωBQ ]× · CIQ ,

which gives finally:

                  I ωIQ = I ωIB + I ωBQ
                              h                                          i           (2.251)
                             = 03×3        CIB         CIB · B JRqj (qj ) · u

                                                                                T                 
                                                                                                  T T
Hence, the mapping from generalized velocities u to the operational space twist I vQ           I ωIQ
of frame Q is realized by the spatial Jacobian:

                                
                       I JP
         I JQ (q) =
                          I JR
                      "                                                          #   (2.252)
                   I3×3              −CIB · [B rBQ ]×       CIB · B JPqj (qj )
                 =
                   03×3                  CIB                CIB · B JRqj (qj )


2.10.4     Contacts and Constraints
In kinematics, contacts between the robot and its environment can be modeled as kine-
matic constraints. Every point Ci that is in contact with the environment (attached to
coordinate frame I) imposes three constraints
                                                            
                                                             0
                       r
                     I ICi  = const,      ṙ
                                        I ICi  =   r̈
                                                  I ICi =   0 .              (2.253)
                                                             0

These contact constraints can be expressed as a function of the generalized velocities
and accelerations using the contact point Jacobian

                            I JCi u = 0,      I JCi u̇ + I J̇Ci u = 0                (2.254)

In case there are nc active contacts, the constraints are simply stacked to
                                            
                                        JC 1
                                            
                              Jc =  ...  ∈ R3nc ×nn .                              (2.255)
                                           JCnc

The rank(Jc ) indicates the number of independent contact constraints. This stacked
Jacobian can be split into                     
                                Jc = Jc,b Jc,j                              (2.256)

                                                  56
whereby Jc,b indicates the relation between base motion and contact constraints. In
case the rank of Jc,b (i.e. number of base constraints) is full (rank(Jc,b ) = 6), the
system features enough constraints such that the base motion can be controlled from
joint motion. The difference between the number of independent contact constraints
rank(Jc ) and the number of base constraints rank(Jc,b ) is the number of internal
kinematic constraints that must be fulfilled.

Point Contacts - Quadruped




      (a) Fully-constraints                        (b) Under-constrained


Figure 2.16: Depending on the number and arrangement of point contacts, a quadruped
is fully-constrained (a) or under-constrained (b).

    The point feet of a quadrupedal robot impose three (independent) constraints each.
In case of two point contacts, the stacked contact Jacobian has rank(Jc ) = 6 but
the Jacobian w.r.t. base coordinates has only rank(Jc,b ) = 5. This implies that the
system is under-actuated and the base can not be arbitrarily moved by the joints. This
becomes intuitively clear when looking at Fig. 2.16(b), as the robot cannot change the
orientation around the line of support.
    In contrast thereto, three point contacts as illustrated in Fig. 2.16(a) imply rank(Jc ) =
9 and rank(Jc,b ) = 6. This means that the body position and orientation is fully con-
trollable through the joints. At the same time, there are three internal constraints that
can be interpreted by the fact that the three legs cannot be moved one with respect to
another.

Extended Contacts - Humanoid
For systems with extended feet, additional constraints are required in order to limit
the foot rotation. One possible option is to introduce a rotational Jacobian. Much
more common is to assign multiple contact points on the same link. A single con-
tact point (Fig. 2.18, left) imposes three constraints as already seen in the previous
section. In case of two contact points, the rank of the constraints is rank(Jc ) =
rank(Jc,b ) = 5 and in case of three points assigned to the same element we get
rank(Jc ) = rank(Jc,b ) = 6 although Jc ∈ R9×nj .

2.10.5     Support Consistent Inverse Kinematics
Applying inverse kinematics to floating base systems answers the question how to
move individual joints in order to achieve certain task-space motion without violat-
ing contact constraints. This seeks for the application of a multi-task approach with
prioritization, whereby the contact constraints are considered to have higher priority

                                            57
            (a) Fully-constraints                         (b) Under-constrained


Figure 2.17: Depending on the number and arrangement of point contacts, a humanoid
is fully-constrained (a) or under-constrained (b).




             Figure 2.18: Multiple contact points attached to a single foot.


than the task-space motion. As introduced above, contact constraints of the nc legs in
ground contact are given by
                                     Jc u = 0,                                (2.257)
which implies that the motion of the system in contact is given by

                               u = J+
                                    c 0 + N (Jc ) u0 = Nc u0 .                    (2.258)

Hence, given a demanded task space motion

                                         wt = Jt ui                               (2.259)

the joint velocity required to achieve this is
                                                      +
                                    u = Nc (Jt Nc ) wt                            (2.260)




                                             58
Chapter 3

Dynamics

Mathematical models of a robot’s dynamics provide a description of why things move
when forces are generated in and applied on the system. They play an important role
for both simulation and control. This chapter presents a concise overview regarding
different approaches for modeling the dynamics of a robot and provides insight into
model-based control techniques.


3.1     Introduction
For many applications with fixed-based robots we need to find a multi-body dynamics
formulated as
                   M (q) q̈ + b (q, q̇) + g (q) = τ + Jc (q)T Fc               (3.1)
consisting of the following components:

 M (q)       ∈ Rnq ×nq    Generalized mass matrix (orthogonal).
 q, q̇, q̈   ∈ Rn q       Generalized position, velocity and acceleration vectors.
 b (q, q̇)   ∈ Rn q       Coriolis and centrifugal terms.
 g (q)       ∈ Rn q       Gravitational terms.
 τ           ∈ Rn q       External generalized forces.
 Fc          ∈ R3×nc      External Cartesian forces (e.g. from contacts).
 Jc (q)      ∈ Rnc ×nq    Geometric Jacobian corresponding to the external forces.
Please note: For simplicity and compactness, we use here the formulation for fixed
base systems with q̈ instead of u̇ as introduced for floating base systems. Section 3.7
will specifically deal with the dynamics of floating base systems.
    In literature, different methods exist to compute the so-called Equations of Mo-
tion (EoM) of a given system, i.e., a closed-form mathematical model of the system
dynamics. All such methods are usually based on Newtonian and/or Lagrangian me-
chanics formulations, but despite the different approaches taken, all methods will result
in equivalent descriptions of the dynamics.
    In this text we present the most common methods used in robotics. The first such
approach presented in section 3.3, is the well-known classical Newton-Euler method,
which essentially applies the principles of conservation of linear and angular momen-
tum for all links of a robot, and considers the motion explicitly in Cartesian space.
The second approach presented in section 3.4, known as the Lagrange Method, is an
analytical technique which utilizes scalar energy-based functions over the the space of

                                           59
generalized coordinates which adhere to certain minimization principles, thus resulting
in trajectories which automatically satisfy the kinematic constraints of the system. The
third and arguably most useful approach of all is presented in section 3.5 and is that
of the Projected Newton-Euler method, which manages to combine the advantages of
both the Newton-Euler and Lagrange methods, thus constituting a reformulation of the
Newton-Euler method in terms of the generalized coordinates and hence directly con-
siders the feasible motions of the system, i.e., those satisfying the applicable kinematic
constraints.
     Although the methods are often presented to be quite different, and may appear as
such initially, their equivalence will become quite clear by the end. In the end, it is up
to the reader to identify the appropriate approach to use for modeling a given robotic
system or problem setting.


3.2     Foundations from Classical Mechanics
Prior to presenting each of the aforementioned methods for deriving the EoM, there are
certain principles and necessary analytical tools which one must be acquainted with
first. These are necessary for understanding the foundations upon which the presented
methods are based.

3.2.1    Newton’s Law for Particles

                               dm
                                         r̈
                               dF
                                                   r




                       Figure 3.1: Force acting on single particle

    The most basic formulation of Newtonian mechanics describes the motion of point-
masses, i.e., particles with mass m and of infinitely small dimensions, were the entire
mass is concentrated at the single point defined by the position vector r. Keep in mind
that a point-mass does not have an orientation as it is impossible to define any geometry.
This means that we need only consider the Newton’s second law to fully describe the
motion of the system:
                                        r̈m = F                                      (3.2)
Considering again the fact that we have defined the mass to be of infinitely small di-
mensions, we can think of it as an infinitesimal mass dm subject to infinitesimal forces
dF concentrated at the position of the particle:

                                       r̈dm = dF                                     (3.3)

As we will see in the sections that follow, these relations still play an important role in
the derived methods. (3.2) still applies for the case of computing the linear dynamics
of the Center of Mass (CoM) of rigid bodies, while (3.3) is used for to describe the
effects of internal forces in a system via the Principle of Virtual Work.

                                              60
3.2.2    Virtual Displacements
We will now introduce the concept of variational notation via the δ operator. Essen-
tially, this operator behaves exactly as the differential d operator except that it has a
completely different meaning. The differential is defined to describe an infinitesimal
quantity which is then used to define “rates of change” of one quantity with respect
to another. On the contrary the variation of a quantity describes, for a fixed instant in
time, all possible directions the quantity may move in while adhering to the applicable
constraints.
     The most important fact to remember regarding a variation, is that if it taken with
respect to quantity which is a function of time, then any temporal dependence is disre-
garded completely. To demonstrate this property, we will define the admissible varia-
tion of a position vector, called a virtual displacement δr, and assume that the position
is a function of generalized coordinates q and time t, thus r = r(q, t). By applying the
chain rule over the nq elements of q we compute the variation δr:
                                               nq
                                               X  ∂r
                                 δr(q, t) =                δqk                       (3.4)
                                                     ∂qk
                                               k=1

Notice that the expression in (3.4) does not include ∂r
                                                     ∂t , and can thus be understood to
be a purely geometric interpretation of displacement.



3.2.3    Virtual Displacement of Single Rigid Bodies

                                                      Ψ = Ω̇
                                          δΦ            Ω = ωIB
                            dm
                                                                 {B}
                           dF
                                      ρ
                           r                          vS
                                               S
                                                       aS

                   {I}                    rOS        δrS



                       O

                         Figure 3.2: Kinematics of a single body

   A body with mass existing in 3D Cartesian space, as shown in Fig. 3.2, is very
simply a large number of particles closely placed together to form a single rigid body.
Each infinitesimal point-mass dm is subject to the motion of the total body and hence
can be assigned an absolute position and velocity at any instant in time. Lets now
consider another point S on the body, such that we can define the relative position ρ of
dm w.r.t. the point S.




                                               61
    Thus one can then use the rigid body kinematics formulation introduced in sec-
tion 2.7 to describe the motion an arbitrary point-mass dm defined on the body B via
another body point S:


   r = rOS + ρ                                                                        (3.5)
                                    
                                  vs
   ṙ = vS + Ω × ρ = I3×3 − [ρ]×                                                      (3.6)
                                     Ω
                                                 
                                               as
   r̈ = aS + Ψ × ρ + Ω × (Ω × ρ) = I3×3 − [ρ]×      + [Ω]× [Ω]× ρ                     (3.7)
                                                 Ψ

Where, rOS is the absolute position of body point S, ρ is the relative position of dm
w.r.t S, and vS , Ω, aS , and Ψ are the absolute velocities and accelerations of point S.
Applying (3.4) to (3.5), we get the expression for the virtual displacement of the body
element dm:
                                                               
                                                             δrs
                    δr = δrS + δΦ × ρ = I3×3 − [ρ]×                                 (3.8)
                                                                δΦ
    and δΦ is the variation of the infinitesimal rotation of the local body-fixed frame
defined at S and describes all constraint-compatible changes in orientation of the local
frame at S. Note the bold face over the entire quantity of δΦ; this is due to the fact that
the variation is not taken w.r.t. an orientation quantity, just like angular velocity is not
the result of time-differentiating an orientation.

3.2.4    Virtual Displacement of Multi-Body Systems
Multi-body systems can only exhibit motions that are compatible with the constraints
enforced by the joints, which limit the relative motion between links. As we have seen
section 2.8, the motion is typically described using generalized coordinates q:
                                 
                                vs       J
                                      = P q̇                                     (3.9)
                                Ω         JR
                                                
                                as       JP         J̇
                                      =        q̈ + P q̇                        (3.10)
                                Ψ         JR        J̇R
Again applying (3.4) to (3.9) and (3.10), the concept of virtual displacements now
becomes relevant to multi-body systems, and implies that virtual displacements that
are consistent with the joints must have the form:
                                     
                                     δrs       J
                                           = P δq                            (3.11)
                                     δΦ        JR

3.2.5    Principle of Virtual Work
A fundamental principle in mechanics is the principle of virtual work which describes
the fact that configuration constraints actually define forces which do not perform work
in the direction of the virtual displacements. For a constraint force Fc applied at
point rc , contributed by an arbitrary joint, and equally onto the relevant bodies (action-
reaction principle), the principle of virtual work states that:
                                   δW = δrTc · Fc = 0                                (3.12)

                                            62
    We can extend this further by considering again an infinitesimal dm in a body B. By
also considering d’Alambert’s Principle describing dynamic equilibrium for particles,
the virtual work integrated over the entire geometry of body B becomes:
                             Z
                     δW =       δrT · (r̈dm − dFext ) = 0, ∀ δr                   (3.13)
                               B

Where the quantities are defined as follows:


             dm          infinitesimal mass element
             dFext       external forces acting on element dm
             r̈          acceleration of element dm
             δr          virtual displacement of dm
             B           Body system containing infinitesimal particles dm

    Thus the virtual work is zero for all displacements δr, those changes in configura-
tion which are consistent with the constraints of the system. Although this formulation
might seems somewhat complicated, it will become clearer in the continuation that it
describes most of the well know concepts in a quite compact and well understandable
manner.


3.3       Newton-Euler Method
3.3.1     Newton-Euler for Single Bodies
Evaluating the principle of virtual work (3.13) for a single body results to:
            Z        T                                                         
                  δrs      I3×3                   as                2
0 = δW =                             I3×3 − [ρ]×           dm + [Ω]× ρdm − dFext
              B δΦ         [ρ]×                       Ψ
      T Z         "                      #                            !               !
                                      T                         2
       δrs            I3×3 dm      [ρ]× dm     as           [Ω]× ρdm               dFext
  =                                    2             +             2       −
       δΦ       B     [ρ]× dm − [ρ]× dm        Ψ         [ρ]× [Ω]× ρdm          [ρ]× dFext
                                                                                  (3.14)
Please note that this formulation must hold for arbitrary virtual displacements as there
are no active constraints from joints or contacts. Knowing the computation rule a ×
(b × (b × a)) = −b × (a × (a × b)) and introducing
                                Z
                                    dm =: m       body mass                       (3.15)
                               Z B
                                  ρdm =: 0        since S = COG                   (3.16)
                                B
    Z                  Z
            2                     T
       − [ρ]× dm =       [ρ]× [ρ]× dm =: ΘS       Inertia matrix around COG (3.17)
      B                  B

we get
                     T                                                     
                δrs        I3×3 m 0    as       0        Fext                       δrs
0 = δW =                                  +           −                          ∀        .
                δΦ           0    ΘS   Ψ    [Ω]× ΘS Ω    Text                       δΦ
                                                                                 (3.18)

                                           63
In order to define the laws of conservation of linear and angular momentum we intro-
duce the definitions:

        pS = mvS                           linear momentum                         (3.19)
     N S = ΘS · Ω                          angular momentum around COG             (3.20)
        ṗS = maS                          change in linear momentum               (3.21)
     ṄS = ΘS · Ψ + Ω × ΘS · Ω             change in angular momentum              (3.22)

A free moving body needs to fulfill that the change in linear momentum equals the sum
of all external forces
                          T                               
                           δrs           ṗS       Fext           δrs
                0 = δW =                       −               ∀      ,         (3.23)
                           δΦ            ṄS       Text           δΦ

which results in the well-known formulations by Newton and Euler:

                                      ṗS = Fext,S                                 (3.24)
                                     ṄS = Text                                    (3.25)

where Fext,S are the resultant external forces that act through the COG and Text are the
resultant external torques. External forces which do not act through the COG need to
be shifted to an equivalent force/moment pair of which the force acts through the COG.
Please note again that for numerical calculation, the terms of the change in linear and
angular momentum must be expressed in the same coordinate system. For the inertia
tensor Θ we must apply B Θ = CBA · A Θ · CTBA .


3.3.2     Newton-Euler for Multi-Body Systems
When dealing with multi-body systems, a valid approach is to separate all bodies at the
joints as depicted in Fig. 3.3 and to consider every body as a single unit. Thereby, the
constraint forces Fi at the joints must be introduced as external forces acting on each
of the bodies when cut free. For all these bodies, we must then apply conservation
of linear (3.24) and angular momentum (3.25) in all DoFs, subject to external forces
(which now include the joint forces Fi , too). For a general 3D case and a fixed base,
this results in a 6 nj -dimensional systems of equations. Additionally, there are 5 nj
motion constraint due to the ideal joints. They ensure that the two connected bodies
only move along the direction of the joint but don’t move in all other directions that are
blocked by the joint.
    Many simulation packages build upon such formalism and enforce the joint motion
constraints using hard or soft constraints. The latter method often speeds up simula-
tion due to the type of solvers that can be applied. However, it fulfills the ideal joint
constraints only approximately, which can lead to physically inconsistent phenomena
in simulation.
    When solving such a system by hand, the approach is to describe the motion only
as a function generalized coordinates. This still leads to 6 nj equations (3 nj for planar
systems) but ensures already the ideal joint constraints. The 6 nj equations linearly
depend on nj generalized coordinates as well as on the 5 nj joint constraint forces.
Algebraic manipulation of the system of equations allows to eliminate all constraints
forces.

                                           64
                                                            Fi2
                                       Ψi   Ωi


                                 aSi
                        vSi

                Fi1


                                       Fg
                                                  rOSi




    Figure 3.3: Free-cut of multi-body system with constraint forces due to joints


   Example 3.3.1: Cart-Pendulum with Newton-Euler




3.4     Lagrange Method
3.4.1    Introduction
Another common approach for deriving the equations of motion of a system is that
of using the so-called Lagrange Method. It originates from the sub-field of physics
known as Analytical Mechanics [1][4], and is closely tied to both the d’Alembert and
Hamilton principles, as it is one of the analytical methods used to describe the motion
of physical systems. The method is centered around three fundamental concepts:

   1. The definition of generalized coordinates q and generalized velocities q̇, which
      may or may not encode the information regarding the constraints applicable to
      the system.
   2. A scalar function called the Lagrangian function L. For mechanical systems, it
      is exactly the difference between the total kinetic energy T and the total potential
      energy U, of the system at each instant:

                                            L=T −U                                 (3.26)

   3. The so-called Euler-Lagrange equation, also known as the Euler-Lagrange of the
      second kind, which applies to the Lagrangian function L and to the total external

                                            65
        generalized forces τ :
                                                                        
                                         d        ∂L                  ∂L
                                                             −                 =τ                (3.27)
                                         dt       ∂ q̇                ∂q

    In the most general case, the Lagrangian is a function of the generalized coordinates
and velocities q and q̇, and it may also have an explicit dependence on time t, hence
we redefine the aforementioned scalar energy functions as T = T (t, q, q̇) and U =
U(t, q), thus L = L(t, q, q̇).
    In the end, one of the most notable properties of this formulation is the capacity to
eliminate all internal reaction forces of the system from the final EoM, in contrast to the
Newton-Euler formulation where there they are explicitly accounted for. To apply this
method to derive EoM of a complex multi-body system, there are additional aspects
which must be considered. These are presented in a concise overview at the end of this
section, and are explained in the immediate continuation.


3.4.2     Kinetic Energy
The kinetic energy of a system of nb bodies is defined as:
                        nb 
                        X                                                                   
                             1                         1
                  T =                miA ṙTSi A ṙSi + B ΩTSi · B ΘSi · B ΩSi                   (3.28)
                        i=1
                                 2                            2

For every body Bi in the system, although the linear part may be computed while
expressed in some frame A, it may be more convenient to compute the rotational kinetic
energy using expressions in another frame B, rotated w.r.t to A, where the inertia matrix
ΘS,i may have a diagonal form, i.e. the basis vectors of B are principle w.r.t. the
mass distribution. This computation will yield correct results as long as both linear
and angular velocities A ṙS,i and B ΩS,i express the absolute velocities of the body, i.e
velocities w.r.t. to the inertial frame.
    We now need to express the kinetic energy as a function of the generalized quanti-
ties. To achieve this, we make use of the Jacobian matrices described by (2.163) and
(2.164), but computed for each body Bi instead of the end-effector. This then allows
us to use the following kinematic relationships:

                                               ṙSi = JSi q̇                                     (3.29)
                                              ΩSi = JRi q̇                                       (3.30)

Replacing these relationships into the definition of the kinetic energy in (3.28), results
in the kinetic energy expressed in the generalized coordinates:
                                             nb
                                                                                        !
                             1               X                                      
                  T (q, q̇) = q̇T                   JTSi mJSi + JTRi ΘSi JRi                q̇   (3.31)
                             2               i=1
                                         |                            {z                }
                                                                  M(q)


The underlined quantity M(q) is defined as the generalized mass matrix or generalized
inertia matrix, and as we will see in the continuation, is solely responsible for gener-
ating both the inertial and non-linear centrifugal and Coriolis force terms in the final
EoM.

                                                         66
3.4.3    Potential Energy
In typical mechanics problems, there are two basic contributions to the potential energy
in a system; masses contributing via their gravitational potential energy, and elastic
elements via the energy stored when deflected from rest.
    In the first case, each body Bi holds potential energy due to the effect of the gravita-
tional potential field of the earth. Although not linear on large scales, in most cases we
approximate its effect on bodies via a uniform and unidirectional potential field defined
along the unit vector I eg acting through the CoM of each body. Knowing the position
rSi of the CoM of each body This then allows us to compute the potential energy of
each body as:
                                      Fgi = mi g I eg                                 (3.32)
                                            nb
                                            X
                                   Ug = −         rTSi Fgi                           (3.33)
                                            i=1

Note that the zero energy level can be arbitrarily chosen. In addition to gravitational po-
tential energy contributions, many applications involve elastic elements such as springs
or other compliant components. If such a element Ej can be reasonably approximated
to have a linear deflection-to-force or deflection-to-torque relationship, then the poten-
tial energy contribution can be described by the following relation:

                                         1                2
                                U Ej =     kj (d(q) − d0 )                           (3.34)
                                         2
Where d(q) expresses the instantaneous configuration of the elastic element (e.g. the
length of a spring) as a function of generalized coordinates. d0 is defined as the rest
configuration where no forces are exerted by the element, e.g., the unsprung length of
a linear spring. We call the difference (d(q) − d0 ) the deflection of the elastic element.
     Note: Spring forces may equivalently be considered as external forces whose mag-
nitude and possibly direction depends on the generalized coordinates q. The formalism
is similar to introducing actuator torques.


3.4.4    External Forces
All external forces that do work on the system are accounted by the generalized force
vector τ . Please refer to section 3.5.3 for a derivation.


3.4.5    Additional Constraints
The final case we have to account for is that of when additional constraints are imposed
on the system. When we define generalized coordinates, in most cases, we aim to
describe the system using a minimal set of coordinates so that we can express the the
DoFs which we can control or at least measure.
Consider the case presented in section 2.10.4, when contact constraints are imposed on
a floating-based system. These constraints may not be active at all times, e.g., as in the
case of a walking robot or a ball bouncing on a table. Such a contact constraint cannot,
in general, be explicitly accounted for when we defining the vector q since it may not
always apply on the system. The most common way to overcome this to use Lagrange
Multipliers, usually denoted by a vector λ. Constraints which are explicitly defined

                                            67
using velocities, are known as motion constraints and are usually expressed as linear
combinations of the general velocities:
                      nq
                      X
                            ak,j (q) q̇k + a0,j (t),    j = 1, 2..nc,m             (3.35)
                      k=1

For nc,m motion constraints, we can stack all ak,j (q) coefficients to a motion constraint
Jacobian matrix Jm :                                      
                                    a1,1 . . . a1,nc,m
                                                          
                           Jm =  ...       ...
                                                       ..
                                                        .                         (3.36)
                                       anq ,1    ...   anq ,nc,m
On the other hand, there are situations where constraints will be defined as functions
of the configuration, i.e. as scalar functions fj (q) : Rnq → R, and are known as
configuration constraints. In these cases, computing the gradient of such a function
w.r.t the generalized coordinates results in the constraint Jacobian matrix described in
section 2.10.4.
     In total, incorporating these constraints results in a description of the constrained
EoM, since the additional constraints being applied for by the parameters λ are not
account for in the definition of q. Thus the final EoM, are derived using the so-called
Constrained Euler-Lagrange (CEL) equation, also known as the Euler-Lagrange of the
first kind:
                                                         T
                    d ∂L           ∂L         T           ∂fc
                               −         + Jm λ m +               λc = τ            (3.37)
                   dt ∂ q̇          ∂q                    ∂q
    Where λm ∈ Rnc,m is the vector of Lagrangian multipliers for the motion con-
straints, while λc ∈ Rnc,c is the vector of Lagrangian multipliers for the configuration
constraints.
    In conclusion, we note that it should be clear why this method is also referred to
as being energy-based, as the equations of motion are derived from a scalar energy
function, and thus, we did not make explicit use of any Cartesian vector quantities. All
the kinematic information is encoded into the definition of the generalized coordinates,
which are then used to define the scalar Lagrangian, and then applied to (3.27) in order
to produce the EoM. This is in stark contrast to Newton-Euler methods which explicitly
deal with Cartesian vector quantities.


3.5     Projected Newton-Euler Method
3.5.1    Introduction
The final method we will describe for deriving EoM of multi-body systems is that
which makes use of the Projected Newton-Euler (PNE) formulation. Essentially, this
method combines the classical Newton-Euler equation for dynamic equilibrium in
Cartesian coordinates, with the constraint compliant Lagrange formulation using gen-
eralized coordinates. In fact, as we will see in the continuation, one can derive the PNE
equations from both of the other two formulations.
    Let us briefly recapitulate what the resulting EoM using PNE will look like:

                       M (q) q̈ + b (q, q̇) + g (q) = τ + JTc Fc                   (3.38)

                                                68
3.5.2     Deriving Generalized Equations of Motion
As outlined in section 3.2.4, the use of generalized coordinates allows to describe the
motion and virtual displacements of bodies in ways which are consistent with the ap-
plicable constraints. Thus, we can rewrite principles of linear and angular momentum
applied to each body Bi as:
                                                 
           ṗSi                   maSi
                  =
           ṄSi        ΘSi ΨSi + ΩSi × ΘSi ΩSi
                                                                             (3.39)
                        mJSi                         mJ̇Si q̇
                  =              q̈ +
                       ΘSi JRi          ΘSi J̇Ri q̇ + JRi q̇ × ΘSi JRi q̇
Furthermore, using the expressions for virtual displacements of generalized coordi-
nates, we can rewrite the principle of virtual work as follows:
             Xnb        T                                    
                    δrSi         ṗSi        Fext,i               δrs
 0 = δW =                               −                    ∀                   , (3.40)
                   δΦSi          ṄSi        Text,i              δΦSi consistent
             i=1
                  Xnb       T                   
                T        JSi      ṗSi         Fext,i
           = δq                           −                  ∀δq                   (3.41)
                        JRi       ṄSi         Text,i
                         i=1

Combining (3.39) and (3.41) directly yields:
     Xnb      T                   T                                         T        
           JSi      mJSi          JSi                  mJ̇Si q̇                 JPi      Fext,i
0=                           q̈+                                             −
           JRi     ΘSi JRi        JR i     ΘSi J̇R q̇ + JRi q̇ × ΘSi JRi q̇     JR i     Text,i
     i=1
                                                                                   (3.42)
A final re-grouping of terms results in the components of (3.38):
                  n
                  X b
                                                        
         M=               JTSi mJSi + JTRi ΘSi JRi                                            (3.43)
                  i=1
                  Xnb                                                    
          b=              JTSi mJ̇Si q̇ + JTRi ΘSi J̇Ri q̇ + ΩSi × ΘSi ΩSi                    (3.44)
                                                                                     i
                  i=1
                  Xnb
          g=             −JTSi Fg,i                                                           (3.45)
                   i=1

    Again, we must stress the importance of selecting an appropriate choice of coordi-
nate frame to express all Cartesian vectors. We apply the same reasoning as we did in
computing the kinetic energy in section 3.4.2, where, we stated that both angular and
linear velocities must be absolute, i.e., measured w.r.t an. inertial frame. It does not
matter then if linear and angular are expressed differently, however, an careful selection
can simplify the final expressions:
        n
        X b
                 T                   T
                                                                
M=            A JSi · m · A JSi + B JRi · B ΘSi · B JRi                                       (3.46)
        i=1
        Xnb                                                                                         
                   T                         T
 b=             A JSi · m · A J̇Si · q̇ + B JRi ·       B ΘSi · B J̇Ri · q̇ + B ΩSi × B ΘSi · B ΩSi
        i=1
                                                                                              (3.47)
        n
        X b
                               
 g=           −A JTSi A Fg,i                                                                  (3.48)
        i=1


                                                    69
3.5.3    External Forces & Actuation
As we have seen in section 3.4.4, in order to account for external forces in EoM ex-
pressed in generalized coordinates, we can project Cartesian forces and torques onto
the space of generalized coordinates using appropriate Jacobian matrices. The latter
project the effect of the forces onto the subspace of the generalized coordinates on
which work is done. We will now consider how to effectively account for all acting
forces and torques on a multi-body system.
    Lets assume we know that nf,ext external forces Fj , j ∈ {1, . . . , nf,ext } and
nm,ext external torques Tk , k ∈ {1, . . . , nm,ext } act on the system (on any body). The
generalized forces τF,ext due to the external forces can be calculated in the following
way: Assume the Cartesian force Fj acts on point Pj and the translational Jacobian of
that point is JP,j . Then the generalized forces are computed as
                                          nf,ext
                                            X
                               τF,ext =            JP,j T Fj .                     (3.49)
                                            j=1

Similarly, the generalized forces τT,ext can be evaluted by projecting each Cartesian
torque by the rotational Jacobian of the body they act on, which we shall call JB,k,rot :
                                       nm,ext
                                        X
                            τT,ext =            JR,k T Text,k .                    (3.50)
                                        k=1

Finally, the contributions of external forces and torques can simply be added as they
are both represented in the space of generalized coordinates:

                                τext = τF,ext + τT,ext                             (3.51)

    For the special case of actuator forces or torques that act between two body links,
we need only consider the kinematic relations defined between those two (successive)
body links. Thus, an actuator acting between body links Bk−1 and Bk , imposes a
force Fa,k and/or torque Ta,k on both equally and in opposite directions, i.e., action-
reaction. What thus need to compute are the Jacobian matrices to appropriately project
onto the dimensions of q.
    To this end, we recall that Jacobian matrices, when expressed in the same refer-
ence frame, can be simply added or subtracted, and thus having computed JSk−1 , JSk ,
JRk−1 , and JRk from our previous analysis of the kinematics, we can compute the
contribution of the actuators to the generalized forces as:
                                       T                         T
               τa,k = JSk − JSk−1           Fa,k + JRk − JRk−1         Ta,k        (3.52)

In the most simple, and in fact also the most common, case of an actuator acting in
the direction of a generalized coordinate qj , the difference between the Jacobian at the
point of action and reaction multiplied with the force or torque provides the single entry
in the generalized force vector τj . Thus, the vector of total external generalized forces
is simply a combination of the aforementioned parts, accounting for nA joint actuators
and nB body links:
                                       XnA
                                  τ =       τa,k + τext                             (3.53)
                                       k=1

   Comments:

                                             70
    • The translational Jacobian of an arbitrary point on a body can be obtained by
      starting with the translational Jacobian of the CoM of that body and applying
      (2.154).

    • Alternatively, one may transform all forces that do not act through the CoM of
      a body into an equivalent force/moment pair which allows usage of the CoM
      translational and rotational Jacobians.

    • Actuator forces/torques are no different to any other external forces/torques ex-
      cept that both the torque/force and its reaction act on the system.


3.6     Summary and Relation between Methods
When looking at three methods, we can identify

    • All need definition of generalized coordinates

    • All of them need Jacobians of CoGs

    • Evaluate one or the other equation

    To check correctness of the implementation, it can help to observe the time evolu-
tion of the total energy (Hamiltonian H)

                                     H=T +U .                                     (3.54)

In absence of friction, actuation, and external forces the total energy in the system
should remain constant.


3.7     Dynamics of Floating Base Systems
                   M (q) u̇ + b (q, u) + g (q) = ST τ + JText Fext                (3.55)
consisting of the following components:

 M (q)       ∈ Rnq ×nq    Mass matrix (orthogonal)
 q           ∈ Rn q       generalized coordinates
 u           ∈ Rn q       generalized velocity
 u̇          ∈ Rn q       generalized acceleration
 b (q, u)    ∈ Rn q       Coriolis and centrifugal terms
 g (q)       ∈ Rn q       gravitational terms
 S           ∈ Rnτ ×nq    selection matrix of actuated joints
 τ           ∈ Rn τ       generalized torques acting in direction of generalized coordinates
 Fext        ∈ Rn c       external forces acting
 Jext        ∈ Rnc ×nq    (geometric) Jacobian of location where external forces apply
As we have seen in section 2.10, the generalized coordinates of a floating base systems
consist of actuated joint coordinates qj and unactuated base coordinates qb respec-
tively the corresponding velocities uj = q̇j ∈ Rnj and ub ∈ R6 . Please note again
at this place that ub is not equal to the time derivative of the position and orientation

                                           71
Figure 3.4: In soft contact model, the contact force is modeled as a spring-damper force


parameterization q̇, since no angular position exists but only different ways of param-
eterizing the orientation. The selection matrix S selects the actuated joints according
to                                                            
                                    ub                       ub
                   uj = Su = S           = 06×6        I6×nj                      (3.56)
                                    uj                           uj
In order to control also the unactuated base coordinates qb , external forces Fext are
necessary. Depending on the type of robot, they can come from very different sources.
For example, this force can originate from contacts (interaction) with the environment
(e.g. legged robots) or from aerodynamics (e.g. flying robots). In many text books
and in particular when working with contact forces (e.g. legged robots), people use the
alternative notation

                    M (q) u̇ + b (q, u) + g (q) + JTc Fc = ST τ ,                (3.57)

with Fc representing a force that the robot exerts on its environment.


3.7.1    Contact Forces
There exist two fundamentally different methods to model contact forces. The soft
contact method models the interaction by force elements (i.e. spring-damper) where
the force is only a function of the location and velocity of the point in contact. The
hard contact method treats the contact as a kinematic constraint.

Soft Contact Model
For the soft contact model, we typically identify the point when first making contact
with the environment as rc0 . When using a liner spring-damper model for the environ-
ment, the contact force (exerted by the robot on its environment) is

                             Fc = kp (rc − rc0 ) + kd ṙc .                      (3.58)

While modeling the environment like this seems logic and physically correct from a
first point of view, it turns out that finding physically correct spring and damping pa-
rameters to simulate the system dynamics is almost impossible. One of the big prob-
lems is that the combined differential equations for multi-body system and contacts
become very stiff (slow multi-body dynamics and very fast contact dynamics). Solving
such problems either result in poor speed or low accuracy. To overcome this problem,
the contact parameters for stiffness and damping are often tuned as numerical simula-
tion parameters that have nothing to do with the actual physical parameters.

                                          72
Contact Forces from Constraints

Instead of contact forces resulting from force elements at the contact, contacts can also
be handled as kinematics constraints. If a point C with position rc is in contact, it is
not allowed to move anymore:

                                 rc = const                                        (3.59)
                                 ṙc = Jc u = 0                                    (3.60)
                                 r̈c = Jc u̇ + J̇c u = 0                           (3.61)

The same formulation can be made for rotational constraints in case of and extended
contact area. From the constraint (3.61) and the equation of motion (3.57) we can
identify the contact force:
                                  −1                              
               Fc = Jc M−1 JTc            Jc M−1 ST τ − b − g + J̇c u              (3.62)

This is of great benefit as it provides direct access to estimated ground reaction forces
solely based on the description of the multi-body system dynamics and without any
further contact force sensor.


3.7.2    Constraint Consistent Dynamics
We can define the dynamically consistent support null-space matrix as
                                                           −1
                        Nc = I − M−1 JTc Jc M−1 JTc              Jc .              (3.63)

Nc defines a generalized space of motion with no acceleration or force coupling effects
on the supporting links. Substituting the solution for the contact force (3.62) into the
equation of motion (3.57) results in
                                                     −1
              Mu̇ + NTc (b + g) + JTc Jc M−1 JTc           J̇c u = NTc ST τ .      (3.64)

By further including the support constraint (3.61) which implies J̇c u = −Jc u̇, the
constraint consistent equations of motion can be compactly formulated as

                            NTc (Mu̇ + b + g) = NTc ST τ .                         (3.65)


3.7.3    Contact Switches and Impact Collisions
A hard contact model requires subdividing the analysis of the system dynamics into
two intervals, before and after a change in the contact situation respectively an impact.
The impact itself is a complex physical phenomenon which occurs when two or more
bodies collide with each other. The characteristic of an impact is a very short duration
with high peak forces that results in a rapid dissipation of energy and large acceler-
ations. To model the process of energy transfer and dissipation, various coefficients
are employed, such as the coefficient of restitution and the impulse ratio. Idealizing the
process, respectively considering the impact as an infinitesimally short process requires
to include instantaneous changes in velocities if bodies are making contact.

                                            73
Impulse Transfer
To resolve the contact impulse, we use the integrated equation of motion over a single
point in time t0
   Z
                                                            
           Mu̇ + b + g + JTc Fc − ST τ dt = M u+ − u− + JTc Fc = 0, (3.66)
     {t0 }

with the impulsive force Fc and the pre- respectively post-impact generalized velocities
u− and u+ . Assuming a perfect inelastic collision with a Newtonian collision law,
all contact points that are considered part of the collision instantaneously come to rest
(ṙ+        +
   c = Jc u = 0). Combining this post-impact constraint with the integrated equation
of motion, we can solve for the impulsive force as
                                            −1
                         Fc = Jc M−1 JTc          Jc q̇− = Λc ṙ−
                                                                c .                 (3.67)

Analyzing this formalism a bit more in detail by considering the basic mechanics that
defines impulse = mass · speed, we identify the inertia that is seen at the support
point as the so called end-effector inertia:
                                                      −1
                                 Λc = Jc M−1 JTc                                    (3.68)

Substituting (3.68) into (3.67) yields the instantaneous change in generalized velocities:
                                                               −1
                 ∆u = u+ − u− = −M−1 JTc Jc M−1 JTc                   Jc u− .       (3.69)

Using again the nomenclature introduced previously for the dynamically consistent
support null-space projector Nc , the post-impact generalized velocities are determined
by                                              −1  −
               u+ = I − M−1 JTc Jc M−1 JTc           Jc u = Nc u− .               (3.70)

The result that is obtained by satisfying the post impact contact constraint is intuitively
clear: Using the support null-space projector Nc , the pre-impact velocity u− is pro-
jected onto the support consistent manifold.

Energy Loss
The instantaneous change in the contact situation is always associated with a kinetic
energetic loss. This can be quantified in generalized coordinates or as a function of the
end-effector inertia and the change in velocity at the support point by

                 Eloss = ∆Ekin = − 21 ∆uT M∆u                                       (3.71)
                                   = − 21 ∆ṙTc Λc ∆ṙc = − 21 ṙ−T     −
                                                                 c Λc ṙc .         (3.72)




                                            74
3.8     Joint-space Dynamic Control
Current industrial robots rely almost exclusively on the concept of joint position con-
trol. They build upon PID controllers to independently regulate the position or velocity
of every joint of the robot. Such a controller compensates for disturbances in the ac-
tuators and the entire robot and leads in the ideal case to perfect tracking of a desired
motion. Only by additionally sensing of the joint torque (e.g., by measuring it with
a load cell or by estimating it from motor current and actuator models) it becomes
possible to integrate model-based load compensation.

3.8.1    Joint Impedance Regulation
In case of torque controllable actuators, the joint feedback gains for joint position kp
and velocity kd correspond to joint stiffness and damping and the desired actuator
torque can be calculated as
                           τ ∗ = kp (q∗ − q) + kd (q̇∗ − q̇) ,                       (3.73)
with q∗ and q̇∗ representing the desired joint position and velocity, respectively. When
applying this control law to the robot arm, we get a steady-state tracking error:
                    :0
                   ∗      :0
             M(q)
                q̈   +
                       b  q̇) + g (q) = kp (q∗ − q) + kd (q̇∗ − q̇)
                        (q,
                            
                                                                                    (3.74)

Gravity Compensation
In order to compensate for steady-state offset and to adjust the joint impedance, a
common approach is to select the desired actuator torque as
                      τ ∗ = kp (q∗ − q) + kd (q̇∗ − q̇) + ĝ (q) ,                   (3.75)
with ĝ (q) representing the estimated gravity effects. Unfortunately, since the inertia
seen at each joint varies with the robot configuration, the PD gains must be selected
for some average configuration in the workspace. This reduces the performance when
dynamic effects become significant. There is still a steady-state error, because the
model is never perfectly accurate.

Inverse Dynamics Control
A simple way to get around these short-comings is to implement an inverse dynam-
ics control method. Thereby, dynamic decoupling and motion control is achieved by
selecting the joint torque as
                          τ ∗ = M̂ (q) q̈∗ + b̂ (q, q̇) + ĝ (q) ,                   (3.76)

where M̂ (q), b̂ (q, q̇), and ĝ (q) represent the estimates of M (q), b (q, q̇), and g (q).
In case of a perfectly modeled plant, the closed-loop dynamics of the system (3.1) with
control (3.76) results in
                                          Iq̈ = q̈∗ .                                 (3.77)
In other words, this method allows to directly shape the decoupled dynamics of every
joint. Similar to the impedance law introduced in (3.73), a common approach is to
select the desired acceleration according to
                           q̈∗ = kp (q∗ − q) + kd (q̇∗ − q̇) ,                       (3.78)

                                            75
which corresponds to a linear mass-spring-damper system with unitary mass. As a
great benefit, the tuning and selection of feedback gains kp and kd becomes intuitively
clear since they represent physical parameters of a decoupled point mass oscillator.
Hence, the eigenfrequency and a dimensionless damping value of the system are given
by
                                                p
                                           ω= kp ,                                                 (3.79)
                                              kd
                                           D= p .                                                  (3.80)
                                             2 kp

Critical damping is achieved for D = 1, overcritical damping for D > 1 and un-
dercritical damping for D < 1. The compliance of the controller can be adjusted
by varying kp . For example, assuming that the time constant respectively oscillation
frequency around the nominal point should be 3 Hz, the ideal control gain kp is 350.
Furthermore, critical damping requires kd = 37. This holds as good starting values for
controller gain tuning.



3.9      Task-space Dynamics Control
So far we have only considered model-based joint space control. However, in most
situation, we want to move a specific point in task-space, i.e., in world-fixed frame.
The linear and rotational acceleration of the end-effector e (or any other point and link)
is coupled to the generalized accelerations through the geometric Jacobians:
                                          
                                          r̈
                                   ẇe =       = Je q̈ + J̇e q̇.                                   (3.81)
                                          ω̇ e


3.9.1    Multi-task Decomposition
Similar to the kinematic multi-tasks control outlined in section 2.9.2, we can perform
inverse dynamics while fulfilling multiple tasks. Given a set of motion objectives by
the desired task space acceleration and the corresponding Jacobian, we can treat all
goals with the same priority:
                                       +         
                                    J1        ẇ1    J̇1
                                    ..   ..   ..  
                              q̈ =  .   .  −  .  q̇                                        (3.82)
                                    J nt        ẇnt         J̇nt

   In case some tasks have higher priority, we can determine the solution using a
similar recursive algorithm as outlined in (2.207):

             nt                                                           i−1
                                                                                         !
             X                                   +
                                                                          X
      q̈ =         Ni q̈i ,   with q̈i = (Ji Ni )      wi∗ − J̇i q̇ − J         Nk q̇k       ,     (3.83)
             i=1                                                          k=1

                                                                                                          T
whereby Ni is the null-space projection of the stacked Jacobian J̄i = JT1                    ...   JTi−1        .

                                                76
3.9.2     End-effector Dynamics
An interesting method for analysis and control description is to have a look at the end-
effector dynamics. To this end we can solve (3.1) for q̈, insert into (3.81):

                         ẇe = Je M−1 (τ − b − g) + J̇e q̇.                      (3.84)

Substituting the joint torque with the end-effector force pre-multiplied with the Jaco-
bian transposed
                                      τ = JTe Fe                                 (3.85)
yields the end-effector dynamics

                                Λe ẇe + µ + p = Fe ,                            (3.86)

whereby
                                                  −1
                             Λe = Je M−1 JTe                                     (3.87)
                                            −1
                              µ = Λe Je M        b − Λe J̇e q̇                   (3.88)
                                            −1
                              p = Λe Je M        g                               (3.89)

represent the end-effector inertia, centrifugal/Coriolis, and gravitational terms in the
task space. For more details, the interested reader is referred to [5].


3.9.3     End-efector Motion Control
Similar to joint-space inverse dynamics control, we can use the task-space equations of
motion in inverse form to define the desired joint torque. Combining (3.85) and (3.86)
results in                                              
                             τ ∗ = ĴT Λ̂e ẇe∗ + µ̂ + p̂ .                      (3.90)

We use this formalism together with control strategy for the desired acceleration ẇ∗
such as e.g.:
                                ∗      
                        ∗       re − re
                     ẇe = kp              + kd (we∗ − we ) .                  (3.91)
                                  ∆φe
Please note that we use ∆φe to represent the end-effector rotation error. Remember
that, for rotation errors, we can not simply subtract two rotations but need follow the
procedure introduced in section 2.9.3. For small errors we can make use of the error-
approximation
                          ∗                   ∗         
                           re − re       I   0       r −r
                                     =                          ,                 (3.92)
                            ∆φe          0 ER χ∗R − χR
whereby the matrix ER (χ) is used due to the different methods of rotation parametriza-
tion.

Alternative Notation
In many papers you will find the expression Λ = J−T        −1
                                                    e MJe although Je is not neces-
sarily invertible. However, this simplifies algebraic manipulation of the equations. In

                                          77
fact, (3.90) can be straight forward simplified to

 τ ∗ = JT (Λe ẇe∗ + µ + p)                                                        (3.93)
     =J   T
              Λe ẇe∗ + JT J−T  −1
                            e MJe Je M
                                      −1
                                         b − JT Λe J̇e q̇ + JT J−T  −1
                                                                e MJe Je M
                                                                          −1
                                                                             g
                                                                                   (3.94)
     =J   T
              Λe ẇe∗ + b − JT Λe J̇e q̇ +g                                        (3.95)
                       |         {z   }
                                 b̃

     =J   T
              Λe ẇe∗ + b̃ + g                                                     (3.96)

The following operational space formulation can be equally written in this formulation.

3.9.4    Operational Space Control
There exist many situations where the robot should apply a force in some directions
while it needs to move in other directions. An example is cleaning a window, whereby
the robot applies a specific pressure force in normal direction and controls the motion
in all other directions. Another example would be inserting a pin into a hole: Whereby,
the pin should be moved in direction of the pin and should not rotate round the main
axis of the pin, while the forces and moments around the two other axis should be
kept zero. In order to achieve this, we make use of so-called operational space control.
Following the work of Khatib [5], we can define selection matrices SM and SF for the
motion and force directions, yielding the combined control problem
                                                              
                         τ ∗ = ĴT Λ̂SM ẇe + SF Fc + µ̂ + p̂ .                   (3.97)

Following [5], we can define specification matrices for position and orientation
                                                                    
                      σpx     0     0                 σrx      0    0
              Σp =  0 σpy          0       Σr =  0 σry           0           (3.98)
                       0      0 σpz                     0      0 σrz

where σi are binary numbers assigned the value 1 when a free motion is specified along
(linear) or around (rotation) specific axis, and zero otherwise. In case the contact force
coordinate frame is rotated with respect to the inertial frame described by the rotation
transformation matrix C, we need to transform the selection matrix. The two selection
matrices SF and SM are then defined as
            T                                  T                                   
            C Σp C          0                    C (I3 − Σp ) C              0
   SM =                                 SF =
                0       C T Σr C                         0           CT (I3 − Σr ) C
                                                                                    (3.99)




                                              78
3.10      Inverse Dynamics for Floating-Base Systems
When working with floating-base systems, we need to perform inverse dynamics while
ensuring that the contact constraints (3.61) are satisfied. Given a desired acceleration
u̇∗consistent , we can invert the constraint consistent equation of motion (3.65):
                                          +
                           τ ∗ = NTc ST NTc (Mu̇ + b + g) .                        (3.100)
                                                          +
Notice that we need to take the pseudo-inverse NTc ST . Recall the multi-task so-
lution from kinematics: depending on the structure of the matrix of which we take the
pseudo-inverse, there exists a null-space that allows to modify τ ∗ :
                         +                                     
           τ ∗ = NTc ST NTc (Mu̇∗ + b + g) + N NTc ST τ0∗ ,                   (3.101)

while the support consistent equation of motion NTc ST τ ∗ = NTc (Mu̇ + b + g) is
still valid. In other words, there exist different joint torque distributions which all lead
to the same motion u̇∗ of the system. In fact, the different torque distributions change
the contact force distribution. In case of multiple contacts, we can create internal forces
between the contacts which does not change the net force and moment on the robot and
hence does not create any additional acceleration. When taking the pseudo-inverse as
in (3.100), the solution is the least square minimal torque τ ∗ that fulfills the constraint
consistent equation of motion.

3.10.1     Quadratic Problems
There exist many approaches that tackle the problem of simultaneously controlling
different operational-space objectives. These tasks involve motion at selected locations
(e.g. end-effector, COG, etc.), desired contact forces, or joint torques.
     A very comprehensive method is to understand operational space control as sequen-
tial least square optimization problem of linear objectives. To prepare for prioritized
task-space inverse dynamics, we introduce in this section the concept of hierarchical
least square optimization of a set of nT linear equations

                                        Ai x = bi ,                                 (3.102)

with the optimization variable x. Problems of the same priority i ≥ 1, with i = 1 being
the highest priority, are stacked in matrix Ai and vector bi . As it will be shown later,
motion tasks as well as joint torque and contact force tasks can be brought into this
linear form whereby the optimization variable is the joint acceleration and joint torque,
respectively. In the proposed hierarchical framework, the goal is to solve each task as
good as possible in a least square sense
                                 min     kAi x − bi k2 ,                            (3.103)
                                   x

without influencing task of higher priority. There exist different methods to solve this
problem such as e.g. iterative null-space projection (section 3.10.2) or as a sequence of
constrained quadratic programs (QP) using standard numerical solvers.

3.10.2     Iterative Null-Space Projection
The requirement that a task is not allowed to influence any task with higher priority
can be formulated by defining x as a sum of task specific xi pre-multiplied with the

                                            79
null-space projection matrix Ni of higher prioritized tasks:
                                           n
                                           X T

                                      x=            Nk xk .                                       (3.104)
                                           k=1
                                                                                      T 
The null-space projector Ni is defined as Ni = N            AT1         ...   ATi−1            with N1 =
I and the sufficient property

                                 Ai Nj = 0             ∀i < j.                                    (3.105)
As we have seen in the kinematics part, there exist different methods for null-space
projector calculation. Using property (3.105), the prioritized minimization problem
(3.103) can be solved for each task individually by inserting (3.104) and solving for
xi :
                                        nT
                                        X
                  Ai x − bi      = Ai         Nk xk − bi                                          (3.106)
                                        k=1
                                                                  i−1
                                                                                !
                                                +
                                                                  X
                          xi     =   (Ai Ni )         bi − Ai           Nk xk       .             (3.107)
                                                                  k=1

The calculation sequence of the optimization procedure is implemented as:


Algorithm 2 Hierarchical Least Square Optimization
  nT = Number of Tasks
  x=0                                                                   . initial optimal solution
  N1 = I                                                            . initial null-space projector
  for i = 1 → nT do
                   +
      xi = (Ai Ni ) (bi − Ai x)
      x = x + Nixi
                                 T 
      Ni+1 = N AT1 . . . ATi
  end for



3.10.3    Sequence of Constrained Optimization
Every single step of the hierarchical least square optimization corresponds to a quadratic
optimization with the linear constraint that tasks of lower priority are not allowed to
change:

                         min         kAi x − bi k2
                          x
                                                     
                                       A1            b1
                                      ..          . 
                          s.t.        .  x −  ..  = c.                                        (3.108)
                                      Ai−1              bi−1
                                     | {z }            | {z }
                                      Âi−1               b̂i−1

Note: As long as Âi−1 has full column rank, the cost c is 0.
This sequence of constrained quadratic optimization can be solved using a standard QP
solver.

                                              80
3.10.4     Task-Space Control for Floating Base Systems as QP
The complex behaviors of robotic systems can be described as multi-tasks control prob-
lems with the optimization variable as stacked vector of generalized acceleration u̇,
contact force Fc , and joint torque τ :
                                             
                                             u̇
                                        x = Fc                              (3.109)
                                             τ

Please note: Our formulation here is for floating base systems using generalized veloci-
ties u, but the approach can be also used for fixed base systems. Using this optimization
variable, the equation of motion Mu̇ + b + g + JTc Fc = ST τ can be formulated as
least square problem with
                                                 
                     A = M̂        ĴTc     −ST         b = −b̂ − ĝ.             (3.110)

To achieve a desired acceleration at a point of interest Ju̇ + J̇u = ẇ∗ , we can simply
define a task                              
                     A = Ĵi                       b = ẇ∗ − J̇ˆu
                                    0     0                      i               (3.111)
There are also many other objectives of interest. In the following we give some exam-
ples but there are many more that can be achieved. In case we would like to push with
a specific force or moment Fi = F∗i at certain location, we can define
                                             
                         A= 0         I      0        b = F∗i                  (3.112)

Moreover, if we want to find a solution that minimizes the overall joint torque, we can
define a task:                                
                          A= 0          0     I      b=0                         (3.113)

    Example 3.10.1: Inverse joint space dynamics as QP

    Given desired accelerations q̈∗ , please formulate joint space inverse dynamics
    control for a fixed base manipulator that is not in contact with the environment.
    Note: this is a purely academic example since solving this problem using the
    optimization approach presented in this section is an overkill.

    Task 1: EoM
                                              
                      A = M̂          0      −I        b = −b̂ − ĝ.            (3.114)

    Task 2: Achieve desired joint space acceleration
                                             
                         A= I         0     0        b = q̈∗ .                  (3.115)




3.11      Quasi-static (Virtual Model) Control
Note: This section is not part of this years lecture but is still provided for the interested
reader.

                                             81
For relatively slow maneuvers, the predominant forces are external loads acting on the
robot. In such situation, we can look at the quasistatic equations of motion which ne-
glect the terms Mq̈ and b (q, q̇). A widely used quasi-static control approach is Virtual
model control (VMC) as introduced by Pratt et al. [6] This method generates desired
joint torques to produce the same effect on the system as if there were external (virtual)
forces Fvi acting at specified locations rvi . To derive a generalized form of VMC for
floating base systems, we apply the principle of virtual work (see section 3.2.5) which
states that variations in work must cancel for all virtual displacements of the multi-body
system. We remember that a virtual displacement at an arbitrary point pi of a floating
base systems can be written as
                                                                         
                                                                   δrb
      δrpi = δrb + δϕb × rbpi + δrbpi = I − [rbpi ]× Jbpi δϕb  ,                 (3.116)
                                                                      δqr

with δrb and δϕb being the variation in position and rotation of the base node b with
                                                                                 T
respect to an inertial frame. The skew-symmetric matrix [rbpi ]× = − [rbpi ]× corre-
sponds to the cross-multiplication matrix [rbpi ]× ϕb = rbpi ×ϕb of the relative position
vector rbpi from base b to point pi . The relative position variation δrbpi = Jbpi δqr is
expressed by a variation in generalized joint coordinates δqr projected by the relative
                  ∂r
Jacobian Jbpi = ∂qbpri . With this parametrization of an arbitrary field of variations the
virtual work generated by external and internal forces results in
                         X
   δW = δqTr τ +               δrTpi Fpi
                           i
                                                                                           
                                      0     X      I                                        δrb
       = δrTb         δϕTb      δqTr  0  +   [rbpi ]×  Fpi  = 0                      ∀ δϕb  ,
                                        τ     i    JTbpi                                      δqr
          X
  →0=           Fp i ,                                                                          (3.117)
            i
          X
  →0=           rbpi × Fpi ,                                                                    (3.118)
            i
                X
  →0=τ+                  JTbpi Fpi ,                                                            (3.119)
                  i
     P           P           P           P
with i Fpi = i Fgi − i Fvi − i Fci representing all external forces such as
the gravitational forces (Fgi ), virtual control forces (−Fvi ), and the contact forces
(−Fci ). Equations (3.117) and (3.118) correspond to the force respectively torque
equilibrium of all external loads and are used to determine the unknown ground contact
forces Fci . In most cases, this is done by a pseudo-inversion according to
        
    Fc1                                             +         P         P           
    ..      I                   ...       I                     Fg i − P Fv i
    .  = [r ]                                          P                               .      (3.120)
             c1 ×                 ...       rcnc ×           rg i × Fg i − rv i × Fv i
    Fcnc

Given all external forces, the desired joint torques are extracted from (3.119):
                                 X                    X                  X
                      τ =−              JTbgi Fgi +        JTbvi Fvi +       JTbci Fci .        (3.121)
                                   i                  i                  i


                                                      82
For simplicity of notation, we avoided the inclusion of external moments τia . They
can
P be    simply added in the formalism with the corresponding rotational Jacobian as
      T   a
    J
  i Ri τ i .




                                        83
84
Appendix A

Matlab Code for Examples

This chapter collects all MATLAB code snippets for the individual examples.


A.1     Multi-task Control
Code for example 2.9.1.

clc
clear all
close all

% define the end-effector jacobian
J_E = @(q) [
    cos(q(1))+cos(q(1)+q(2))+cos(q(1)+q(2)+q(3)),...
    cos(q(1)+q(2))+cos(q(1)+q(2)+q(3)), cos(q(1)+q(2)+q(3)) ;
    -sin(q(1))-sin(q(1)+q(2))-sin(q(1)+q(2)+q(3)),...
    -sin(q(1)+q(2))-sin(q(1)+q(2)+q(3)), -sin(q(1)+q(2)+q(3)) ];
w_E_des = [1;1];

% numerical evaluation at time t
q_t = [pi/6,pi/3,pi/3];
J_Et = J_E(q_t);

% define the jacobian s.t. joint 1 has zero velocity
J_j1 = [1,0,0];
w_j1_des = [0];

% define the jacobian s.t. joint 2 has zero velocity
J_j2 = [0,1,0];
w_j2_des = [0];

% combined joint Jacobian
Jj = [J_j1;J_j2];
wj = [w_j1_des;w_j2_des];

%% Fulfill only the first task
disp('EX 1: fulfill only end-effector tracking')
dq_single = pinv(J_Et)*w_E_des;
printmat(pinv(J_Et),'pinv(J_Et)')
printmat(dq_single,'dq_single=pinv(J_Et)*w_E_des')
% Error calculation
printmat(J_Et*dq_single,'J_Et*dq_single')


                                        85
printmat(abs(w_E_des - J_Et*dq_single),'|w_E_des - J_Et*dq_single|')
disp(['||w_E_des - J_Et*dq_single||ˆ2 = ',...
    num2str((w_E_des - J_Et*dq_single)'*(w_E_des - J_Et*dq_single))]) ;

printmat(Jj*dq_single,'Jj*dq_single')
printmat(abs(wj - Jj*dq_single),'|wj - Jj*dq_single|')
disp(['||wj - Jj*dq_single||ˆ2 = ',...
    num2str((wj - Jj*dq_single)'*(wj - Jj*dq_single))]) ;


%% Fulfill all tasks with equal priority
disp('EX 2: fulfill all tasks with equal priority')
dq_stack = pinv([J_Et;Jj])*[w_E_des;wj];
printmat(pinv([J_Et;Jj]),'pinv([J_Et;Jj])')
printmat(dq_stack,'dq_stack=pinv([J_Et;Jj])*[w_E_des;wj]')
% Error calculation
printmat(J_Et*dq_stack,'J_Et*dq_stack')
printmat(abs(w_E_des - J_Et*dq_stack),'|w_E_des - J_Et*dq_stack|')
disp(['||w_E_des - J_Et*q_stack||ˆ2 = ',...
    num2str((w_E_des - J_Et*dq_stack)'*(w_E_des - J_Et*dq_stack))]);

printmat(Jj*dq_stack,'Jj*dq_stack')
printmat(abs(wj - Jj*dq_stack),'|wj - Jj*dq_stack|')
disp(['||wj - Jj*q_stack||ˆ2 = ',...
    num2str((wj - Jj*dq_stack)'*(wj - Jj*dq_stack))]);

%% Fulfill both tasks but give the tracking a higher priority
disp('EX 3: fulfill tracking task with higher priority')
J1 = J_Et;
J2 = Jj;
w1 = w_E_des;
w2 = wj;
% calculate the null-space matrix
N1 = eye(3)-pinv(J1)*J1;
printmat(N1,'N1');
disp(['rank(N1) = ',num2str(rank(N1))]);
dq_prio = pinv(J1)*w1+N1*pinv(J2*N1,1e-6)*(wj-J2*pinv(J1)*w1);
printmat(dq_prio,'dq_prio = pinv(J1)*w1+N1*pinv(J2*N1)*(w2-J2*pinv(J1)*w1')
% Error calculation
printmat(J_Et*dq_prio,'J_Et*dq_prio')
printmat(abs(w_E_des - J_Et*dq_prio),'|w_E_des - J_Et*dq_prio|')
disp(['||w_E_des - J_Et*q_prio||ˆ2 = ',...
    num2str((w_E_des - J_Et*dq_prio)'*(w_E_des - J_Et*dq_prio))]) ;

printmat(Jj*dq_prio,'Jj*dq_prio')
printmat(abs(wj - Jj*dq_prio),'|wj - Jj*dq_prio|')
disp(['||wj - Jj*dq_prio||ˆ2 = ',...
    num2str((wj - Jj*dq_prio)'*(wj - Jj*dq_prio))]) ;




A.2     Inverse Kinematics for Rotations
Code for example 2.9.7.


clc
clear all
close all

%%


                                  86
% consider a robot with three successive joints rotating around z, y, z
% the end-effector rotation matrix is
Cx = @(x) [1,0,0;0,cos(x),-sin(x);0,sin(x),cos(x)];
Cy = @(y) [cos(y),0,sin(y);0,1,0;-sin(y),0,cos(y)];
Cz = @(z) [cos(z),-sin(z),0;sin(z),cos(z),0;0,0,1];
Czyx = @(q) Cz(q(1))*Cy(q(2))*Cx(q(3));

% basic Jacobian is given by
w1 = @(q) [0;0;1];
w2 = @(q) Cz(q(1))*[0;1;0];
w3 = @(q) Cz(q(1))*Cy(q(2))*[1;0;0];
J0 = @(q) [w1(q),w2(q),w3(q)];

%% analytical Jacobian and E matrix for ZYX Euler angles
% chi_EulerZYX = [z;y;x];
% omega = E(chi)*dchi
% J0 = E*JA ≤> JA=E\J0
E_eulerZYX = @(chi)[
0,-sin(chi(1)),cos(chi(2))*cos(chi(1));
0,cos(chi(1)),cos(chi(2))*sin(chi(1));
1,0,-sin(chi(2))];
JA_eulerZYX = @(chi,q) E_eulerZYX(chi)\J0(q);
rotmat2euleranglesZYX = @(C) [
atan2(C(2,1),C(1,1));
-atan2(C(3,1),sqrt(C(3,2)ˆ2+C(3,3)ˆ2));
atan2(C(3,2), C(3,3))];

%% analytical Jacobian and E matrix for XYZ Euler angles
% chi_EulerXYZ = [x;y;z];
E_eulerXYZ = @(chi)[
1,      0,         sin(chi(2));
0, cos(chi(1)), -cos(chi(2))*sin(chi(1));
0, sin(chi(1)), cos(chi(1))*cos(chi(2))];
JA_eulerXYZ = @(chi,q) E_eulerXYZ(chi)\J0(q);
rotmat2euleranglesXYZ = @(C) [
atan2(-C(2,3), C(3,3));
atan2(C(1,3), sqrt(C(1,1)ˆ2+C(1,2)ˆ2));
atan2(-C(1,2),C(1,1))];

%% analytical Jacobian and E matrix for rotation vector
% chi_rotvec = [rx;ry;rz]
skew = @(a) [0 ,-a(3), a(2);a(3), 0,-a(1);-a(2), a(1) 0];
E_rotvec = @(x) ...
eye(3)+skew(x)*(1-cos(norm(x)))/norm(x)ˆ2+...
skew(x)*skew(x)*(norm(x)-sin(norm(x)))/norm(x)ˆ3;
JA_rotvec = @(chi,q) E_rotvec(chi)\J0(q);
rotmat2rotvec = @(C) ...
acos((C(1,1)+C(2,2)+C(3,3)-1)/2)*1/...
(2*sin(acos((C(1,1)+C(2,2)+C(3,3)-1)/2)))*...
[C(3,2)-C(2,3);C(1,3)-C(3,1);C(2,1)-C(1,2)];
rotvec2rotmat = @(x) ...
eye(3)+sin(norm(x))/norm(x)*skew(x)+...
(1-cos(norm(x)))*skew(x)*skew(x)/norm(x)ˆ2;


%%%%%%%%%%%%%%%%%%%%%%%%
%% Numerical evaluation
%%%%%%%%%%%%%%%%%%%%%%%%

% start conditions
q_0 = [-0.7;0;1.5];
q_goal = [0.7;1.5;-0.5];



                                  87
C0 = Czyx(q_0);
Cgoal = Czyx(q_goal);

% define k parameter
k =0.001;


%% ZYX euler angles
q_eulerZYX_v(:,1) = q_0;
chi_eulerZYX_goal = rotmat2euleranglesZYX(Czyx(q_goal));
for i=1:10000
    chi_eulerZYX_v(:,i) = rotmat2euleranglesZYX(Czyx(q_eulerZYX_v(:,i)));
    JA_eulerZYX_eval = JA_eulerZYX(chi_eulerZYX_v(:,i),q_eulerZYX_v(:,i));
    ∆_chi_eulerZYX = chi_eulerZYX_goal-chi_eulerZYX_v(:,i);
    q_eulerZYX_v(:,i+1) = ...
        q_eulerZYX_v(:,i) + k*(JA_eulerZYX_eval\∆_chi_eulerZYX);

      C_eulerZYX_mat(i,:,:) = Czyx(q_eulerZYX_v(:,i));

      if norm(∆_chi_eulerZYX)<0.01
          break
      end
end

%% XYZ euler angles
q_eulerXYZ_v(:,1) = q_0;
chi_eulerXYZ_goal = rotmat2euleranglesXYZ(Czyx(q_goal));
for i=1:10000
    chi_eulerXYZ_v(:,i) = rotmat2euleranglesXYZ(Czyx(q_eulerXYZ_v(:,i)));
    JA_eulerXYZ_eval = JA_eulerXYZ(chi_eulerXYZ_v(:,i),q_eulerXYZ_v(:,i));
    ∆_chi_eulerXYZ = chi_eulerXYZ_goal-chi_eulerXYZ_v(:,i);
    q_eulerXYZ_v(:,i+1) = ...
        q_eulerXYZ_v(:,i) + k*(JA_eulerXYZ_eval\∆_chi_eulerXYZ);

      C_eulerXYZ_mat(i,:,:) = Czyx(q_eulerXYZ_v(:,i));

      if norm(∆_chi_eulerXYZ)<0.01
          break
      end
end

%% rotvector
q_rotvec_v(:,1) = q_0;
chi_rotvec_goal = rotmat2rotvec(Czyx(q_goal));
for i=1:10000
    chi_rotvec_v(:,i) = rotmat2rotvec(Czyx(q_rotvec_v(:,i)));
    JA_rotvec_eval = JA_rotvec(chi_rotvec_v(:,i),q_rotvec_v(:,i));
    ∆_chi_rotvec = chi_rotvec_goal-chi_rotvec_v(:,i);
    q_rotvec_v(:,i+1) = ...
        q_rotvec_v(:,i) + k*(JA_rotvec_eval\∆_chi_rotvec);

      C_rotvec_mat(i,:,:) = Czyx(q_rotvec_v(:,i));

      if norm(∆_chi_rotvec)<0.01
          break
      end
end


%% error function calculated from relative rotation
q_omega_v(:,1) = q_0;
for i=1:10000



                                     88
      chi_omega_v(:,i) = rotmat2rotvec(Czyx(q_omega_v(:,i)));
      J0e = J0(q_omega_v(:,i));
      C∆ = Czyx(q_goal)*Czyx(q_omega_v(:,i))';
      chi_C∆ = rotmat2rotvec(C∆);
      q_omega_v(:,i+1) = q_omega_v(:,i) + k*(J0e\chi_C∆);

      C_omega_mat(i,:,:) = Czyx(q_omega_v(:,i));
      if norm(chi_C∆)<0.01
          break
      end
end

%% plotting
figure
hold on
axis equal
grid on

[xs,ys,zs] = sphere;
surf(xs,ys,zs,'FaceColor',[0.8 0.8 0.8],'FaceAlpha',0.5)


for i=1:3
    % initial CS
    plot3([0,C0(1,i)],[0,C0(2,i)],[0,C0(3,i)],'b','linewidth',2)
    % goal CS
    plot3([0,Cgoal(1,i)],[0,Cgoal(2,i)],[0,Cgoal(3,i)],'r','linewidth',2)

      % trajectories
      plot3(C_eulerZYX_mat(:,1,i),C_eulerZYX_mat(:,2,i),...
      C_eulerZYX_mat(:,3,i),'b','linewidth',4)
      plot3(C_eulerXYZ_mat(:,1,i),C_eulerXYZ_mat(:,2,i),...
      C_eulerXYZ_mat(:,3,i),'k','linewidth',4)
      plot3(C_rotvec_mat(:,1,i),C_rotvec_mat(:,2,i),...
      C_rotvec_mat(:,3,i),'r','linewidth',4)
      plot3(C_omega_mat(:,1,i),C_omega_mat(:,2,i),...
      C_omega_mat(:,3,i),'g','linewidth',4)
end




                                    89
90
Appendix B

Matlab Code for 3D rotations

This chapter collects functions which implement the theory discussed for rotations
in the three dimensional space. This code is part of the open-source project Kindr -
Kinematics and Dynamics for Robotics.


B.1     Euler angles to rotation matrix
This section implements the composition of elementary rotations to obtain a rotation
matrix which is associated to a given set of Euler angles (ZYZ, ZXZ, ZYX and XYZ).

function R = mapEulerAnglesXYZToRotationMatrix(angles)
% MAPEULERANGLESXYZTOROTATIONMATRIX(angles) maps a set of Euler angles to a
% rotation matrix in SO(3). The Euler angles represent a set successive
% rotations around X-Y'-Z''. This is equivalent to rotating around the
% fixed axes in Z-Y-X order.
%
% Author(s): Dario Bellicoso

x = angles(1);
y = angles(2);
z = angles(3);

R = getRotationMatrixX(x)*getRotationMatrixY(y)*getRotationMatrixZ(z);

if isa(angles, 'sym')
    R = simplify(R);
end

end



function R = mapEulerAnglesZXZToRotationMatrix(angles)
% MAPEULERANGLESZXZTOROTATIONMATRIX(angles) maps a set of Euler angles to a
% rotation matrix in SO(3). The Euler angles represent a set successive
% rotations around Z-X'-Z''.
%
% Author(s): Dario Bellicoso

z1 = angles(1);
x = angles(2);


                                        91
z2 = angles(3);

R = getRotationMatrixZ(z1)*getRotationMatrixX(x)*getRotationMatrixZ(z2);

if isa(angles, 'sym')
    R = simplify(R);
end

end



function R = mapEulerAnglesZYXToRotationMatrix(angles)
% MAPEULERANGLESZYXTOROTATIONMATRIX(angles) maps a set of Euler angles to a
% rotation matrix in SO(3). The Euler angles represent a set successive
% rotations around Z-Y'-X''. This is equivalent to rotating around the
% fixed axes in X-Y-Z order.
%
% Author(s): Dario Bellicoso

z = angles(1);
y = angles(2);
x = angles(3);

if isa(angles, 'sym')
    R = simplify(getRotationMatrixZ(z)*getRotationMatrixY(y)*getRotationMatrixX(x));
else
    R = getRotationMatrixZ(z)*getRotationMatrixY(y)*getRotationMatrixX(x);
end

end



function R = mapEulerAnglesZYZToRotationMatrix(angles)
% MAPEULERANGLESZYZTOROTATIONMATRIX(angles) maps a set of Euler angles to a
% rotation matrix in SO(3). The Euler angles represent a set successive
% rotations around Z-Y'-Z''.
%
% Author(s): Dario Bellicoso

z1 = angles(1);
y = angles(2);
z2 = angles(3);

R = getRotationMatrixZ(z1)*getRotationMatrixY(y)*getRotationMatrixZ(z2);

if isa(angles, 'sym')
    R = simplify(R);
end

end




B.2    Rotation matrix to Euler angles
This section implements the extraction of Euler angles (ZYZ, ZXZ, ZYX and XYZ)
from a given rotation matrix.



                                     92
function ph = getEulAngXYZFromRotationMatrix(C)
% GETEULANGXYZFROMROTATIONMATRIX(C) extracts XYZ Euler angles from a
% rotation matrix.
%
% Author(s): Dario Bellicoso

x = atan2(-C(2,3),C(3,3));
y = atan2(C(1,3), sqrt(C(1,1)ˆ2+C(1,2)ˆ2));
z = atan2(-C(1,2),C(1,1));

ph = [x y z]';



function ph = getEulAngZXZFromRotationMatrix(C)
% GETEULANGZYXFROMROTATIONMATRIX(C) extracts ZXZ Euler angles from a
% rotation matrix.
%
% Author(s): Dario Bellicoso

z1 = atan2(C(1,3),-C(2,3));
x = atan2(sqrt(C(1,3)ˆ2+C(2,3)ˆ2), C(3,3));
z2 = atan2(C(3,1),C(3,2));

ph = [z1 x z2]';



function ph = getEulAngZYXFromRotationMatrix(C)
% GETEULANGZYXFROMROTATIONMATRIX(C) extracts ZYX Euler angles from a
% rotation matrix.
%
% Author(s): Dario Bellicoso

z = atan2(C(2,1),C(1,1));
y = atan2(-C(3,1), sqrt(C(3,2)ˆ2+C(3,3)ˆ2));
x = atan2(C(3,2),C(3,3));

ph = [z y x]';



function ph = getEulAngZYZFromRotationMatrix(C)
% GETEULANGZYXFROMROTATIONMATRIX(C) extracts ZYZ Euler angles from a
% rotation matrix.
%
% Author(s): Dario Bellicoso

z1 = atan2(C(2,3),C(1,3));
x = atan2(sqrt(C(1,3)ˆ2+C(2,3)ˆ2), C(3,3));
z2 = atan2(C(3,2),-C(3,1));

ph = [z1 x z2]';




                                  93
94
Bibliography

[1] Haim Baruh. Analytical Dynamics. WCB/McGraw-Hill Boston, 1999. ISBN
    0073659770.   URL http://coewww.rutgers.edu/˜baruh/book.
    html.
[2] Michael Bloesch, Hannes Sommer, Tristan Laidlow, Michael Burri, Gabriel
    Nuetzi, Péter Fankhauser, Dario Bellicoso, Christian Gehring, Stefan Leuteneg-
    ger, Marco Hutter, and Roland Siegwart. A Primer on the Differential Calculus of
    3D Orientations. Technical report, jun 2016. URL http://arxiv.org/abs/
    1606.05285.
[3] S. R. Buss. Introduction to inverse kinematics with Jacobian transpose, pseu-
    doinverse and damped least squares methods. Technical report, 2004. URL
    http://math.ucsd.edu/˜sbuss/ResearchWeb.
[4] H. Goldstein, C.P. Poole, and J.L. Safko. Classical Mechanics. Addison Wesley,
    2002. ISBN 9780201657029.
[5] O Khatib. A unified approach for motion and force control of robot manipula-
    tors: The operational space formulation. IEEE Journal of Robotics and Automa-
    tion, 3(1):43–53, 1987. URL http://dx.doi.org/10.1109/JRA.1987.
    1087068.
[6] Jerry Pratt, Chee-Meng Chew, Ann Torres, Peter Dilworth, and Gill Pratt.
    Virtual model control: An intuitive approach for bipedal locomotion. In-
    ternational Journal of Robotics Research (IJRR), 20(2):129–143, 2001. doi:
    10.1177/02783640122067309.       URL http://dx.doi.org/10.1177/
    02783640122067309.
[7] Bruno Siciliano and Oussama Khatib. Springer Handbook of Robotics. Springer
    Berlin Heidelberg, Berlin, Heidelberg, 2008. ISBN 978-3-540-23957-4. doi: 10.
    1007/978-3-540-30301-5. URL http://link.springer.com/10.1007/
    978-3-540-30301-5.
[8] Bruno Siciliano, Lorenzo Sciavicco, Luigi Villani, and Giuseppe Oriolo. Robotics
    - Modelling, Planning and Control. Advanced Textbooks in Control and Signal
    Processing. Springer London, London, 2009. ISBN 978-1-84628-641-4. doi: 10.
    1007/978-1-84628-642-1. URL http://link.springer.com/10.1007/
    978-1-84628-642-1.
[9] Joan Sola. Quaternion Kinematics for the Error-State KF. Technical report,
    2016. URL http://www.iri.upc.edu/people/jsola/JoanSola/
    objectes/notes/kinematics.pdf.

                                        95
