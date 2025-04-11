from sys import stdout
from os import system
import datetime
def lprint(s):
    stdout.write(s)
    stdout.flush()

lensuc=1
lentarg=100
s=datetime.time.microsecond
for lensuc in range(lentarg+1):
    system("cls")
    lprint('\r[%s%s] ' % ('█' * int(lensuc*65/lentarg), '░'*(65-int(lensuc*65/lentarg))))
    lprint('sadsad')
s2=datetime.time().microsecond

z=datetime.time().microsecond
for lensuc in range(lentarg+1):
    system("cls")
    print('\r[%s%s] ' % ('█' * int(lensuc*65/lentarg), '░'*(65-int(lensuc*65/lentarg))))
    print('sadsad')
z2=datetime.time().microsecond

print(s,s2," -",z,z2)