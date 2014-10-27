__author__ = 'miguelbarbosa'

from haystack import indexes
from slides.models import Resource


class ResourceIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    creator = indexes.CharField(model_attr='creator')
    date = indexes.CharField(model_attr='date')
    text2 = indexes.CharField(model_attr='text')
    slide = indexes.CharField(model_attr='slide')

    def get_model(self):
        return Resource

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()