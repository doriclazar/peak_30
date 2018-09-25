from django.db import models
from django.contrib.auth.models import User

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete = models.DO_NOTHING, related_name='user_settings')
    chart_capacity_type = models.CharField(max_length = 32, default='doghnut')
    chart_comparison_type = models.CharField(max_length = 32, default='line')
    chart_period = models.IntegerField(default=3)

    class Meta:
        verbose_name = "User Settings"
        verbose_name_plural = "User Settings"
