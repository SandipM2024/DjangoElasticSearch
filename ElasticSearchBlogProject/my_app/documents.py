from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Blog

@registry.register_document
class BlogDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'blog'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Blog  # The model associated with this document
        fields = [
            'title',
            'content',
           
        ]
