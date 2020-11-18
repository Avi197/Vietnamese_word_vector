from vncorenlp import VnCoreNLP
import pandas as pd
import time
import itertools
# import file_path

"H:/Vietnamese word representations/VncoreNLP_lite/VnCoreNLP-1.1.1.jar"
# vncorenlp -Xmx500m "H:/Vietnamese word representations/VncoreNLP_lite/VnCoreNLP-1.1.1.jar" -p 9000 -a "wseg"

# datafile = 'H:/Vietnamese word representations/Data/Dantri_title_link_category_with_header.csv'
dummy = 'H:/Vietnamese word representations/Data/dummy.csv'
datafile_tokenized = 'H:/Vietnamese word representations/Data/Dantri_title_link_category_tokenized.csv'


# def tokenizer(text):
#     print(text)
#     try:
#         word_seg = vncorenlp.tokenize(text)
#     except:
#         time.sleep(5)
#     seg = list(itertools.chain.from_iterable(word_seg))
#     sent = ' '.join(seg)
#     return sent


def tokenized_file(infile, outfile):
    count = 0
    with VnCoreNLP(address='http://127.0.0.1', port=9000) as vncorenlp:
        df = pd.read_csv(infile)
        for i, row in df.iterrows():
            try:
                word_seg = vncorenlp.tokenize(row['title'])
            except:
                time.sleep(5)
            seg = list(itertools.chain.from_iterable(word_seg))
            sent = ' '.join(seg)
            df.at[i, 'title'] = sent
            print(f'done line {count}')
            count += 1
        df.to_csv(outfile, header=None, index=None)
        # df['title'] = df['title'].apply(lambda row: tokenizer, axis=1)
        # df.to_csv(outfile, mode='a', header=None)

    print(f'done {infile}')

# for i, row in df.iterrows():
#     ifor_val = something
#     if <condition>:
#         ifor_val = something_else
#     df.at[i,'ifor'] = ifor_val

tokenized_file(dummy, datafile_tokenized)

# tokenized(file_path.Tuoitre_text, file_path.Tuoitre_tokenized)
# tokenized(file_path.Vnexpress_text, file_path.Vnexpress_tokenized)
# tokenized(file_path.Vnn_text, file_path.Vnn_tokenized)
