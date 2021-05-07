import warnings
import csv
import time
import networkx as nx
import seaborn as sns
import re
warnings.filterwarnings('ignore')
sns.set_style('whitegrid')
# list data 및 속성 node 추가
G = nx.Graph()

# List 속성
cve_id_list = []
text_token_list = []

G.add_nodes_from(cve_id_list, kind='cve_id')
G.add_nodes_from(text_token_list, kind='text_token')

save_csv = open("C:/Users/DI_Lab/Desktop/연구실 자료/국보연/전지원/cve_전처리.csv", "w", newline='')
write = csv.writer(save_csv)
G = nx.Graph()

start = time.time()
with open('C:/Users/DI_Lab/Desktop/연구실 자료/국보연/전지원/cve-tokenize.csv', 'r', encoding='UTF8') as f:
    reader = csv.reader(f)
    rupe = 0
    i = 0
    for text in reader:
        rupe_count = len(text)
        #if  i == 20000:
        #    break
        for k in range(rupe_count):
            if k == 0:
                cve_id = str(text[0])
                G.add_node(cve_id)
            else:
                cve_token = str(text[k])
                G.add_node(cve_token)
                G.add_edge(cve_id, cve_token)
        i = i + 1
        print(i)
    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
    start = time.time()
    print("저장")
    nx.write_gml(G, "C:/Users/DI_Lab/Desktop/연구실 자료/국보연/전지원/g_data.gml")
    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
