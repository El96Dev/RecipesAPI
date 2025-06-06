from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr
)


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(self):
        return f"{self.__name__.lower()}s"
