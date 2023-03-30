from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.utils.database import Base


class RecColor(Base):
    __tablename__ = 'rec_colors'
    rec_color_id = Column(String(30), primary_key=True)
    rec_color = Column(String(30))
    closet_id = Column(String(30), ForeignKey('closets.closet_id'), nullable=True)

    closet = relationship('Closet', back_populates='rec_colors')

    class Config:
        arbitrary_types_allowed = True

    def __str__(self):
        return f'옷 아이디: {self.rec_color_id}, \n ' \
               f'옷장 아이디: {self.closet_id} \n' \
                f'추천 컬러: {self.rec_color} \n'


