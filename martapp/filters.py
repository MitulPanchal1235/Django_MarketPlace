import django_filters
from .models import *
from django_filters import CharFilter
class Datafilter(django_filters.FilterSet):
    name=CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model=Posts
        field='__all__'
        exclude=['user','cost','contact','time','category','detail','about','p1','p2','p3','p4','video','dop']