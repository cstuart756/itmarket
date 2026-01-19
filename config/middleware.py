class SecurityHeadersMiddleware:
    """
    Adds additional security headers to every response.

    Django can also set many of these via settings. This middleware is a simple,
    explicit place to enforce baseline headers for beginners.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Prevent MIME sniffing
        response.setdefault("X-Content-Type-Options", "nosniff")

        # Clickjacking protection (also set by X_FRAME_OPTIONS in settings)
        response.setdefault("X-Frame-Options", "DENY")

        # Referrer policy
        response.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")

        return response
