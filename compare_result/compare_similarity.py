# -*- coding: utf-8 -*-

"""

"""

__author__ = 'Zhang'
__version__ = '3.8.5'
__create__ = '2022-04-08 2:19 PM'
__modify__ = '2022-04-08 2:19 PM'

# coding: utf-8
import os
import re


def readLines(filepath):
    lines = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print(filepath, 'Read success!')
    except Exception:
        with open(filepath, 'r', encoding='gbk') as f:
            lines = f.readlines()
    return lines


def compare(file1, file2):
    text1 = readLines(file1)
    text2 = readLines(file2)

    # text1 = text1[0].split('<user name=')
    text1 = re.split(r'<user name=|<review>|</users>|<review_t', text1[0])
    text2 = re.split(r'<user name=|<review>|</users>|<review_t', text2[0])
    print(len(text1))
    print(len(text2))

    count = 0.
    for line in text1:
        if text2.count(line) > 0:
            count += 1
        # else:
        #     print(line) # 查看哪些行不一样
    print('similarity result =', count / max(len(text1), len(text2)))
    return count / max(len(text1), len(text2))


def compare_all_in_folder(folder):
    path = folder  # 输入文件夹路径，根据实际情况决定。
    dirs = os.listdir(path)
    files = []
    error_files = []
    for file in dirs:
        files.append(os.path.join(path, file))

    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            try:
                degree = compare(files[i], files[j])
                if degree > 0.7:
                    print("{}和{}的相似度为：{:.2%}".format(files[i].split(" ")[0], files[j].split(" ")[0], degree).replace(
                        folder + "\\", ""))
            except Exception as e:
                if error_files.count(j) == 0:
                    error_files.append(j)
                continue


compare_all_in_folder('result_folder')


# 0.41156419643984343
# 0.5163489458401717
# 0.41181668981189246
# 0.4120691831839414
# 0.542608256533266
# 0.542608256533266
# 0.5672809896490785

# 0.9120114074819661
# 0.9554604932058379






# print(re.split(r',| ', '07 9, 2014'))

# def deal_text_return(text):
#     one_line_text = ''
#     for line in text.split('\n'):
#         if len(line.strip()) == 0:
#             one_line_text += ''
#         elif re.match(r'[^\w\s]',line[-1]):
#             print(line)
#             one_line_text += line+' '
#         else:
#             one_line_text += line+ '. '
#     return one_line_text.strip()
#
# print('xxxxx!\n \n ssssss\n eeeee')
# print(deal_text_return('xxxxx!\n \n ssssss\n eeeee'))
#
#
# print(len(re.sub(r'[^\w\s]','','xxxxx!'[-1])))