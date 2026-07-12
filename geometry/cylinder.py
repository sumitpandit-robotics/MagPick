"""
cylinder.py

Cylinder geometry utilities.

Author : Sumit Pandit
Project : MagPick
"""

from dataclasses import dataclass

from models.geometry import Cylinder


@dataclass
class SafePickZone:

    start_offset: float
    end_offset: float
    usable_length: float


class CylinderGeometry:

    def __init__(self, cylinder: Cylinder):

        self.cylinder = cylinder

    @property
    def radius(self):

        return self.cylinder.radius

    @property
    def length(self):

        return self.cylinder.length

    def safe_pick_zone(self, end_margin=20.0):

        usable = self.length - 2 * end_margin

        return SafePickZone(

            start_offset=-usable / 2.0,

            end_offset=usable / 2.0,

            usable_length=usable

        )

    def center_of_mass(self):

        return 0.0

    def max_stable_offset(self):

        zone = self.safe_pick_zone()

        return zone.usable_length / 2.0


if __name__ == "__main__":

    billet = Cylinder(

        diameter=50,

        length=200

    )

    geometry = CylinderGeometry(billet)

    zone = geometry.safe_pick_zone()

    print()

    print("Cylinder Geometry Test")

    print()

    print("Radius :", geometry.radius)

    print("Length :", geometry.length)

    print("Safe Zone :", zone.start_offset, zone.end_offset)