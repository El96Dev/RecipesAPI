from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class IdPkMixin(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
