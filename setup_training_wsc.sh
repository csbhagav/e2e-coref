#!/bin/bash

python get_char_vocab.py

python filter_embeddings.py glove.840B.300d.txt data/dev.coref_format.jsonl data/train.coref_format.jsonl
python cache_elmo.py data/dev.coref_format.jsonl data/train.coref_format.jsonl
