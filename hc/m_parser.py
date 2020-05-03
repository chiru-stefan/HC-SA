from scipy.spatial import distance

with open("burma14.tsp", 'r') as f:
    contents = f.read()
    f.close()

contents = contents.split('\n')
contents = [x.split(' ') for x in contents]
values = []
for i in contents:
    for c in i:
        if '.' in c:
            values.append(c)

left = [x for x in values[::2]]

right = [x for x in values[1::2]]

nodes = dict()

lz = list(zip(left, right))
added = []
for i, x in enumerate(lz):
    for j, y in enumerate(lz[i+1:]):
        nodes[str(str(i)+"-"+str((j+i+1)%len(lz) ))] = distance.euclidean([float(x[0]), float(x[1])], [float(y[0]), float(y[1])])

with open("m_burma.csv","w") as f:
    for m in nodes.items():
        f.write(str(m[0] + "," + str(m[1])[:4]) +"\n")
    f.close()