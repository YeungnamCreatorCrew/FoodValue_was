from datetime import datetime
from typing import Annotated

from pydantic import Field, StringConstraints, model_validator

from app.core.constants import (
    ID_MAX,
    RECIPE_EXCLUDED_INGREDIENTS_MAX,
    RECIPE_FRIDGE_INGREDIENTS_MAX,
    RECIPE_INGREDIENT_NAME_MAX_LENGTH,
    RECIPE_ITEM_NAME_MAX_LENGTH,
    RECIPE_LIST_MAX_COUNT,
    RECIPE_MAIN_INGREDIENTS_MAX,
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


FridgeIngredientId = Annotated[int, Field(ge=1, le=ID_MAX)]


class RecipeGenerateRequest(CamelModel):
    # 직접 입력한 재료. 냉장고 재료를 고르면 비워도 된다
    main_ingredients: list[IngredientText] = Field(default_factory=list, max_length=RECIPE_MAIN_INGREDIENTS_MAX)
    # 내 냉장고 재료(fridge_ingredient.id). 서버가 소유자·삭제·잔량을 확인한 뒤 이름으로 바꿔 주재료에 합친다
    fridge_ingredient_ids: list[FridgeIngredientId] = Field(
        default_factory=list, max_length=RECIPE_FRIDGE_INGREDIENTS_MAX
    )
    excluded_ingredients: list[IngredientText] = Field(default_factory=list, max_length=RECIPE_EXCLUDED_INGREDIENTS_MAX)
    request_note: Annotated[str, Field(max_length=RECIPE_REQUEST_NOTE_MAX_LENGTH)] = ""

    @model_validator(mode="after")
    def _need_main_ingredient(self):
        if not self.main_ingredients and not self.fridge_ingredient_ids:
            raise ValueError("주재료를 직접 입력하거나 냉장고 재료를 선택해야 합니다")
        return self


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
