from datetime import date
from typing import Annotated

from fastapi import APIRouter, Depends, File, Form, HTTPException, Path, Query, UploadFile
from sqlalchemy.orm import Session

from app.core.constants import ID_MAX, IMAGE_MAX_BYTES, PAGE_MAX_SIZE
from app.core.db import get_db
from app.core.deps import get_current_user
from app.models.user import User
from app.schemas.common import Page
from app.schemas.fridge import (Consume, FoodType, IngredientCreate, IngredientResponse, IngredientUpdate,
                                ItemResponse, ReceiptConfirm, Sort, Storage, UsageResponse)
from app.services import fridge_service as service, receipt_service

router = APIRouter(prefix='/fridge', tags=['fridge'])
Db = Annotated[Session, Depends(get_db)]
CurrentUser = Annotated[User, Depends(get_current_user)]
Id = Annotated[int, Path(ge=1, le=ID_MAX)]


def call(fn, *args, **kwargs):
    try:
        return fn(*args, **kwargs)
    except service.NotFoundError as exc:
        raise HTTPException(404, str(exc)) from None
    except service.InvalidOperationError as exc:
        raise HTTPException(400, str(exc)) from None
    except receipt_service.OcrError as exc:
        raise HTTPException(exc.status, str(exc)) from None


@router.get('/catalog', response_model=Page[ItemResponse])
def catalog(db: Db, user: CurrentUser, keyword: str | None = Query(None, max_length=50),
            page: int = Query(1, ge=1), size: int = Query(20, ge=1, le=PAGE_MAX_SIZE)):
    return service.list_items(db, keyword, page, size)


@router.get('/items', response_model=Page[IngredientResponse])
def listing(db: Db, user: CurrentUser, storage: Storage | None = None, food_type: FoodType | None = None,
            keyword: str | None = Query(None, max_length=50), sort: Sort = Sort.PURCHASED,
            include_empty: bool = False, page: int = Query(1, ge=1),
            size: int = Query(20, ge=1, le=PAGE_MAX_SIZE)):
    return service.list_ingredients(db, user, storage=storage, food_type=food_type,
                                    keyword=keyword, sort=sort, include_empty=include_empty, page=page, size=size)


@router.post('/items', response_model=IngredientResponse, status_code=201)
def create(body: IngredientCreate, db: Db, user: CurrentUser):
    return call(service.create, db, user, body)


@router.get('/summary')
def summary(db: Db, user: CurrentUser):
    return service.summary(db, user)


@router.get('/nutrition')
def nutrition(db: Db, user: CurrentUser):
    return service.nutrition(db, user)


@router.get('/items/{ingredient_id}', response_model=IngredientResponse)
def detail(ingredient_id: Id, db: Db, user: CurrentUser):
    return call(service.detail, db, user, ingredient_id)


@router.patch('/items/{ingredient_id}', response_model=IngredientResponse)
def update(ingredient_id: Id, body: IngredientUpdate, db: Db, user: CurrentUser):
    return call(service.update, db, user, ingredient_id, body)


@router.delete('/items/{ingredient_id}', status_code=204)
def delete(ingredient_id: Id, db: Db, user: CurrentUser):
    return call(service.delete, db, user, ingredient_id)


@router.post('/items/{ingredient_id}/consume', response_model=IngredientResponse)
def consume(ingredient_id: Id, body: Consume, db: Db, user: CurrentUser):
    return call(service.consume, db, user, ingredient_id, body)


@router.get('/items/{ingredient_id}/usage', response_model=Page[UsageResponse])
def usages(ingredient_id: Id, db: Db, user: CurrentUser, page: int = Query(1, ge=1),
           size: int = Query(20, ge=1, le=PAGE_MAX_SIZE)):
    return call(service.usages, db, user, ingredient_id, page, size)


@router.post('/receipts', status_code=201)
def upload(db: Db, user: CurrentUser, file: UploadFile = File(...), purchased_at: date | None = Form(None)):
    data = file.file.read(IMAGE_MAX_BYTES + 1)
    return call(receipt_service.upload, db, user, data, purchased_at)


@router.get('/receipts/{receipt_id}')
def receipt(receipt_id: Id, db: Db, user: CurrentUser):
    return receipt_service.receipt_response(call(receipt_service.owned, db, user, receipt_id))


@router.post('/receipts/{receipt_id}/confirm', response_model=list[IngredientResponse], status_code=201)
def confirm(receipt_id: Id, body: ReceiptConfirm, db: Db, user: CurrentUser):
    return call(receipt_service.confirm, db, user, receipt_id, body)
