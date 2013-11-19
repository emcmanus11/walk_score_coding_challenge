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
  intree = dict((key,dic[key][1]) for key in dic if not(len(dic[key][1])==len(dic[key][0]) and len(dic[key][0])==1) and len(dic[key][1])>0)
  notintree = dict((key,dic[key][1]) for key in dic if len(dic[key][1])==len(dic[key][0]) and len(dic[key][0])==1)
  print dic
  newtree={}
  for x in intree:
    lis = Set([])
    for y in intree[x]:
      if(y in notintree):
        lis.update(notintree[y])
        if(y in lis):
          lis.remove(y)
      else:
        lis.add(y)
    newtree[x]=lis
      
  for x in newtree:
    for y in newtree[x]:
      print x+"\t"+y
  print "newtree "+ str(newtree)


main()
