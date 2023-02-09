from django.apps import AppConfig


class LancelotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lancelot'

    def ready(self):
        import lancelot.signals
