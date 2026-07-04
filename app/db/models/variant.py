# Third party and python modules
from sqlalchemy import Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

# Project module
from .question import Question


class Variant(Base):
    __tablename__ = "variants"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    question_id: Mapped[int] = mapped_column(ForeignKey(Question.id))
    text: Mapped[str] = mapped_column(Text(), nullable=False)
