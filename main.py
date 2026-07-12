"""
main.py

MagPick

Baseline Version 1

Author : Sumit Pandit
"""

from perception.perception_interface import PerceptionInterface

from planning.planner import MagneticPickPlanner

from visualization.visualizer import Visualizer


def main():

    print()

    print("=====================================")

    print("MAGPICK")

    print("Baseline Planner Version 1")

    print("=====================================")

    perception = PerceptionInterface()

    planner = MagneticPickPlanner()

    visualizer = Visualizer()

    objects = perception.detect_objects()

    print()

    print(

        "Objects Found :",

        len(objects)

    )

    print()

    obj = objects[0]

    ranked = planner.plan(

        obj

    )

    visualizer.show(

        ranked

    )

    print()

    print("Planner Finished.")

    print()


if __name__ == "__main__":

    main()