#Fibonacci dizisi 
toplamsayi = int(input("Terim sayısı giriniz: "))
a1 = 0
a2 = 1
saydir = 0
if toplamsayi <= 0:
    print("Lütfen pozitif bir sayı giriniz.")
elif toplamsayi == 1:
    print("Fibonacci dizisi girdiğiniz",toplamsayi,"değerine kadar :")
    print(a1)
else:
    print("Fibonacci dizisi girdiğiniz",toplamsayi,"değerine kadar :")
while saydir < toplamsayi:
    print(a1,end=' , ')
    aa1 = a1 + a2
    a1 = a2
    a2 = aa1
    saydir += 1
    
