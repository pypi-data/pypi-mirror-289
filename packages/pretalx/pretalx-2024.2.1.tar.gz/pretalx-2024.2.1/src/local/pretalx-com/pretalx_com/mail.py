from contextlib import suppress

import dns.resolver
from django.core.mail.backends.smtp import EmailBackend


class OptionalMailjetBackend(EmailBackend):
    """This email backend is only used if an event has no custom email server
    configured."""

    MAILJET_USER = "8f9a84f51de29849a91e3123c4e12c0a"
    MAILJET_PASS = "fb33d292cb7669362331497981659f5e"
    MAILJET_SERVER = "in-v3.mailjet.com"
    MAILJET_PORT = 587

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.uses_mailjet = False
        self.connection_data = {
            key: getattr(self, key, None)
            for key in (
                "host",
                "port",
                "username",
                "password",
                "use_tls",
                "use_ssl",
                "timeout",
                "ssl_keyfile",
                "ssl_certfile",
            )
        }

    def switch_to_mailjet(self):
        self.close()
        self.host = "in-v3.mailjet.com"
        self.port = 587
        self.username = self.MAILJET_USER
        self.password = self.MAILJET_PASS
        self.use_tls = True
        self.use_ssl = False
        self.timeout = None
        self.ssl_keyfile = None
        self.ssl_certfile = None
        self.uses_mailjet = True
        self.open()

    def switch_from_mailjet(self):
        self.close()
        for key in (
            "host",
            "port",
            "username",
            "password",
            "use_tls",
            "use_ssl",
            "timeout",
            "ssl_keyfile",
            "ssl_certfile",
        ):
            setattr(self, key, self.connection_data.get(key))
        self.uses_mailjet = False
        self.open()

    def _send(self, email_message):
        """Copied from the Django version."""
        if not email_message.recipients():
            return False
        if "@pretalx.com" not in email_message.from_email:
            return super()._send(email_message)
        needs_mailjet = False
        with suppress(Exception):
            domains = {
                recipient.split("@")[-1] for recipient in email_message.recipients()
            }
            lookups = set()
            with suppress(Exception):
                for domain in domains:
                    lookups |= {
                        resolved.to_text()
                        for resolved in dns.resolver.query(domain, "MX")
                    }
            needs_mailjet = any(
                "mail.protection.outlook" in lo or "eo.outlook.com" in lo.lower()
                for lo in lookups
            )
        if not needs_mailjet and self.uses_mailjet:
            self.switch_from_mailjet()
        elif needs_mailjet and not self.uses_mailjet:
            self.switch_to_mailjet()
        super()._send(email_message)
