from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base, CommonMixin


class Donation(CommonMixin, Base):
    comment: Mapped[str] = mapped_column(String, nullable=True)
