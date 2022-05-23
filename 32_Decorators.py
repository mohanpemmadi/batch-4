'''

	Decorators are functions that adds functionality to an existing function without changing the original structure of the function.

'''


def decorator_funcation(fun_name):
    print('fun name -',fun_name.__name__)
    def inner(value1,value2):
        print('decorator called')
        fun_name(value1,value2)  # delete()
    return inner
@decorator_funcation
def create():
    print('create')

# @decorator_funcation
def update():
    print('update')

@decorator_funcation
def delete(value1,value2):
    print(value1,value2)
    print('delete')

delete(123,456)


# create()
# update()
