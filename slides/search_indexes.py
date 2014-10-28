from haystack import indexes
from slides.models import Resource, StaticPage


class ResourceIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(
        document=True,
        use_template=True,
        model_attr='text'
    )
    creator = indexes.CharField(model_attr='creator')
    date = indexes.CharField(model_attr='date')
    slide = indexes.CharField(model_attr='slide')

    def get_model(self):
        return Resource

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


class StaticPageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(
        document=True,
        use_template=True,
        model_attr='text',
    )
    title = indexes.CharField(model_attr='pres_title')
    url = indexes.CharField(model_attr='url')

    def get_model(self):
        return StaticPage

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()