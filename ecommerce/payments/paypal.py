from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = ''
        self.secret_key = ''
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.secret_key)
        self.client = PayPalHttpClient(self.environment)

