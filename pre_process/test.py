import sentencepiece as spm
from vncorenlp import VnCoreNLP

# vncore_path = "E:/VnCoreNLP-master/VnCoreNLP-master/VnCoreNLP-1.1.1.jar"
# vncorenlp -Xmx500m "E:/VnCoreNLP-master/VnCoreNLP-master/VnCoreNLP-1.1.1.jar" -p 9000 -a "wseg"


# annotator = VnCoreNLP(address="http://127.0.0.1", port=9000)
#
# string = 'Sở Y tế TP Hà Nội vừa thông tin trường hợp mắc SARS-CoV-2 mới, từng ở cùng phòng với bệnh nhân 1034 cách ly tại Hải Dương về TP Hà Nội sau 14 ngày cách ly.'
# string2 = 'Chiều28/8,báocáotạicuộchọpBanchỉđạo phòng chốngCovid-19 TP HàNội, ông Hoàng Đức Hạnh - Phó Giám đốc Sở Y tế cho biết, từ ngày 19/8 đến nay trên địa bàn TP không ghi nhận thêm ca mắc mới ngoài cộng đồng.'
# bad_string2 = 'Chiều28/8,báoc áotại cu ộ chọp Banchỉđạo phòng chốngCovid-19 TP HàNội, ông Hoàng Đức Hạnh - Phó Giám đốc Sở Y tế cho biết, từ ngày 19/8 đến nay trên địa bàn TP không ghi nhận thêm ca mắc mới ngoài cộng đồng.'
#
# # text = "Ông Nguyễn Khắc Chúc  đang làm việc tại Đại học Quốc gia Hà Nội. Bà Lan, vợ ông Chúc, cũng làm việc tại đây."
# # To perform word segmentation only
# word_segmented_text = annotator.tokenize(bad_string2)
# result = ''
# if len(word_segmented_text) == 1:
#     result = ' '.join(word_segmented_text[0])
# print(result)


# -------------------------------------------------------------------------------
# SENTENCPIECE
# unigram -  32k vocab - 500k sent - no space
model = "H:/Vietnamese word representations/sentencepiece/unigram -  32k vocab - 500k sent - no space/vietnamese_news.model"

sp = spm.SentencePieceProcessor(model)

string = 'Sở Y tế TP Hà Nội vừa thông tin trường hợp mắc SARS-CoV-2 mới, từng ở cùng phòng với bệnh nhân 1034 cách ly tại Hải Dương về TP Hà Nội sau 14 ngày cách ly.'
string2 = 'Chiều 28/8, báo cáo tại cuộc họp Ban chỉ đạo phòng chống Covid-19 TP Hà Nội, ông Hoàng Đức Hạnh - Phó Giám đốc Sở Y tế cho biết, từ ngày 19/8 đến nay trên địa bàn TP không ghi nhận thêm ca mắc mới ngoài cộng đồng.'
bad_string2 = 'Chiều28/8,báoc áotại cu ộ chọp Banchỉđạo phòng chốngCovid-19 TP HàNội, ông Hoàng Đức Hạnh - Phó Giám đốc Sở Y tế cho biết, từ ngày 19/8 đến nay trên địa bàn TP không ghi nhận thêm ca mắc mới ngoài cộng đồng.'
test = sp.encode(string, out_type=str)
print(test)
print(''.join(test).replace('▁', ' '))
