from django import template
register = template.Library()

# without decorator
def myreplace(value, arg):
    return value.replace(arg, 'We are')

register.filter('imToweare', myreplace)

# # with decorator
# @register.filter(name='imToweare')
# def myreplace(value, arg):
#     return value.replace(arg, 'We are')