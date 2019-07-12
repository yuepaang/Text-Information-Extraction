import pickle
import os
import random
import numpy as np

# tags, BIO
tag2label = {"O": 0,
             "B-a": 1, "I-a": 2,
             "B-b": 3, "I-b": 4,
             "B-c": 5, "I-c": 6,
             }


def read_corpus(corpus_path):
    """
    read txt to [([12,34,5,], [o,o,a,o]), (), ()...]
    """
    data = []
    with open(corpus_path, encoding='utf-8') as fr:
        lines = fr.readlines()

    for i, line in enumerate(lines):
        chunks = line.split('  ')
        word_, label_ = [], []
        for chunk_ in chunks:
            chunk_clean = chunk_.strip().replace('\n', '')
            mark = chunk_clean[-1:]
            word_ = word_ + chunk_clean[:-2].strip().split('_')
            chunk_size = len(chunk_clean[:-2].strip().split('_'))
            if mark == 'o':
                label_ = label_ + ['O'] * chunk_size
                continue
            if mark == 'a':
                label_ = label_ + (['B-a'] + ['I-a'] * (chunk_size-1))
                continue
            if mark == 'b':
                label_ = label_ + (['B-b'] + ['I-b'] * (chunk_size-1))
                continue
            if mark == 'c':
                label_ = label_ + (['B-c'] + ['I-c'] * (chunk_size-1))
                continue
        data.append((word_, label_))
    return data


def read_corpus_test(corpus_path):
    data = []
    with open(corpus_path, encoding='utf-8') as fr:
        lines = fr.readlines()
    for i, line in enumerate(lines):
        word_ = line.replace('\n', '').strip().split('_')
        tag_ = ['O'] * len(word_)
        data.append((word_, tag_))
    return data


def vocab_build(vocab_path, corpus_path, min_count):
    data = read_corpus(corpus_path)
    word2id = {}
    for sent_, tag_ in data:
        for word in sent_:
            if word.isdigit():
                word = '<NUM>'
            elif ('\u0041' <= word <= '\u005a') or ('\u0061' <= word <= '\u007a'):
                word = '<ENG>'
            if word not in word2id:
                word2id[word] = [len(word2id)+1, 1]
            else:
                word2id[word][1] += 1
    low_freq_words = []
    for word, [word_id, word_freq] in word2id.items():
        if word_freq < min_count and word != '<NUM>' and word != '<ENG>':
            low_freq_words.append(word)
    for word in low_freq_words:
        del word2id[word]

    new_id = 1
    for word in word2id.keys():
        word2id[word] = new_id
        new_id += 1
    word2id['<UNK>'] = new_id
    word2id['<PAD>'] = 0

    print(len(word2id))
    with open(vocab_path, 'wb') as fw:
        pickle.dump(word2id, fw)


def sentence2id(sent, word2id):
    sentence_id = []
    for word in sent:
        if word.isdigit():
            word = '<NUM>'
        elif ('\u0041' <= word <= '\u005a') or ('\u0061' <= word <= '\u007a'):
            word = '<ENG>'
        if word not in word2id:
            word = '<UNK>'
        sentence_id.append(word2id[word])
    return sentence_id


def read_dictionary(vocab_path):
    vocab_path = os.path.join(vocab_path)
    with open(vocab_path, 'rb') as fr:
        word2id = pickle.load(fr)
    print('vocab_size:', len(word2id))
    return word2id


def get_max_id(train_data):
    ids = []
    for (seq_, tag_) in train_data:
        ids = ids + [int(word_) for word_ in seq_]
    return max(ids)


def random_embedding(vocab_size, embedding_dim):
    embedding_mat = np.random.uniform(-0.25, 0.25, (vocab_size, embedding_dim))
    embedding_mat = np.float32(embedding_mat)
    return embedding_mat


def pad_sequences(sequences, pad_mark=0):
    """

    :param sequences:
    :param pad_mark:
    :return:
    """
    max_len = max(map(lambda x: len(x), sequences))
    seq_list, seq_len_list = [], []
    for seq in sequences:
        seq = list(seq)
        seq_ = seq[:max_len] + [pad_mark] * max(max_len - len(seq), 0)
        seq_list.append(seq_)
        seq_len_list.append(min(len(seq), max_len))
    return seq_list, seq_len_list


def batch_yield(data, batch_size, tag2label, shuffle=False):
    if shuffle:
        random.shuffle(data)

    seqs, labels = [], []
    for (word_, tag_) in data:
        word_ = [int(w) for w in word_]
        label_ = [tag2label[tag] for tag in tag_]

        if len(seqs) == batch_size:
            yield seqs, labels
            seqs, labels = [], []

        seqs.append(word_)
        labels.append(label_)

    if len(seqs) != 0:
        yield seqs, labels
