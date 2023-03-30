from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.utils.database import Base


class Cloth(Base):
    __tablename__ = 'clothes'
    cloth_id = Column(String(30), primary_key=True)
    name = Column(String(30))
    brand = Column(String(30))
    gender = Column(String(30))
    price = Column(String(30))
    category = Column(String(30))
    cloth_img = Column(String(100))

    closets = relationship('Closet', back_populates='cloth')

    class Config:
        arbitrary_types_allowed = True

    def __str__(self):
        return f'옷 아이디: {self.cloth_id}, \n ' \
               f'상품명: {self.name}, \n ' \
               f'브랜드: {self.brand} \n' \
               f'성별: {self.gender} \n' \
               f'가격: {self.price} \n' \
               f'카테고리: {self.category} \n' \
               f'컬러: {self.color} \n' \
               f'이미지: {self.cloth_img} \n'
