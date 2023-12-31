from sqlalchemy.orm import Mapped

from .base import Base



class Product(Base):
    __tablemane__ = "product"

    name: Mapped[str]   
    description: Mapped[str]
    price: Mapped[int]
