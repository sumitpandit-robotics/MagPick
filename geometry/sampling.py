"""
sampling.py

Surface Patch Sampling for MagPick.

Author : Sumit Pandit
Project : MagPick
"""

from typing import List

from models.geometry import *

from geometry.cylinder import CylinderGeometry


class SurfaceSampler:

    """
    Generates magnetic contact patches
    inside the safe pick zone.
    """

    def __init__(self):

        pass

    # ------------------------------------------------------
    # Sample Surface Patches
    # ------------------------------------------------------

    def sample_patches(
            self,
            cylinder: Cylinder,
            magnet_diameter: float = 50.0,
            end_margin: float = 20.0,
            overlap: float = 10.0):

        geometry = CylinderGeometry(cylinder)

        zone = geometry.safe_pick_zone(end_margin)

        radius = magnet_diameter / 2.0

        step = magnet_diameter - overlap

        patches = []

        current = zone.start_offset

        while current <= zone.end_offset:

            patch = SurfacePatch(

                center=Point3D(

                    current,

                    0,

                    0

                ),

                normal=SurfaceNormal(

                    Vector3D(

                        0,

                        0,

                        1

                    )

                ),

                radius=radius,

                area=3.14159 * radius * radius

            )

            patches.append(patch)

            current += step

        return patches


# ==========================================================
# Standalone Test
# ==========================================================

if __name__ == "__main__":

    billet = Cylinder(

        diameter=50,

        length=200

    )

    sampler = SurfaceSampler()

    patches = sampler.sample_patches(

        billet

    )

    print()

    print("========== Surface Patches ==========")

    print()

    print(f"Total Patches : {len(patches)}")

    print()

    for i, p in enumerate(patches):

        print(

            f"Patch {i}"

        )

        print(

            f"Center : "

            f"{p.center.x:.1f}, "

            f"{p.center.y:.1f}, "

            f"{p.center.z:.1f}"

        )

        print(

            f"Radius : {p.radius:.1f}"

        )

        print()