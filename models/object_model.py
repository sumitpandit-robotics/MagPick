"""
object_model.py

Object representation used by MagPick.

This file defines everything the planner needs to know
about one detected object.

Author : Sumit Pandit
Project : MagPick
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List

from models.geometry import *


# ==========================================================
# Object Type
# ==========================================================

class ObjectType(Enum):

    CYLINDER = "Cylinder"

    BOX = "Box"

    PLATE = "Plate"

    CUSTOM = "Custom"


# ==========================================================
# Material
# ==========================================================

class Material(Enum):

    STEEL = "Steel"

    CAST_IRON = "Cast Iron"

    STAINLESS = "Stainless Steel"

    UNKNOWN = "Unknown"


# ==========================================================
# CAD Information
# ==========================================================

@dataclass
class CADModel:

    model_id: str

    revision: str

    description: str = ""


# ==========================================================
# Object Model
# ==========================================================

@dataclass
class ObjectModel:

    # --------------------------------------------
    # Identification
    # --------------------------------------------

    object_id: int

    object_type: ObjectType

    cad_model: CADModel

    # --------------------------------------------
    # Geometry
    # --------------------------------------------

    pose: Pose6D

    geometry: Cylinder

    # --------------------------------------------
    # Physical Properties
    # --------------------------------------------

    material: Material

    mass: float

    # --------------------------------------------
    # Perception Information
    # --------------------------------------------

    confidence: float

    visible_percentage: float

    point_cloud: PointCloud = field(default_factory=PointCloud)

    surface_patches: List[SurfacePatch] = field(default_factory=list)

    # --------------------------------------------
    # Runtime Information
    # --------------------------------------------

    timestamp: float = 0.0

    frame_id: str = "world"