import math


def checkPrime(n):
    if n <= 1:
        return False
    for i in range(2, (int(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True


def findX(n, m, A, B, C):
    listResult = []
    for i in range(n, m):
        if checkPrime(A * (i ** 2) + B * i + C):
            listResult.append(i)
    return listResult


def main():
    while True:
        n = int(input("Nhập N: "))
        m = int(input("Nhập M: "))
        if n < m:
            break
        else:
            print("Vui lòng nhập N < M")
    A = int(input("Nhập A: "))
    B = int(input("Nhập B: "))
    C = int(input("Nhập C: "))
    listRes = findX(n, m, A, B, C)
    if len(listRes) > 0:
        print(f"Số nguyên cần tim là: ", end="")
        print(findX(n, m, A, B, C))
    else:
        print("Không tim thấy số nguyên thoả yêu cầu")


if __name__ == "__main__":
    main()
