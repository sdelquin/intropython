src_path = '../../resources/netflix_shows.csv'
dest_path = '../../resources/netflix_shows.min.csv'

info = {}

# Read of source file
with open(src_path) as f:
    # ignore first line with headers
    f.readline()
    for line in f:
        fields = line.strip().split(',')
        serie = fields[0]
        premiere_year = fields[4]
        info[serie] = premiere_year

# Write of target file
with open(dest_path, 'w') as f:
    for serie, premiere_year in info.items():
        f.write(f'{serie}|{premiere_year}\n')
