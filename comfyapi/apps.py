from django.apps import AppConfig


class ComfyapiConfig(AppConfig):
    name = 'comfyapi'

    def ready(self):
        import comfyapi.signals
