import networkx as nx
from nodevectors import Node2Vec
import time
from gensim.models import KeyedVectors

g2v = Node2Vec.load('C:/Users/DI_Lab/Desktop/연구실 자료/국보연/전지원/word2vec_20000test.model.zip')

# Save model to gensim.KeyedVector format
g2v.save_vectors("wheel_model.bin")

# load in gensim
print(g2v)
model = KeyedVectors.load_word2vec_format("wheel_model.bin")
print(model)
model[str("cve-2019-1020019")]