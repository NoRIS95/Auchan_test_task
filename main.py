import os
import logging
import glob


RESULTS_DIR = 'Result'


def process_file(dir, dir_path, file_path):
    with open(file_path, 'r') as f:
        file_name = file_path.replace(f'{dir_path}/', '')
        nums = []
        for string in f:
            string = string.replace('"', '')
        for sym in string.split(','):
            if '-' not in sym:
                num = int(sym)
                nums.append(num)
            else:
                start_finish_nums = sym.split('-')
                for num in range(int(start_finish_nums[0]), int(start_finish_nums[1]) + 1):
                    nums.append(num)
        if not os.path.exists(RESULTS_DIR):
            os.mkdir(RESULTS_DIR)
        with open(f'{RESULTS_DIR}/TEST_AUCHAN_success_{dir}_{file_name}', 'w') as file:
            for i in sorted(set(nums)):
                file.write(str(i) + '\n')
    return


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