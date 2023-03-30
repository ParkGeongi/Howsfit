from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.utils.database import Base


class Closet(Base):
    __tablename__ = 'closets'
    closet_id = Column(String(30), primary_key=True)
    my_cloth = Column(String(100))
    category = Column(String(30))
    cloth_color = Column(String(30))
    user_id = Column(String(30), ForeignKey('users.user_id'), nullable=True)
    cloth_id = Column(String(30), ForeignKey('clothes.cloth_id'), nullable=True)

    user = relationship('User', back_populates='closets')
    cloth = relationship('Cloth', back_populates='closets')

    class Config:
        arbitrary_types_allowed = True

    def __str__(self):
        return f'옷장 아아디: {self.closet_id}, \n ' \
                f'유저 아이디: {self.user_id} \n' \
                f'옷 아이디: {self.cloth_id} \n' \
                f'나의 옷 이미지: {self.my_cloth} \n' \
                f'카테고리: {self.category} \n' \
                f'컬러: {self.cloth_color} \n'

