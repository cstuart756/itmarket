# config/middleware.py
class SecurityHeadersMiddleware:
    """
    Adds additional security headers to every response.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Prevent MIME sniffing
        response.setdefault("X-Content-Type-Options", "nosniff")

        # Clickjacking protection
        response.setdefault("X-Frame-Options", "DENY")

        # Referrer policy
        response.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")

        # Optional CSP: upgrades accidental http:// and blocks mixed content
        response.setdefault(
            "Content-Security-Policy",
            "upgrade-insecure-requests; block-all-mixed-content"
        )

        return response
