from django.db import models


class DynamicTable(models.Model):
    name = models.CharField(max_length=150, unique=True)
    schema = models.JSONField()

    def __str__(self):
        return self.name
