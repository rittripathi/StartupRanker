from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
import uuid
from app.model import User
from app.schemas import UserSignup, UserOut, UserLogin
from app.auth_utils import hash_password,verify_password
from app.jwt_utils import create_access_token


router = APIRouter()

@router.post("/signup", response_model=UserOut)
def signup(payload: UserSignup, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == payload.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(
        id=str(uuid.uuid4()),
        email=payload.email,
        hashed_password=hash_password(payload.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login")
def login(payload:UserLogin, db: Session=Depends(get_db)):
    user=db.query(User).filter(User.email == payload.email).first()

    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password ")
    
    token= create_access_token({"sub": user.id})
    return {"access_toke": token, "token_type":"bearer"}
