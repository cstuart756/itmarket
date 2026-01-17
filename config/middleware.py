# config/middleware.py
class SecurityHeadersMiddleware:
    """
    Minimal security headers including CSP.
    Adjust domains as needed if you add analytics/CDNs.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # CSP: keep it simple but effective
        csp = (
            "default-src 'self'; "
            "img-src 'self' data: https:; "
            "script-src 'self' https://cdn.jsdelivr.net; "
            "style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://fonts.googleapis.com; "
            "font-src 'self' https://fonts.gstatic.com; "
            "connect-src 'self'; "
            "base-uri 'self'; "
            "frame-ancestors 'none'; "
            "object-src 'none'; "
        )
        response["Content-Security-Policy"] = csp

        # These complement CSP
        response["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
        return response
