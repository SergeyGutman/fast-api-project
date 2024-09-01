from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .mixins import UserRelationMixin

from .base import Base

# Импортируем только при проверке типа, дабы не было циклического импорта



class Post(UserRelationMixin, Base):
    # _user_id_nullable = False
    # _user_id_unique = False
    _user_back_populates = 'posts'
    title: Mapped[str] = mapped_column(String(100))
    body: Mapped[str] = mapped_column(
        Text,
        default='',
        server_default='',
    )
    # Больше не требуется так как из mixins подмешиваем сюда
    # user_id: Mapped[int] = mapped_column(
    #     ForeignKey('users.id'),
    # )
    # Это также подмешивается и берется _user_back_populates
    # user: Mapped['User'] = relationship(back_populates='posts')
