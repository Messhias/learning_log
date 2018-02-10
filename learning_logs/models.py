from django.db import models


# TOPIS models

class Topic(models.Model):
    # A SUBJECT THAT WHAT YOU LEARNING
    text = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # RETURNS THIS MODEL STRING REPRESENTATION
        return self.text

class Entry(models.Model):
    # SPECIFIC DATA FOR SOMETING LEARNED
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        # returns string model
        return self.text[:50] + "..."
