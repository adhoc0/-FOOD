from recipes.selectors import RecipeSelector


class SearchService:
    """Recipe search."""

    @staticmethod
    def search(query: str):
        return RecipeSelector.search(query)