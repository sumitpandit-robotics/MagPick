"""
feasibility.py

MagPick Feasibility Checker

Author : Sumit Pandit
"""

from models.evaluation import Evaluation, RejectReason


class FeasibilityChecker:

    def __init__(self):

        self.minimum_holding_margin = 20.0

        self.minimum_visibility = 60.0

    def check(self,
              obj,
              candidate,
              evaluation: Evaluation):

        if evaluation.holding_margin < self.minimum_holding_margin:

            evaluation.feasible = False

            evaluation.reject_reason = RejectReason.LOW_HOLDING_FORCE

            return evaluation

        if obj.visible_percentage < self.minimum_visibility:

            evaluation.feasible = False

            evaluation.reject_reason = RejectReason.LOW_VISIBILITY

            return evaluation

        evaluation.feasible = True

        evaluation.reject_reason = RejectReason.NONE

        return evaluation


if __name__ == "__main__":

    print()

    print("Feasibility Module Ready")