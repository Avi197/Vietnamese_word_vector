# Word_vector_github
Pre-processing scripts for news data


using visim-400 data for similarity test
calculate cosine similarity of word pair
compare the cosine similarity to the [0,10] scale similarity of visim data

opposite meaning words don't have ~ 0 cosine similarity, it stay around 0.4 ~ 0.5
news model works better with similar words, word pairs that have similar meaning have much closer cosine similarity to [0,10] scale , but fasttext model has better score overall 



E.g. :
khử_trùng	sát_trùng	9.22

news model: 0.8220183849334717

fasttext_model: 0.6976749300956726

ban_mai	sớm_mai	9.0

news model: 0.7367316484451294

fasttext_model: 0.6704784631729126

rỗi	rỗi_rãi	9.22

0.7575374245643616

0.5365913510322571


khung_thành	cầu_môn	9.0

0.8784187436103821

0.7981183528900146

khấp_khểnh	gập_ghềnh	9.12

0.5719184279441833

0.49278998374938965

mệt_mỏi	mỏi_mệt	9.55

0.8442257642745972

0.8327637910842896
