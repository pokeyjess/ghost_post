from django.db import models
from django.utils import timezone

class Posts(models.Model):
    boast_or_roast = models.BooleanField()
    content = models.CharField(max_length=280)
    up_votes = models.IntegerField()
    down_votes = models.IntegerField()
    post_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        if self.boast_or_roast == "Boast":
            return True
        else:
            return False

    def message(self):
        return f"{self.content} - {self.post_time}"

    def votes(self):
        return self.up_votes - self.down_votes

    
