import uuid

from sqlalchemy import String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.models.base import Base


class User(Base):
    __tablename__ = "users"  # noqa

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )
    username: Mapped[str] = mapped_column(
        String(),
        unique=True,
    )
    hashed_password: Mapped[str] = mapped_column(
        String(),
    )