from datetime import timedelta
from typing import Any

from sqlalchemy.orm import Session

from fastapi import (APIRouter, Depends, HTTPException, Request, Response,
                     status)
from fastapi.security import OAuth2PasswordRequestForm
from model import crud, schemas
from model.api import deps
from model.core import security
from model.core.config import settings
from model.core.model import OAuth2PasswordBearerWithCookie

router = APIRouter()
_reusable_OAuth = OAuth2PasswordBearerWithCookie(tokenUrl="/status")


@router.post("/")
def login(
    db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = crud.user.authenticate(
        db, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Введен некорректный email или пароль",
        )

    elif not crud.user.is_active(user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Аккаунт неактивен"
        )

    expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    jwt_access_token = security.create_access_token(
        user.id,
        expires_delta=expires_delta,
    )

    response = Response(status_code=status.HTTP_200_OK, content={"id": user.id})
    response.set_cookie(
        key=schemas.TokenCookies.ACCESS_TOKEN.value,
        value=jwt_access_token,
        expires=expires_delta.seconds,
        path="/",
    )
    return response


@router.get("/status", response_model=schemas.TokenValid)
def validate_token(req: Request) -> Any:
    """ OAuth2-like валидация токено """

    token = _reusable_OAuth(request=req)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )

    return {"status": True}
