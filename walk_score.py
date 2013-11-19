import fileinput
from sets import Set

def main():
  dic = dict()
  for line in fileinput.input():
    edge = line.split()
    if(len(edge)!=2):
      break 
    if(edge[0] in dic):
      dic[edge[0]]=(dic[edge[0]][0],dic[edge[0]][1]+[edge[1]])
    else:
      dic[edge[0]]=([],[edge[1]])
    if(edge[1] in dic):
      dic[edge[1]]=(dic[edge[1]][0]+[edge[0]],dic[edge[1]][1])
    else:
      dic[edge[1]]=([edge[0]],[])
  inTree = dict((key,(dic[key][0],dic[key][1])) for key in dic if not(len(dic[key][1])==len(dic[key][0]) and len(dic[key][0])==1) and len(dic[key][1])>0)
  
  notInTree = dict((key,(dic[key][0],dic[key][1])) for key in dic if len(dic[key][1])==len(dic[key][0]) and len(dic[key][0])==1)

  while(notInTree!={} and inTree!={}):
    for x in notInTree:
      inTreeInput = dict((a,inTree[a]) for a in inTree if x in inTree[a][0])
      inTreeOutput = dict((a,inTree[a]) for a in inTree if x in inTree[a][1])
      notInTreeInput = dict((a,notInTree[a]) for a in notInTree if x in notInTree[a][0])
      notInTreeOutput = dict((a,notInTree[a]) for a in notInTree if x in notInTree[a][1])
      childNodes = [notInTreeOutput, inTreeOutput]
      parentNodes = [notInTreeInput, inTreeInput]
      for isinput in parentNodes:
        for y in isinput:
          tree=notInTree
          if y in inTree:
            tree = inTree
          tree[y]=(list(Set([z for z in tree[y][0] if z != x]+notInTree[x][0])),tree[y][1])
      for isinput in childNodes:
        for y in isinput:
          tree=notInTree
          if y in inTree:
            tree = inTree
          tree[y]=(tree[y][0],list(Set([z for z in tree[y][1] if z != x]+notInTree[x][1])))
    dic = inTree
    inTree = dict((key,(dic[key][0],dic[key][1])) for key in dic if not(len(dic[key][1])==len(dic[key][0]) and len(dic[key][0])==1) and len(dic[key][1])>0)
    notInTree = dict((key,(dic[key][0],dic[key][1])) for key in dic if len(dic[key][1])==len(dic[key][0]) and len(dic[key][0])==1)

  for x in inTree:
    for y in inTree[x][1]:
      print x+"\t"+y
  
main()
