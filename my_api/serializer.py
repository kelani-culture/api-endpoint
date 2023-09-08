from rest_framework import serializers
from .models import UserInfo

"""
    serializes the python object
"""
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['slack_name', 'current_day',\
                  'utc_time', 'track',\
                  'github_file_url',\
                  'github_repo_url',\
                  'status_code']