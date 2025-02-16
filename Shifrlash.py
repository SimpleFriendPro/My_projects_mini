#shifrlash
import math
p, q = map(int,input("Ikkita son kiriting: ").split())
n = p * q
xabar = input("Xabar kiriting: ")
shifrlar = []
#Eyler funksiyasini hisoblaymiz: f(n)=(p-1)*(q-1)
F = (p-1)*(q-1)
for i in range(2,F+1):
  if math.gcd(i,F)==1:
    e = i
    break;
for j in range(2,10000000):
  if (j*e)%F==1:
    d = j
    break;
print("Shifrlash kalitingiz: " , e)
print("Maxfiy kalitingiz: " , d)
for k in range(0,len(xabar)):
  shifrlar.append(int(math.pow(ord(xabar[k]),e)%n))
print(shifrlar)

#deshifrlash
suz = []
c = input("Shifrlangan raqamlarni kiriting: ")
smslar = set(map(int, c.split(',')))
for l in range(0,len(smslar)):
  m=pow(smslar[l]%n,d,n)
  suz.append(str(chr(m)))
print(suz)
