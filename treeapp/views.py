from django.shortcuts import render, redirect
from django.views.generic import View
from .models import TreeNode
from .forms import TreeNodeForm

class TreeView(View):
    template_name = 'treeapp/tree.html'

    def get(self, request):
        nodes = TreeNode.objects.all()
        form = TreeNodeForm()
        return render(request, self.template_name, {'nodes': nodes, 'form': form})

class AddNodeView(View):
    template_name = 'treeapp/tree.html'

    def get(self, request):
        nodes = TreeNode.objects.all()
        form = TreeNodeForm()
        return render(request, self.template_name, {'nodes': nodes, 'form': form})

    def post(self, request):
        form = TreeNodeForm(request.POST)
        if form.is_valid():
            parent_id = request.POST.get('parent')
            if parent_id:
                parent_node = TreeNode.objects.get(id=parent_id)
                form.instance.parent = parent_node
            form.save()
        return redirect('tree')

class EditNodeView(View):
    def post(self, request, node_id):
        node = TreeNode.objects.get(id=node_id)
        form = TreeNodeForm(request.POST, instance=node)
        if form.is_valid():
            form.save()
        return redirect('tree')

class DeleteNodeView(View):
    def post(self, request, node_id):
        node = TreeNode.objects.get(id=node_id)
        node.delete()
        return redirect('tree')
