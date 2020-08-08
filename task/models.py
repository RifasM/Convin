from django.db import models


choices = (("daily", "Daily"), ("weekly", "Weekly"), ("monthly", "Monthly"))


class Task(models.Model):
    """
     task should have task_type(integer) and task_desc(string)
    """
    task_type = models.IntegerField(help_text="Enter Task Type",
                                    blank=False)
    task_desc = models.CharField(max_length=100,
                                 help_text="Task Description",
                                 blank=False)

    class Meta:
        ordering = ['task_type']

    def __str__(self):
        return "{}".format(self.task_type)


class TaskTracker(models.Model):
    """
    tracker should have task_type(type of task to track),
    update_type(per day, weekly or monthly) and email
    """
    task_type = models.ForeignKey(to=Task,
                                  on_delete=models.CASCADE)
    update_type = models.CharField(choices=choices,
                                   blank=False,
                                   default="daily")
    email = models.EmailField(help_text="Enter Email to send Updates",
                              blank=False)

    class Meta:
        ordering = ["task_type"]

    def __str__(self):
        return "{}".format(self.task_type)
