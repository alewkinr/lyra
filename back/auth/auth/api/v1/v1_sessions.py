from datetime import timedelta
from typing import Any

from sqlalchemy.orm import Session

from auth import crud, schemas
from auth.api import deps
from auth.core import errors, security
from auth.core.auth import OAuth2PasswordBearerWithCookie
from auth.core.config import settings
from fastapi import APIRouter, Depends, Request, Response, status
from fastapi.security import OAuth2PasswordRequestForm

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
        raise errors.BadRequestErr(detail="wrong username or password")

    elif not crud.user.is_active(user):
        raise errors.BadRequestErr(detail="account is inactive")

    expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    jwt_access_token = security.create_access_token(
        user.id,
        expires_delta=expires_delta,
    )

    resp = Response(status_code=status.HTTP_200_OK, content={"id": user.id})
    resp.set_cookie(
        key=schemas.TokenCookies.ACCESS_TOKEN.value,
        value=jwt_access_token,
        expires=expires_delta.seconds,
        path="/",
    )
    return resp


@router.get("/status", response_model=schemas.TokenValid)
def validate_token(req: Request) -> Any:
    """ OAuth2-like валидация токено """

    token = _reusable_OAuth(request=req)
    if not token:
        raise errors.NotAuthorizedErr()

    return {"status": True}
