import pytest

from core.ambient.world import World
from core.ambient.tile import GRASS, WATER
from core.being.entity import Entity

def test_set_get_tile():
    world = World(5,5)
    world.set_tile(2, 2, WATER)
    assert world.get_tile(2, 2) is WATER

def test_set_tile_fora_do_mundo_gera_erro():
    world = World(5, 5)
    with pytest.raises(ValueError):
        world.set_tile(10, 10, WATER)

def test_is_inside():
    world = World(5, 5)
    assert world.is_inside(0, 0) is True
    assert world.is_inside(4, 4) is True
    assert world.is_inside(5, 5) is False
    assert world.is_inside(-1, 0) is False

def test_move_entity_para_posicao_livre():
    world = World(5, 5)
    entity = Entity("teste", "@", 2, 2)
    world.add_entity(entity)
    moved = world.move_entity(entity, 1, 0)
    assert moved is True
    assert (entity.x, entity.y) == (3, 2)

def test_move_entity_bloqueado_por_outra_entidade():
    world = World(5, 5)
    a = Entity("a", "@", 2, 2)
    b = Entity("b", "@", 3, 2)
    world.add_entity(a)
    world.add_entity(b)
    moved = world.move_entity(a, 1, 0)
    assert moved is False
    assert (a.x, a.y) == (2, 2)

def test_move_entity_bloqueado_pela_borda():
    world = World(5, 5)
    entity = Entity("teste", "@", 4, 4)
    world.add_entity(entity)
    moved = world.move_entity(entity, 1, 0)
    assert moved is False
    assert (entity.x, entity.y) == (4, 4)

