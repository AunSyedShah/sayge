from datetime import datetime
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from .snowflake_data import company_snapshot as company_snapshot_data
from .serializers import CompanySnapshotSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def company_snapshot(request):
    try:
        date = datetime.strptime(request.GET['date'], '%Y-%m-%d')
    except MultiValueDictKeyError:
        date = datetime.today()
    data = company_snapshot_data(date=date)

    serializer = CompanySnapshotSerializer(data=data, many=True)
    if serializer.is_valid():
        return Response(serializer.validated_data)
    return Response(serializer.errors)
