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
    
  
