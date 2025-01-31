from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.database.db_helper import db_helper
from app.database.models import Tile, SpecialTile

router = APIRouter(prefix="/tiles", tags=["tiles"])


@router.get("/")
async def get_tiles(session: AsyncSession = Depends(db_helper.session_dependency)):
    stmt = select(Tile).options(
        joinedload(Tile.group),  # Load the related Group
        joinedload(Tile.property),  # Load the related Property (if any)
        joinedload(Tile.railway),  # Load the related Railway (if any)
        joinedload(Tile.utility),  # Load the related Utility (if any)
        joinedload(Tile.special_tile).joinedload(
            SpecialTile.action
        ),  # Load SpecialTile and its Action
    )

    # Execute the query
    result = await session.execute(stmt)

    # Fetch all tiles
    tiles = result.scalars().all()

    return tiles


@router.get("/cards")
async def get_cards(session: AsyncSession = Depends(db_helper.session_dependency)):
    stmt = select(SpecialTile).options(
        joinedload(SpecialTile.action),  # Load the related Action
    )

    # Execute the query
    result = await session.execute(stmt)

    # Fetch all special tiles
    special_tiles = result.scalars().all()

    return special_tiles
