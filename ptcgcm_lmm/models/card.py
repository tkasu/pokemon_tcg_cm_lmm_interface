from enum import Enum
from pydantic import BaseModel, Field


class Ability(BaseModel):
    name: str = Field(..., description="Name of the ability")
    effect: str = Field(..., description="Effect of the ability")


class Cost(str, Enum):
    Colorless = "Colorless"
    Grass = "Grass"
    Fire = "Fire"
    Water = "Water"
    Lightning = "Lightning"
    Psychic = "Psychic"
    Fighting = "Fighting"
    Darkness = "Darkness"
    Metal = "Metal"
    Fairy = "Fairy"
    Dragon = "Dragon"


class Attack(BaseModel):
    name: str = Field(..., description="Name of the attack")
    costs: list[Cost] = Field(..., description="Costs of the attack")
    effect: str = Field(..., description="Effect of the attack")
    damage: int = Field(..., description="Damage of the attack")


class Card(BaseModel):
    # Add examples as well to the decription
    category: str = Field(
        ..., description="Category of the card (Pokemon / Energy / Trainer)"
    )
    name: str = Field(..., description="Name of the card, e.g. Mew-ex")
    set_name: str = Field(
        ..., description="Name of the set, e.g. Scarlet & Violet / 151"
    )
    card_id_in_set: int = Field(..., description="Card ID in the set, e.g. 151")
    id: str = Field(
        ...,
        description="Combination of set_name and id, e.g. Scarlet & Violet / 151 / 151",
    )
    rarity: str = Field(..., description="Rarity of the card, e.g. Double Rare")
    is_holo: bool = Field(..., description="Is the card holo or not")
    pokemon_name: str = Field(
        None, description="Name of the Pokemon, if category is Pokemon"
    )
    hp: int = Field(None, description="HP of the Pokemon, if category is Pokemon")
    types: list[str] = Field(
        None, description="Types of the Pokemon, if category is Pokemon"
    )
    evolves_from: str = Field(
        None, description="Name of the Pokemon from which this Pokemon evolves"
    )
    stage: str = Field(
        None, description="Stage of the Pokemon, if evolves from other Pokemon"
    )
    abilities: list[Ability] = Field(
        None, description="Abilities of the Pokemon, if category is Pokemon"
    )
    attacks: list[Attack] = Field(
        None, description="Attacks of the Pokemon, if category is Pokemon"
    )
