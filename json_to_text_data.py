import jsonlines
import os
from Word_vector_github import file_path


Dantri_text = file_path.Dantri_text
Tuoitre_text = file_path.Tuoitre_text
Thanhnien_text = file_path.Thanhnien_text
Vnexpress_text = file_path.Vnexpress_text
Vnn_text = file_path.Vnn_text
Vtv_text = file_path.Vtv_text


def get_train_data_vnn(infile, outfile):
    count = 0

    filename = os.path.dirname(outfile)
    if not os.path.exists(filename):
        os.makedirs(filename)

    with jsonlines.open(infile) as file:
        with open(outfile, 'w', encoding='utf-8') as out:
            for obj in file:
                out.write(obj['title'] + '\n')
                out.write(obj['lead'] + '\n')
                for paragraph in obj['content']:
                    out.write(paragraph + '\n')
                print('done line {0}'.format(count))
                count += 1


def get_train_data(infile, outfile):
    count = 0

    filename = os.path.dirname(outfile)
    if not os.path.exists(filename):
        os.makedirs(filename)

    with jsonlines.open(infile) as file:
        with open(outfile, 'w', encoding='utf-8') as out:
            for obj in file:
                out.write(obj['title'] + '\n')
                out.write(obj['description'] + '\n')
                for paragraph in obj['content']:
                    out.write(paragraph + '\n')
                print('done line {0}'.format(count))
                count += 1


get_train_data(file_path.Dantri, Dantri_text)
get_train_data(file_path.Thanhnien, Thanhnien_text)
get_train_data(file_path.Tuoitre, Tuoitre_text)
get_train_data(file_path.Vnexpress, Vnexpress_text)
get_train_data_vnn(file_path.Vnn, Vnn_text)
get_train_data(file_path.Vtv, Vtv_text)

