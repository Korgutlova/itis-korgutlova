from django.db import models
import datetime

statuses = (
    ("T", "To Do"),
    ("P", "In Progress"),
    ("R", "Review"),
    ("D", "Done"),
)


class Task(models.Model):
    # text = models.TextField()
    text = models.CharField(max_length=140)
    deadline = models.DateTimeField(blank=True, null=True, default=datetime.datetime.today)
    status = models.CharField(max_length=1, choices=statuses, default="T")
    priority = models.IntegerField(default=5)

    def __str__(self):
        return "%s : %s : %s" % (self.text, self.priority, self.get_status_display())

