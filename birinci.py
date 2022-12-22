"""1.	2 basamakh mastermind oyununun programm1 yazm1z: 10 ile 98 arasmda bilgisayar bir say1 tutar. (10 ve 98 dahil)
 Oyuncu tahmin yaparak say1ya ula§maya c;ah§Ir. Oyunun diizgiin c;ah§abilmesi ic;in programm basamak­ lan aym olan bir say1 tutmamas1 gerekir.
  Aym §ekilde oyuncu da 10 dan kiic;iik, 98 den biiyiik ve basamaklan aym olan bir tahminde bulunama­ mahd1r.
   Eger boyle bir durumla program kar§ila§Irsa, program herhangi bir hesap yapmay1p sadece kullamc1y1 nizami bir say1 girmesi konusunda uyarmahd1r
   . Kullamcmm soyledigi saymm basamaklarmdaki rakamlar, rastgele tutulan saymm ic;inde varsa ve basamak ac;1smdan dogru yerde ise dogruyer sayac1 1 artmah
   , yanh§ basamakta ise yanh§yer sayac1 1 azaltil­ mahd1r. Daha sonra sonuc; kullamc1ya soylenmelidir."""


import random

print("10 ile 98 arasında bu iki sayı da dahil olmak üzere bir sayı seçiniz. seçtiğiniz sayının basamakları aynı olmamalıdır.")
s=random.randint(10,98)
s_str=str(s)
if s%11==0:
    s=random.randint(10,98)

def mastermind():
    a=0
    while a==0:
        sayi=int(input("iki basamaklı bir sayı giriniz: "))
        sayi_str=str(sayi)
        if len(sayi_str)!=2 or sayi%11==0 or sayi_str[0]==0 or sayi==99:
            print("lütfen iki basamaklı bir sayı giriniz ! ")
            a+=1
        else:
            count_true=0
            count_false=0
            if sayi_str==s_str:
                count_true+=2
                print("tebrikler oyunu kazandınız",count_true)
                a+=1
            elif sayi_str[::-1]==s_str:
                count_false-=2
                print("çok yaklaştınız ",count_false)
            else:
                b=0
                while b==0:
                    if sayi_str[0] in s_str:
                        if sayi_str[0]==s_str[0]:
                            b+=1
                            count_true+=1
                            print(count_true)
                        else:
                            b+=1
                            count_false-=1
                            print(count_false)
                    if sayi_str[1] in s_str:
                        if sayi_str[1]==s_str[1]:
                            b+=1
                            count_true+=1
                            print(count_true)
                        else:
                            b+=1
                            count_false-=1
                            print(count_false)
                    if  sayi_str[0] not in s_str and sayi_str[1] not in s_str:
                        b+=1
                        print("0")
                          
mastermind()




            

