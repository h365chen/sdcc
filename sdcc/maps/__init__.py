"""Contain necessary information for SocAssess to provide feedback.."""

from . import general, compilation

__all__ = [
    # required
    "questions",
    "selected",
]


# ========
# Required
# ========

selected = {
    "general": general.mappings,
    "compilation": compilation.mappings,
}


questions = {
    "general": "this is a general question",
    "compilation": "",
}
