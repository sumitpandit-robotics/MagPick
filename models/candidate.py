"""
candidate.py

MagPick Candidate Model

Defines one possible magnetic pick candidate.

Author : Sumit Pandit
Project : MagPick
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional

from models.geometry import *
from models.evaluation import Evaluation


# ==========================================================
# Candidate Status
# ==========================================================

class CandidateStatus(Enum):

    GENERATED = "Generated"

    FEASIBLE = "Feasible"

    REJECTED = "Rejected"

    SELECTED = "Selected"


# ==========================================================
# Candidate
# ==========================================================

@dataclass
class Candidate:

    # --------------------------------------------------
    # Identification
    # --------------------------------------------------

    candidate_id: int

    object_id: int

    # --------------------------------------------------
    # Contact Information
    # --------------------------------------------------

    contact_patch: SurfacePatch

    # --------------------------------------------------
    # Robot Poses
    # --------------------------------------------------

    pick_pose: Pose6D

    approach_pose: Pose6D

    retreat_pose: Pose6D

    # --------------------------------------------------
    # Planning State
    # --------------------------------------------------

    status: CandidateStatus = CandidateStatus.GENERATED

    # --------------------------------------------------
    # Evaluation
    # --------------------------------------------------

    evaluation: Optional[Evaluation] = None