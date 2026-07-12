"""
geometry.py

Core geometric data models used throughout MagPick.

Author : Sumit Pandit
Project : MagPick
"""

from dataclasses import dataclass, field
from typing import List


# ==========================================================
# Basic Geometry
# ==========================================================

@dataclass(frozen=True)
class Point3D:
    """
    3D point in world coordinates (mm)
    """
    x: float
    y: float
    z: float


@dataclass(frozen=True)
class Vector3D:
    """
    3D vector
    """
    x: float
    y: float
    z: float


@dataclass(frozen=True)
class Quaternion:
    """
    Quaternion orientation
    """
    x: float
    y: float
    z: float
    w: float


@dataclass(frozen=True)
class EulerAngles:
    """
    Roll Pitch Yaw (degrees)

    Used only for visualization/debugging.
    """
    roll: float
    pitch: float
    yaw: float


# ==========================================================
# Pose
# ==========================================================

@dataclass(frozen=True)
class Pose6D:
    """
    Complete object pose.
    """

    position: Point3D

    orientation: Quaternion


# ==========================================================
# Primitive Geometry
# ==========================================================

@dataclass(frozen=True)
class Cylinder:
    """
    Billet geometry
    """

    diameter: float

    length: float

    @property
    def radius(self):

        return self.diameter / 2.0


@dataclass(frozen=True)
class BoundingBox:

    length: float

    width: float

    height: float


# ==========================================================
# Surface
# ==========================================================

@dataclass(frozen=True)
class SurfaceNormal:

    direction: Vector3D


@dataclass(frozen=True)
class SurfacePatch:
    """
    One candidate magnetic contact region.
    """

    center: Point3D

    normal: SurfaceNormal

    radius: float

    area: float


# ==========================================================
# Point Cloud
# ==========================================================

@dataclass
class PointCloud:

    points: List[Point3D] = field(default_factory=list)