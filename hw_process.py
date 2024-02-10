import time
from multiprocessing import Pool, cpu_count


def factorize(*numbers):
    result = []
    for el in numbers:
        factors = []
        for i in range(1, el + 1):
            if el % i == 0:
                factors.append(i)
        result.append(factors)
    print("result", result)
    return result


def factorize_wrapper(number):
    result = []
    for i in range(1, number + 1):
        if number % i == 0:
            result.append(i)
    return result


def factorize_multicore(*numbers):
    pool = Pool(cpu_count())
    results = pool.map(factorize_wrapper, numbers)
    pool.close()
    pool.join()
    print("results", results)
    return results


# if __name__ == "__main__":
start_time_single = time.time()
a, b, c, d = factorize(128, 255, 99999, 10651060)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316,
             380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
end_time_single = time.time()

print("single", end_time_single - start_time_single)

start_time_multi = time.time()
a, b, c, d = factorize_multicore(128, 255, 99999, 10651060)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316,
             380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
end_time_multi = time.time()

print("multi", end_time_multi - start_time_multi)
