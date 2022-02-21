from copy import copy

from services import NotificationService


class NotificationWorker:
    def process(self, body):
        service = NotificationService()
        service.eloqua_register(copy(body))
        service.sm_register(copy(body))
        service.notify_reporters()
