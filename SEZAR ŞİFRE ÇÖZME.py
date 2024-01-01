k_alfabe = "abcçdefgğhıijklmnoöprsştuüvyzxwq +-*\\/)(}{}&%#^'!"
b_alfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZXWQ "
cumle = input("Cümle: ")
yeniCumle = ""
for i in cumle:
    if i in k_alfabe:
        indeks = k_alfabe.index(i)
        yeniCumle += k_alfabe[indeks - 3]
    elif i in b_alfabe:
        indeks = b_alfabe.indeks(i)
        yeniCumle += b_alfabe_[indeks - 3]
    else:
        print("Bu karakter alfabe düzeninde mevcut değil!")
        print("Çevrilebilen kısım:" , yeniCumle)
        quit()
print(yeniCumle)