from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.models.charity_project import CharityProject


async def check_name_duplicate(
        charity_project_name: str,
        session: AsyncSession,
        current_charity_project_id: int | None = None
) -> None:
    charity_project_id = await \
        (charity_project_crud.get_charity_project_id_by_name(
            charity_project_name, session))
    if (charity_project_id is not None and
            charity_project_id != current_charity_project_id):
        raise HTTPException(
            status_code=400,
            detail='Проект с таким именем уже существует!',
        )


async def check_charity_project_exists(
        charity_project_id: int,
        session: AsyncSession
) -> CharityProject:
    charity_project = await charity_project_crud.get(charity_project_id,
                                                     session)
    if charity_project is None:
        raise HTTPException(
            status_code=404,
            detail='Благотворительный проект не найден!'
        )
    return charity_project


async def check_total_amount(
        charity_project: CharityProject,
        new_full_amount: int | None,
) -> None:
    if (new_full_amount is not None and
            new_full_amount < charity_project.invested_amount):
        raise HTTPException(
            status_code=400,
            detail='Нелья установить значение full_amount меньше'
                   ' уже вложенной суммы.'
        )


async def check_closed_project_or_invested_project(
        charity_project_id: int,
        session: AsyncSession
) -> CharityProject:
    charity_project = await charity_project_crud.get(charity_project_id,
                                                     session)
    if (charity_project.fully_invested is True or
            charity_project.invested_amount > 0):
        raise HTTPException(
            status_code=400,
            detail='В проект были внесены средства, не подлежит удалению!'
        )
