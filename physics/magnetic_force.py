"""
magnetic_force.py

Magnetic Force Calculator

Version 1 (Baseline)

Author : Sumit Pandit
Project : MagPick
"""

from models.object_model import ObjectModel
from models.candidate import Candidate


class MagneticForceCalculator:

    """
    Baseline magnetic force model.

    Version 1 assumptions:

    - Constant magnetic holding force
    - No air-gap effect
    - No surface roughness effect
    - No material saturation
    - No dynamic derating

    These will be added in Version 2.
    """

    def __init__(self):

        # Nominal magnetic holding force (N)
        self.nominal_force = 150.0

        # Safety factor (reserved for future use)
        self.safety_factor = 2.0

    # =====================================================
    # Compute Magnetic Forces
    # =====================================================

    def compute(
        self,
        obj: ObjectModel,
        candidate: Candidate
    ):

        # ------------------------------------------
        # Weight of billet
        # ------------------------------------------

        required_force = obj.mass * 9.81

        # ------------------------------------------
        # Available magnetic force
        # ------------------------------------------

        holding_force = self.nominal_force

        # ------------------------------------------
        # Safety Margin
        # ------------------------------------------

        holding_margin = holding_force - required_force

        return {

            "holding_force": holding_force,

            "required_force": required_force,

            "holding_margin": holding_margin

        }


# ==========================================================
# Standalone Test
# ==========================================================

if __name__ == "__main__":

    print()

    print("===================================")
    print(" Magnetic Force Calculator")
    print("===================================")

    calculator = MagneticForceCalculator()

    print()

    print(f"Nominal Holding Force : {calculator.nominal_force:.2f} N")

    mass = 3.0

    required = mass * 9.81

    margin = calculator.nominal_force - required

    print(f"Billet Mass           : {mass:.2f} kg")
    print(f"Required Force        : {required:.2f} N")
    print(f"Holding Margin        : {margin:.2f} N")