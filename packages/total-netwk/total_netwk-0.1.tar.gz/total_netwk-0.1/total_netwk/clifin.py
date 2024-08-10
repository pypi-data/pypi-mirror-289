import os
from collections import Counter
import networkx as nx

class clifin():
    def __init__(self, Gephi):
        self.Gephi = Gephi

    def clifinpackage(self, Zidian):
        G = nx.read_edgelist(self.Gephi, comments='S', delimiter=',', create_using=nx.Graph(), data=(('type', str),))
        Uniq_ = G.nodes() 
        Uniq_node = [i for i in Uniq_]
        output_estimate_cli = estimate_cli(G)
        aDict = {} 
        i = 0
        while i < len(Uniq_node):
            j = 0
            thx = []
            while j < len(output_estimate_cli):
                for z in output_estimate_cli[j]:
                    if Uniq_node[i] == z[0] or Uniq_node[i] == z[1]:
                        thx.append(j + 1)
                j += 1
            i += 1
            BLs = Counter(thx)
            aDict[Uniq_node[i - 1]] = len(BLs)
        nWlist = sorted(aDict.items(), reverse=True, key=lambda kv: (kv[1], kv[0])) 
        INdx = []
        for i in nWlist:
            aKey = i[0]
            aVal = Zidian.get(aKey, "none")
            if aVal == "none":
                indx = nWlist.index(i)
                INdx.append(indx)
        if len(INdx) != 0:
            INdx.sort(reverse=True)
            for i in INdx:
                del nWlist[i]
        with open('clifin_output.txt', 'w') as file:
            for item in nWlist:
                file.write(str(item) + '\n')
        os.remove("clifin_output.txt")
        return nWlist
