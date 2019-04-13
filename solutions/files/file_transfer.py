# cambie las rutas a los ficheros para que funcione correctamente la
# solución desde Jupyter Notebook
src_path = '../../resources/files/netflix_shows.csv'
dest_path = '../../resources/files/netflix_shows.min.csv'


def read_csv(filepath):
    info = {}
    with open(filepath) as f:
        # ignore first line with headers
        f.readline()
        for line in f:
            fields = line.strip().split(',')
            serie = fields[0]
            premiere_year = fields[4]
            info[serie] = premiere_year
    return info


def write_csv(filepath, info):
    with open(filepath, 'w') as f:
        for serie, premiere_year in info.items():
            f.write(f'{serie}|{premiere_year}\n')


info = read_csv(src_path)
write_csv(dest_path, info)
