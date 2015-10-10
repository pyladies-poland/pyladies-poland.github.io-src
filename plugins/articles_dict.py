"""
This plugin appends 'articles_dict' to articles' generator context.
Keys are article slugs, while values are article objects.
"""

from pelican import signals


def create_articles_dict(article_generator):
    articles_dict = {}
    for article in article_generator.articles:
        articles_dict[article.slug] = article

    article_generator.context['articles_dict'] = articles_dict


def register():
    signals.article_generator_finalized.connect(create_articles_dict)
