import fileinput
from sets import Set

def main():
  #dictionary of node --> (input nodes, output nodes)
  dic = dict()
  for line in fileinput.input():
    edge = line.split()
    if(edge[0] in dic):
      dic[edge[0]]=(dic[edge[0]][0],dic[edge[0]][1]+[edge[1]])
    else:
      dic[edge[0]]=([],[edge[1]])
    if(edge[1] in dic):
      dic[edge[1]]=(dic[edge[1]][0]+[edge[0]],dic[edge[1]][1])
    else:
      dic[edge[1]]=([edge[0]],[])
  intree = dict((key,(dic[key][0],dic[key][1])) for key in dic if not(len(dic[key][1])==len(dic[key][0]) and len(dic[key][0])==1) and len(dic[key][1])>0)
  notintree = dict((key,(dic[key][0],dic[key][1])) for key in dic if len(dic[key][1])==len(dic[key][0]) and len(dic[key][0])==1)
  newtree=intree

  while(notintree!={}):
    newtree={}
    for x in notintree:
      isinput = dict((a,intree[a]) for a in intree if x in intree[a][0])
      isoutput = dict((a,intree[a]) for a in intree if x in intree[a][1])
      for y in isinput:
        if y in intree:
          lis = intree[y][0]
          lis.remove(x)
          lis = Set(lis)
          lis.update(notintree[x][0])
          intree[y]=(list(lis),intree[y][1])
      for y in isoutput:
        if y in intree:
          lis = intree[y][1]
          lis.remove(x)
          lis = Set(lis)
          lis.update(notintree[x][1])
          intree[y]=(intree[y][0],list(lis))

    dic = intree
    intree = dict((key,(dic[key][0],dic[key][1])) for key in dic if not(len(dic[key][1])==len(dic[key][0]) and len(dic[key][0])==1) and len(dic[key][1])>0)
    notintree = dict((key,(dic[key][0],dic[key][1])) for key in dic if len(dic[key][1])==len(dic[key][0]) and len(dic[key][0])==1)

  for x in intree:
    for y in intree[x][1]:
      print x+"\t"+y


main()
