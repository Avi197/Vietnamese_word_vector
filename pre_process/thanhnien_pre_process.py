import jsonlines
import os
from Word_vector_github import file_path

Thanhnien_infile = file_path.Thanhnien
Thanhnien_data = file_path.Thanhnien_data

filename = os.path.dirname(Thanhnien_data)
if not os.path.exists(filename):
    os.makedirs(filename)


"""

"""


def get_tuoitre_vnexpress(infile):
    count_line = 1

    with jsonlines.open(infile) as file:
        with jsonlines.open(Thanhnien_data, 'w') as outfile:
            for obj in file:
                # condition here
                outfile.write(obj)
                print(f'done line {count_line}')
                count_line += 1
            print(f'wrote to {Thanhnien_data}')


get_tuoitre_vnexpress(Thanhnien_infile)
