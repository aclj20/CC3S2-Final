from app import ExternalAnalyzer
import pytest
from unittest.mock import create_autospec

class FakeExternalAnalyzer:
    # Reemplaza la variable de ruta del binario a NOne
    def test_set_path_binary_file(self, monkeypatch):
        monkeypatch.setattr(ExternalAnalyzer, "set_path_binary_file", "none")
            
        c = ExternalAnalyzer()
        assert(c.set_path_binary_file() == "none")
    
    def test_search_api(monkeypatch):
        # json de respuesta somulado
        fake_response = {
            "results": [
                {"nombre": "Ariana", "apellido": "Lopez"}
            ]
        }
        
        monkeypatch.setattr(ExternalAnalyzer, "search_api", lambda self: fake_response)
        
        c = ExternalAnalyzer()
        assert(c.search_api() == fake_response)
    
    
