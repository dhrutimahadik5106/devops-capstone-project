
"""
Accounts Service Application.

Flask application configuration with Talisman
security headers and CORS policies.
"""

from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman


app = Flask(__name__)

app.config["SECRET_KEY"] = "change-this-in-production"

CORS(
    app,
    resources={
        r"/api/*": {
            "origins": ["http://localhost:8080"]
        }
    }
)

csp = {
    "default-src": "'self'",
    "script-src": "'self'",
    "style-src": "'self'",
    "img-src": "'self' data:",
}

Talisman(
    app,
    content_security_policy=csp,
    force_https=False
)
