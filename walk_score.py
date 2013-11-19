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
  print "intree "+str(intree)
  print "notintree "+str(notintree)
  while(notintree!={} and intree!={}):
    newtree={}
    for x in intree:
      lis= Set([])
      inputlis = Set([])
      for y in intree[x][1]:
        if(y in notintree):
          lis.update(notintree[y][1])
          if(y in lis):
            lis.remove(y)
        else:
          lis.add(y)
      for y in intree[x][0]:
        if(y in notintree):
          inputlis.update(notintree[y][0])
          if(y in inputlis):
            inputlis.remove(y)
        else:
          inputlis.add(y)
      newtree[x]=(list(inputlis),list(lis))
      intree[x]=(list(inputlis),list(lis))
    dic = newtree
    intree = dict((key,(dic[key][0],dic[key][1])) for key in dic if not(len(dic[key][1])==len(dic[key][0]) and len(dic[key][0])==1) and len(dic[key][1])>0)
    notintree = dict((key,(dic[key][0],dic[key][1])) for key in dic if len(dic[key][1])==len(dic[key][0]) and len(dic[key][0])==1) 
    print "intree "+str(intree)
    print "notintree "+str(notintree)
  print newtree
  # print str(dic)
  # print str(intree)
  # print str(notintree)
      
  # for x in newtree:
  #   for y in newtree[x]:
  #     print x+"\t"+y
  # print "newtree "+ str(newtree)
  # print "notintree "+str(notintree)
  # print "intree "+str(intree)


main()
