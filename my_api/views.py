from .models import UserInfo
from .serializer import UserInfoSerializer
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from .models import UserInfo

def welcome_view(request):
    return HttpResponse("Welcome")


def user_info(request) -> JsonResponse:
    """
        Return User request in Json response
    """
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    if slack_name and track:
        update_info = UserInfo.objects.create(slack_name=slack_name,
                                               track=track)
        user_info = UserInfo.objects.all()
        user_data = {
            "slack_name": user_info[1].slack_name,
            "current_day":user_info[1].current_day,
            "utc_time": user_info[1].utc_time,
            "track": user_info[1].track,
            "github_file_url": user_info[1].github_file_url,
            "github_repo_url": user_info[1].github_repo_url,
            "status_code": user_info[1].status_code
        }
        return JsonResponse(user_data, safe=False)
    else:
        return JsonResponse({"error": None}, safe=False)