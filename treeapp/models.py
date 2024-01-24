from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class TreeNode(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.label