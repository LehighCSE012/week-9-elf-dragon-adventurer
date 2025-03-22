import pytest
from adventure import Elf, Character  # Assuming student's code is in adventure.py

def test_elf_class_exists():
    """Test that the Elf class is defined."""
    assert "Elf" in globals(), "Elf class not defined"

def test_elf_inherits_from_character():
    """Test that Elf class inherits from Character."""
    assert issubclass(Elf, Character), "Elf class does not inherit from Character"

def test_elf_constructor():
    """Test Elf constructor initializes attributes correctly."""
    elf = Elf(name="TestElf")
    assert elf.name == "TestElf", "Elf name not initialized correctly"
    assert elf.health == 100, "Elf health not initialized to default correctly"
    assert elf.attack_power == 25, "Elf attack_power not initialized to default correctly"

def test_elf_special_ability():
    """Test Elf special_ability method returns correct string."""
    elf = Elf(name="TestElf")
    ability_desc = elf.special_ability()
    assert ability_desc == "Elven Agility: Dodges the next attack completely.", "Elf special_ability returned incorrect string"

def test_elf_take_damage():
    """Test Elf take_damage method reduces health correctly."""
    elf = Elf(name="DamageElf")
    elf.take_damage(25)
    assert elf.health == 75, "Elf health not reduced correctly"
    elf.take_damage(120)  # Should not go below zero
    assert elf.health == 0, "Elf health went below zero"
