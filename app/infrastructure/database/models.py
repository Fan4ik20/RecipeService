from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    salt = Column(String(32), nullable=False)
    
    recipes = relationship("Recipe", back_populates="user")
    
    def __str__(self):
        return f"{self.username}: {self.email}"

class Recipe(Base):
    __tablename__ = "recipes"
    
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    instructions = Column(Text, nullable=True)
    image = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    likes_count = Column(Integer, default=0)
    comments_count = Column(Integer, default=0)
    stars_count = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    user = relationship("User", back_populates="recipes")
    
    def __init__(self, title, description, instructions, user_id, likes_count, comments_count, stars_count, image=None):
        self.title = title
        self.description = description
        self.instructions = instructions
        self.user_id = user_id
        self.image = image
        self.likes_count = likes_count
        self.comments_count = comments_count
        self.stars_count = stars_count
        
    def __str__(self):
        return f"Recipe id: {self.id}, title: '{self.title}', user_id: {self.user_id}"

class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(Integer, primary_key=True)
    comment = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    recipe_id = Column(Integer, ForeignKey("recipes.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    user = relationship("User", back_populates="comments")
    recipe = relationship("Recipe", back_populates="comments")
    
    def __init__(self, comment, recipe_id, user_id):
        self.comment = comment
        self.recipe_id = recipe_id
        self.user_id = user_id
        
    def __str__(self):
        return f"Comment id: {self.id}, recipe_id: '{self.recipe_id}', user_id: {self.user_id}"

class Watchlist(Base):
    __tablename__ = "watchlists"
    
    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    user = relationship("User", back_populates="watchlists")
    recipe = relationship("Recipe", back_populates="watchlists")
    
    def __init__(self, recipe_id, user_id):
        self.recipe_id = recipe_id
        self.user_id = user_id