import os
from topoly import alexander
from topoly.params import Closure
from tqdm import tqdm

def check_alexander():
    xyz_list = os.listdir('xyz')
    for xyz in tqdm(xyz_list):
        res = alexander('xyz/{}'.format(xyz), closure=Closure.TWO_POINTS,
                        tries=100, max_cross=60, run_parallel=False)
        res = str(res).replace(' ','')[1:-1]
        with open('alexander.txt', 'w') as f:
            f.write('{} {}\n'.format(xyz,res))

if __name__ == '__main__':
    print('remember to load venv!')
    check_alexander()
