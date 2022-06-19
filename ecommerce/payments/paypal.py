from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = 'AWPXqTwYrPwxDqQ_JMYTMeDlkDL7XmCnpiSWnNe-gIluk7O8T423_Q0LLKEDO-FczfzZIh4wEYJWbKhU'
        self.secret_key = 'EKvnjOdD5Pb9uiXtVbRwo-yoyTNajqnKl53AjOps_HXBrS2K_rMLFYvGEhkiyteB7DDx47uuuOBTW7-o'
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.secret_key)
        self.client = PayPalHttpClient(self.environment)

