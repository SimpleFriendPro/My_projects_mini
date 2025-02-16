
import random

def func():
    a = random.randint(1,100)
    print("\nO'yin sharti: Men son o'ylayman 1 dan 100 gacha va siz uni tezroq topishingiz kerak!")
    son = int(input("Men nechchini o'yladim: "))
    hisobla(son, a)
    
def hisobla(son, a):
    S = 0
    while son != a:
        if son > a:
            print(f"Men o'ylagan son {son} dan kichik")
            son = int(input("Yangi qiymat kiriting: "))
            S += 1
        else:
            print(f"Men o'ylagan son {son} dan katta")
            son = int(input("Yangi qiymat kiriting: "))
            S += 1
    print(f"Siz {S+1} urunishda to'g'ri topdingiz, men {son} ni o'ylagandim")
    return func()

func()