import textwrap #metinleri bölmemize yarayan bir kütüphane

def wrap(string, max_width):
    return textwrap.fill(string, max_width)#fill stringi belli parçalarda böler ve string döner

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
