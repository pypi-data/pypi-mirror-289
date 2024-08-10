def read_loewdin_table(file: str) -> list[dict[str, float]]:

    dfs = []

    with open(file, 'r') as f:
        for line in f:
            if f'LOEWDIN ORBITAL-COMPOSITIONS' in line:
                line = next(f)
                line = next(f)
                line = next(f)
                # Read each subtable into a DF
                while '----' not in line:
                    _str = ''
                    while len(line.lstrip().rstrip()):
                        _str += line
                    dfs.append()

                # Then add to large complete DF

    return
