from haystack import indexes
from haystack_static_pages.models import StaticPage


class StaticPageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(
        document=True, use_template=True,
        template_name='staticpage_text.txt'
    )
    title = indexes.CharField(model_attr='title')
    url = indexes.CharField(model_attr='url')
    content = indexes.CharField(model_attr='content')
    description = indexes.CharField(model_attr='description')
    language = indexes.CharField(model_attr='language')

    def get_model(self):
        return StaticPage

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


#site.register(StaticPage, StaticPageIndex)
