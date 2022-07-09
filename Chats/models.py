from django.db import models


# Create your models
class Text(models.Model):
    from_user = models.ForeignKey('Accounts.Profile', on_delete=models.CASCADE, related_name='from_user')
    text = models.CharField(max_length=1000)
    to = models.ForeignKey('Accounts.Profile', on_delete=models.CASCADE, related_name='to')
    time = models.DateTimeField(auto_now=True)