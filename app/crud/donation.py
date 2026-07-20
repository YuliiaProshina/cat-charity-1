from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.donation import Donation


class CRUDDonation(CRUDBase):
    async def get_free_donations(
        self,
        session: AsyncSession,
    ) -> list[Donation]:
        result = await session.execute(
            select(Donation)
            .where(
                Donation.fully_invested.is_(False)
            )
            .order_by(Donation.create_date)
        )

        return list(result.scalars().all())


donation_crud = CRUDDonation(Donation)