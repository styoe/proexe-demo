from django.db import models


class Table(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=180)
    fields = models.JSONField() # Add custom schema validator
    created = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name
    
