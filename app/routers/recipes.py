from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, Query, status
from sqlalchemy.orm import Session

from app.core.constants import ID_MAX, PAGE_DEFAULT_SIZE, PAGE_MAX_SIZE
from app.core.db import get_db
from app.core.deps import get_current_user
from app.models.user import User
from app.schemas.common import Page
from app.schemas.recipe import (
    Recipe,
    RecipeGenerateRequest,
    SavedRecipeDetail,
    SavedRecipeSummary,
)
from app.services import recipe_service

router = APIRouter(tags=["recipes"])

SavedRecipeId = Annotated[int, Path(ge=1, le=ID_MAX)]


@router.post("/recipes/generate", response_model=Recipe)
def generate_recipe(
    body: RecipeGenerateRequest, db: Session = Depends(get_db), user: User = Depends(get_current_user)
):
    try:
        return recipe_service.generate_recipe(db, user, body)
    except recipe_service.FridgeIngredientNotFoundError:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "냉장고 재료를 찾을 수 없습니다") from None
    except recipe_service.InvalidIngredientsError as e:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_CONTENT, str(e)) from None
    except recipe_service.RecipeTimeoutError:
        raise HTTPException(status.HTTP_504_GATEWAY_TIMEOUT, "레시피 생성 시간이 초과되었습니다") from None
    except recipe_service.RecipeGenerationError:
        raise HTTPException(status.HTTP_502_BAD_GATEWAY, "레시피를 생성하지 못했습니다") from None


@router.post("/recipes/saved", response_model=SavedRecipeDetail, status_code=status.HTTP_201_CREATED)
def save_recipe(body: Recipe, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return recipe_service.save_recipe(db, user, body)


@router.get("/recipes/saved", response_model=Page[SavedRecipeSummary])
def list_saved_recipes(
    page: int = Query(1, ge=1),
    size: int = Query(PAGE_DEFAULT_SIZE, ge=1, le=PAGE_MAX_SIZE),
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return recipe_service.list_saved(db, user, page, size)


@router.get("/recipes/saved/{recipe_id}", response_model=SavedRecipeDetail)
def get_saved_recipe(recipe_id: SavedRecipeId, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    try:
        return recipe_service.get_saved(db, user, recipe_id)
    except recipe_service.NotFoundError:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "저장한 레시피를 찾을 수 없습니다") from None


@router.delete("/recipes/saved/{recipe_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_saved_recipe(
    recipe_id: SavedRecipeId, db: Session = Depends(get_db), user: User = Depends(get_current_user)
):
    try:
        recipe_service.delete_saved(db, user, recipe_id)
    except recipe_service.NotFoundError:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "저장한 레시피를 찾을 수 없습니다") from None
