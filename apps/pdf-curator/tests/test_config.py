import pytest

from pdf_curator.config import load_mistral_api_key
from pdf_curator.errors import ConfigurationError


def test_dotenv_file_is_not_loaded(tmp_path, monkeypatch):
    monkeypatch.delenv("MISTRAL_API_KEY", raising=False)
    monkeypatch.chdir(tmp_path)
    (tmp_path / ".env").write_text("MISTRAL_API_KEY=must-not-be-read\n")
    with pytest.raises(ConfigurationError):
        load_mistral_api_key()


def test_process_environment_is_the_only_key_source(monkeypatch):
    monkeypatch.setenv("MISTRAL_API_KEY", "injected-for-test")
    assert load_mistral_api_key() == "injected-for-test"
