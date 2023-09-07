from django.db import models
from .utils import get_current_day, get_current_time

class UserInfo(models.Model):
    """User information model
    """
    slack_name = models.CharField(max_length=50)
    current_day = models.CharField(max_length=10,\
                                  default=get_current_day(),\
                                  )
    
    track = models.CharField(max_length=10,
                             default='backend'
                             )
    utc_time = models.CharField(max_length = 100,
                                default=get_current_time())

    github_file_url = models.URLField()

    github_repo_url = models.URLField()

    status_code = models.IntegerField(default=200)    