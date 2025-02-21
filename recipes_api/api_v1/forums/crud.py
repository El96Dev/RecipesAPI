from datetime import datetime

from fastapi.exceptions import HTTPException
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select 

from .schemas import ForumThreadBase
from core.models import db_helper, ForumThread, ForumMessage, User


async def get_approved_forum_threads(skip: int, limit: int, session: AsyncSession) -> list[ForumThread]:
    stmt = select(ForumThread).where(ForumThread.is_approved==True).offset(skip).limit(limit)
    result = await session.execute(stmt)
    threads = result.scalars().all()
    return threads


async def get_forum_thread(thread_id: int, session: AsyncSession) -> ForumThread:
    stmt = select(ForumThread).where(ForumThread.id==thread_id)
    result = await session.execute(stmt)
    thread = result.scalars().one_or_none()
    if not thread:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Thread with id {thread_id} wasn't found!")
    else:
        return thread


async def create_forum_thread(new_thread: ForumThreadBase, author: User, session: AsyncSession) -> ForumThread:
    stmt = select(ForumThread).where(ForumThread.title==new_thread.title).exists()
    if not await session.scalar(select(stmt)):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Thread with this title already exists!")
    
    thread = ForumThread(
        **new_thread.model_dump(), 
        author_id=author.id,
        created_at=datetime.utcnow
    )
    session.add(thread)
    await session.commit()
    return thread


async def delete_forum_thread(thread_id: int, session: AsyncSession):
    stmt = select(ForumThread).where(ForumThread.id==thread_id)
    result = await session.execute(stmt)
    thread = result.scalars().one_or_none()
    if not thread:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Thread with id {thread_id} wasn't found!")
    session.delete(thread)
    await session.commit()


async def get_forum_messages(
    thread_id: int, 
    skip: int, 
    limit: int, 
    session: AsyncSession
) -> list[ForumMessage]:
    stmt = select(ForumMessage).where(ForumMessage.thread_id==thread_id).order_by(ForumMessage.created_at.desc()).offset(skip).limit(limit)
    result = await session.execute(stmt)
    messages = result.scalars().all()
    return messages


async def create_forum_message(
    thread_id: int,
    message: str,
    author: User,
    session: AsyncSession
) -> ForumMessage:
    stmt = select(ForumThread).where(ForumThread.id==thread_id)
    result = await session.execute(stmt)
    thread = result.scalars().one_or_none()
    if not thread:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Thread with id {thread_id} wasn't found!")
    elif not thread.is_approved:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Thread with id {thread_id} wasn't approved yet!")
    else:
        forum_message = ForumMessage(message=message, thread_id=thread_id, author_id=author.id, created_at=datetime.utcnow)
        session.add(forum_message)
        await session.commit()
        return forum_message