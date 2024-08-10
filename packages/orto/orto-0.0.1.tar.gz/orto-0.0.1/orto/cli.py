import argparse
import xyz_py as xyzp
import matplotlib.pyplot as plt
import os
import copy

from . import reader
from . import plotter
from . import extractor
from . import job
from . import utils as ut
from . import input


def extract_coords_func(uargs):
    '''
    Wrapper for extract_coords function
    '''

    # Open file and extract coordinates
    labels, coords = extractor.get_coords(
        uargs.file_name,
        coord_type=uargs.type,
        index_style=uargs.index_style
    )

    # Save to new .xyz file
    head = os.path.splitext(uargs.file_name)[0]
    xyzp.save_xyz(
        f'{head}_coords.xyz',
        labels,
        coords,
        comment=f'Coordinates extracted from {uargs.file_name}'
    )

    return


def gen_job_func(uargs):
    '''
    Wrapper for CLI gen_job call

    Parameters
    ----------
    uargs : argparser object
        User arguments

    Returns
    -------
    None
    '''

    oj = job.OrcaJob(
        uargs.file_name
    )

    # Get orca module and pre- and post- commands
    orca_args = [
        'orca_load',
        'pre_orca',
        'post_orca'
    ]

    required = [
        'orca_load'
    ]

    for oarg in orca_args:
        uarg_val = getattr(uargs, oarg)
        if len(uarg_val):
            oarg_val = copy.copy(uarg_val)
        elif os.getenv(f'orto_{oarg}'):
            try:
                if len(os.getenv(f'orto_{oarg}')):
                    oarg_val = os.getenv(f'orto_{oarg}')
            except ValueError:
                ut.red_exit(
                    (
                        f'Error in orto_{oarg} environment variable'
                    )
                )
        elif oarg in required:
            ut.red_exit(
                (
                    f'Missing orto_{oarg} environment variable or '
                    f'--{oarg} argument'
                )
            )
        else:
            oarg_val = ''

        if oarg == 'orca_load':
            oarg = 'load'
            oarg_val = f'{oarg_val}'
        setattr(oj, oarg, oarg_val)

    # Load submission system config from template file, either from cli
    # or environment variable
    if len(uargs.sub_template):
        config = oj.scheduler_job_class.read_template_file(
            uargs.sub_template
        )
    elif os.getenv('orto_sub_template'):
        config = oj.scheduler_job_class.read_template_file(
            os.getenv('orto_sub_template')
        )
    else:
        config = {}

    # Load number of procs and amount of memory from orca input file
    n_procs = input.get_nprocs(uargs.file_name)
    maxcore = input.get_maxcore(uargs.file_name)

    # If memory and procs specified as arguments, give warning when
    # these dont match numbers in orca input file
    if n_procs > uargs.n_procs:
        ut.red_exit('Too few processors requested for input file')
    elif n_procs < uargs.n_procs:
        ut.cprint(
            (
                'Warning: Requesting more cores than in input file\n'
                '            ... this may be fine!'
            ),
            'yellow'
        )
    config['ntasks_per_node'] = n_procs

    if uargs.memory > 0:
        if uargs.memory * uargs.n_procs < n_procs * maxcore:
            ut.red_exit('Requested too little memory for orca input')
        config['mem_per_cpu'] = uargs.memory
    elif 'mem_per_cpu' not in config.keys():
        ut.red_exit(
            'Missing mem_per_cpu in both command line and template file'
        )

    # Write job script
    oj.write_script(True, **config)

    return


def plot_uvvis_func(uargs):
    '''
    Wrapper for CLI plot_uvvis call

    Parameters
    ----------
    uargs : argparser object
        User arguments

    Returns
    -------
    None
    '''

    # Read output file
    wavenumbers, fosc, p2 = reader.read_uvvis(
        uargs.file_name,
        uargs.intensity_type
    )

    if uargs.x_lim is None:
        if uargs.x_unit == 'wavenumber':
            uargs.x_lim = [0, 50000]
        if uargs.x_unit == 'wavelength':
            # 1 to 2000 nm
            uargs.x_lim = [5000., 10000000.]

    # Plot uvvis spectrum
    fig, ax = plotter.plot_uvvis(
        wavenumbers,
        fosc,
        show=False,
        x_lim=uargs.x_lim,
        y_lim=uargs.y_lim,
        x_unit=uargs.x_unit,
        linewidth=uargs.linewidth,
        lineshape=uargs.lineshape,
        window_title=f'UV-Visible Spectrum from {uargs.file_name}',
        show_osc=not uargs.no_osc
    )

    if uargs.x_unit == 'wavenumber':
        ax[0].set_xlim([0, 50000])
    if uargs.x_unit == 'wavelength':
        ax[0].set_xlim([0, 2000])
    plt.show()

    return


def plot_ir_func(uargs):
    '''
    Wrapper for CLI plot_ir call

    Parameters
    ----------
    uargs : argparser object
        User arguments

    Returns
    -------
    None
    '''

    # Read output file
    wavenumbers, intensities, _ = reader.read_infrared(
        uargs.file_name
    )
    # Plot uvvis spectrum
    fig, ax = plotter.plot_ir(
        wavenumbers,
        intensities,
        linewidth=uargs.linewidth,
        lineshape=uargs.lineshape,
        window_title=f'Infrared Spectrum from {uargs.file_name}'
    )

    return


