"""
evaluation.py

MagPick Candidate Evaluation Model

Stores the complete evaluation result of one candidate.

Author : Sumit Pandit
Project : MagPick
"""

from dataclasses import dataclass
from enum import Enum


# ==========================================================
# Reject Reason
# ==========================================================

class RejectReason(Enum):

    NONE = "None"

    LOW_HOLDING_FORCE = "Holding Force Too Low"

    LOW_VISIBILITY = "Low Visibility"

    COLLISION = "Collision"

    POOR_SURFACE = "Poor Surface"

    EXCESSIVE_TORQUE = "Excessive Torque"

    MULTI_PICK_RISK = "Multiple Object Pickup Risk"

    UNKNOWN = "Unknown"


# ==========================================================
# Candidate Evaluation
# ==========================================================

@dataclass
class Evaluation:

    # ------------------------------------------------------
    # Feasibility
    # ------------------------------------------------------

    feasible: bool = True

    reject_reason: RejectReason = RejectReason.NONE

    # ------------------------------------------------------
    # Physics
    # ------------------------------------------------------

    holding_force: float = 0.0          # N

    required_force: float = 0.0         # N

    holding_margin: float = 0.0         # N

    torque: float = 0.0                 # N·m

    # ------------------------------------------------------
    # Geometry
    # ------------------------------------------------------

    contact_area: float = 0.0           # mm²

    center_offset: float = 0.0          # mm

    normal_alignment: float = 0.0       # 0-1

    clearance: float = 0.0              # mm

    # ------------------------------------------------------
    # Perception
    # ------------------------------------------------------

    visibility: float = 0.0             # %

    confidence: float = 0.0             # 0-1

    # ------------------------------------------------------
    # Planning
    # ------------------------------------------------------

    escape_possible: bool = True

    multi_pick_probability: float = 0.0

    collision_free: bool = True

    # ------------------------------------------------------
    # Final Result
    # ------------------------------------------------------

    final_score: float = 0.0