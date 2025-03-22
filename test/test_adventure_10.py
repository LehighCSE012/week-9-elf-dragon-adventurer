import pytest
from adventure import EnchantedArtifact  # Assuming student's code is in adventure.py

def test_enchanted_artifact_is_enchanted_staticmethod_true():
    """Test EnchantedArtifact is_enchanted static method returns True for power level > 75."""
    assert EnchantedArtifact.is_enchanted(80) == True, "EnchantedArtifact is_enchanted static method returned False for power level > 75"

def test_enchanted_artifact_is_enchanted_staticmethod_false():
    """Test EnchantedArtifact is_enchanted static method returns False for power level <= 75."""
    assert EnchantedArtifact.is_enchanted(75) == False, "EnchantedArtifact is_enchanted static method returned True for power level <= 75"
    assert EnchantedArtifact.is_enchanted(50) == False, "EnchantedArtifact is_enchanted static method returned True for power level <= 75"
