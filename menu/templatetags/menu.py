from django import template
from menu.models import Menu

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu = Menu.objects.get(name=menu_name)
    menu_items = menu.items.all()
    return {'menu_items': menu_items}
