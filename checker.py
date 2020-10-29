import os

def transform(file):
  f = open(file,'r').read()
  mass = f.split('\n')
  #transformation
  start = 0
  end = len(mass)
  print(mass)
  for start in range(start,end,1):
    iop = mass[start].split(':')
    os.system('echo "'+iop[0]+'">>resolved_base.txt')
    os.system('echo "'+iop[1]+'">>passwords.txt')

def transform_big(file):
    with open(file) as f:
        for line in f:
          st(line)

def st(line):
  iop =line.split(':')
  os.system('echo "'+iop[0]+'">>resolved_base.txt')
  pol = iop[1].split('\n')
  os.system('echo "'+pol[0]+'">>passwords.txt')