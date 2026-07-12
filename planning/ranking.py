"""
ranking.py

Candidate Ranking

Author : Sumit Pandit
"""

class CandidateRanker:

    def rank(self,
             candidates):

        feasible = []

        for c in candidates:

            if c.evaluation.feasible:

                feasible.append(c)

        feasible.sort(

            key=lambda x: x.evaluation.final_score,

            reverse=True

        )

        return feasible


if __name__ == "__main__":

    print()

    print("Ranking Module Ready")