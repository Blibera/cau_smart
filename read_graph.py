import networkx as nx
import time
from node2vec import Node2Vec
from node2vec.edges import HadamardEmbedder

start = time.time()
# 2만개 : 약 1분
G= nx.read_gml("C:/Users/DI_Lab/Desktop/연구실 자료/국보연/전지원/20000_G.gml")
print("읽은 시간 time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
#print(f"nodes: {G_loaded.nodes(data=True)}")
#print(f"edges: {G_loaded.edges(data=True)}")


start = time.time()
node2vec_model = Node2Vec(graph=G, # target graph
                    dimensions=50, # embedding dimension
                    walk_length=10, # number of nodes in each walks
                    p = 1, # return hyper parameter
                    q = 0.0001, # inout parameter, q값을 작게 하면 structural equivalence를 강조하는 형태로 학습됩니다.
                    weight_key=None, # if weight_key in attrdict
                    num_walks=200,
                    workers=1,
                   )
print("모델 학습 시간 time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
start = time.time()
node2vec_model.save("C:/Users/DI_Lab/Desktop/연구실 자료/국보연/전지원/word2vec_20000.model")
print("모델 저장 시간 time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

