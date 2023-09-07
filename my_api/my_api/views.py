from .models import UserInfo
from .serializer import UserInfoSerializer
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from .models import UserInfo

def welcome_view(request):
    return HttpResponse("Welcome")


def user_info(request):
    """
        Return User request in Json response
    """
    slack_name = request.GET.get('slack_name')
    track_name = request.GET.get('track')

    if (slack_name and track_name):
        try:
            slack_name = UserInfo.objects.get(slack_name=slack_name)
            track_name = UserInfo.objects.get(track=track_name)

        except UserInfo.DoesNotExist:
            return HttpResponseBadRequest("Invalid parameters")

        else:
            info = UserInfo.objects.all()
            serializer = UserInfoSerializer(info, many=True)
            return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponseBadRequest("Missing parameter")