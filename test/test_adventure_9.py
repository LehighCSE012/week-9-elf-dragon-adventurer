import pytest
from adventure import EnchantedArtifact  # Assuming student's code is in adventure.py

def test_enchanted_artifact_magic_power_property_getter():
    """Test EnchantedArtifact magic_power property getter."""
    artifact = EnchantedArtifact(name="PropertyArtifact", magic_power=60)
    assert artifact.magic_power == 60, "EnchantedArtifact magic_power property getter returned incorrect value"

def test_enchanted_artifact_magic_power_property_setter_valid():
    """Test EnchantedArtifact magic_power property setter with valid value."""
    artifact = EnchantedArtifact(name="SetterArtifact", magic_power=50)
    artifact.magic_power = 80
    assert artifact._magic_power == 80, "EnchantedArtifact magic_power property setter did not set valid value"

def test_enchanted_artifact_magic_power_property_setter_invalid():
    """Test EnchantedArtifact magic_power property setter with invalid (negative) value raises ValueError."""
    artifact = EnchantedArtifact(name="InvalidSetterArtifact", magic_power=100)
    with pytest.raises(ValueError) as excinfo:
        artifact.magic_power = -10
    assert "Magic power cannot be negative!" in str(excinfo.value), "EnchantedArtifact magic_power setter did not raise ValueError for negative value or message incorrect"
