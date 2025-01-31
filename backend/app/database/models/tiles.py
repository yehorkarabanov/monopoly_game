from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.models import Base


class Action(Base):
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)

    # Relationship with SpecialTiles
    special_tiles: Mapped[list["SpecialTile"]] = relationship(back_populates="action")


# Groups Table
class Group(Base):
    name: Mapped[str] = mapped_column(unique=True, nullable=False)

    # Relationship with Tiles
    tiles: Mapped[list["Tile"]] = relationship(back_populates="group")


# Tiles Table
class Tile(Base):
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"), nullable=False)
    tile_position: Mapped[int] = mapped_column(unique=True, nullable=False)

    # Relationships
    group: Mapped["Group"] = relationship(back_populates="tiles")
    property: Mapped["Property"] = relationship(uselist=False, back_populates="tile")
    railway: Mapped["Railway"] = relationship(uselist=False, back_populates="tile")
    utility: Mapped["Utility"] = relationship(uselist=False, back_populates="tile")
    special_tile: Mapped["SpecialTile"] = relationship(
        uselist=False, back_populates="tile"
    )


# Properties Table
class Property(Base):
    tile_id: Mapped[int] = mapped_column(
        ForeignKey("tiles.id"), unique=True, nullable=False
    )
    price: Mapped[float] = mapped_column(nullable=False)
    house_price: Mapped[float] = mapped_column(nullable=False)
    base_rent: Mapped[float] = mapped_column(nullable=False)
    one_house_rent: Mapped[float] = mapped_column(nullable=False)
    two_houses_rent: Mapped[float] = mapped_column(nullable=False)
    three_houses_rent: Mapped[float] = mapped_column(nullable=False)
    four_houses_rent: Mapped[float] = mapped_column(nullable=False)
    hotel_rent: Mapped[float] = mapped_column(nullable=False)

    # Relationship with Tiles
    tile: Mapped["Tile"] = relationship(back_populates="property")


# Railways Table
class Railway(Base):
    tile_id: Mapped[int] = mapped_column(
        ForeignKey("tiles.id"), unique=True, nullable=False
    )
    price: Mapped[float] = mapped_column(nullable=False)
    one_owned_rent: Mapped[float] = mapped_column(nullable=False)
    two_owned_rent: Mapped[float] = mapped_column(nullable=False)
    three_owned_rent: Mapped[float] = mapped_column(nullable=False)
    four_owned_rent: Mapped[float] = mapped_column(nullable=False)

    # Relationship with Tiles
    tile: Mapped["Tile"] = relationship(back_populates="railway")


# Utilities Table
class Utility(Base):
    tile_id: Mapped[int] = mapped_column(
        ForeignKey("tiles.id"), unique=True, nullable=False
    )
    price: Mapped[float] = mapped_column(nullable=False)
    one_company_owned_multiplier: Mapped[int] = mapped_column(nullable=False)
    two_companies_owned_multiplier: Mapped[int] = mapped_column(nullable=False)

    # Relationship with Tiles
    tile: Mapped["Tile"] = relationship(back_populates="utility")


# Special Tiles Table
class SpecialTile(Base):
    tile_id: Mapped[int] = mapped_column(
        ForeignKey("tiles.id"), unique=True, nullable=False
    )
    description: Mapped[str] = mapped_column(nullable=False)
    action_id: Mapped[int] = mapped_column(
        ForeignKey("actions.id"), nullable=True
    )  # Nullable for non-action tiles

    # Relationships
    tile: Mapped["Tile"] = relationship(back_populates="special_tile")
    action: Mapped["Action"] = relationship(back_populates="special_tiles")


# Card Types Table
class CardType(Base):
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    # Relationship with SpecialCards
    special_cards: Mapped[list["SpecialCard"]] = relationship(back_populates="card_type")

# Special Cards Table
class SpecialCard(Base):
    type_id: Mapped[int] = mapped_column(ForeignKey("cardtypes.id"), nullable=False)
    code_name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)

    # Relationship with CardType
    card_type: Mapped["CardType"] = relationship(back_populates="special_cards")
