import fasttext
import csv
import pandas
import sklearn.metrics.pairwise as sk
from gensim.models.fasttext import load_facebook_vectors
from scipy.spatial import distance


# with open(visim, newline='', encoding='utf-8') as csvfile:
#     simreader = csv.reader(csvfile, delimiter=' ')
#     for row in simreader:
#         print(row)
# fields = ['Word1', 'Word2', 'Sim2']
# df = pandas.read_csv(visim, sep='\t', skipinitialspace=True, usecols=fields)

# .iloc[row num, column num]
# df.iloc[0, 0])
model_location = "H:/Vietnamese word representations/result/news.bin"
fasttext_model = "H:/Vietnamese word representations/Fasttext vi.300/cc.vi.300.bin/cc.vi.300.bin"
visim_location = "H:/Vietnamese word representations/Analogy task/ViData/ViData/ViSim-400/Visim-400.txt"
fasttext_result = "H:/Vietnamese word representations/Word_vector_github/cossim_result_fasttext_model.txt"
model_result = "H:/Vietnamese word representations/Word_vector_github/cossim_result.txt"


def cossim_compare(infile, outfile, visim):
    fields = ['Word1', 'Word2', 'Sim2']
    df = pandas.read_csv(visim, sep='\t', skipinitialspace=True, usecols=fields)
    print('loading model')
    model = load_facebook_vectors(infile)
    print('calculating cosine similarity')
    score_list = []
    with open(outfile, 'w') as result:
        for i in range(df.shape[0]):
            word1 = model[(df.iloc[i, 0])]
            word2 = model[(df.iloc[i, 1])]
            similarity = df.iloc[i, 2] / 10
            cossim = 1 - distance.cosine(word1, word2)
            result.write(f'{cossim}\t{similarity}\n')
            score = cossim - similarity
            score_list.append(abs(score))

    with open(outfile, 'a') as result:
        score = sum(score_list)
        result.write(str(score))


# cossim_compare(fasttext_model, fasttext_result, visim_location)
cossim_compare(model_location, model_result, visim_location)


# model = load_facebook_vectors("H:/Vietnamese word representations/result/news.bin")
# word1 = model[(df.iloc[27, 0])]
# word2 = model[(df.iloc[27, 1])]
# cossim = sk.cosine_similarity(word1, word2)
# similarity = df.iloc[27, 2] / 10
# print(cossim, similarity)

