from pplox.scanner import Scanner

def test_parens():
    scanner = Scanner("(()")
    tokens = scanner.scan_tokens()
    assert len(tokens) == 4
    assert tokens[0].to_string() == "LEFT_PAREN ( null"
    assert tokens[1].to_string() == "LEFT_PAREN ( null"
    assert tokens[2].to_string() == "RIGHT_PAREN ) null"
    assert tokens[3].to_string() == "EOF  null"

def test_braces():
    scanner = Scanner("{{}}")
    tokens = scanner.scan_tokens()
    assert len(tokens) == 5
    assert tokens[0].to_string() == "LEFT_BRACE { null"
    assert tokens[1].to_string() == "LEFT_BRACE { null"
    assert tokens[2].to_string() == "RIGHT_BRACE } null"
    assert tokens[3].to_string() == "RIGHT_BRACE } null"
    assert tokens[4].to_string() == "EOF  null"

def test_single_characters():
    scanner = Scanner("({*.,+*})")
    tokens = scanner.scan_tokens()
    assert len(tokens) == 10
    assert tokens[0].to_string() == "LEFT_PAREN ( null"
    assert tokens[1].to_string() == "LEFT_BRACE { null"
    assert tokens[2].to_string() == "STAR * null"
    assert tokens[3].to_string() == "DOT . null"
    assert tokens[4].to_string() == "COMMA , null"
    assert tokens[5].to_string() == "PLUS + null"
    assert tokens[6].to_string() == "STAR * null"
    assert tokens[7].to_string() == "RIGHT_BRACE } null"
    assert tokens[8].to_string() == "RIGHT_PAREN ) null"
    assert tokens[9].to_string() == "EOF  null"

def test_empty_file():
    scanner = Scanner("")
    tokens = scanner.scan_tokens()
    assert len(tokens) == 1
    assert tokens[0].to_string() == "EOF  null"
