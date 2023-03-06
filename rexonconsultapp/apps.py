from django.apps import AppConfig


class RexonconsultappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rexonconsultapp'

    def ready(self):
    	import rexonconsultapp.signals
