sayi = int(input("Kontrol edilmesini istediğiniz sayıyı giriniz:")) #kullanıcıdan bir int olan bir input alınır
x = 1  #"x" adlı bir değişken tanımlanır ve 1 olarak atanır
bolunensayi = 0  #bolunensayı isimli bir değişken tanımlanır ve 0 olarak atanır
while x <= sayi: #while döngüsü kullanılır ve koşul x değişkeninin sayi değişkeninden küçük eşit olduğu değerler olarak belirlenir
    y = sayi % x #y adlı değişken tanımlanır ve sayi ile x değişkenlerinin modu alınmış hali olarak atanır
    if (y == 0): #if kullanılır ve koşul; y değişkeninin 0'a eşit olduğu değerler olarak atanır
        bolunensayi = bolunensayi + 1 #"bolunensayi" değişkeni bir artırılır
        x = x + 1   #"x" değişkeni bir artırılır
    else:
        x = x + 1 #else durumunda da "x" değişkeni bir artırılır
z = sayi % bolunensayi #"z" isimli bir değişken tanımlanır ve "sayi" ve "bolunensayi" değişkenlerinin modu alınmış hali olarak atanır
if (z == 0): #if kullanılır ve koşulu z değişkeninin 0'a eşit olduğu değerler olarak belirlenir
    print(sayi, "Tau sayısıdır.") #eğer koşul doğruysa yazdır
else:
    print(sayi, "Tau değildir.") #eğer koşul yanlışsa yazdır

print("-_-") #imzam