import pytest
from adventure import Dragon, Character  # Assuming student's code is in adventure.py

def test_dragon_class_exists():
    """Test that the Dragon class is defined."""
    assert "Dragon" in globals(), "Dragon class not defined"

def test_dragon_inherits_from_character():
    """Test that Dragon class inherits from Character."""
    assert issubclass(Dragon, Character), "Dragon class does not inherit from Character"

def test_dragon_constructor():
    """Test Dragon constructor initializes attributes correctly."""
    dragon = Dragon(name="TestDragon")
    assert dragon.name == "TestDragon", "Dragon name not initialized correctly"
    assert dragon.health == 200, "Dragon health not initialized to default correctly"
    assert dragon.attack_power == 30, "Dragon attack_power not initialized to default correctly"
    assert Dragon.breath_attack_damage == 50, "Dragon class attribute breath_attack_damage not initialized correctly"

def test_dragon_special_ability():
    """Test Dragon special_ability method returns correct string."""
    dragon = Dragon(name="TestDragon")
    ability_desc = dragon.special_ability()
    assert ability_desc == "Dragon's Fire Breath: Deals massive fire damage to all enemies.", "Dragon special_ability returned incorrect string"

def test_dragon_take_damage():
    """Test Dragon take_damage method reduces health correctly."""
    dragon = Dragon(name="DamageDragon")
    dragon.take_damage(50)
    assert dragon.health == 150, "Dragon health not reduced correctly"
    dragon.take_damage(250)  # Should not go below zero
    assert dragon.health == 0, "Dragon health went below zero"

def test_dragon_get_breath_attack_damage():
    """Test Dragon get_breath_attack_damage class method returns correct value."""
    damage = Dragon.get_breath_attack_damage()
    assert damage == 50, "Dragon get_breath_attack_damage class method returned incorrect value"
