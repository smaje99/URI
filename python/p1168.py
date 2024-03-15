n = int(input())
if 1 <= n <= 2000:  
    l=[]
    for i in range(n):
        v = str(input())
        j = 0
        for s in v:
            if s == '0' or s=='6' or s=='9':
                j += 6
            elif s == '1':
                j += 2
            elif s == '2' or s=='3' or s=='5':
                j += 5
            elif s == '4':
                j += 4
            elif s == '7':
                j += 3
            elif s == '8':
                j += 7
        l.append(j)
    for i in l:
        print(i,"leds")
