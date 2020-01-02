from django.apps import AppConfig


class AwardsConfig(AppConfig):
    name = 'awards'

    def ready(self):
        '''
        function that helps in importing the signals to auto create a profile for a new user
        '''
        import awards.signals
