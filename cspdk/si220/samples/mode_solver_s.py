"""Silicon mode solver."""

import gplugins.tidy3d as gt

nm = 1e-3

if __name__ == "__main__":
    wg_sc = gt.modes.Waveguide(
        wavelength=1.55,
        core_width=0.45,
        core_thickness=0.22,
        slab_thickness=0.0,
        core_material="si",
        clad_material="sio2",
        group_index_step=10 * nm,
    )

    print("wg_sc_ng = ", wg_sc.n_group)
    print("wg_sc_neff = ", wg_sc.n_eff)

    wg_so = gt.modes.Waveguide(
        wavelength=1.31,
        core_width=0.40,
        core_thickness=0.22,
        slab_thickness=0.0,
        core_material="si",
        clad_material="sio2",
        group_index_step=10 * nm,
    )

    print("wg_so_ng = ", wg_so.n_group)
    print("wg_so_neff = ", wg_so.n_eff)
