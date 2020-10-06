import jsonlines
import re
from Word_vector_github import file_path
from vncorenlp import VnCoreNLP
import time

# java -Xmx2g -jar /home/pham/vncorenlp/VnCoreNLP/VnCoreNLP-1.1.1.jar -fin
# /home/pham/news_data/news_data_no_thanhnien -fout /home/pham/news_data/news_data_tokenized -annotators wseg
# vncorenlp_file = "E:\VnCoreNLP-master\VnCoreNLP-master\VnCoreNLP-1.1.1.jar"

# vncorenlp -Xmx2g E:\VnCoreNLP-master\VnCoreNLP-master\VnCoreNLP-1.1.1.jar -p 9000 -a "wseg"

# data = 'Tuoitre'
# output = data + '_data'
# output = 'test'


def tokenized(infile, outfile):
    count = 0

    with VnCoreNLP(address='http://127.0.0.1', port=9000) as vncorenlp:
        with jsonlines.open(infile + '.json') as file:
            with open(outfile, 'w', encoding='utf-8') as out:
                for obj in file:
                    # tags = obj['tags']
                    if len(obj['tags']) > 1:
                        for tag in obj['tags']:
                            tag = tag.strip()
                            for _ in range(5):
                                try:
                                    tag = vncorenlp.tokenize(tag)
                                    break
                                except:
                                    print("retry")
                                    time.sleep(5)
                            if len(tag) > 1:
                                print("NOPE")
                                for t in tag:
                                    label = ' '.join(t)
                            else:
                                label = ' '.join(tag[0])
                                label = re.sub(r' ', '-', label)
                            # out.write('__label__%s ' % label)
                            out.write(f'__label__{label} ')
                        for _ in range(5):
                            try:
                                word_seg = vncorenlp.tokenize(obj['title'])
                                break
                            except:
                                print('retry')
                                time.sleep(5)
                        if len(word_seg) > 1:
                            print("NOPE-2")
                            for sent in word_seg:
                                seg = ' '.join(sent)
                                out.write(seg + ' ')
                        else:
                            seg = ' '.join(word_seg[0])
                            out.write(f'{seg} ')
                        out.write('\n')
                    print('done line {0}'.format(count))
                    count += 1


tokenized()


# for obj in file:
#     tags = obj['tags']
#     if tags[0]:
#         for tag in tags:
#             tag = tag.strip()
#             tag = re.sub(r' ', '-', tag)
#             print(tag)
