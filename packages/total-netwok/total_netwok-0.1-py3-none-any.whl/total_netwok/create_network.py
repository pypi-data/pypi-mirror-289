import os
from Connnet import generate_network_file
class Create_network():  
    def __init__(self, network_file, gephi):
        self.network_file = network_file
        self.gephi = gephi

    def create_net(self, zidian, LIs, filter_seq):
        generate_network_file(self.network_file, LIs, filter_seq)
        LieBiao = []
        for line in open(self.network_file):  
            Sor = line.strip().split("|")[0]
            Sor = Sor.replace("'", "").replace(" ", "")
            Sink = line.strip().split("|")[1]
            Sink = Sink.replace("'", "").replace(" ", "")
            liiao = []
            Sorce_value = zidian.get(Sorce, 0)
            Sorce_value = int(Sorce_value)
            liiao.append(Sorce_value)
            Sink_value = zidian.get(Sink, 0)
            Sink_value = int(Sink_value)
            liiao.append(Sink_value)
            linshi = set(liiao)
            LieBiao.append(linshi)
        LieBiao_dplication_remove = [list(t) for t in set(tuple(_) for _ in LieBiao)]
        with open(self.gephi, 'w') as fout:
            print('Source', 'Target', 'Type', sep=",", file=fout)
            for i in LieBiao_dplication_remove:
                nEWlIST = list(i)
                Source = nEWlIST[0]
                Sink = nEWlIST[-1]
                print(Source, Sink, 'Undirected', sep=",", file=fout)
