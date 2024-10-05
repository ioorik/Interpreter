
import unittest
from Interpreter import Lexer, UnclosedStringError, InvalidNumberError
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


def test_float():

    with mock.patch('builtins.print') as mock_print:
        Lexer(text="""1.1
0.1
1.0
0.0
10.0
0.10
.20""").run(debug=True)
        
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
            call(['\n', 'EOL']),
            call(['.20', 'FLOAT'])
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


class test_errors(unittest.TestCase):

    def test_unclosed_string(self) -> None:
        with self.assertRaises(expected_exception=UnclosedStringError) as context:
            Lexer(text="'Hello").run()
        
        assert str(object=context.exception) == "Unclosed String!"

        with self.assertRaises(expected_exception=UnclosedStringError) as context:
            Lexer(text='"Hello').run()
        
        assert str(object=context.exception) == "Unclosed String!"
            
    def test_invalid_number(self) -> None:
        with self.assertRaises(expected_exception=InvalidNumberError) as context:
            Lexer(text="1.0.0").run()

        assert str(object=context.exception) == "Invalid Number Format!"

        with self.assertRaises(expected_exception=InvalidNumberError) as context:
            Lexer(text="01").run()

        assert str(object=context.exception) == "Invalid Number Format!"
