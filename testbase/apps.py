from django.apps import AppConfig

class TestbaseConfig(AppConfig):
    name = 'testbase'

    def ready(self):
        import testbase.signals