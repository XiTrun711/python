n = int(input("Nhập vào một số nguyên:"))
def sntcheck(n):
    if n <= 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

print(sntcheck(n))