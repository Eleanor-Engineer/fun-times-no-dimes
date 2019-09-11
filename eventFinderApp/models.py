from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_time = models.DateTimeField('start time and date')
    end_time = models.DateTimeField('end time and date')
    #07/09/2019 Eleanor. The line below is to add a new "venue" field to the Event model.  The null part means the user doesn't have to enter a value.
    venue=models.CharField(max_length=200, null=True)
    ##07/09/2019 Eleanor. This is an optional line for a link to the main event page. This may not work.
    #link=models.link('link to event page') #Yep, it doesn't work. Maybe it can be fixed at a later point.

    #07/09/2019 Eleanor. This is to make a many to many relationship with categories. 
    category = models.ManyToManyField('Category')


class Category(models.Model):
    name = models.CharField(max_length=50)