def split_and_join(line):
   a=line.split("")
   result "-".join(a)
    
   
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
