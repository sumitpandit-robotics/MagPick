	# MagPick

## Physics-Based Magnetic Grasp Planning Framework

MagPick is an in-house magnetic grasp planning framework for robotic bin picking of cylindrical metal steel billets.

Current target application:

- FANUC CRX-10iA/L
- Schmalz / equivalent Magnetic Gripper
- Mech-Mind 3D / suitable Vision
- Metal Steel Billets 

---

# Project Objective

Develop a modular magnetic grasp planner capable of selecting the optimal magnetic contact location using perception outputs.

The planner operates between the perception system and the robot motion planner.

```
Perception
      ↓
Object Model
      ↓
Surface Sampling
      ↓
Candidate Generation
      ↓
Magnetic Physics
      ↓
Quality Evaluation
      ↓
Ranking
      ↓
Best Pick Pose
      ↓
Motion Planner
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
Objects Found : 1

Candidates Generated : 5

Best Candidate : 2

Score : 1.286
```

---

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


