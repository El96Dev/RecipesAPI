from core.models import Article
from .schemas import ArticleGet


def orm_to_pydantic(article_orm: Article) -> ArticleGet:
    """
    Converts Article ORM object into Pydantic ArticleGet.
    """
    return ArticleGet(
        id=article_orm.id,
        title=article_orm.title,
        text=article_orm.text,
        image_filename=article_orm.image_filename,
        created_at=article_orm.created_at,
        views_count=len(article_orm.views)
    )

def orm_list_to_pydantic(orm_articles: Article) -> list[ArticleGet]:
    """
    Converts a list of Article ORM objects into list of Pydantic ArticleGet.
    """
    return [orm_to_pydantic(article) for article in orm_articles]