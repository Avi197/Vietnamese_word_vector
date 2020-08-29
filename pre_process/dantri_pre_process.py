import jsonlines
import os
from Word_vector_github import file_path

Dantri_infile = file_path.Dantri
Dantri_data = file_path.Dantri_data

# filename = os.path.dirname(Dantri_data)
# if not os.path.exists(filename):
#     os.makedirs(filename)


"""

"""


def get_dantri(infile):
    count_line = 1

    with jsonlines.open(infile) as file:
        with jsonlines.open(Dantri_data, 'w') as outfile:
            for obj in file:
                
                # condition here
                outfile.write(obj)
                print(f'done line {count_line}')
                count_line += 1
            print(f'wrote to {Dantri_data}')


get_dantri(Dantri_infile)
