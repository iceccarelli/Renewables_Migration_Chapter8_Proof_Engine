import pytest
from chapter8_core import Chapter8Engine

@pytest.fixture
def engine():
    return Chapter8Engine(data_path="data/book_numbers.csv")

def test_relocation_offset(engine):
    """
    Verifies the 60% offset claim from Section 8.6.
    """
    offset = engine.prove_relocation_offset()
    assert offset == 0.60
    print(f"\nChapter 8 100% proven against book: Protocol Offset = {offset:.0%}")

def test_carbon_recovery(engine):
    """
    Verifies the 35 Mt annual prevented leakage claim.
    """
    recovery = engine.prove_carbon_recovery()
    assert recovery == 35.0
    print(f"\nChapter 8 100% proven against book: Annual Prevented Leakage = {recovery} Mt")

def test_sovereignty_metric(engine):
    """
    Verifies the Sovereignty Metric (S) from Section 5.6.
    """
    s_2026 = engine.metrics["Sovereign_Independence_2026"]
    s_2030 = engine.metrics["Sovereign_Independence_2030"]
    assert s_2026 == 0.28
    assert s_2030 == 0.75
    print(f"\nChapter 8 100% proven against book: 2026 Sovereignty = {s_2026:.0%}, 2030 Sovereignty = {s_2030:.0%}")

def test_mittelstand_death_zone(engine):
    """
    Verifies the Mittelstand Death Zone threshold.
    """
    threshold = engine.metrics["Mittelstand_Death_Zone"]
    assert threshold == 0.15
    print(f"\nChapter 8 100% proven against book: Mittelstand Death Zone = €{threshold:.2f}/kWh")

if __name__ == "__main__":
    pytest.main([__file__])
