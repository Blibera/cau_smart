import networkx as nx
from nodevectors import Node2Vec
import time

start = time.time()
# 2만개 : 약 1분
G= nx.read_gml("C:/Users/DI_Lab/Desktop/연구실 자료/국보연/전지원/Full_G.gml")
print("읽은 시간 time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

start = time.time()
node2vec_model = Node2Vec(n_components=32,
    walklen=10)
node2vec_model.fit(G)
print("모델 학습 시간 time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
start = time.time()
node2vec_model.save("C:/Users/DI_Lab/Desktop/연구실 자료/국보연/전지원/word2vec_Full.model")
print("모델 저장 시간 time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
