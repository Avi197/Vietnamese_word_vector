import fasttext

fasttext_model_path = "H:/Vietnamese word representations/Fasttext vi.300/cc.vi.300.bin/cc.vi.300.bin"

news_model_path = "H:/Vietnamese word representations/Word2Vec models/v0.3/VnNewsWord2Vec_v0.3.bin"

model = fasttext.load_model(news_model_path)

[model.get_word_vector(x) for x in ["asparagus", "pidgey", "yellow"]]
model.get_nearest_neighbors('mới_tinh')
model.get_nearest_neighbors('tha_thẩn')
model.get_nearest_neighbors('hoàng_gia')
model.get_nearest_neighbors('quỷ_quyệt')
model.get_nearest_neighbors('nguây_nguẩy')
model.get_nearest_neighbors('diễu_hành')
model.get_nearest_neighbors('tập_dượt')
model.get_nearest_neighbors('lắng_nghe')
model.get_nearest_neighbors('Nguyên_Xuân_Phúc')
