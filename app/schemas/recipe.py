from datetime import datetime
from typing import Annotated

from pydantic import Field, StringConstraints

from app.core.constants import (
    RECIPE_EXCLUDED_INGREDIENTS_MAX,
    RECIPE_INGREDIENT_NAME_MAX_LENGTH,
    RECIPE_ITEM_NAME_MAX_LENGTH,
    RECIPE_LIST_MAX_COUNT,
    RECIPE_MAIN_INGREDIENTS_MAX,
    RECIPE_MAIN_INGREDIENTS_MIN,
    RECIPE_REQUEST_NOTE_MAX_LENGTH,
    RECIPE_SERVINGS_MAX,
    RECIPE_STEP_MAX_LENGTH,
    RECIPE_STEPS_MAX_COUNT,
    RECIPE_TITLE_MAX_LENGTH,
)
from app.schemas.common import CamelModel

IngredientText = Annotated[
    str, StringConstraints(strip_whitespace=True, min_length=1, max_length=RECIPE_INGREDIENT_NAME_MAX_LENGTH)
]
ItemText = Annotated[str, Field(min_length=1, max_length=RECIPE_ITEM_NAME_MAX_LENGTH)]


class RecipeGenerateRequest(CamelModel):
    main_ingredients: list[IngredientText] = Field(
        min_length=RECIPE_MAIN_INGREDIENTS_MIN, max_length=RECIPE_MAIN_INGREDIENTS_MAX
    )
    excluded_ingredients: list[IngredientText] = Field(default_factory=list, max_length=RECIPE_EXCLUDED_INGREDIENTS_MAX)
    request_note: Annotated[str, Field(max_length=RECIPE_REQUEST_NOTE_MAX_LENGTH)] = ""


class RecipeItem(CamelModel):
    name: ItemText
    amount: ItemText


class Recipe(CamelModel):
    title: Annotated[str, Field(min_length=1, max_length=RECIPE_TITLE_MAX_LENGTH)]
    servings: Annotated[int, Field(ge=1, le=RECIPE_SERVINGS_MAX)]
    ingredients: list[RecipeItem] = Field(min_length=1, max_length=RECIPE_LIST_MAX_COUNT)
    seasonings: list[RecipeItem] = Field(max_length=RECIPE_LIST_MAX_COUNT)
    steps: list[Annotated[str, Field(min_length=1, max_length=RECIPE_STEP_MAX_LENGTH)]] = Field(
        min_length=1, max_length=RECIPE_STEPS_MAX_COUNT
    )


class SavedRecipeSummary(CamelModel):
    id: int
    title: str
    created_at: datetime


class SavedRecipeDetail(SavedRecipeSummary):
    content: Recipe
