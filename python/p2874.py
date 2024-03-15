try:
    while True:
        n = int(input())
        m = ""
        for i in range(n):
            num = input()
            m += int(num, 2).to_bytes(((int(num, 2).bit_length() + 7) // 8), 'big').decode()
        print(m)
except EOFError as error:
    pass