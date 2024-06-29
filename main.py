import os
import logging
import glob


RESULTS_DIR = 'Result'
FIRST_PART_NEW_NAME = 'TEST_AUCHAN_success'


def read_file(file_path, dir_path):
    file_info = {}
    with open(file_path, 'r') as f:
        file_name = file_path.replace(f'{dir_path}/', '')
        for line in f:
            string = line.replace('"', '')
        file_info['File_name'] = file_name
        file_info['String'] = string
    return file_info



def write_file(dir, file_name, nums):
    with open(f'{RESULTS_DIR}/{FIRST_PART_NEW_NAME}_{dir}_{file_name}', 'w') as file:
        for i in nums:
            file.write(str(i) + '\n')


def process_file(dir, dir_path, file_path):
    file_info = read_file(file_path, dir_path)
    nums = []
    for sym in file_info['String'].split(','):
        if '-' not in sym:
            num = int(sym)
            nums.append(num)
        else:
            start_finish_nums = sym.split('-')
            for num in range(int(start_finish_nums[0]), int(start_finish_nums[1]) + 1):
                nums.append(num)
    if not os.path.exists(RESULTS_DIR):
        os.mkdir(RESULTS_DIR)
    sorted_nums = sorted(set(nums))
    write_file(dir, file_info['File_name'], sorted_nums)


if __name__ == '__main__':
    dirs = os.listdir()
    dirs.remove('main.py')
    dirs.remove('README.md')
    dirs.remove('.git')
    for dir in dirs:
        if dir != RESULTS_DIR:
            if not os.path.exists(dir):
                logging.error(f"Directory {dir} is not found")
                continue
            dir_path = f'{os.getcwd()}/{dir}'
            file_pathes_for_dir = glob.glob(dir_path + '/TEST_*')
            if len(file_pathes_for_dir) == 0:
                logging.warning(f"Directory {dir} is empty")
            for file_path in file_pathes_for_dir:
                process_file(dir, dir_path, file_path)