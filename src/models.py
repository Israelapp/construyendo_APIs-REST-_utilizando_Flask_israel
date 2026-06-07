from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()
Followers = Table (
    "followers"
    db.metadata,
    colum("user_id", ForeignKey("u"ser.id")),
    colum("user_id", ForeignKey("following.id")),
)

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    firtsname: Mapped [str] =mapped_column(String(40), nullable=False),
    lastname: Mapped [str] =mapped_column(String(40), nullable=False),
    username:Mapped[str] =mapped_column(String(60)nullable=False)
    posts: Mapped[List["Post"]]= relationship("Post",back_populates="user")


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "firtsname": self.firtsname,
            "lastname": self.lastname,
            "username": self.username,
            # do not serialize the password, its a security breach
        }

class Following (db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    firtsname: Mapped [str] =mapped_column(String(40), nullable=False),
    lastname: Mapped [str] =mapped_column(String(40), nullable=False),
    username:Mapped[str] =mapped_column(String(60)nullable=False)
    posts: Mapped[List["Post"]]= relationship("Post",back_populates="user")


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "firtsname": self.firtsname,
            "lastname": self.lastname,
            "username": self.username,

class Post(db.Model):
    __tablename__="post"
    id:Mapped[int]=mapped_column(primary_key=True)
    description: Mapped[str]=mapped_column(String(120), nullable=False)


    user_id: Mapped[int] mapped_column(ForeignKey=("user.id"))
    media: Mapped[List["Media"]] = relationship("Media" back_populates="media")  

        return{"id": self.id, "user.id": self.user_id}
class Media (db.Model):
    __tablename__="media"
    id: Mapped[int] =mapped_column(primary_key=True)
    url: Mapped[int] =mapped_column(String(255), nullable=False)
    type: Mapped[str] =mapped_column (String(10), nullable=False)

    post: Mapped["Post"] =mapped_column("Post" back_populates="media")

    def serialize(self):
        return{
            "id":self.id
            "url": self.url
            "type": self.type
        }

    class Follower (db.Model)