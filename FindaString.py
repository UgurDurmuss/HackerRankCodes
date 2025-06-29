def count_substring(string, sub_string):
    sayac=0
    for i in range(len(string)-len(sub_string)+1):
       mains= string[i:i+len(sub_string)]#slicing
       if mains==sub_string:
        sayac=sayac+1 
    return sayac

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
