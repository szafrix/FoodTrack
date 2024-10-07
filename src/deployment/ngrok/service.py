import ngrok
from src.configs.app_config import AppConfig


class NgrokService:
    def __init__(self, app_config: AppConfig):
        self.app_config = app_config
        self.listener = None

    def start_ngrok(self):
        if self.app_config.ngrok.use_ngrok:
            if self.app_config.ngrok.allowed_emails:
                self.listener = ngrok.forward(
                    self.app_config.rest_api.port,
                    authtoken=self.app_config.ngrok.auth_token,
                    oauth_provider="google",
                )
            else:
                self.listener = ngrok.forward(
                    self.app_config.rest_api.port,
                    authtoken=self.app_config.ngrok.auth_token,
                )
            print(f"Ngrok connection opened: {self.listener.url()}")

    def stop_ngrok(self):
        if self.listener:
            ngrok.disconnect(self.listener.url())
            print("Ngrok connection closed.")
