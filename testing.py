import warnings
import networkx as nx
import seaborn as sns
from gensim.models import Word2Vec
from node2vec.edges import HadamardEmbedder
import time
warnings.filterwarnings('ignore')
sns.set_style('whitegrid')

start = time.time()
model2 = Word2Vec.load('node2vec.model')
edges_embs = HadamardEmbedder(keyed_vectors=model2.wv)
print("모델 학습 시간 time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간