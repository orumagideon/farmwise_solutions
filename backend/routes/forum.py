# routes/forum.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.session import SessionLocal
from db.models.forum import ForumPost
from schemas.forum import ForumPostCreate, ForumPostOut

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to create a forum post
@router.post("/forum/", response_model=ForumPostOut, status_code=status.HTTP_201_CREATED)
def create_forum_post(post: ForumPostCreate, db: Session = Depends(get_db)):
    db_post = ForumPost(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

# Route to get all forum posts
@router.get("/forum/", response_model=list[ForumPostOut])
def get_all_forum_posts(db: Session = Depends(get_db)):
    posts = db.query(ForumPost).all()
    return posts

# Route to upvote a forum post
@router.post("/forum/{post_id}/upvote")
def upvote_forum_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(ForumPost).filter(ForumPost.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    post.upvotes += 1
    db.commit()
    db.refresh(post)
    return {"message": "Post upvoted successfully", "upvotes": post.upvotes}