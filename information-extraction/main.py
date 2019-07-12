import tensorflow as tf
from core.model import BiLSTM_CRF
from core.utils import str2bool, get_logger
from core.data import read_corpus, tag2label, random_embedding, get_max_id, read_corpus_test
import numpy as np
import argparse
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


# Session configuration
os.environ['CUDA_VISIBLE_DEVICES'] = '7'
config = tf.ConfigProto(allow_soft_placement=True)
# config.gpu_options.allow_growth = True
config.gpu_options.per_process_gpu_memory_fraction = 0.7

parser = argparse.ArgumentParser(description='BiLSTM-CRF for Chinese NER task')
parser.add_argument('--train_data', type=str, default='datagrand', help='train data source')
parser.add_argument('--dev_data', type=str, default='datagrand', help='test data source')
parser.add_argument('--batch_size', type=int, default=64, help='#sample of each minibatch')
parser.add_argument('--epoch', type=int, default=100, help='#epoch of training')
parser.add_argument('--hidden_dim', type=int, default=200, help='#dim of hidden state')
parser.add_argument('--optimizer', type=str, default='Adam', help='Adam/Adadelta/Adagrad/RMSProp/Momentum/SGD')
parser.add_argument('--CRF', type=str2bool, default=True, help='use CRF at the top layer. if False, use Softmax')
parser.add_argument('--lr', type=float, default=0.001, help='learning rate')
parser.add_argument('--clip', type=float, default=5.0, help='gradient clipping')
parser.add_argument('--dropout', type=float, default=0.5, help='dropout keep_prob')
parser.add_argument('--update_embedding', type=str2bool, default=True, help='update embedding during training')
parser.add_argument('--pretrain_embedding', type=str, default='random', help='use pretrained char embedding / init it randomly')
parser.add_argument('--embedding_dim', type=int, default=300, help='random init char embedding_dim')
parser.add_argument('--shuffle', type=str2bool, default=True, help='shuffle training data before each epoch')
parser.add_argument('--mode', type=str, default='test', help='train/test/demo')
parser.add_argument('--demo_model', type=str, default='v8_29000_adam64_seq1_price', help='model for test and demo')
args = parser.parse_args()


if args.mode != 'demo':
    train_path = os.path.join('.', args.train_data, 'train.txt')
    dev_path = os.path.join('.', args.dev_data, 'dev.txt')
    test_path = os.path.join('.', args.dev_data, 'test.txt')
    train_data = read_corpus(train_path)
    dev_data = read_corpus(dev_path)
    test_data = read_corpus_test(test_path)
    dev_size = len(dev_data)
    test_size = len(test_data)

paths = {}
output_path = os.path.join('.', args.train_data+"_save", args.demo_model)
if not os.path.exists(output_path): os.makedirs(output_path)
summary_path = os.path.join(output_path, "summaries")
paths['summary_path'] = summary_path
if not os.path.exists(summary_path): os.makedirs(summary_path)
model_path = os.path.join(output_path, "checkpoints/")
if not os.path.exists(model_path): os.makedirs(model_path)
ckpt_prefix = os.path.join(model_path, "model")
paths['model_path'] = ckpt_prefix
result_path = os.path.join(output_path, "results")
paths['result_path'] = result_path
if not os.path.exists(result_path): os.makedirs(result_path)
log_path = os.path.join(result_path, "log.txt")
paths['log_path'] = log_path
get_logger(log_path).info(str(args))


vocab_size = get_max_id(train_data) + 1
if args.pretrain_embedding == 'random':
    embeddings = random_embedding(vocab_size, args.embedding_dim)
else:
    embedding_path = 'char_pretrain_embedding.npy'
    embeddings = np.array(np.load(embedding_path), dtype='float32')

# training model
if args.mode == 'train':
    model = BiLSTM_CRF(args, embeddings, tag2label, paths, config=config)
    model.build_graph()
    print("train data: {}".format(len(train_data)))
    model.train(train=train_data, dev=dev_data)

# testing model
elif args.mode == 'test':
    ckpt_file = tf.train.latest_checkpoint(model_path)
    print(ckpt_file)
    paths['model_path'] = ckpt_file
    model = BiLSTM_CRF(args, embeddings, tag2label, paths, config=config)
    model.build_graph()
    print("test data: {}".format(test_size))
    model.test(test_data)
