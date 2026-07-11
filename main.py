import pytest

if __name__ == "__main__":
    pytest.main([
        "tests/",
        "-v",
        "--headed",
        "--slowmo=1000"
    ])