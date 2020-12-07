def num6dig(num):
    l = ['0','0','0','0','0','0']
    index = 6

    while (num !=0):
        l.insert(index, str(num%10))
        num = num // 10
        index -= 1
    
        l.pop(0)
    
    return ''.join(l)

def main():
   
   print(num6dig(1234))

if __name__ == "__main__":
    main()