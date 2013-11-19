import fileinput

def main():
  dic = dict()
  for line in fileinput.input():
    edge = line.split()
    if(edge[0] in dic):
      dic[edge[0]]=(dic[edge[0]][0],dic[edge[0]][1]+[edge[1]])
    else:
      dic[edge[0]]=([edge[0]],[])
    if(edge[1] in dic):
      dic[edge[1]]=(dic[edge[1]][0]+[edge[0],dic[edge[1]][1])
    else:
      dic[edge[1]]=([edge[1]],[])

    intree = dict((key,(dic[key][0],dic[key][1])) for key in dic if not(len(dic[key][1])==len(dic[key][0]) and len(dic[key][0])==1) and len(dic[key][1])>0)
    notintree = dict((key,(dic[key][0],dic[key][1])) for key in dic if len(dic[key][1])==len(dic[key][0]) and len(dic[key][0])==1)
    newtree=intree

main()
    
  
