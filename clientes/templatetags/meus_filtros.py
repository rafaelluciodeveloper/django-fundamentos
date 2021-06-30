from django import template

register = template.Library()

@register.filter(name="addclass")
def addclass(values, args):
  return values.as_widget(attrs={'class': args})