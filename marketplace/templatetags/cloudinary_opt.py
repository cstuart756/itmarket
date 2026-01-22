from __future__ import annotations

from urllib.parse import urlsplit, urlunsplit

from django import template

register = template.Library()


def _force_https(url: str) -> str:
    if not url:
        return url
    if url.startswith("http://"):
        return "https://" + url[len("http://"):]
    return url


@register.filter(name="cld_transform")
def cld_transform(url: str, transform: str = "") -> str:
    """
    Apply a Cloudinary transformation string to an existing Cloudinary delivery URL.

    Example:
      url = https://res.cloudinary.com/<cloud>/image/upload/v123/abc.jpg
      transform = f_auto,q_auto,w_600,c_limit

    Result:
      https://res.cloudinary.com/<cloud>/image/upload/f_auto,q_auto,w_600,c_limit/v123/abc.jpg

    Safety:
      - Always upgrades to https
      - If the URL does not contain '/upload/', it returns the https-upgraded URL unchanged.
    """
    url = (url or "").strip()
    transform = (transform or "").strip().strip("/")

    url = _force_https(url)

    if not transform:
        return url

    marker = "/upload/"
    if marker not in url:
        return url

    before, after = url.split(marker, 1)

    # Avoid double-inserting transformations if they are already present
    if after.startswith(transform + "/"):
        return url

    new_url = f"{before}{marker}{transform}/{after}"

    # Keep scheme/host normalized (and https)
    parts = urlsplit(new_url)
    new_url = urlunsplit(("https", parts.netloc, parts.path, parts.query, parts.fragment))
    return new_url
