"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os

import django
from channels.routing import get_default_application
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

try:
    from newrelic import agent
except ImportError:
    pass
else:
    agent.initialize()
    agent.wrap_web_transaction("django.core.handlers.base", "BaseHandler.get_response")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

django.setup()

SENTRY_DSN = os.environ.get("SENTRY_DSN")
if SENTRY_DSN:  # pragma: nocover
    application = SentryAsgiMiddleware(get_default_application())
else:
    application = get_default_application()
