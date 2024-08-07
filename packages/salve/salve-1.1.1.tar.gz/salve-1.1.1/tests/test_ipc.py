from pathlib import Path
from sys import platform
from time import sleep

from salve import (
    AUTOCOMPLETE,
    DEFINITION,
    EDITORCONFIG,
    HIGHLIGHT,
    IPC,
    LINKS_AND_CHARS,
    REPLACEMENTS,
    Response,
)


def test_IPC():
    context = IPC()

    context.update_file(
        "test", open(Path("tests/testing_file1.py"), "r+").read()
    )

    context.request(
        AUTOCOMPLETE,
        file="test",
        expected_keywords=[],
        current_word="t",
    )
    context.request(
        REPLACEMENTS,
        file="test",
        expected_keywords=[],
        current_word="thid",
    )
    context.request(
        HIGHLIGHT, file="test", language="python", text_range=(1, 18)
    )
    context.request(EDITORCONFIG, file_path=__file__)
    context.request(
        DEFINITION,
        file="test",
        current_word="Bar",
        definition_starters=[
            (r"def ", "after"),
            (r"import .*,? ", "after"),
            (r"from ", "after"),
            (r"class ", "after"),
            (r":?.*=.*", "before"),
        ],
    )
    context.request(LINKS_AND_CHARS, file="test", text_range=(1, 18))
    sleep(1)

    # Check output
    autocomplete_output: Response | None = context.get_response(AUTOCOMPLETE)
    if autocomplete_output is None:
        raise AssertionError("Autocomplete output is None")
    autocomplete_output["id"] = 0
    assert autocomplete_output == {
        "id": 0,
        "type": "response",
        "cancelled": False,
        "command": AUTOCOMPLETE,
        "result": ["test", "this"],
    }

    replacements_output: Response | None = context.get_response(REPLACEMENTS)
    if replacements_output is None:
        raise AssertionError("Replacements output is None")
    replacements_output["id"] = 0
    assert replacements_output == {
        "id": 0,
        "type": "response",
        "cancelled": False,
        "command": REPLACEMENTS,
        "result": ["this"],
    }

    highlight_output: Response | None = context.get_response(HIGHLIGHT)
    if highlight_output is None:
        raise AssertionError("Highlight output is None")
    highlight_output["id"] = 0

    expected_output: Response = {
        "id": 0,
        "type": "response",
        "cancelled": False,
        "command": HIGHLIGHT,
        "result": [
            ((1, 0), 4, "Keyword"),
            ((1, 5), 4, "Name"),
            ((1, 10), 6, "Keyword"),
            ((1, 17), 1, "Name"),
            ((1, 20), 12, "Comment"),
            ((3, 0), 3, "Name"),
            ((3, 4), 1, "Operator"),
            ((3, 6), 3, "Name"),
            ((3, 11), 7, "Comment"),
            ((5, 0), 5, "Name"),
            ((5, 5), 1, "Punctuation"),
            ((5, 6), 3, "String"),
            ((5, 9), 1, "Punctuation"),
            ((5, 12), 16, "Comment"),
            ((8, 0), 5, "Keyword"),
            ((8, 6), 3, "Name"),
            ((8, 9), 1, "Punctuation"),
            ((8, 10), 3, "Name"),
            ((8, 13), 2, "Punctuation"),
            ((9, 4), 3, "String"),
            ((10, 4), 4, "String"),
            ((11, 4), 3, "String"),
            ((13, 4), 3, "Keyword"),
            ((13, 8), 8, "Name"),
            ((13, 16), 1, "Punctuation"),
            ((13, 17), 4, "Name"),
            ((13, 21), 2, "Punctuation"),
            ((14, 8), 4, "Keyword"),
            ((17, 0), 3, "Name"),
            ((17, 3), 2, "Punctuation"),
            ((18, 0), 24, "Comment"),
        ],
    }
    # Deal with Windows weirdness
    if platform == "win32":
        expected_output = {
            "id": 0,
            "type": "response",
            "cancelled": False,
            "command": HIGHLIGHT,
            "result": [
                ((1, 0), 4, "Keyword"),
                ((1, 5), 4, "Name"),
                ((1, 10), 6, "Keyword"),
                ((1, 17), 1, "Name"),
                ((1, 20), 12, "Comment"),
                ((3, 0), 3, "Name"),
                ((3, 4), 1, "Operator"),
                ((3, 6), 3, "Name"),
                ((3, 11), 7, "Comment"),
                ((5, 0), 5, "Name"),
                ((5, 5), 1, "Punctuation"),
                ((5, 6), 5, "String"),
                ((5, 11), 1, "Punctuation"),
                ((5, 14), 16, "Comment"),
                ((8, 0), 5, "Keyword"),
                ((8, 6), 3, "Name"),
                ((8, 9), 1, "Punctuation"),
                ((8, 10), 3, "Name"),
                ((8, 13), 2, "Punctuation"),
                ((9, 4), 3, "String"),
                ((10, 4), 4, "String"),
                ((11, 4), 3, "String"),
                ((13, 4), 3, "Keyword"),
                ((13, 8), 8, "Name"),
                ((13, 16), 1, "Punctuation"),
                ((13, 17), 4, "Name"),
                ((13, 21), 2, "Punctuation"),
                ((14, 8), 4, "Keyword"),
                ((17, 0), 3, "Name"),
                ((17, 3), 2, "Punctuation"),
                ((18, 0), 24, "Comment"),
            ],
        }

    assert highlight_output == expected_output

    links_and_hidden_chars_result: Response | None = context.get_response(
        LINKS_AND_CHARS
    )
    if links_and_hidden_chars_result is None:
        raise AssertionError("links_and_hidden_chars_result output is None")
    links_and_hidden_chars_result["id"] = 0
    expected_output = {
        "id": 0,
        "type": "response",
        "cancelled": False,
        "command": LINKS_AND_CHARS,
        "result": [((18, 2), 22, "Link"), ((5, 7), 1, "Hidden_Char")],
    }
    if platform == "win32":
        expected_output = {
            "id": 0,
            "type": "response",
            "cancelled": False,
            "command": LINKS_AND_CHARS,
            "result": [((18, 2), 22, "Link")],
        }
    assert links_and_hidden_chars_result == expected_output

    context.update_file(
        "foo", open(Path("tests/testing_file2.py"), "r+").read()
    )
    context.request(HIGHLIGHT, file="foo", language="python")
    while not (output := context.get_response(HIGHLIGHT)):
        pass
    response = output["result"]  # type: ignore
    assert response != []

    context.remove_file("test")
    context.kill_IPC()


if __name__ == "__main__":
    test_IPC()
