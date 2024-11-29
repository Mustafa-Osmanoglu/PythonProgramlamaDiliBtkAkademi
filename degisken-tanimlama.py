# 4000 + 4000 * %18
# 3000 + 3000 * %18
urunAFiyat=4000
urunBFiyat=3000
kdvOrani = 0.18
print ( urunAFiyat + ( urunAFiyat * kdvOrani )) # ürün A
print ( urunBFiyat + ( urunBFiyat * kdvOrani )) # ürün B

urunToplami = urunAFiyat + urunBFiyat
print(urunToplami+(urunToplami * kdvOrani))
