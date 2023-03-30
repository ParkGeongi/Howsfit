from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.utils.database import Base


class Viton(Base):
    __tablename__ = 'vitons'
    viton_id = Column(String(30), primary_key=True)
    viton_img = Column(String(50))
    closet_id = Column(String(30), ForeignKey('closets.closet_id'), nullable=True)

    closet = relationship('Closet', back_populates='vitons')

    class Config:
        arbitrary_types_allowed = True

    def __str__(self):
        return f'옷 아이디: {self.viton_id}, \n ' \
                f'옷장 아이디: {self.closet_id} \n' \
                f'비톤 이미지: {self.viton_img} \n'


