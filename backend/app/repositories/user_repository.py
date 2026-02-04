from sqlalchemy.orm import Session
from app.db.models import User


class UserRepository:

    def create_user(self, db: Session, email: str, hashed_password: str) -> User:
        user = User(
            email=email,
            hashed_password=hashed_password
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get_user_by_email(self, db: Session, email: str) -> User | None:
        return db.query(User).filter(User.email == email).first()
