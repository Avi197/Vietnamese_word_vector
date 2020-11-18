import pandas as pd
import numpy as np


less_than_1k_path = "H:/Vietnamese word representations/Word_vector_data/datafile_count_less_than_1000.txt"
metadata_path = "H:/Vietnamese word representations/Word_vector_github/visualizer/runs/Nov04_15-03-42_pham-VirtualBox" \
                "/00000/default/metadata.tsv "
less_than_1k_df = pd.read_json(less_than_1k_path, typ='series')
less_than_1k = less_than_1k_df.keys()

with open(metadata_path, 'r', encoding='utf-8') as metadata_file:
    metadata = metadata_file.readlines()
    metadata = [x.strip() for x in metadata]

metadata_df = pd.DataFrame(metadata)
df = pd.concat([less_than_1k_df, metadata_df])
df_gpby = df.groupby(list(df.columns))
idx = [x[0] for x in df_gpby.groups.values() if len(x) == 1]

print(df.reindex(idx))
