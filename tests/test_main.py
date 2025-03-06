"""Tests for the main module."""

from your_package_name.main import main


def test_main(capsys) -> None:
    """Test the main function."""
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\n"