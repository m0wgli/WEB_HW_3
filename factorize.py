import logging
from time import time
from multiprocessing import cpu_count, Pool


def factorize(*number):
    # YOUR CODE HERE
    result = dict()
    for num in number:
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        result[num] = divisors
    return result


if __name__ == '__main__':
    timer = time()
    result = factorize(128, 255, 99999, 10651060)
    print(result)
    print(f'Done by 1 process: {round(time() - timer, 4)}')

    logging.basicConfig(level=logging.DEBUG,
                        format="%(threadName)s %(message)s")
    with Pool(cpu_count()) as pool:
        timer = time()
        print(pool.map(factorize, [128, 255, 99999, 10651060]))
        pool.close()
        pool.join()
        print(f'Done by {cpu_count()} process: {round(time() - timer, 4)}')
