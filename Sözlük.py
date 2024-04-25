meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "SLAY": "Çok havalı bir harekete verilen cevap",
            "SHEESH": "Onaylamamak",
            "ERKO": "Kötü davranışları olan erkekler",
            "RED FLAG": "İlişkilerdeki kötü davranış ve hareketler",
            "GREEN FLAG": "İlişkilerdeki iyi hareketler",
            "RANDOM": "Komik veya saçma şeylere verilen cevap/Elini rastgele klavyede gezdirerek oluşturulur"
             }

word = input("Anlamadığınız bir kelime/söz grubu yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Bu kelime malesef sözlüğümüzde yok. Başka bir kelime/söz grubu giriniz")


