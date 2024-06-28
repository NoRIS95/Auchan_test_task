import os
import logging

dirs = ['TEST_Folder_1', 'TEST_Folder_2']
REC_DIR = 'Result'


def rec_file(dir, text_file):
    num_file = (text_file[text_file.find("N_") + 1 : text_file.find(".txt")])
    f = open(f'{dir}/{text_file}', 'r')
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
    if not os.path.exists(REC_DIR):
        os.mkdir(REC_DIR)
    with open(f'{REC_DIR}/TEST_AUCHAN_success{num_file}.txt', 'a') as file:
        for i in sorted(set(nums)):
            file.write(str(i) + '\n')
    return


for dir in dirs:
    if not os.path.exists(dir):
        logging.error(f"Directory {dir} is not found")
        continue
    files_for_dir = os.listdir(dir)
    if len(files_for_dir) == 0:
        logging.warning(f"Directory {dir} is empty")
    for text_file in files_for_dir:
        rec_file(dir, text_file)

