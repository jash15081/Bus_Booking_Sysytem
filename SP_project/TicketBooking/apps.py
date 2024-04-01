from django.apps import AppConfig


class TicketbookingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TicketBooking'

    def ready(self):
        import TicketBooking.signals 