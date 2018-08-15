from .models import Post
import django_filters

class BlogFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['country', 'state', 'theme', ]