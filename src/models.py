from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()

Followers = Table(
    "followers",
    db.metadata,
    Column("follower_id", ForeignKey("user.id"), primary_key=True),
    Column("followed_id", ForeignKey("user.id"), primary_key=True),
)

class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(40), nullable=False)
    lastname: Mapped[str] = mapped_column(String(40), nullable=False)
    username: Mapped[str] = mapped_column(String(60), nullable=False)
    posts: Mapped[List["Post"]] = relationship("Post", back_populates="user")
    following: Mapped[List["User"]] = relationship(
        "User", secondary=Followers,
        primaryjoin="User.id == Followers.c.follower_id",
        secondaryjoin="User.id == Followers.c.followed_id",
        back_populates="followers"
    )
    followers: Mapped[List["User"]] = relationship(
        "User", secondary=Followers,
        primaryjoin="User.id == Followers.c.followed_id",
        secondaryjoin="User.id == Followers.c.follower_id",
        back_populates="following"
    )

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "username": self.username,
        }

class Post(db.Model):
    __tablename__ = "post"
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String(120), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship("User", back_populates="posts")
    media: Mapped[List["Media"]] = relationship("Media", back_populates="post")

    def serialize(self):
        return {"id": self.id, "user_id": self.user_id, "description": self.description}

class Media(db.Model):
    __tablename__ = "media"
    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(String(255), nullable=False)  # era Mapped[int], error de tipo
    type: Mapped[str] = mapped_column(String(10), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    post: Mapped["Post"] = relationship("Post", back_populates="media")

    def serialize(self):
        return {
            "id": self.id,
            "url": self.url,
            "type": self.type,
        }
class Follower(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    firtsname: Mapped [str] =mapped_column(String(40), nullable=False),
    lastname: Mapped [str] =mapped_column(String(40), nullable=False),
    username:Mapped[str] =mapped_column(String(60),nullable=False),
    posts: Mapped[List["Post"]]= relationship("Post",back_populates="user"),
