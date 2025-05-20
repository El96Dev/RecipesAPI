from fastapi_users.password import PasswordHelper

from core.models import User, db_helper


async def create_admin_user(username: str, email: str, password: str):
    async for session in db_helper.scoped_session_dependency():
        password_helper = PasswordHelper()
        hashed_password = password_helper.hash(password)
        admin_user = User(
            username=username,
            email=email,
            hashed_password=hashed_password,
            is_admin=True
        )

        session.add(admin_user)
        await session.commit()
        print(f"Created admin user {username}, {email}")
