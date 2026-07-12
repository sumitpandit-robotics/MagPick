"""
perception_interface.py

Dummy perception interface for MagPick Version 1.

Author : Sumit Pandit
Project : MagPick
"""

from models.geometry import *

from models.object_model import *


class PerceptionInterface:

    """
    Simulated perception system.

    Later this class will be replaced by
    MechMind / Photoneo interface.
    """

    def detect_objects(self):

        obj = ObjectModel(

            object_id=1,

            object_type=ObjectType.CYLINDER,

            cad_model=CADModel(

                model_id="Billet_50x200",

                revision="A"

            ),

            pose=Pose6D(

                position=Point3D(

                    250,

                    120,

                    80

                ),

                orientation=Quaternion(

                    0,

                    0,

                    0,

                    1

                )

            ),

            geometry=Cylinder(

                diameter=50,

                length=200

            ),

            material=Material.STEEL,

            mass=3.0,

            confidence=0.97,

            visible_percentage=92.0,

            point_cloud=PointCloud(),

            surface_patches=[],

            timestamp=0.0,

            frame_id="world"

        )

        return [

            obj

        ]


# ==========================================================
# Standalone Test
# ==========================================================

if __name__ == "__main__":

    perception = PerceptionInterface()

    objects = perception.detect_objects()

    print()

    print("========== Perception ==========")

    print()

    print(

        f"Objects Detected : "

        f"{len(objects)}"

    )

    obj = objects[0]

    print()

    print(

        f"Object ID : "

        f"{obj.object_id}"

    )

    print(

        f"Type : "

        f"{obj.object_type.value}"

    )

    print()

    print(

        f"Position : "

        f"{obj.pose.position.x:.1f}, "

        f"{obj.pose.position.y:.1f}, "

        f"{obj.pose.position.z:.1f}"

    )

    print()

    print(

        f"Confidence : "

        f"{obj.confidence:.2f}"

    )