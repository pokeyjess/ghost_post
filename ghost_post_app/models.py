from django.db import models
from django.utils import timezone

class Posts(models.Model):
    boast_or_roast = models.BooleanField()
    content = models.CharField(max_length=280)
    up_votes = models.IntegerField()
    down_votes = models.IntegerField()
    total_votes = models.IntegerField(default=0)
    post_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.content} - {self.post_time}"
        if self.boast_or_roast == "Boast":
            return True
        else:
            return False

    

    
