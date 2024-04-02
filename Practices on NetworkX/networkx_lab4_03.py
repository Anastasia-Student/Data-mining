# Import necessary modules
import networkx as nx
import random
import matplotlib.pyplot as plt


# Generate random Poisson network G(n,m)
n = 400
m = 600
G = nx.dense_gnm_random_graph(n, m, seed=None)


# Add to nodes of G the attribute: status (S, I, R) 
for i in range(n):
    G.nodes[i]['status'] = 'S'

# Randomly select start node, initialise time and three counters
start = random.randint(0, n-1)
G.nodes[start]['status'] = 'I'


time = 0
S = [n-1]
I = [1]
R = [0]
T = 100

def foo(prob):
    if random.random() < prob:
        return 0
    else:
        return 1

# Do loop: for time in range (1, T)
for time in range(1, T):
    # 0. Select from nodes infected ones and put into separate list
    infected_at_t = []
    for i in range(n):
        if G.nodes[i]['status'] == 'I':
            infected_at_t.append(i)
    # 1. Do loop over infected nodes and infect their neighbors with
    #    certain prob,
    #    when doing this change status of
    #    infected to recovered

    for j in infected_at_t:
        neighbors_of_j = G.adj[j]
        #print(neighbors_of_j, type(neighbors_of_j))

        for k in neighbors_of_j:
            
            if foo(0.4):
                if G._node[k]['status'] == 'S':
                    G._node[k]['status'] = 'I'
                
    for j in infected_at_t:
        G._node[j]['status'] = 'R'        
        

     #      2. Calculate number of S, I, R
    St = 0
    It = 0
    Rt = 0
    for n in G.nodes():
        if G._node[n]['status'] == 'I':
            It += 1
        elif G._node[n]['status'] == 'R':
            Rt += 1
        elif G._node[n]['status'] == 'S':
            St += 1

    S.append(St)
    I.append(It)
    R.append(Rt)


# Draw time series for S, I, R
plt.plot(S)
plt.plot(I)
plt.plot(R)
plt.show()
