from app import ExternalAnalyzer
import pytest
from unittest.mock import create_autospec, call

@pytest.fixture
def analyzer_mock():
        return create_autospec(ExternalAnalyzer, instance=True)

def test_mock_called(analyzer_mock):
    analyzer_mock.set_path_binary_file.return_value = "none"
    c = analyzer_mock
    assert(c.set_path_binary_file() == "none")
    # no tiene parametros de entrada asi que solo verifique que se llame una vex
    analyzer_mock.assert_called_once()

def test_mock_call_args(analyzer_mock):
    analyzer_mock.set_path_binary_file.return_value = "none"
    
    # llamo una vez
    analyzer_mock.set_path_binary_file()
    # verifica que llamo una vez a esa funcion
    analyzer_mock.call_args_list == [call.set_path_binary_file()]