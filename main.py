import time
print("Program Başlatılıyor...")
print(" ")
time.sleep(4)
while "true":
    
    ad = input("Adınız ? : \n")
    print(" ")
    time.sleep(1)
    yıl = int(input ("Doğum tarihiniz ? : \n"))
    print(" ")
    print("Lüten bekleyiniz, hesaplanıyor...")
    sonuc = 2023 - int(yıl)
    
    time.sleep(3)
    print(" ")
    print(ad + ', yaşın ' + '"' + str(sonuc) + '"')
    print(" ")
    time.sleep(2)
    print("--------------------------")
