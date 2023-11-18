
from django.views.generic import ListView, DetailView
from menu.models import Menu


class MenuListView(ListView):
    """Страница со всеми меню"""

    model = Menu

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_list'] = Menu.objects.prefetch_related('soup', 'main', 'dessert').all()
        return context


class MenuDetailView(DetailView):
    """Отображение единственного меню """
    model = Menu

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Menu.objects.filter(pk=self.object.pk)
        return context