def read_args(arg_list=None):
    '''
    Reader for command line arguments. Uses subReaders for individual programs

    Parameters
    ----------
        args : argparser object
            command line arguments

    Returns
    -------
        None

    '''

    description = '''
    A package for working with Orca
    '''

    epilog = '''
    To display options for a specific program, use splash \
    PROGRAMFILETYPE -h
    '''
    parser = argparse.ArgumentParser(
        description=description,
        epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    subparsers = parser.add_subparsers(dest='prog')

    extract_coords = subparsers.add_parser(
        'extract_coords',
        description='Extracts coordinates from Orca output file'
    )
    extract_coords.set_defaults(func=extract_coords_func)

    extract_coords.add_argument(
        'file_name',
        type=str,
        help='Orca output file name(s)'
    )

    extract_coords.add_argument(
        '--type',
        type=str,
        help='Which coordinates to extract',
        choices=['opt', 'init'],
        default='init'
    )

    extract_coords.add_argument(
        '--index_style',
        type=str,
        help='Style of indexing used for output atom labels',
        choices=['per_element', 'sequential', 'sequential_orca', 'none'],
        default='per_element'
    )

    gen_job = subparsers.add_parser(
        'gen_job',
        description='Generate submission script for orca calculation'
    )
    gen_job.set_defaults(func=gen_job_func)

    gen_job.add_argument(
        'file_name',
        type=str,
        help='Orca output file name(s)'
    )

    gen_job.add_argument(
        'n_procs',
        type=int,
        help=(
            'Number of cores requested in submission system\n'
            ' This does not need to match the orca input, but must not be less'
        )
    )

    gen_job.add_argument(
        '--memory',
        '-mem',
        type=int,
        default=0,
        help=(
            'Per core memory requested in submission system\n'
            ' This does not need to match the orca input, but must not be less'
        )
    )

    gen_job.add_argument(
        '-st',
        '--sub_template',
        type=str,
        default='',
        help='Template file for submission system'
    )

    gen_job.add_argument(
        '-om',
        '--orca_load',
        type=str,
        default='',
        help='Orca environment module (overrides environment variable)'
    )

    gen_job.add_argument(
        '-pre',
        '--pre_orca',
        type=str,
        default='',
        help='Commands to include before Orca call'
    )

    gen_job.add_argument(
        '-post',
        '--post_orca',
        type=str,
        default='',
        help='Commands to include after Orca call'
    )

    plot_uvvis = subparsers.add_parser(
        'plot_uvvis',
        description='Plots uvvis spectrum from CI calculation output'
    )
    plot_uvvis.set_defaults(func=plot_uvvis_func)

    plot_uvvis.add_argument(
        'file_name',
        type=str,
        help='Orca output file name(s)'
    )

    plot_uvvis.add_argument(
        '--intensity_type',
        type=str,
        choices=['velocity', 'electric'],
        default='electric',
        help='Type of intensity to plot (orca_mapspc uses electric)'
    )

    plot_uvvis.add_argument(
        '--linewidth',
        '-lw',
        type=float,
        default=2000,
        help=(
            'Width of signal (FWHM for Gaussian, Width for Lorentzian),'
            ' in Wavenumbers'
        )
    )

    plot_uvvis.add_argument(
        '--no_osc',
        action='store_true',
        help=(
            'Disables oscillator strength stem plots'
        )
    )

    plot_uvvis.add_argument(
        '--lineshape',
        '-ls',
        type=str,
        choices=['gaussian', 'lorentzian'],
        default='lorentzian',
        help='Lineshape to use for each signal'
    )

    plot_uvvis.add_argument(
        '--x_unit',
        type=str,
        choices=['wavenumber', 'wavelength'],
        default='wavelength',
        help='x units to use for spectrum'
    )

    plot_uvvis.add_argument(
        '--x_lim',
        type=float,
        nargs=2,
        help='Wavenumber or Wavelength limits of spectrum'
    )

    plot_uvvis.add_argument(
        '--y_lim',
        nargs=2,
        default=['auto', 'auto'],
        help='Epsilon limits of spectrum in cm^-1 mol^-1 L'
    )

    plot_ir = subparsers.add_parser(
        'plot_ir',
        description='Plots IR spectrum from frequency calculation output'
    )
    plot_ir.set_defaults(func=plot_ir_func)

    plot_ir.add_argument(
        'file_name',
        type=str,
        help='Orca output file name(s)'
    )

    plot_ir.add_argument(
        '--linewidth',
        '-lw',
        type=float,
        default=2000,
        help=(
            'Width of signal (FWHM for Gaussian, Width for Lorentzian),'
            ' in Wavenumbers'
        )
    )

    plot_ir.add_argument(
        '--lineshape',
        '-ls',
        type=str,
        choices=['gaussian', 'lorentzian'],
        default='lorentzian',
        help='Lineshape to use for each signal'
    )

    # If argument list is none, then call function func
    # which is assigned to help function
    parser.set_defaults(func=lambda _: parser.print_help())

    # read sub-parser
    _args, _ = parser.parse_known_args(arg_list)

    # select parsing option based on sub-parser
    if _args.prog in ['rst_opt']:
        args, job_args = parser.parse_known_args(arg_list)
        args.func(args, job_args)
    else:
        args = parser.parse_args(arg_list)
        args.func(args)
    return args


def interface():
    read_args()
    return
