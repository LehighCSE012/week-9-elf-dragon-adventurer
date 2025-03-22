import pytest
import abc
from adventure import Character  # Assuming student's code is in adventure.py

def test_character_class_exists():
    """Test that the Character class is defined."""
    assert "Character" in globals(), "Character class not defined"

def test_character_is_abstract_base_class():
    """Test that Character is an Abstract Base Class (ABC)."""
    assert isinstance(Character, abc.ABCMeta), "Character is not an Abstract Base Class"

def test_character_cannot_be_instantiated():
    """Test that Character class cannot be instantiated directly."""
    with pytest.raises(TypeError):
        Character(name="TestChar", health=100, attack_power=10)

def test_character_has_abstract_methods():
    """Test that Character class has abstract methods special_ability and take_damage."""
    assert hasattr(Character, "special_ability"), "Character class does not have special_ability method"
    assert hasattr(Character, "take_damage"), "Character class does not have take_damage method"
    assert isinstance(Character.special_ability, abc.abstractmethod), "Character.special_ability is not an abstract method"
    assert isinstance(Character.take_damage, abc.abstractmethod), "Character.take_damage is not an abstract method"
