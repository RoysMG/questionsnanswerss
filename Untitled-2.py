while True:
    a=input("evet ya da hayır a bas")
    if (a=="hayır"):
        a=input("devam etmek istiyor musun?")
        if (a=="hayır"):
            break
        else :
            print("istediğim cevabı alamadım o yüzden en başa dönüyorsun")
    elif(a=="evet"):
        a=input("o zaman bu şeyin devamını merak ediyorsun")
        if (a=="evet"):
            print("o zaman seni test edicem")
            a=int(input("3 * 5 kaçtır "))
            if (a==15):
                print("doğru cevap ama devam edemezsin")
                break
            else :
                print("bu soruyu bile bilemiyorsan atıyorum seni sg")
                break
        elif (a=="hayır"):
            print("ne korkak adamsın seni burdan atıyorum")
            break
        else :
            print("istediğim cevabı alamadım o yüzden en başa dönüyorsun") 

    else: 
        print("random atma sadece evet ya da hayır de ")
