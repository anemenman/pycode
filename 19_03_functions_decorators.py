def first_test():
    print("Test function 1")


def second_test():
    print("Test function 2")


# decorator
def simple_decore(fn):
    def wrapper():
        print("Run function")
        fn()
        print("Stop function")

    return wrapper


print(simple_decore(first_test))
print(simple_decore(second_test))


@simple_decore
def decore_test():
    print("Test decore function 1")


print('-------')
decore_test()
