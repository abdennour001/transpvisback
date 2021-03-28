from django.apps import AppConfig


class TransparencyConfig(AppConfig):
    name = "transparency"

    def ready(self):
        import transparency.signals