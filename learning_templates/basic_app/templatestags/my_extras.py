from django import template

register = template.Library()
@register.filter(name='cut')
def cut(value,arg):
    """
    this cut the valu arg
    """
    return value.replace(arg,'')

# register.filter('cut',cut)
