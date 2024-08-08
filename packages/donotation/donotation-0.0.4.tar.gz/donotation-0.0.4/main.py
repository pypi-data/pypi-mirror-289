import ast
import inspect


def f1():

    def f2():
        # print(inspect.stack()[0])
        pass
    #     yield v+1

    return f2
    # print(inspect.getsourcefile(f2))
    # print(inspect.getsource(f2))
    # yield 3

func = f1()

# inspect.getlineno(func)
# print(dir(func))
# print(inspect.findsource(func))
print(func.__code__.co_firstlineno)
# print(inspect.stack())

func_source = inspect.getsource(f1)
func_ast = ast.parse(func_source).body[0]
print(func_ast.lineno)
