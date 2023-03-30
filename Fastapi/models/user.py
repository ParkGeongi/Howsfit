
from sqlalchemy import Column, String

from sqlalchemy.orm import relationship

from app.utils.database import Base

class User(Base):
    __tablename__ = 'users'
    user_id = Column(String(30), primary_key=True)
    email = Column(String(50),unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    name = Column(String(20), nullable=False)
    phone = Column(String(20))
    pers_color = Column(String(20))
    token = Column(String(256))
    closets = relationship('Closet', back_populates='user')

    class Config:
        arbitrary_types_allowed = True

    def __str__(self):
        return f'아이디: {self.userid}, \n ' \
                f'이메일: {self.email}, \n ' \
                f'비밀번호: {self.password} \n' \
                f'이름: {self.name} \n' \
                f'전화번호: {self.phone} \n' \
                f'퍼스널컬러: {self.pers_color} \n' \
                f'토큰: {self.token} \n'