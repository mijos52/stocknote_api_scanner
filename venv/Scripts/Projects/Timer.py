import timeit


def timer(number, repeat):
    def response(func):
        runs = timeit.repeat(func, number=number, repeat=repeat)
        print(sum(runs) / len(runs))

        return response

