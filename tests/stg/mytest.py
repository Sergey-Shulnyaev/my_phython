from unittest.mock import patch, call

from mygayme import main

def test_1():
    with patch('main.randint', return_value=7):
        with patch('main.input', side_effect=['девка тупая', 'да', 'пизда', 'да', 'марка']):
            with patch('main.print') as mock_print:
                main()
                assert list(mock_print.mock_calls) == [
                        call('Попробуйте отгадать следующую загадку:'),
                        call('Вы не отгадали, желаете попробовать ещё раз?'),
                        call('Вы не отгадали, желаете попробовать ещё раз?')
                        ]