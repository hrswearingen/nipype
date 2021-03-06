# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..model import Randomise


def test_Randomise_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        base_name=dict(
            argstr='-o "%s"',
            position=1,
            usedefault=True,
        ),
        c_thresh=dict(
            argstr="-c %.1f",
        ),
        cm_thresh=dict(
            argstr="-C %.1f",
        ),
        demean=dict(
            argstr="-D",
        ),
        design_mat=dict(
            argstr="-d %s",
            extensions=None,
            position=2,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        f_c_thresh=dict(
            argstr="-F %.2f",
        ),
        f_cm_thresh=dict(
            argstr="-S %.2f",
        ),
        f_only=dict(
            argstr="--f_only",
        ),
        fcon=dict(
            argstr="-f %s",
            extensions=None,
        ),
        in_file=dict(
            argstr="-i %s",
            extensions=None,
            mandatory=True,
            position=0,
        ),
        mask=dict(
            argstr="-m %s",
            extensions=None,
        ),
        num_perm=dict(
            argstr="-n %d",
        ),
        one_sample_group_mean=dict(
            argstr="-1",
        ),
        output_type=dict(),
        p_vec_n_dist_files=dict(
            argstr="-P",
        ),
        raw_stats_imgs=dict(
            argstr="-R",
        ),
        seed=dict(
            argstr="--seed=%d",
        ),
        show_info_parallel_mode=dict(
            argstr="-Q",
        ),
        show_total_perms=dict(
            argstr="-q",
        ),
        tcon=dict(
            argstr="-t %s",
            extensions=None,
            position=3,
        ),
        tfce=dict(
            argstr="-T",
        ),
        tfce2D=dict(
            argstr="--T2",
        ),
        tfce_C=dict(
            argstr="--tfce_C=%.2f",
        ),
        tfce_E=dict(
            argstr="--tfce_E=%.2f",
        ),
        tfce_H=dict(
            argstr="--tfce_H=%.2f",
        ),
        var_smooth=dict(
            argstr="-v %d",
        ),
        vox_p_values=dict(
            argstr="-x",
        ),
        x_block_labels=dict(
            argstr="-e %s",
            extensions=None,
        ),
    )
    inputs = Randomise.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Randomise_outputs():
    output_map = dict(
        f_corrected_p_files=dict(),
        f_p_files=dict(),
        fstat_files=dict(),
        t_corrected_p_files=dict(),
        t_p_files=dict(),
        tstat_files=dict(),
    )
    outputs = Randomise.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
