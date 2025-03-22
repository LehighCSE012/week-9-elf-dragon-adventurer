import pytest
from adventure import EnchantedArtifact  # Assuming student's code is in adventure.py

def test_enchanted_artifact_class_exists():
    """Test that the EnchantedArtifact class is defined."""
    assert "EnchantedArtifact" in globals(), "EnchantedArtifact class not defined"

def test_enchanted_artifact_constructor():
    """Test EnchantedArtifact constructor initializes attributes correctly."""
    artifact = EnchantedArtifact(name="TestArtifact", magic_power=75)
    assert artifact.name == "TestArtifact", "EnchantedArtifact name not initialized correctly"
    assert artifact._magic_power == 75, "EnchantedArtifact _magic_power not initialized correctly" # Testing protected attribute directly for constructor check
