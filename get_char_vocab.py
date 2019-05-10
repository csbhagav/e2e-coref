from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import argparse

import sys
import json


def get_char_vocab(input_filenames, output_filename):
    vocab = set()
    for filename in input_filenames:
        with open(filename) as f:
            for line in f.readlines():
                for sentence in json.loads(line)["sentences"]:
                    for word in sentence:
                        vocab.update(word)
    vocab = sorted(list(vocab))
    with open(output_filename, "w") as f:
        for char in vocab:
            f.write(u"{}\n".format(char).encode("utf8"))
    print("Wrote {} characters to {}".format(len(vocab), output_filename))


def get_char_vocab_language(language):
    get_char_vocab(
        ["{}.{}.jsonlines".format(partition, language) for partition in ("train", "dev", "test")],
        "char_vocab.{}.txt".format(language))


def main(dataset):
    if dataset == "conll":
        get_char_vocab_language("english")
        get_char_vocab_language("chinese")
        get_char_vocab_language("arabic")
    elif dataset == "wsc":
        get_char_vocab(["data/train.coref_format.jsonl", "data/dev.coref_format.jsonl"])
    else:
        assert False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='get_char_vocab.py',
        usage='%(prog)s dataset',
        description=''
    )
    parser.add_argument('--dataset', type=str,
                        dest="dataset",
                        help='Dataset name')
    args = parser.parse_args()

    # Run seed selection if args valid
    print('====Input Arguments====')
    print(json.dumps(vars(args), indent=2, sort_keys=True))
    print("=======================")
    main(args.dataset)
