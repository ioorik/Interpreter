

class InvalidNumberError(Exception):
    """Raised when there are two or more dots in an iteger/float."""
    def __init__(self) -> None:
        super().__init__("Invalid Number Format!")


class UnclosedStringError(Exception):

    def __init__(self) -> None:
        super().__init__("Unclosed String!")


class Lexer:

    def __init__(self, text: str) -> None:
        self._source: list[str] = list(text)
        self._tokens: list[list[str]] = []
    
    def run(self, debug: bool = False):
        while self._source:
            char: str = self._source.pop(0)
            token: str = char

            if char.isalpha():
                while self._source and self._source[0].isalpha():
                    token += self._source.pop(0)
                self._tokens.append([token, "WORD"])
            elif char in ".1234567890":
                dot = False
                if char == ".":
                    dot = True
                while self._source and self._source[0] in ".1234567890":
                    nextC = self._source.pop(0)
                    if nextC == "." and not dot:
                        dot = True
                        token += nextC
                    elif nextC == "." and dot:
                        raise InvalidNumberError
                    else:
                        token += nextC
                if not dot:
                    self._tokens.append([token, "INT"])
                else:
                    self._tokens.append([token, "FLOAT"])
            elif char in """"'""":
                while self._source and (self._source[0].isalpha() or self._source[0] in "<>,./?\\| !@#$%^&*()_+-=`~;:[]{}" or (self._source[0] == "'" and char == '"') or (self._source[0] == '"' and char == "'")):
                    token += self._source.pop(0)
                if self._source and self._source[0] == char:
                    token += self._source.pop(0)
                    self._tokens.append([token, "STR"])
                else:
                    raise UnclosedStringError
            elif char == " ":
                self._tokens.append([' ', 'SPACE'])
            elif char == "\n":
                self._tokens.append(["\n", "EOL"])
                
            if debug:
                print(self._tokens[-1])


if __name__ == "__main__":
    lex = Lexer(text="""Hello
123
1.1
0.3
10.5
"Hello"
'Hello'
"Don't"
'Quote "Something something something"'
""")
    lex.run(debug=True)