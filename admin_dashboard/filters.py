from django_filters import rest_framework as filters
from user_details.models import Details


class CandidateFilter(filters.FilterSet):

    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    user__cnic = filters.CharFilter(
        field_name='user__cnic', lookup_expr='user__cnic__contains')
    courseCategory = filters.CharFilter(
        field_name='courseCategory', lookup_expr='icontains')
    domicile = filters.CharFilter(
        field_name='domicile', lookup_expr='icontains')
    appId = filters.CharFilter(
        field_name='user', lookup_expr='appId__contains')
    appIdGreaterThan = filters.CharFilter(
        field_name='user', lookup_expr='gte')
    appIdSmallerThan = filters.CharFilter(
        field_name='user', lookup_expr='lte')

    class Meta:
        model = Details
        # fields = ['appId', 'name', 'user__cnic', 'courseCategory', 'domicile']
        exclude = ['appIdGreaterThan', 'appIdSmallerThan']
