"""
transforms.py

Transformation utilities for MagPick.

Author : Sumit Pandit
Project : MagPick
"""

import math
import numpy as np

from models.geometry import *


class TransformUtils:

    # =====================================================
    # Quaternion -> Rotation Matrix
    # =====================================================

    @staticmethod
    def quaternion_to_rotation_matrix(q: Quaternion):

        x = q.x
        y = q.y
        z = q.z
        w = q.w

        xx = x * x
        yy = y * y
        zz = z * z

        xy = x * y
        xz = x * z
        yz = y * z

        wx = w * x
        wy = w * y
        wz = w * z

        R = np.array([

            [
                1 - 2 * (yy + zz),
                2 * (xy - wz),
                2 * (xz + wy)
            ],

            [
                2 * (xy + wz),
                1 - 2 * (xx + zz),
                2 * (yz - wx)
            ],

            [
                2 * (xz - wy),
                2 * (yz + wx),
                1 - 2 * (xx + yy)
            ]

        ])

        return R

    # =====================================================
    # Cylinder Axis
    # =====================================================

    @staticmethod
    def cylinder_axis(pose: Pose6D):

        R = TransformUtils.quaternion_to_rotation_matrix(

            pose.orientation

        )

        axis = R @ np.array([1.0, 0.0, 0.0])

        axis = axis / np.linalg.norm(axis)

        return Vector3D(

            axis[0],

            axis[1],

            axis[2]

        )

    # =====================================================
    # Move Along Axis
    # =====================================================

    @staticmethod
    def move_along_axis(

            point: Point3D,

            axis: Vector3D,

            distance: float):

        return Point3D(

            point.x + axis.x * distance,

            point.y + axis.y * distance,

            point.z + axis.z * distance

        )

    # =====================================================
    # Distance
    # =====================================================

    @staticmethod
    def distance(

            p1: Point3D,

            p2: Point3D):

        return math.sqrt(

            (p1.x - p2.x) ** 2 +

            (p1.y - p2.y) ** 2 +

            (p1.z - p2.z) ** 2

        )


# ==========================================================
# Standalone Test
# ==========================================================

if __name__ == "__main__":

    q = Quaternion(

        0,

        0,

        0,

        1

    )

    pose = Pose6D(

        Point3D(

            100,

            50,

            25

        ),

        q

    )

    axis = TransformUtils.cylinder_axis(

        pose

    )

    print()

    print("========== Transform Test ==========")

    print()

    print(

        f"Axis : "

        f"{axis.x:.2f}, "

        f"{axis.y:.2f}, "

        f"{axis.z:.2f}"

    )

    new_point = TransformUtils.move_along_axis(

        pose.position,

        axis,

        50

    )

    print()

    print(

        f"Moved Point : "

        f"{new_point.x:.2f}, "

        f"{new_point.y:.2f}, "

        f"{new_point.z:.2f}"

    )