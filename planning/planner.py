"""
planner.py

MagPick Planner

Author : Sumit Pandit
"""

from planning.candidate_generator import CandidateGenerator

from planning.quality import QualityEvaluator

from planning.feasibility import FeasibilityChecker

from planning.ranking import CandidateRanker


class MagneticPickPlanner:

    def __init__(self):

        self.generator = CandidateGenerator()

        self.quality = QualityEvaluator()

        self.feasibility = FeasibilityChecker()

        self.ranker = CandidateRanker()

    def plan(self,
             obj):

        candidates = self.generator.generate(

            obj

        )

        evaluated = []

        for c in candidates:

            c = self.quality.evaluate(

                obj,

                c

            )

            c.evaluation = self.feasibility.check(

                obj,

                c,

                c.evaluation

            )

            evaluated.append(c)

        ranked = self.ranker.rank(

            evaluated

        )

        return ranked


if __name__ == "__main__":

    print()

    print("Planner Module Ready")