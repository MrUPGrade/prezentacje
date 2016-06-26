class MyTestClass:
    def my_print(self, value: str) -> None:
        print(value)


def executor(instance: MyTestClass) -> None:
    instance.my_print('this is a call from executor')


def f():
    pass


f.my_print = lambda x: print(x)

executor(f)
