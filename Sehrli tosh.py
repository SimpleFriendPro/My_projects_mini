import random

Name = "Zufar"

Question = "Men qanday o'quvchiman?"

answer = ''

random_number = random.randint(1,10)

if random_number == 1:
  answer = "Diqqatini jamlashda qiynaladigan"
elif random_number == 2:
  answer = "O'qishga kechikadigan"
elif random_number == 3:
  answer = "Yangi narsalarni o'rganishga ishtiyoqi katta"
elif random_number == 4:
  answer = "Guruh ishlarida passiv"
elif random_number == 5:
  answer = "O'z vaqtini boshqarish uchun harakat qiladigan"
elif random_number == 6:
  answer = "Doimo yangiliklarga ochiq"
elif random_number == 7:
  answer = "Ba'zan sekin harakat qiladigan"
elif random_number == 8:
  answer = "Maktabdan tashqari faoliyatlarda ham ishtirok etadigan"
elif random_number == 9:
  answer = "Haddan tashqari xavotirga tushadigan"
elif random_number == 10:
  answer = "O'zing bilasanku"
else:
  answer = "Error"

print(Name + " so'radi: " + Question)
print("Magic 8-Ball ning javobi: " + answer)
