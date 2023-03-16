def sieveOfEratosthenes(m, n):
    s = 0
    check = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if check[p]:
            for i in range(p * p, n + 1, p):
                check[i] = False
        p += 1
    if m < 2:
        m = 2
    for p in range(m, n + 1):
        if check[p]:
            s += p
    return s


def main():
    a = int(input("Nhập A: "))
    b = int(input("Nhập B: "))
    print(f"Tổng các số nguyên tố trong khoảng từ {a} đến {b} là: {sieveOfEratosthenes(a, b)}")


if __name__ == "__main__":
    main()
