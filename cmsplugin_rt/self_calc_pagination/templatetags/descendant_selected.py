from django import template

register = template.Library()

@register.assignment_tag
def descendant_selected(node):
    """Returns true if this node or a descendant of it is selected.
    Use as e.g.: {% if descendant_selected node %}
    """
    if node.selected:
        return True

    for child in node.children:
        if descendant_selected(child):
            return True
        
    return False

