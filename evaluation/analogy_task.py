import fasttext
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

news_model_path = "H:/Vietnamese word representations/Word2Vec models/v0.3/VnNewsWord2Vec_v0.3.bin"
fasttext_model_path = "H:/Vietnamese word representations/Fasttext vi.300/cc.vi.300.bin"
news_model = fasttext.load_model(news_model_path)
fasttext_model = fasttext.load_model(fasttext_model_path)

higher_than_7 = "H:/Vietnamese word representations/Word_vector_github/evaluation/Visim-400_higher_than_7"
result = "H:/Vietnamese word representations/Word_vector_github/evaluation/result"
df = pd.read_csv(higher_than_7, sep='\t')

with open(result, mode='a', encoding='utf-8') as file:
    file.write(f'Word1\tWord2\tSim\tFt_cossim\tVn_cossim\tFt_diff\tVn_diff\n')
    ft_total_diff = 0
    vn_total_diff = 0
    for index, row in df.iterrows():
        word1 = row['Word1']
        word2 = row['Word2']
        sim = row['Sim2'] / 10

        ft_w1_vec, ft_w2_vec = [fasttext_model.get_word_vector(x) for x in [word1, word2]]
        vn_w1_vec, vn_w2_vec = [news_model.get_word_vector(x) for x in [word1, word2]]

        ft_cossim = (cosine_similarity([ft_w1_vec], [ft_w2_vec]))
        vn_cossim = (cosine_similarity([vn_w1_vec], [vn_w2_vec]))

        ft_cossim = ft_cossim[0][0]
        vn_cossim = vn_cossim[0][0]

        ft_diff = ft_cossim - sim
        vn_diff = vn_cossim - sim

        ft_total_diff += ft_diff
        vn_total_diff += vn_diff

        file.write(f'{word1}\t{word2}\t{sim:.2f}\t{ft_cossim:.2f}\t{vn_cossim:.2f}\t{ft_diff:.2f}\t{vn_diff:.2f}\n')

    file.write(f'fasttext_sum_difference:\t{ft_total_diff}\nnews_sum_difference:\t{vn_total_diff}')
    # file.write(f'fasttext_sum_difference:\t{ft_total_diff}\t|\t{ft_total_diff/}\nnews_sum_difference:\t{vn_total_diff}')



# [model.get_word_vector(x) for x in []]


