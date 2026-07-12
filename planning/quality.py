"""
quality.py

Candidate Quality Evaluation

Author : Sumit Pandit
"""

from physics.magnetic_force import MagneticForceCalculator

from physics.dynamics import DynamicsCalculator

from models.evaluation import Evaluation


class QualityEvaluator:

    def __init__(self):

        self.force = MagneticForceCalculator()

        self.dynamics = DynamicsCalculator()

    def evaluate(self,
                 obj,
                 candidate):

        physics = self.force.compute(

            obj,

            candidate

        )

        torque = self.dynamics.compute_torque(

            obj.mass,

            abs(candidate.contact_patch.center.x)

        )

        evaluation = Evaluation()

        evaluation.holding_force = physics["holding_force"]

        evaluation.required_force = physics["required_force"]

        evaluation.holding_margin = physics["holding_margin"]

        evaluation.torque = torque

        evaluation.visibility = obj.visible_percentage

        evaluation.confidence = obj.confidence

        evaluation.contact_area = candidate.contact_patch.area

        evaluation.center_offset = abs(

            candidate.contact_patch.center.x

        )

        evaluation.normal_alignment = 1.0

        evaluation.clearance = 100.0

        evaluation.escape_possible = True

        evaluation.collision_free = True

        evaluation.multi_pick_probability = 0.0

        score = 1.0

        score -= evaluation.center_offset / 200.0

        score += evaluation.confidence * 0.20

        score += evaluation.visibility / 1000.0

        score -= torque * 0.05

        evaluation.final_score = score

        candidate.evaluation = evaluation

        return candidate


if __name__ == "__main__":

    print()

    print("Quality Module Ready")