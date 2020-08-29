from nltk.tokenize import sent_tokenize


file = "H:/Vietnamese word representations/Word_vector_data/text data/datafile.txt"
out = "H:/Vietnamese word representations/Word_vector_data/text data/datafile_sentences.txt"

with open(file, 'r', encoding='utf-8') as infile:
    with open(out, 'w', encoding='utf-8') as outfile:
        for line in infile:
            sentences = sent_tokenize(line)
            for sent in sentences:
                outfile.write(f'{sent}\n2')
