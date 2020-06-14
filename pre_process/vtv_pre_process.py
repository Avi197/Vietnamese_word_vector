import jsonlines
from Word_vector_github import file_path
from langdetect import detect
import os.path


Vtv = file_path.Vtv
Vtv_data = file_path.Vtv_data

filename = os.path.dirname(Vtv_data)
if not os.path.exists(filename):
    os.makedirs(filename)


# check if title is in bad_title list
def check_bad_title(obj, bad_title_list=None):
    title = obj['title']
    title = title.strip()
    if bad_title_list is not None:
        count = 0
        for bad_title in bad_title_list:
            if bad_title in title:
                count += 1
        return count > 0


def check_english(tags, english_keys):
    for tag in tags:
        count = 0
        if english_keys not in tag:
            count += 1
        if count == 0:
            return True


# check for vietnamese news
# remove bad titles
# write to new file
def get_data_vtv(infile, bad_title_list='', english_keys=''):
    count_line = 1

    with jsonlines.open(infile) as infile:
        with jsonlines.open(Vtv_data, 'w') as outfile:
            for obj in infile:
                title = obj['title']
                if detect(title) == 'vi':
                    if not check_bad_title(obj, bad_title_list):
                        outfile.write(obj)
                print(f'done line {count_line}')
                count_line += 1
            print(f'wrote to {Vtv_data}')


get_data_vtv(Vtv)


#


#


#


#


#


# TESTING SECTION
# ------------------------------------------------------------------------------------------------------
# get_data_vnn(Vnn, vnn_bad_tags)

# name = Vnn.replace('.json', '')
# name = f'{name}_data'
# remove_english_news(f'{name}_data', vnn_english)
# Vnn_vi = 'H:/Vietnamese word representations/Text_classification_data/Vnn/Vnn_vi_1'

# check_english_news(Vnn, vnn_english)
# check_vi_news(Vnn, vnn_english)


# 1
# remove_english_news(Vnn, vnn_english)

# 2
# remove_english_news(Vnn, vnn_english, '3')


# QUARANTINE SECTION
# PURPOSE UNKNOWN
# ------------------------------------------------------------------------------------------------------
# # Vnn has some english news
# # what for?
# def remove_english_news(infile, english_keys, num=''):
#     count_line = 1
#
#     if 'json' in infile:
#         file_name = infile.replace('.json', '')
#     else:
#         file_name = infile
#     with jsonlines.open(infile) as infile:
#         with jsonlines.open(f'{file_name}_no_english_{num}', 'w') as outfile:
#             for obj in infile:
#                 tags = obj['tags']
#                 title = obj['title']
#                 if not check_english(tags, english_keys):
#                     if detect(title) == 'vi':
#                         outfile.write(obj)
#                 # title = obj['title']
#                 # if detect(title) != 'en':
#                 #     outfile.write(obj)
#                     # json.dump(obj, outfile, indent=2, ensure_ascii=False)
#
#                 print(f'done line {count_line}')
#                 count_line += 1
#             print(f'wrote to {file_name}_no_english')
#
#
# def check_vi_news(infile, num=''):
#     count_line = 1
#
#     if 'json' in infile:
#         file_name = infile.replace('.json', '')
#     else:
#         file_name = infile
#     with jsonlines.open(infile) as infile:
#         with jsonlines.open(f'{file_name}_vi_{num}', mode='w') as outfile:
#             for obj in infile:
#                 title = obj['title']
#                 if detect(title) == 'vi':
#                     outfile.write(obj)
#                 print(f'done line {count_line}')
#                 count_line += 1
#             print(f'wrote to {file_name}_vi')
#
#
# def check_english_news(infile, english_keys):
#     count_line = 1
#     if 'json' in infile:
#         file_name = infile.replace('.json', '')
#     else:
#         file_name = infile
#     with jsonlines.open(infile) as infile:
#         with jsonlines.open(f'{file_name}_english', mode='w') as outfile:
#             for obj in infile:
#                 title = obj['title']
#                 if detect(title) == 'en':
#                     outfile.write(obj)
#                     # json.dump(obj, outfile, indent=2, ensure_ascii=False)
#
#                 print(f'done line {count_line}')
#                 count_line += 1
#             print(f'wrote to {file_name}_english')
# --------------------------------------------------------------------------------------------------------




