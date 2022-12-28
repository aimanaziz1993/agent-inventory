from django_filters import rest_framework as filters

from inventory.models import Inventory


class CustomInventoryFilter(filters.FilterSet):
    # min_price = filters.(field_name="price", lookup_expr='gte')
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    location = filters.CharFilter(field_name='location', lookup_expr='icontains')
    username = filters.CharFilter(field_name='realtor__user__user_name', lookup_expr='icontains')
    category = filters.CharFilter(field_name='category', lookup_expr='exact')

    class Meta:
        model = Inventory
        fields = ['username', 'title', 'location', 'category']