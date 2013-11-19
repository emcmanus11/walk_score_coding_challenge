import fileinput
from sets import Set

def main():
  #dictionary : Edges --> (parent nodes, child nodes)
  dic = dict()
  
  #Reads from STDIN
  for line in fileinput.input():
    edge = line.split()
  
    #Breaks if input is not correctly formatted
    if(len(edge)!=2):
      break 
  
    #Puts parent node into dictionary
    if(edge[0] in dic):
      dic[edge[0]]=(dic[edge[0]][0],dic[edge[0]][1]+[edge[1]])
    else:
      dic[edge[0]]=([],[edge[1]])
    
    #Puts child node into dictionary
    if(edge[1] in dic):
      dic[edge[1]]=(dic[edge[1]][0]+[edge[0]],dic[edge[1]][1])
    else:
      dic[edge[1]]=([edge[0]],[])

  #Sorts by edges probably in tree
  inTree = dict((key,(dic[key][0],dic[key][1])) for key in dic if not(len(dic[key][1])==len(dic[key][0]) and len(dic[key][0])==1) and len(dic[key][1])>0)
  
  #Sorts by edges definitely not in tree
  notInTree = dict((key,(dic[key][0],dic[key][1])) for key in dic if len(dic[key][1])==len(dic[key][0]) and len(dic[key][0])==1)

  #While there are edges that should not be in the final tree
  while(notInTree!={} and inTree!={}):
    for x in notInTree:
      #Edges in the tree with x as a parent node
      inTreeInput = dict((a,inTree[a]) for a in inTree if x in inTree[a][0])
      #Edges in the tree with x as a child node
      inTreeOutput = dict((a,inTree[a]) for a in inTree if x in inTree[a][1])
      #Edges not in the tree with x as a parent node
      notInTreeInput = dict((a,notInTree[a]) for a in notInTree if x in notInTree[a][0])
      #Edges not in the tree with x as a child node
      notInTreeOutput = dict((a,notInTree[a]) for a in notInTree if x in notInTree[a][1])

      childNodes = [notInTreeOutput, inTreeOutput]
      parentNodes = [notInTreeInput, inTreeInput]

      #Goes through nodes where x is the parent node
      for isinput in parentNodes:
        for y in isinput:
          tree=notInTree
          if y in inTree:
            tree = inTree
          #Takes x out as a parent and replaces it with all the parent nodes of x
          tree[y]=(list(Set([z for z in tree[y][0] if z != x]+notInTree[x][0])),tree[y][1])
      

      #Goes through nodes where x is the child node
      for isinput in childNodes:
        for y in isinput:
          tree=notInTree
          if y in inTree:
            tree = inTree
          #Takes x out as a child and replaces it with all the child nodes of x
          tree[y]=(tree[y][0],list(Set([z for z in tree[y][1] if z != x]+notInTree[x][1])))

    #Update variables
    dic = inTree
    inTree = dict((key,(dic[key][0],dic[key][1])) for key in dic if not(len(dic[key][1])==len(dic[key][0]) and len(dic[key][0])==1) and len(dic[key][1])>0)
    notInTree = dict((key,(dic[key][0],dic[key][1])) for key in dic if len(dic[key][1])==len(dic[key][0]) and len(dic[key][0])==1)

  #Print out final tree
  for x in inTree:
    for y in inTree[x][1]:
      print x+"\t"+y
  
main()
