# Word_vector_github

using visim-400 data for similarity test
calculate cosine similarity of word pair
compare the cosine similarity to the [0,10] scale similarity of visim data

Tokenized using VnCoreNlp

opposite meaning words don't have ~ 0 cosine similarity, it stay around 0.4 ~ 0.5
news model works better with similar words, word pairs that have similar meaning have much closer cosine similarity to [0,10] scale , but fasttext model has better score overall 

Train using Fasttext with these parameter
```-min 2 -max 5 -dim 200 -epoch 3```  


#### Similarity test
Using Visim dataset to test similarity of pair words

word_1  word_2  score/1 (2 similar meaning word will have score closer to 1)
news model (1): this model trained using Vietnamese news
fasttext_model (2): the model trained by Mikolov using wiki
```
khử_trùng	sát_trùng	0.922  
news model (1): 0.8220183849334717  
fasttext_model (2): 0.6976749300956726  
  
ban_mai	sớm_mai	0.9  
(1): 0.7367316484451294  
(2): 0.6704784631729126  
  
rỗi	rỗi_rãi	0.922  
(1): 0.7575374245643616  
(2): 0.5365913510322571  
  
khung_thành	cầu_môn	0.90  
(1): 0.8784187436103821  
(2): 0.7981183528900146  
  
khấp_khểnh	gập_ghềnh	0.912  
(1): 0.5719184279441833  
(2): 0.49278998374938965  
  
mệt_mỏi	mỏi_mệt	0.955  
(1): 0.8442257642745972  
(2): 0.8327637910842896  
```

#### Analogy test

A proportional analogy holds between two word pairs: a:a* :: b:b* (a is to a* as b is to b*) For example, Tokyo is to Japan as Paris is to France.\
With the pair-based methods, given a:a* :: b:?, the task is to find b*.\
With set-based methods, the task is to find b* given a set of other pairs (excluding b:b*) that hold the same relation as b:b*.\

Analogy score closer to 1 is better

```
("Hà_Nội","Việt_Nam", "Campuchia")   (0.6863046288490295, 'Phnom_Penh')

("Tổng_bí_thư", "Nguyễn_Phú_Trọng", "Nguyễn_Xuân_Phúc")  (0.8964422345161438, 'Thủ_tướng')
("Chủ_tịch","Hồ_Chí_Minh", "Nguyễn_Phú_Trọng")   (0.7754886150360107, 'Tổng_Bí_thư')

("chậm", "nhanh", "cao") (0.7500340342521667, 'thấp')

("đô_la","Mỹ", "Trung_Quốc") (0.7915549278259277, 'nhân_dân_tệ')
("USD","Mỹ", "Trung_Quốc")   (0.8098106384277344, 'nhân_dân_tệ')

("cô","chú", "anh")  (0.7152935266494751, 'chị')
("dì","chú", "anh")  (0.7390031218528748, 'chị')

("chạy_án","Con_ông_cháu_cha", "quan_liêu")
[(0.6325034499168396, 'chạy_tội'), (0.6051946878433228, 'nhũng_nhiễu'), (0.6001415848731995, 'tham_nhũng'), (0.5994342565536499, 'tham_ô'), (0.5857940912246704, 'Quan_liêu')
, (0.5827884674072266, 'nhũng_lạm'), (0.5800005197525024, 'rửa_tiền'), (0.5690904259681702, 'hối_lộ'), (0.5688171982765198, 'tư_pháp'), (0.5666439533233643, 'tố_tụng')]
```


##### SentencePiece tokenizer vs VnCoreNLP

```
Input
'Sở Y tế TP Hà Nội vừa thông tin trường hợp mắc SARS-CoV-2 mới, từng ở cùng phòng với bệnh nhân 1034 cách ly tại Hải Dương về TP Hà Nội sau 14 ngày cách ly.'
```
```
VnCoreNLP
['Sở', 'Y_tế', 'TP', 'Hà_Nội', 'vừa', 'thông_tin', 'trường_hợp', 'mắc', 'SARS-CoV', '-2', 'mới', 'từng', 'ở', 'cùng', 'phòng', 'với', 'bệnh_nhân', '1034', 'cách_ly', 'tại', 'Hải_Dương', 'về', 'TP', 'Hà_Nội', 'sau', '14', 'ngày', 'cách_ly', '.']


SentencePiece:
['▁Sở▁Y▁tế▁TP', '▁Hà▁Nội', '▁vừa', '▁thông▁tin', '▁trường▁hợp', '▁mắc', '▁SARS', '-', 'CoV', '-2', '▁mới', ',', '▁từng', '▁ở', '▁cùng', '▁phòng', '▁với', '▁bệnh▁nhân', '▁10', '34', '▁cách▁ly', '▁tại', '▁Hải▁Dương', '▁về', '▁TP▁Hà▁Nội', '▁sau', '▁14', '▁ngày', '▁cách▁ly', '.']  
```
