from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

  # add this
    def ready(self):
        import home.signals  # noqa
