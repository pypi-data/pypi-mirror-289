import numpy as np
from numpy.typing import NDArray
import xyz_py as xyzp


def get_coords(file_name: str, coord_type: str = 'init',
               index_style: str = 'per_element') -> tuple[list, NDArray]:
    '''
    Extracts cartesian coordinates and atom labels from Orca output file

    Parameters
    ----------
    file_name: str
        Name of Orca output file to parse
    coord_type: str, {'init', 'opt'}
        Specifies which set of coordinates to extract\n
        Options are:\n
        "init" = Initial coordinates\n
        "opt" = Final optimised coordinates
    index_style: str {'per_element', 'sequential', 'sequential_orca', 'none'}
        Specifies what type of atom label indexing used for final atom labels\n
        Options are:\n
        'per_element' = Index by element e.g. Dy1, Dy2, N1, N2, etc.\n
        'sequential' = Index the atoms 1->N regardless of element\n
        'sequential_orca' = Index the atoms 0->N-1 regardless of element\n
        'none' = No label indexing

    Returns
    -------
    list
        Atomic labels
    ndarray of floats
        (n_atoms,3) array containing xyz coordinates of each atom
    '''

    labels, coords = [], []

    with open(file_name, 'r') as f:
        for line in f:
            if 'CARTESIAN COORDINATES (ANGSTROEM)' in line:
                labels, coords = [], []
                line = next(f)
                line = next(f)
                while len(line.lstrip().rstrip()):
                    labels.append(line.split()[0])
                    coords.append([float(val) for val in line.split()[1:4]])
                    line = next(f)
                if coord_type.lower() == 'init':
                    break

    if not len(labels):
        raise ValueError(f'Cannot find coordinates in {file_name}')

    if index_style in ['per_element', 'sequential']:
        labels = xyzp.add_label_indices(labels, style=index_style)
    elif index_style == 'sequential_orca':
        labels = xyzp.add_label_indices(
            labels, style='sequential', start_index=0
        )
    else:
        labels = xyzp.remove_label_indices(labels)

    return labels, np.asarray(coords)
