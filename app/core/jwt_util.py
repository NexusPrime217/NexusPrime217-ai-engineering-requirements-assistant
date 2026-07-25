import jwt
from fastapi import HTTPException
# from app.core.config import setting
import logging

logger = logging.getLogger(__name__)



def create_access_token(payload : dict)->str:

    payload = payload.copy()

    access_token = jwt.encode(
        payload,
        "asgbiawbwbebwiaincubeiwbcwcwbegbwgbwfdoa9fhwf3874tg83rdr991bgf7g29f2bf92983gft972fc92wd23bf",
        algorithm="HS256"
        # setting.SECRETKEY,
        # algorithm=setting.JWT_ALG,
    )
    return access_token


def decode_access_token(access_token:str):
    try:
        return jwt.decode(access_token,
                  "asgbiawbwbebwiaincubeiwbcwcwbegbwgbwfdoa9fhwf3874tg83rdr991bgf7g29f2bf92983gft972fc92wd23bf",
                  algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401,
                            detail="Token has expired")
    except jwt.InvalidTokenError:
        logger.exception("Failed to decode the token")
        raise HTTPException(status_code=401,
                            detail="Invalid token")



