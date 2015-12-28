from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def replace ( string ): 
    st = string.replace("&", "&amp;")
    st = st.replace("<", "&lt;")
    st = st.replace(" ", "&nbsp;")
    st = st.replace("\n", "</br>")
    return mark_safe(st)
