import re
import mmap


def get_nprocs(file_name: str) -> int:
    '''
    Extracts nprocs number from orca input file

    Parameters
    ----------
    file_name: str
        Orca input file

    Returns
    -------
    int
        nprocs value
    '''
    pattern = re.compile(
        r' ?%PAL NPROCS (\d+) END'.encode(),
        re.DOTALL | re.IGNORECASE | re.MULTILINE
    )

    with open(file_name, 'rb') as f:
        content = mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_READ)
        it = pattern.findall(content)

    return int(it[0].decode())


def get_maxcore(file_name: str) -> int:
    '''
    Extracts maxcore number from orca input file

    Parameters
    ----------
    file_name: str
        Orca input file

    Returns
    -------
    int
        maxcore value
    '''
    pattern = re.compile(
        r' ?%maxcore (\d+)'.encode(),
        re.DOTALL | re.IGNORECASE | re.MULTILINE
    )

    with open(file_name, 'rb') as f:
        content = mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_READ)
        it = pattern.findall(content)

    return int(it[0].decode())
