# MagPick

## Physics-Based Magnetic Grasp Planning Framework

MagPick is an in-house magnetic grasp planning framework for robotic bin picking of cylindrical ferromagnetic billets.

Current target application:

- FANUC CRX-10iA/L
- Schmalz Magnetic Gripper
- Mech-Mind 3D Vision
- Steel Billets

---


# Project Objective

Develop a modular magnetic grasp planner capable of selecting the optimal magnetic contact location using perception outputs.

The planner operates between the perception system and the robot motion planner.

```
          CAMERA

             │

             ▼

      PERCEPTION

             │

             ▼

      OBJECT MODEL

             │

             ▼

==========================
       MAGPICK
==========================

Candidate Generation

↓

Physics

↓

Quality

↓

Ranking

↓

Best Pick Pose

==========================

             │

             ▼

 Motion Planner (MoveIt)

             │

             ▼

 Robot Controller

             │

             ▼

 FANUC Robot

             │

             ▼

 Magnetic Gripper
```

---

# Current Features

- Modular software architecture
- Object Model abstraction
- Cylinder geometry utilities
- Surface patch sampling
- Magnetic candidate generation
- Holding force estimation
- Dynamic torque calculation
- Candidate quality evaluation
- Feasibility verification
- Candidate ranking
- Console visualization

---

# Current Status

✅ Baseline Planner Version 1 Complete

Current demonstration:

```

=====================================
MAGPICK
Baseline Planner Version 1
=====================================

Objects Found : 1


========================================================================================================================
MAGPICK BASELINE PLANNER - EVALUATION TABLE
========================================================================================================================

Rank  CandID    Offset(mm)     Hold(N)     Req(N)      Margin(N)     Torque(Nm)    Visibility  Confidence  Score     Feasible  
-------------------------------------------------------------------------------------------------------------------------------
1     2         0.00           150.00      29.43       120.57        0.000         92.0        0.97        1.286     True      
2     1         40.00          150.00      29.43       120.57        1.177         92.0        0.97        1.027     True      
3     3         40.00          150.00      29.43       120.57        1.177         92.0        0.97        1.027     True      
4     0         80.00          150.00      29.43       120.57        2.354         92.0        0.97        0.768     True      
5     4         80.00          150.00      29.43       120.57        2.354         92.0        0.97        0.768     True      

========================================================================================================================
BEST PICK
------------------------------------------------------------------------------------------------------------------------
Candidate ID      : 2
Planner Rank      : 1
Planner Score     : 1.286

Pick Position
X : 250.00
Y : 120.00
Z : 80.00

Approach Position
X : 250.00
Y : 120.00
Z : 130.00

Retreat Position
X : 250.00
Y : 120.00
Z : 180.00

========================================================================================================================

Planner Finished.

```

---
<img width="1536" height="1024" alt="MagPick_V1 0" src="https://github.com/user-attachments/assets/ca83a14f-b09e-440b-8d8d-d40e5a99a536" />
# Repository Structure

```
models/
geometry/
perception/
planning/
physics/
visualization/

main.py
```

---

# Future Work

- Real Mech-Mind integration
- ROS2 interface
- FANUC CRX execution
- Adaptive surface sampling
- Physics-aware magnetic model
- Collision checking
- Escape path planning
- Research publication

---

Author

Sumit Pandit


