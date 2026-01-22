from __future__ import annotations

from django import template

register = template.Library()


def _force_https(url: str) -> str:
    url = (url or "").strip()
    if url.startswith("http://"):
        return "https://" + url[len("http://"):]
    if url.startswith("//"):
        return "https:" + url
    return url


@register.filter(name="cld_transform")
def cld_transform(url: str, transform: str = "") -> str:
    """
    Apply Cloudinary transformation to a Cloudinary delivery URL and ALWAYS return HTTPS.
    """
    url = _force_https(url)
    transform = (transform or "").strip().strip("/")

    if not url or not transform:
        return _force_https(url)

    marker = "/upload/"
    if marker not in url:
        return _force_https(url)

    before, after = url.split(marker, 1)

    # Avoid double insertion
    if after.startswith(transform + "/"):
        return _force_https(url)

    new_url = f"{before}{marker}{transform}/{after}"
    return _force_https(new_url)
