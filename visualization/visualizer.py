"""
visualizer.py

MagPick Console Visualizer

Version 1

Author : Sumit Pandit
"""

class Visualizer:

    def show(self, ranked):

        print()

        print("=" * 120)
        print("MAGPICK BASELINE PLANNER - EVALUATION TABLE")
        print("=" * 120)

        print()

        header = (
            f"{'Rank':<6}"
            f"{'CandID':<10}"
            f"{'Offset(mm)':<15}"
            f"{'Hold(N)':<12}"
            f"{'Req(N)':<12}"
            f"{'Margin(N)':<14}"
            f"{'Torque(Nm)':<14}"
            f"{'Visibility':<12}"
            f"{'Confidence':<12}"
            f"{'Score':<10}"
            f"{'Feasible':<10}"
        )

        print(header)

        print("-" * len(header))

        for rank, c in enumerate(ranked, start=1):

            e = c.evaluation

            print(

                f"{rank:<6}"
                f"{c.candidate_id:<10}"
                f"{e.center_offset:<15.2f}"
                f"{e.holding_force:<12.2f}"
                f"{e.required_force:<12.2f}"
                f"{e.holding_margin:<14.2f}"
                f"{e.torque:<14.3f}"
                f"{e.visibility:<12.1f}"
                f"{e.confidence:<12.2f}"
                f"{e.final_score:<10.3f}"
                f"{str(e.feasible):<10}"

            )

        print()

        print("=" * 120)

        best = ranked[0]

        print("BEST PICK")

        print("-" * 120)

        print(f"Candidate ID      : {best.candidate_id}")

        print(f"Planner Rank      : 1")

        print(f"Planner Score     : {best.evaluation.final_score:.3f}")

        print()

        print("Pick Position")

        print(f"X : {best.pick_pose.position.x:.2f}")

        print(f"Y : {best.pick_pose.position.y:.2f}")

        print(f"Z : {best.pick_pose.position.z:.2f}")

        print()

        print("Approach Position")

        print(f"X : {best.approach_pose.position.x:.2f}")

        print(f"Y : {best.approach_pose.position.y:.2f}")

        print(f"Z : {best.approach_pose.position.z:.2f}")

        print()

        print("Retreat Position")

        print(f"X : {best.retreat_pose.position.x:.2f}")

        print(f"Y : {best.retreat_pose.position.y:.2f}")

        print(f"Z : {best.retreat_pose.position.z:.2f}")

        print()

        print("=" * 120)