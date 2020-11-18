import fasttext

fasttext_model_path = "H:/Vietnamese word representations/Fasttext vi.300/cc.vi.300.bin/cc.vi.300.bin"

model = fasttext.load_model(fasttext_model_path)