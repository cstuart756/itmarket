# marketplace/templatetags/cloudinary_opt.py
from django import template

register = template.Library()

@register.filter
def cld_transform(url: str, transformation: str) -> str:
    """
    Insert a Cloudinary transformation string into an existing Cloudinary URL.
    Example transformation: "f_auto,q_auto,w_600,c_limit"
    """
    if not url:
        return url
    needle = "/upload/"
    if needle not in url:
        return url
    return url.replace(needle, f"{needle}{transformation}/", 1)
