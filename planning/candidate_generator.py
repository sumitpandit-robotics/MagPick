"""
candidate_generator.py

MagPick Candidate Generator

Version 1

Author : Sumit Pandit
"""

from geometry.sampling import SurfaceSampler
from geometry.transforms import TransformUtils

from models.candidate import Candidate

from models.geometry import Pose6D, Vector3D


class CandidateGenerator:

    def __init__(self):

        self.sampler = SurfaceSampler()

    def generate(self,
                 obj):

        patches = self.sampler.sample_patches(

            obj.geometry

        )

        axis = TransformUtils.cylinder_axis(

            obj.pose

        )

        candidates = []

        for idx, patch in enumerate(patches):

            world_point = TransformUtils.move_along_axis(

                obj.pose.position,

                axis,

                patch.center.x

            )

            pick_pose = Pose6D(

                position=world_point,

                orientation=obj.pose.orientation

            )

            approach_pose = Pose6D(

                position=TransformUtils.move_along_axis(

                    world_point,

                    Vector3D(

                        0,

                        0,

                        1

                    ),

                    50

                ),

                orientation=obj.pose.orientation

            )

            retreat_pose = Pose6D(

                position=TransformUtils.move_along_axis(

                    world_point,

                    Vector3D(

                        0,

                        0,

                        1

                    ),

                    100

                ),

                orientation=obj.pose.orientation

            )

            candidate = Candidate(

                candidate_id=idx,

                object_id=obj.object_id,

                contact_patch=patch,

                pick_pose=pick_pose,

                approach_pose=approach_pose,

                retreat_pose=retreat_pose

            )

            candidates.append(candidate)

        return candidates


if __name__ == "__main__":

    from perception.perception_interface import PerceptionInterface

    perception = PerceptionInterface()

    obj = perception.detect_objects()[0]

    planner = CandidateGenerator()

    candidates = planner.generate(obj)

    print()

    print("==============================")

    print("Generated Candidates")

    print("==============================")

    print()

    print("Total :", len(candidates))

    print()

    for c in candidates:

        print(

            c.candidate_id,

            "->",

            round(c.pick_pose.position.x,2),

            round(c.pick_pose.position.y,2),

            round(c.pick_pose.position.z,2)

        )