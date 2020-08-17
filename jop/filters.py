import django_filters
from .models import Jop
class JopFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    jop_description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Jop
        fields = '__all__'
        exclude = ['owner','published_at','vacancy','salary','jop_image','slug',]