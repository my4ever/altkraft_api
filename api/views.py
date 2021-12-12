from django.shortcuts import redirect, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.models import Link, ValidCode
from api.serializers import CodeSerializer
from api.code_generator import generate_code

generate_code()


@api_view(['GET'])
def add_url(request) -> Response or HttpResponse:
    """
    Checks if url parameter in request dictionary.
    Checks for such url existing in DB.
    If url isn`t uniq returns the code for this url.
    If url is uniq generates the uniq code for this url
    and add code in DB.
    """
    url = request.data.get('url') or request.GET.get('url')
    # Checking if url parameter was passed in request.
    if not url:
        return HttpResponse('There is not a url parameter')
    link, obj_status = Link.objects.get_or_create(url=url)
    # If status create equals False. In other words - if url is in DB.
    if not obj_status:
        serializer = CodeSerializer(data={'code': link.code})
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
    # Working with new url
    code = ValidCode.objects.all().first()  # Getting a code
    link.code = str(code)  # assign code to url
    link.save()  # saving instance with new code
    code.delete()  # Delete used code from ValidCode table
    generate_code()  # Creating a new code so storage of Valid Codes would be filled.
    serializer = CodeSerializer(data={'code': link.code})

    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def show_url(request, code) -> redirect or HttpResponse:
    """
    Takes code as an argument.
    Check for correct len of the code.
    Looks in DB for row with given code.
    If row does exist, redirects to url.
    If no such code in DB, return html msg.
    """
    # Checking for code being valid length
    if len(code) != 8:
        return HttpResponse('Код должен состоять из восьми символов. '
                            f'Код предостваленный вами - {code} '
                            f'состит из {len(code)} символов. '
                            'Пожалуйста проверте код.')

    link = Link.objects.filter(code=code)
    # Checking for instance in DB with the code
    if len(link) == 1:
        url = link[0].url
        return redirect(url)

    return HttpResponse(f'{code} этот код не привязан к ссылке.')