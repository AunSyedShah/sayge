from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework import serializers

TO_EMAILS = settings.CONTACT_EMAILS
EMPLOYEE_COUNT_RANGE = {
    '1_50': '1-50 employees',
    '51_200': '51-200 employees',
    '201_500': '201-500 employees',
    '501+': '501+ employees',
}


class EmailSerializer(serializers.Serializer):
    first_name = serializers.CharField(min_length=1, max_length=200)
    last_name = serializers.CharField(min_length=1, max_length=200)
    work_email = serializers.EmailField()
    phone_number = serializers.CharField(allow_blank=True)
    company_name = serializers.CharField(min_length=1, max_length=200)
    employee_count_range = serializers.ChoiceField(choices=[
        (k, v) for k, v in EMPLOYEE_COUNT_RANGE.items()
    ])


def format_subject_and_body(data):
    subject = f'Demo Request - {data["company_name"]}'
    employee_count = EMPLOYEE_COUNT_RANGE[data['employee_count_range']]
    body = (
        f'First Name: {data["first_name"]}\n'
        f'Last Name: {data["last_name"]}\n'
        f'Work Email: {data["work_email"]}\n'
        f'Phone Number (Optional): {data["phone_number"]}\n'
        f'Company Name: {data["company_name"]}\n'
        f'Employee Count Range: {employee_count}\n'
    )
    return subject, body


@api_view(['POST'])
@permission_classes([AllowAny])
@renderer_classes([JSONRenderer])
def send_email(request):
    serializer = EmailSerializer(data=request.data)

    if serializer.is_valid():
        payload = serializer.validated_data
        subject, body = format_subject_and_body(payload)
        send_mail(
            subject,
            body,
            payload['work_email'],
            TO_EMAILS,
            fail_silently=False,
        )

        return Response({}, status=201)

    else:
        return Response({"errors": serializer.errors}, status=400)
