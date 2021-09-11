from admin_dashboard.serializers import AdminDashboardSerializer
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from user_details.models import Details
from .filters import CandidateFilter

# Create your views here.


class AdminDashboardView(viewsets.GenericViewSet, mixins.ListModelMixin):

    queryset = Details.objects.all()
    serializer_class = AdminDashboardSerializer
    filterset_class = CandidateFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        submitted_applicant_queryset = queryset.filter(
            user__applicationStatus__isSubmitted=True, user__applicationStatus__isAccepted=False)
        accepted_applicant_queryset = queryset.filter(
            user__applicationStatus__isAccepted=True)
        submitted_applicant_serializer = self.get_serializer(
            submitted_applicant_queryset, many=True)
        accepted_applicant_serializer = self.get_serializer(
            accepted_applicant_queryset, many=True)
        submitted_applicants = {
            'submittedApplicantsDetails': submitted_applicant_serializer.data,
        }
        accepted_applicants = {
            'acceptedApplicantsDetails': accepted_applicant_serializer.data
        }
        return Response(data={
            'success': True,
            'message': 'successfully fetched records',
            'data': [submitted_applicants, accepted_applicants]
        })
