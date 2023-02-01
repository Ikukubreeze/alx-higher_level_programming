#!/usr/bin/python3
"""
Write a class LockedClass with no class or object attribute,
that prevents the user from dynamically creating new instance
attributes, except if the new instance attribute is called
first_name.
https://stackoverflow.com/questions/3603502/prevent-creating-new-attributes-outside-init
"""


class LockedClass:
    "Lock Class"
    __slots__ = ["first_name"]

    def __init__(self, first_name=""):
        self.first_name = first_name
