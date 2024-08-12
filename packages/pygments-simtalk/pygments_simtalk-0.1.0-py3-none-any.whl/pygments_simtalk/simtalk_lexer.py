"""
    Pygments lexer for the SimTalk programming language.
"""

import re

from pygments.lexer import RegexLexer, bygroups
from pygments.token import (
    Comment,
    Keyword,
    Name,
    Number,
    Operator,
    Punctuation,
    String,
    Text,
    Whitespace,
)

__all__ = ["SimTalkLexer"]


class SimTalkLexer(RegexLexer):
    name = "SimTalk"
    aliases = ["simtalk"]

    # List of SimTalk keywords
    keywords = (
        "else",
        "result",
        "elseif",
        "next",
        "return",
        "to",
        "end",
        "exitLoop",
        "until",
        "byref",
        "continue",
        "for",
        "create",
        "forget",
        "wait",
        "if",
        "print",
        "stopuntil",
        "waitExpired",
        "prio",
        "waituntil",
        "switch",
        "when",
        "downto",
        "loop",
        "repeat",
        "then",
        "while",
    )
    # List of SimTalk data types
    data_types = (
        "Acceleration",
        "Money",
        "Any",
        "Object",
        "Array",
        "Queue",
        "Boolean",
        "Real",
        "Date",
        "Speed",
        "DateTime",
        "Stack",
        "Integer",
        "String",
        "Length",
        "Table",
        "List",
        "Time",
        "Method",
        "Weight",
    )
    # Word operators
    word_operators = ("and", "not", "or", "mod", "div")
    # List of constants
    constants = ("true", "false", "pi", "void")
    # List of anonymous identifiers
    anonymous_identifiers = (
        "@",
        "root",
        "basis",
        "RootFolder",
        "current",
        "self",
        "?",
        "location",
        "~",
    )

    tokens = {
        "root": [
            (r"\s+", Whitespace),  # Whitespace
            (r"--.*?$", Comment.Single),  # Single-line comments
            (r"//.*?$", Comment.Single),  # Single-line comments
            (r"/[*](.|\n)*?[*]/", Comment.Multiline),
            (r'"(?:[^"\\\r\n]|\\.)*"', String),  # Single-line strings
            (
                r'".*?(?:\\\r?\n.*?)*"',
                String,
            ),  # Multiline strings with line continuation
            (
                r"(?i)\b(var|param)(\s+)(\w+)",
                bygroups(Keyword.Declaration, Text.Whitespace, Name),
            ),
            (
                r"[+-]?(?:\d*\.\d+([eE][+-]?\d{1,3})?|\d+([eE][+-]?\d{1,3}))",
                Number.Float,
            ),  # Floating point numbers
            (r"[+-]?\d+", Number.Integer),  # Integers
            (
                r"(?i)\b(?:%s)\b"
                % "|".join(re.escape(data_type) for data_type in data_types),
                Keyword.Type,
            ),  # Data types
            (
                r"(?i)\b(?:%s)\b"
                % "|".join(re.escape(keyword) for keyword in keywords),
                Keyword,
            ),  # Keywords
            (
                r"(?i)\b(?:%s)\b"
                % "|".join(
                    re.escape(word_operator) for word_operator in word_operators
                ),
                Operator.Word,
            ),  # Word operators
            (r"[-+/*=<>&]", Operator),  # Operators
            (r"/=|<=|>=|~=|>~=|<~=|->|:=", Operator),  # Combined operators
            (
                r"(?i)(?:%s)" % "|".join(re.escape(constant) for constant in constants),
                Keyword.Constant,
            ),  # Constants
            (
                r"(?i)(@|root|basis|RootFolder|current|self|\?|location|~)(?=\s|$|\.)",
                Name.Builtin.Pseudo,
            ),  # Anonymous identifiers
            (r"[{}:;().,\[\]]", Punctuation),  # Punctuation
            (r"([a-z]\w*)|([A-Z][A-Z0-9_]*[a-z])", Name),  # Names
            (r"\b\w+\b", Text),  # Other words
        ],
    }
