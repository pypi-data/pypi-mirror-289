from typing import Any, Optional, Union, List, Dict
from enum import Enum

__all__ = ["GeneralEnum", "DescriptiveEnum", "CaseInsensitiveStrEnum"]

class CaseInsensitiveStrEnum(str, Enum):
    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.lower() == value:
                return member
        return None

class GeneralEnum(Enum):
    """
    Extended Enum class with additional parsing and lookup functionalities.

    Args:
        expr (Optional[Union[int, str, GeneralEnum]], optional): The expression to parse into an enum member. 
                        This can be an integer, a string representing the enum member name (case-insensitive), 
                        or an existing `GeneralEnum` instance. Defaults to None.

    Returns:
        GeneralEnum or None: The corresponding enum member if the expression is valid and matches any enum 
                             member or alias. Returns None if expr is None.

    Example:
        class MyEnum(GeneralEnum):
            OPTION_A = 1
            OPTION_B = 2

        # Parsing from string
        option = MyEnum.parse("option_a")  # Returns MyEnum.OPTION_A

        # Alias handling
        MyEnum.__aliases__ = {"alias_a": "option_a"}
        alias_option = MyEnum.parse("alias_a")  # Returns MyEnum.OPTION_A

        # Retrieving enum member by attribute value
        option_with_value = MyEnum.get_member_by_attribute("value", 2)  # Returns MyEnum.OPTION_B
    """
    
    __aliases__ = {
    }

    @classmethod
    def _missing_(cls, value: Any):
        return cls.parse(value)
    
    @classmethod
    def on_parse_exception(cls, expr: str):
        """
        Raises a runtime error for invalid options in the parse() method.

        Args:
            expr (str): The expression representing the invalid option.

        Raises:
            RuntimeError: If the expression is not a valid enum member or alias, providing the list of 
                          allowed options.
        """
        classname = cls.__name__
        option_text = ", ".join(cls.get_members())
        raise RuntimeError(f'Invalid option "{expr}" for the enum class "{classname}" '
                           f'(allowed options: {option_text}).')
        
    @classmethod
    def parse(cls, value: Optional[Union[int, str, "GeneralEnum"]] = None) -> Optional["GeneralEnum"]:
        """
        Parses a given expression into the corresponding enum member or its alias.

        Args:
            value (Optional[Union[int, str, GeneralEnum]], optional): The expression to parse into an enum member. 
                        This can be an integer representing the enum value, a string representing the enum member
                        name (case-insensitive), or an existing `GeneralEnum` instance. Defaults to None.

        Returns:
            GeneralEnum or None: The corresponding enum member if the expression is valid and matches any enum 
                                 member or alias. Returns None if expr is None.

        Raises:
            RuntimeError: If the expression is not valid or does not match any enum member or alias.
        """
        if isinstance(value, str):
            expr = value.strip().lower()
            members_map = cls.get_members_map()
            if expr in members_map:
                return members_map[expr]
            aliases_map = cls.get_aliases_map()
            if expr in aliases_map:
                return cls.parse(aliases_map[expr])
            cls.on_parse_exception(value)
        if value is None:
            return None
        if isinstance(value, cls):
            return value
        values_map = cls.get_values_map()
        if value in values_map:
            return values_map[value]
        cls.on_parse_exception(value)
            
    @classmethod
    def get_members(cls) -> List[str]:
        """
        Returns a list of member names in lowercase.

        Returns:
            list[str]: A list of member names in lowercase.
        """
        return [i.lower() for i in cls.__members__]
    
    @classmethod
    def get_members_map(cls) -> Dict[str, "GeneralEnum"]:
        """
        Returns a dictionary mapping lowercase member names to enum members.

        Returns:
            dict[str, GeneralEnum]: A dictionary mapping lowercase member names to enum members.
        """
        return {k.lower(): v for k, v in cls.__members__.items()}

    @classmethod
    def get_values_map(cls) -> Dict[str, "GeneralEnum"]:
        """
        Returns a dictionary mapping enum values to enum member.

        Returns:
            dict[str, GeneralEnum]: A dictionary mapping enum values to enum member.
        """
        return {v.value: v for k, v in cls.__members__.items()}
    
    @classmethod
    def get_aliases_map(cls) -> Dict[str, "GeneralEnum"]:
        """
        Returns a dictionary mapping lowercase aliases to enum members.

        Returns:
            dict[str, GeneralEnum]: A dictionary mapping lowercase aliases to enum members.
        """
        return {k.lower(): v for k, v in cls.__aliases__.items()}
    
    @classmethod
    def has_member(cls, name: str) -> bool:
        """
        Checks if an enum member exists with the given name (case-insensitive).

        Args:
            name (str): The name of the enum member to check.

        Returns:
            bool: True if the enum member exists, False otherwise.
        """
        return name.lower() in cls.get_members()
    
    @classmethod
    def get_member_by_attribute(cls, attribute: str, value: Any) -> Optional["GeneralEnum"]:
        """
        Returns the enum member that has the specified attribute with the given value.

        Args:
            attribute (str): The name of the attribute to search for.
            value (Any): The value of the attribute to match.

        Returns:
            GeneralEnum or None: The enum member that matches the attribute value. Returns None if not found.
        """
        members = cls.__members__
        return next((x for x in members.values() if getattr(x, attribute) == value), None)

class DescriptiveEnum(GeneralEnum):
    """
    Enum class with support for additional descriptions for each enum member.

    Attributes:
        description (str): The additional description associated with each enum member.

    Example:
        class MyEnum(DescriptiveEnum):
            OPTION_A = 1, "This is option A"
            OPTION_B = 2, "This is option B"

        # Accessing enum member and its description
        print(MyEnum.OPTION_A)  # Output: MyEnum.OPTION_A
        print(MyEnum.OPTION_A.description)  # Output: "This is option A"

        # Parsing from string with description in on_parse_exception
        option = MyEnum.parse("option_b")  # Returns MyEnum.OPTION_B
        print(option.description)  # Output: "This is option B"
    """

    def __new__(cls, value: int, description: str = ""):
        """
        Creates a new `DescriptiveEnum` instance with the given value and an optional description.

        Args:
            value (int): The value associated with the enum member.
            description (str, optional): An additional description for the enum member. Defaults to "".

        Returns:
            DescriptiveEnum: The newly created `DescriptiveEnum` instance with the given value and description.
        """
        obj = object.__new__(cls)
        obj._value_ = value
        obj.description = description
        return obj

    @classmethod
    def on_parse_exception(cls, expr: str):
        """
        Raises a runtime error when an invalid option is passed to the parse() method.

        Args:
            expr (str): The expression representing the invalid option.

        Raises:
            RuntimeError: If the expression is not a valid enum member or alias, providing the list of 
                          allowed options along with their descriptions.
        """
        classname = cls.__name__
        enum_descriptions = "".join([f'    {key.lower()} - {val.description}\n' \
                                     for key, val in cls.__members__.items()])
        raise RuntimeError(f'Invalid option "{expr}" for the enum class "{classname}"\n'
                           f'  Allowed options:\n{enum_descriptions}')