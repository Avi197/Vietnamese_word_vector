from vncorenlp import VnCoreNLP
import time
import file_path


# vncorenlp -Xmx500m /home/pham/VnCoreNLP-master/VnCoreNLP-1.1.1.jar -p 9000 -a "wseg"


def tokenized(infile, outfile):
    count = 0
    with VnCoreNLP(address='http://127.0.0.1', port=9000) as vncorenlp:
        with open(infile, encoding='utf-8') as file:
            with open(outfile, 'w', encoding='utf-8') as out:
                for line in file:
                    if line:
                        try:
                            word_seg = vncorenlp.tokenize(line)
                        except:
                            time.sleep(5)
                        for sent in word_seg:
                            seg = ' '.join(sent)
                            out.writelines(seg + '\n')
                        print('done line ' + str(count))
                    count += 1
    print(f'done {infile}')


# tokenized(file_path.Dantri_text, file_path.Dantri_tokenized)
tokenized(file_path.datafile, file_path.datafile_tokenized)
# tokenized(file_path.Tuoitre_text, file_path.Tuoitre_tokenized)
# tokenized(file_path.Vnexpress_text, file_path.Vnexpress_tokenized)
# tokenized(file_path.Vnn_text, file_path.Vnn_tokenized)
# tokenized(file_path.Vtv_text, file_path.Vtv_tokenized)
