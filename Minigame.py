def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    kevin = 0
    stuart = 0
    string = string.upper()  # Harf karşılaştırmaları için büyük harfe çeviriyoruz

    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif stuart > kevin:
        print(f"Stuart {stuart}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
