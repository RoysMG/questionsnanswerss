print("""*************************************************
    
    ATM YE HOŞGELDİNİZ....

İŞLEMLER :

1. BAKİYE SORGULAMA

2. PARA ÇEKME

3. PARA YATIRMA

HİÇBİR İŞLEM YAPMAK İSTEMİYORSANIZ 'q' YA BASIN 

*************************************************
 """ )
BAKİYE = 1000 
sys_kullanıcı_ad = "mert"
sys_kullanıcı_şifre = "12345"



giriş_hakkı = 3

while True :
    kullanıcı_adı = input("Kullanıcı Adınızı Girin :")
    parola = input("Şifrenizi Girin :")
    
    if (sys_kullanıcı_ad != kullanıcı_adı and sys_kullanıcı_şifre == parola) :
        print("Kullanıcı Adı hatalı...")
        giriş_hakkı -= 1
        print("Kalan Giriş Hakkı :",giriş_hakkı)
    
    elif (sys_kullanıcı_ad == kullanıcı_adı and sys_kullanıcı_şifre != parola) :
        print("Parola Hatalı...")
        giriş_hakkı -= 1
        print("Kalan Giriş Hakkı :",giriş_hakkı)
    
    elif (sys_kullanıcı_ad != kullanıcı_adı and sys_kullanıcı_şifre != parola) :
        print("Kullanıcı Adı Ve Parola Hatalı...")
        giriş_hakkı -= 1
        print("Kalan Giriş Hakkı :",giriş_hakkı)

    else :
        print("Giriş Başarılı...")

    if (giriş_hakkı == 0 ):
        print("Giriş Hakkınız Doldu...")
        break    

    işlem = input("işlemi giriniz :")
    if (işlem == "1") :
        print("Bakiyeniz {} TL dir".format(BAKİYE))
        kart_iade = input("kart iade edilsin mi ? ")
                
        if (kart_iade == "evet"):
            print("kartınız iade ediliyor....")
                
        elif (kart_iade == "hayır"):
            print ("ana ekrana aktartılıyorsunuz....")
            continue
                
        else :
                print("hatalı cevap ana ekrana geri aktarılıyorsunuz")
            
    elif (işlem == "2"):
        miktar = int(input("Ne kadar çekmek istiyorsunuz :"))
        print("işlem gerçekleşiyor...")
                
        if (BAKİYE - miktar < 0  ) :
                print("böyle bir miktar çekemezsiniz")
                continue
        BAKİYE -=miktar
                
        ana_menü_uyarısı=input("ana menüye dönmek istiyorsanız 'ana menü' \ndüğmesine kart iadesi istiyorsanız 'kart iade' düğmesine basın\n")
        if (ana_menü_uyarısı == "ana menü"):
            print("ana menüye dönüyorsunuz... ")
           
        elif (ana_menü_uyarısı == "kart iade"):
                print("karınız iade ediliyor....")
                break
        else: 
            print("Hatalı işlem yaptınız lütfen 'ana menü' ya da 'kart iade' seçeneğine basın")
            continue
            
    elif (işlem == "3"):
        miktar=int(input("yatırmak isstediğin miktarı girin :"))        
        BAKİYE += miktar 
        print(BAKİYE)
                
        ana_menü_uyarısı=input("ana menüye dönmek istiyorsanız 'ana menü' \ndüğmesine kart iadesi istiyorsanız 'kart iade' düğmesine basın\n")
        if (ana_menü_uyarısı == "ana menü"):
            print("ana menüye dönüyorsunuz... ")
        elif (ana_menü_uyarısı == "kart iade"):
            print("karınız iade ediliyor....")
            break
        else: 
            print("Hatalı işlem yaptınız lütfen 'ana menü' ya da 'kart iade' seçeneğine basın")
            continue
            
    elif (işlem == "q"):
        print("çıkış yapılıyor ve kart iade ediliyor...")
        break
    else :
        print("hatalı işlem yapıldı tekrar deneyin...")