from django.contrib import admin
from .models import TreeNode

class TreeNodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'label', 'parent_label')

    def parent_label(self, obj):
        return obj.parent.label if obj.parent else None

    parent_label.short_description = 'Parent Label'

admin.site.register(TreeNode, TreeNodeAdmin)