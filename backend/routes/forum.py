# routes/forum.py
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session
from db.session import SessionLocal
from db.models.forum import ForumPost, ForumReply
from schemas.forum import ForumPostCreate, ForumPostOut, ForumPostUpdate, ForumReplyCreate, ForumReplyOut
from typing import List

router = APIRouter()

# Dependency to get the database session
def get_db():
    """
    Dependency that provides a database session to interact with the database.

    This function is used in the route handlers to get access to the DB session,
    ensuring that the session is properly closed after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to create a forum post (with optional image)
@router.post("/forum/", response_model=ForumPostOut, status_code=status.HTTP_201_CREATED)
def create_forum_post(
    post: ForumPostCreate, 
    image: UploadFile = File(None), 
    db: Session = Depends(get_db)
):
    """
    Create a new forum post. Optionally, an image can be uploaded with the post.

    Args:
        post (ForumPostCreate): Data for the new post.
        image (UploadFile, optional): An optional image to be uploaded.
        db (Session): The database session.

    Returns:
        ForumPostOut: The created forum post.
    """
    image_data = image.file.read() if image else None

    db_post = ForumPost(
        content=post.content,
        user_id=post.user_id,
        image=image_data
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

# Route to get all forum posts with replies
@router.get("/forum/", response_model=List[ForumPostOut])
def get_all_forum_posts(db: Session = Depends(get_db)):
    """
    Retrieve all forum posts.

    Args:
        db (Session): The database session.

    Returns:
        List[ForumPostOut]: A list of all forum posts.
    """
    return db.query(ForumPost).all()

# Route to get a single forum post by ID
@router.get("/forum/{post_id}", response_model=ForumPostOut)
def get_forum_post(post_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single forum post by its ID.

    Args:
        post_id (int): The ID of the post.
        db (Session): The database session.

    Returns:
        ForumPostOut: The requested forum post.
    """
    post = db.query(ForumPost).filter(ForumPost.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post

# Route to reply to a forum post
@router.post("/forum/{post_id}/reply", response_model=ForumReplyOut)
def reply_to_forum_post(post_id: int, reply: ForumReplyCreate, db: Session = Depends(get_db)):
    """
    Reply to a specific forum post.

    Args:
        post_id (int): The ID of the post to reply to.
        reply (ForumReplyCreate): Data for the reply.
        db (Session): The database session.

    Returns:
        ForumReplyOut: The created reply.
    """
    post = db.query(ForumPost).filter(ForumPost.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    db_reply = ForumReply(
        post_id=reply.post_id,
        user_id=reply.user_id,
        content=reply.content
    )
    db.add(db_reply)
    db.commit()
    db.refresh(db_reply)
    return db_reply

# Route to update a forum post
@router.put("/forum/{post_id}", response_model=ForumPostOut)
def update_forum_post(post_id: int, post_update: ForumPostUpdate, db: Session = Depends(get_db)):
    """
    Update an existing forum post.

    Args:
        post_id (int): The ID of the post to update.
        post_update (ForumPostUpdate): Data for updating the post.
        db (Session): The database session.

    Returns:
        ForumPostOut: The updated forum post.
    """
    post = db.query(ForumPost).filter(ForumPost.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    if post_update.content is not None:
        post.content = post_update.content

    db.commit()
    db.refresh(post)
    return post

# Route to delete a forum post
@router.delete("/forum/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_forum_post(post_id: int, db: Session = Depends(get_db)):
    """
    Delete a specific forum post by its ID.

    Args:
        post_id (int): The ID of the post to delete.
        db (Session): The database session.

    Returns:
        dict: A message confirming successful deletion.
    """
    post = db.query(ForumPost).filter(ForumPost.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    db.delete(post)
    db.commit()
    return {"message": "Post deleted successfully"}

# Route to upvote a forum post
@router.post("/forum/{post_id}/upvote")
def upvote_forum_post(post_id: int, db: Session = Depends(get_db)):
    """
    Upvote a forum post, increasing its upvote count.

    Args:
        post_id (int): The ID of the post to upvote.
        db (Session): The database session.

    Returns:
        dict: A message confirming the upvote and updated upvote count.
    """
    post = db.query(ForumPost).filter(ForumPost.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    post.upvotes += 1
    db.commit()
    db.refresh(post)
    return {"message": "Post upvoted successfully", "upvotes": post.upvotes}

# Route to downvote a forum post
@router.post("/forum/{post_id}/downvote")
def downvote_forum_post(post_id: int, db: Session = Depends(get_db)):
    """
    Downvote a forum post, increasing its downvote count.

    Args:
        post_id (int): The ID of the post to downvote.
        db (Session): The database session.

    Returns:
        dict: A message confirming the downvote and updated downvote count.
    """
    post = db.query(ForumPost).filter(ForumPost.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    post.downvotes += 1
    db.commit()
    db.refresh(post)
    return {"message": "Post downvoted successfully", "downvotes": post.downvotes}