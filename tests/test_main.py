# install pytest https://docs.pytest.org/en/latest/ : pip install --user pytest
from unittest.mock import patch, call

from main import main

def test_1():
    with patch('main.randint', return_value=30):
        with patch('main.input', side_effect=[50, 75, 20, 25, 30]):
            with patch('main.print') as mock_print:
                main()
                assert list(mock_print.mock_calls) == [
                        call('Хаха! Я загадал число!'),
                        call('Холоднее...'),
                        call('Ну ты и лох!'),
                        call('Горячее!'),
                        call('Горячее!'),
                        call('Победа! Я и правда загадал 30!')
                        ]

