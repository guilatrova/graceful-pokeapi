from gracy import BaseEndpoint


class PokeApiEndpoint(BaseEndpoint):
    ABILITY = "/ability/{KEY}"

    # Berry Namespace
    BERRY = "/berry/{KEY}"
    BERRY_FLAVOR = "/berry-flavor/{KEY}"
    BERRY_FIRMNESS = "/berry-firmness/{KEY}"

    CHARACTERISTIC = "/characteristic/{KEY}"
    CONTEST_EFFECT = "/contest-effect/{KEY}"
    CONTEST_TYPE = "/contest-type/{KEY}"

    EGG_GROUP = "/egg-group/{KEY}"

    # Encounter Namespace
    ENCOUNTER_CONDITION = "/encounter-condition/{KEY}"
    ENCOUNTER_CONDITION_VALUE = "/encounter-condition-value/{KEY}"
    ENCOUNTER_METHOD = "/encounter-method/{KEY}"

    EVOLUTION_CHAIN = "/evolution-chain/{KEY}"
    EVOLUTION_TRIGGER = "/evolution-trigger/{KEY}"

    GENDER = "/gender/{KEY}"
    GENERATION = "/generation/{KEY}"
    GROWTH_RATE = "/growth-rate/{KEY}"

    # Item Namespace
    ITEM = "/item/{KEY}"
    ITEM_ATTRIBUTE = "/item-attribute/{KEY}"
    ITEM_CATEGORY = "/item-category/{KEY}"
    ITEM_FLING_EFFECT = "/item-fling-effect/{KEY}"
    ITEM_POCKET = "/item-pocket/{KEY}"

    LANGUAGE = "/language/{KEY}"
    LOCATION = "/location/{KEY}"
    LOCATION_AREA = "/location-area/{KEY}"
    MACHINE = "/machine/{KEY}"

    # Move Namespace
    MOVE = "/move/{KEY}"
    MOVE_AILMENT = "/move-ailment/{KEY}"
    MOVE_BATTLE_STYLE = "/move-battle-style/{KEY}"
    MOVE_CATEGORY = "/move-category/{KEY}"
    MOVE_DAMAGE_CLASS = "/move-damage-class/{KEY}"
    MOVE_LEARN_METHOD = "/move-learn-method/{KEY}"
    MOVE_TARGET = "/move-target/{KEY}"

    NATURE = "/nature/{KEY}"
    PAL_PARK_AREA = "/pal-park-area/{KEY}"
    POKEATHLON_STAT = "/pokeathlon-stat/{KEY}"
    POKEDEX = "/pokedex/{KEY}"

    # Pokemon Namespace
    POKEMON = "/pokemon/{KEY}"
    POKEMON_ENCOUNTERS = "/pokemon/{KEY}/encounters"
    POKEMON_COLOR = "/pokemon-color/{KEY}"
    POKEMON_FORM = "/pokemon-form/{KEY}"
    POKEMON_HABITAT = "/pokemon-habitat/{KEY}"
    POKEMON_SHAPE = "/pokemon-shape/{KEY}"
    POKEMON_SPECIES = "/pokemon-species/{KEY}"

    REGION = "/region/{KEY}"
    STAT = "/stat/{KEY}"
    SUPER_CONTEST_EFFECT = "/super-contest-effect/{KEY}"
    TYPE = "/type/{KEY}"
    VERSION = "/version/{KEY}"
    VERSION_GROUP = "/version-group/{KEY}"
