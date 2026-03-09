from django import template

register = template.Library()

@register.filter
def filter_by_student(applications, student):
    return [app for app in applications if app.student == student]