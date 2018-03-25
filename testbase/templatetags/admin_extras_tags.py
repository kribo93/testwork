from django import template
from django.core import urlresolvers

register = template.Library()
"""Creation link for edit object of model in admin panel"""

def create_link_edit(obj):
    link = urlresolvers.reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
    return link

class AdminEditNode(template.Node):
    def __init__(self, object):
        self.object = template.Variable(object)
    def render(self, context):
        return create_link_edit(self.object.resolve(context))

def edit_admin(parser, token):
    tagname, object = token.split_contents()
    return AdminEditNode(object)
register.tag('edit_admin', edit_admin)


"""Creation link for delete object of model in admin panel"""

def create_link_delete(obj):
    link = urlresolvers.reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
    return link

class AdminDeleteNode(template.Node):
    def __init__(self, object):
        self.object = template.Variable(object)
    def render(self, context):
        return create_link_delete(self.object.resolve(context))

def delete_admin(parser, token):
    tagname, object = token.split_contents()
    return AdminDeleteNode(object)
register.tag('delete_admin', delete_admin)

"""Creation link for add object of model in admin panel"""

def create_link_add(obj):
    link = urlresolvers.reverse('admin:%s_%s_add' % (obj._meta.app_label, obj._meta.model_name))
    return link

class AdminAddNode(template.Node):
    def __init__(self, object):
        self.object = template.Variable(object)
    def render(self, context):
        return create_link_add(self.object.resolve(context))

def add_admin(parser, token):
    tagname, object = token.split_contents()
    return AdminAddNode(object)
register.tag('add_admin', add_admin)
