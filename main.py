import random
karakterler="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk= int(input("Kaç karakterli bir şifre istiyorsunuz?:"))
sifre=""
for i in range(uzunluk):
    sifre += random.choice(karakterler)
print(sifre)
