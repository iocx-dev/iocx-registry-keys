from iocx.engine import Engine

def test_registry_plugin_integration():
    text = """
    HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run
    REG_SZ
    """

    engine = Engine()
    result = engine.extract_from_text(text)

    # Keys
    assert "registry.keys" not in result["iocs"]

    # Values
    assert "registry.values" in result["iocs"]
    assert "reg_sz" in [v.lower() for v in result["iocs"]["registry.values"]]

    # Persistence
    assert "registry.persistence" in result["iocs"]

