from slides.models import Person
from django.db import models
from haystack import signals


class UserOnlySignalProcessor(signals.BaseSignalProcessor):
    # Does not work yet.  Don't really know how to customize it yet.

    def setup(self):
        # Listen only to the ``User`` model.
        models.signals.post_save.connect(self.handle_save, sender=Person)
        models.signals.post_delete.connect(self.handle_delete, sender=Person)

    def teardown(self):
        # Disconnect only for the ``User`` model.
        models.signals.post_save.disconnect(self.handle_save, sender=Person)
        models.signals.post_delete.disconnect(self.handle_delete, sender=Person)