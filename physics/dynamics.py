"""
dynamics.py

Dynamic stability calculations.

Version 1

Author : Sumit Pandit
"""

import math


class DynamicsCalculator:

    """
    Version 1

    Calculates torque generated due to
    center offset.
    """

    def compute_torque(self,
                       mass,
                       offset_mm):

        offset = offset_mm / 1000.0

        return mass * 9.81 * offset


if __name__ == "__main__":

    dynamics = DynamicsCalculator()

    torque = dynamics.compute_torque(

        3.0,

        25

    )

    print()

    print("Torque :", round(torque,3),"Nm")