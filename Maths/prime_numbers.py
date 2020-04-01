from typing import Generator


def primes(max: int) -> Generator[int, None, None]:
    numbers: Generator = (i for i in range(1, (max + 1)))
    for i in (n for n in numbers if n > 1):
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            yield i


if __name__ == "__main__":
    number = int(input("Range:\n>> ").strip())
    for ret in primes(number):
        print(ret)
