import os
from topoly import alexander
from topoly.params import TWO_POINTS

def check_alexander()
    xyz_list = os.listdir('xyz')
    for xyz in xyz_list:
        res = alexander(xyz, closure=TWO_POINTS, tries=100, max_cross=60, run_parallel=False)
        print(res)

if __name__ == '__main__':
    print('remember to load venv!')
    check_alexander()
