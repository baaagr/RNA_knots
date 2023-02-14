from topoly import alexander
from topoly.params import Closure
from tqdm import tqdm

def check_alexander(last_cif):
    xyz_list = []
    with open('lists/xyz_files.txt', 'r') as f:
        for i, line in enumerate(f.readlines()):
            line_s = line.strip()
            #print('{:3d} {:16} {:16} {}'.format(i+1, last_cif, line_s, str(last_cif == line_s)))
            if last_cif:
                if last_cif == line_s:
                    last_cif = ''
            else:
                xyz_list.append(line_s)
    for xyz in tqdm(xyz_list):
    #for xyz in xyz_list:
        res = alexander('xyz/{}'.format(xyz), closure=Closure.TWO_POINTS,
                        tries=100, max_cross=60, run_parallel=False)
        res = str(res).replace(' ','')[1:-1]
        with open('alexander.txt', 'a+') as f:
            f.write('{} {}\n'.format(xyz,res))

def where_ended():
    try:
        with open('alexander.txt', 'r') as f:
            last_cif = f.readlines()[-1].split()[0]
    except:
        last_cif = ''
    return last_cif

if __name__ == '__main__':
    print('remember to load venv!')
    #with open('alexander.txt', 'w') as f:
    #    pass
    last_cif = where_ended()
    check_alexander(last_cif)
