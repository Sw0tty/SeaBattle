"""
Game exceptions
"""
import colorsys


class OutOfField(Exception):
    pass


class InSameDot(Exception):
    pass


class BadSettings(Exception):

    __module__ = Exception.__module__

    def __str__(self):
        return """Check 'SHIPS_SET' in settings."""

