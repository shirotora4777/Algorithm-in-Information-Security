import random
import math


def checkPrime(n):
    if n <= 1:
        return False
    for i in range(2, (int(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True


def generateRandomList(n):
    listRandom = []
    for i in range(n):
        listRandom.append(random.randint(1, 500))
    return listRandom


def findPrimeFromRandomList(n):
    listRandom = generateRandomList(n)
    listResult = []
    for i in listRandom:
        if checkPrime(i):
            listResult.append(i)
    return listResult


def main():
    n = int(input("Nhập N: "))
    print(f"Các số nguyên tố trong mảng ngẫu nhiên {n} phần tử là: ", end="")
    print(findPrimeFromRandomList(n))


if __name__ == "__main__":
    main()