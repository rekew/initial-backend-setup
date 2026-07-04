# Third party and python modules
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

# Project modules
from .user import User
from .question import Question
from .variant import Variant


class UserAnswer(Base):
    __tablename__ = "user_answers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    question_id: Mapped[str] = mapped_column(ForeignKey(Question.id))
    variant_id: Mapped[str] = mapped_column(ForeignKey(Variant.id))
