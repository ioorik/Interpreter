
from Interpreter import Lexer
from unittest import mock
from unittest.mock import call


def test_word() -> None:

    with mock.patch("builtins.print") as mock_print:
        Lexer(text="INT MEOW").run(debug=True)
        
        assert mock_print.call_args_list == [
            call(['INT', 'WORD']),
            call([' ', 'SPACE']),
            call(['MEOW', 'WORD'])
        ]


def  test_float():

    with mock.patch('builtins.print') as mock_print:
        Lexer(text="""1.1
0.1
1.0
0.0
10.0
0.10""").run(debug=True)
        
        assert mock_print.call_args_list == [
            call(['1.1', 'FLOAT']),
            call(['\n', 'EOL']),
            call(['0.1', 'FLOAT']),
            call(['\n', 'EOL']),
            call(['1.0', 'FLOAT']),
            call(['\n', 'EOL']),
            call(['0.0', 'FLOAT']),
            call(['\n', 'EOL']),
            call(['10.0', 'FLOAT']),
            call(['\n', 'EOL']),
            call(['0.10', 'FLOAT']),
        ]


def test_int():

    with mock.patch('builtins.print') as mock_print:
        Lexer(text="1 2 3").run(debug=True)
        
        assert mock_print.call_args_list == [
            call(['1', 'INT']),
            call([' ', 'SPACE']),
            call(['2', 'INT']),
            call([' ', 'SPACE']),
            call(['3', 'INT'])
        ]

    
def test_str():

    with mock.patch('builtins.print') as mock_print:
        Lexer(text="""'Hello' "Hi" "Don't" 'Quote "A wise man once said..."'""").run(debug=True)

        assert mock_print.call_args_list == [
            call(["'Hello'", 'STR']),
            call([' ', 'SPACE']),
            call(['"Hi"', 'STR']),
            call([' ', 'SPACE']),
            call(['"Don\'t"', 'STR']),
            call([' ', 'SPACE']),
            call(['\'Quote "A wise man once said..."\'', 'STR'])
        ]