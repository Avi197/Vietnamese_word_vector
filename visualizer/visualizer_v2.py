import numpy as np
import tensorflow as tf
import tensorboard as tb
from torch.utils.tensorboard import SummaryWriter
import pandas as pd
import numpy as np

tf.io.gfile = tb.compat.tensorflow_stub.io.gfile

"H:/Vietnamese word representations/Word2Vec models/v0.3/0.3_metadata.tsv"
"H:/Vietnamese word representations/Word2Vec models/v0.3/0.3_tensor.tsv"

metadata_path = "H:/Vietnamese word representations/Word2Vec models/v0.3/0.3_metadata.tsv"
vectors_path = "H:/Vietnamese word representations/Word2Vec models/v0.3/0.3_tensor.tsv"


with open(metadata_path, 'r', encoding='utf-8') as metadata_file:
    metadata = metadata_file.readlines()
    metadata = [x.strip() for x in metadata]

df = pd.read_csv(vectors_path, sep="\t", header=None)   # read dummy .tsv file into memory

vectors = df.values  # access the numpy array containing values

writer = SummaryWriter()
writer.add_embedding(vectors, metadata)
writer.close()
