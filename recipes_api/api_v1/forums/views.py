from typing import List

from core.models import User, db_helper
from dependencies.authentication.current_user import current_active_user
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import ForumMessageBase, ForumThreadBase, ForumThreadGet

router = APIRouter(tags=["Forums"])


@router.get("", response_model=List[ForumThreadGet])
async def get_approved_forum_threads(skip: int, limit: int, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    threads = await crud.get_approved_forum_threads(skip, limit, session)
    return threads


@router.get("/{thread_id}", response_model=ForumThreadGet)
async def get_forum_thread(thread_id: int, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    thread = await crud.get_forum_thread(thread_id, session)
    return thread


@router.post("", response_model=ForumThreadGet)
async def post_forum_thread(new_thread: ForumThreadBase,
                            user: User = Depends(current_active_user),
                            session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    thread = await crud.create_forum_thread(new_thread, user, session)
    return thread


@router.get("/{thread_id}/messages", response_model=List[ForumMessageBase])
async def get_forum_thread_messages(thread_id: int, 
                                    skip: int, 
                                    limit: int, 
                                    session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    messages = await crud.get_forum_messages(thread_id, skip, limit, session)
    return messages


@router.post("/{thread_id}/messages", response_model=ForumMessageBase)
async def post_forum_message(thread_id: int, 
                             message: str,
                             user: User = Depends(current_active_user),
                             session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    message = await crud.create_forum_message(thread_id, message, user, session)
    return message