import pytest
from adventure import Adventurer, Character  # Assuming student's code is in adventure.py

def test_adventurer_class_exists():
    """Test that the Adventurer class is defined."""
    assert "Adventurer" in globals(), "Adventurer class not defined"

def test_adventurer_inherits_from_character():
    """Test that Adventurer class inherits from Character."""
    assert issubclass(Adventurer, Character), "Adventurer class does not inherit from Character"

def test_adventurer_constructor():
    """Test Adventurer constructor initializes attributes correctly."""
    hero = Adventurer(name="TestHero")
    assert hero.name == "TestHero", "Adventurer name not initialized correctly"
    assert hero.health == 120, "Adventurer health not initialized to default correctly"
    assert hero.attack_power == 20, "Adventurer attack_power not initialized to default correctly"
    assert hero.inventory == {}, "Adventurer inventory not initialized as empty dictionary"

def test_adventurer_special_ability():
    """Test Adventurer special_ability method returns correct string."""
    hero = Adventurer(name="TestHero")
    ability_desc = hero.special_ability()
    assert ability_desc == "Adventurer's Courage: Increases attack power for a short duration.", "Adventurer special_ability returned incorrect string"

def test_adventurer_take_damage():
    """Test Adventurer take_damage method reduces health correctly."""
    hero = Adventurer(name="DamageHero")
    hero.take_damage(30)
    assert hero.health == 90, "Adventurer health not reduced correctly"
    hero.take_damage(150)  # Should not go below zero
    assert hero.health == 0, "Adventurer health went below zero"

def test_adventurer_add_item_to_inventory():
    """Test Adventurer add_item_to_inventory method adds items correctly."""
    hero = Adventurer(name="ItemHero")
    hero.add_item_to_inventory("Potion", quantity=2)
    assert hero.inventory == {"Potion": 2}, "add_item_to_inventory failed to add new item"
    hero.add_item_to_inventory("Potion", quantity=3)
    assert hero.inventory == {"Potion": 5}, "add_item_to_inventory failed to increase quantity"
    hero.add_item_to_inventory("Sword")
    assert hero.inventory == {"Potion": 5, "Sword": 1}, "add_item_to_inventory failed to add different item"

def test_adventurer_display_inventory(capsys):
    """Test Adventurer display_inventory method output."""
    hero = Adventurer(name="StatusHero")
    hero.add_item_to_inventory("Torch")
    hero.add_item_to_inventory("Gold Coins", quantity=10)
    hero.display_inventory()
    captured = capsys.readouterr()
    expected_output = "Adventurer Inventory:\n- Torch: 1\n- Gold Coins: 10\n" # Adjust expected output if formatting differs
    assert captured.out == expected_output, "Adventurer display_inventory output incorrect"
