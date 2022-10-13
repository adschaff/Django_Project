from django.db import models


# Creates model of Campus Name
class CampusName(models.Model):
    Campus_Name = models.CharField(max_length=80, default="", blank=True, null=False)
    Campus_ID = models.IntegerField(default="", blank=True, null=False)
    State = models.CharField(max_length=2, default="", blank=True, null=False)

    # Creates model manager
    object = models.Manager()

    # Displays the object output values in the form of a string
    def __str__(self):
        # Returns the input value of the Campus
        # field as a tuple to display in the browser instead of the default title
        display_campus_state = '{0.Campus_Name}: {0.Campus_ID}'
        return display_campus_state.format(self)
