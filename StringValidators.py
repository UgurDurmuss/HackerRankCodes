if __name__ == '__main__':
    s = input()

print(any(c.isalnum() for c in s)) #sadece sayı ve rakam içermesi lazım
print(any(c.isalpha() for c in s)) #sadece stringlerin olması lazım
print(any(c.isdigit() for c in s)) #sadece sayıların içermesi lazım
print(any(c.islower() for c in s)) #sadece küçük harfler içermesi lazım
print(any(c.isupper() for c in s)) #sadece büyük harfler içermesi lazım

#any methodu sayesinde kelimeyi karakter karakter incelememiz gerekiyor,yoksa boşluklar gözümüzden kaçar
