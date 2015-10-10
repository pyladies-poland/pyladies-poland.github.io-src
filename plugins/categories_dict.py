"""
This plugin appends 'categories_dict' to articles' generator context.
Keys are category slugs, while values are lists of article objects
that are assigned to the category.
"""

from pelican import signals


def create_categories_dict(article_generator):
    categories_dict = {}
    for category, articles in article_generator.categories:
        categories_dict[category.name] = articles

    article_generator.context['categories_dict'] = categories_dict


def register():
    signals.article_generator_finalized.connect(create_categories_dict)
