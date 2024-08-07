from datetime import datetime
from typing import Any

from sqlalchemy import Column, Select

__all__ = [
    "BaseFilter",
    "FilterEqual",
    "FilterNotEqual",
    "FilterStartsWith",
    "FilterNotStartsWith",
    "FilterEndsWith",
    "FilterNotEndsWith",
    "FilterContains",
    "FilterNotContains",
    "FilterGreater",
    "FilterSmaller",
    "FilterGreaterEqual",
    "FilterSmallerEqual",
    "FilterIn",
    "FilterRelationOneToOneOrManyToOneEqual",
    "FilterRelationOneToOneOrManyToOneNotEqual",
    "FilterRelationOneToManyOrManyToManyIn",
    "FilterRelationOneToManyOrManyToManyNotIn",
    "DateFilterEqual",
    "DateFilterNotEqual",
    "DateFilterGreater",
    "DateFilterSmaller",
    "DateFilterGreaterEqual",
    "DateFilterSmallerEqual",
    "DateFilterIn",
    "DateTimeFilterEqual",
    "DateTimeFilterNotEqual",
    "DateTimeFilterGreater",
    "DateTimeFilterSmaller",
    "DateTimeFilterGreaterEqual",
    "DateTimeFilterSmallerEqual",
    "DateTimeFilterIn",
    "SQLAFilterConverter",
]


class BaseFilter:
    name: str
    arg_name: str
    is_heavy = False
    """
    If set to true, will run the filter in a separate thread. Useful for heavy filters that take a long time to execute. Default is False.

    Only works when apply function is not a coroutine.
    """

    def apply(stmt: Select, col: Column, value: Any) -> Select:
        """
        Apply the filter to the given SQLAlchemy Select statement.

        Args:
            stmt (Select): The SQLAlchemy Select statement to apply the filter to.
            col (Column): The SQLAlchemy Column to filter on.
            value (Any): The value to filter by.

        Returns:
            Select: The SQLAlchemy Select statement with the filter applied.

        Raises:
            NotImplementedError: This method should be implemented by subclasses.
        """
        raise NotImplementedError()


class FilterEqual(BaseFilter):
    name = "Equal to"
    arg_name = "eq"

    def apply(stmt: Select, col: Column, value: Any) -> Select:
        if value == "NULL":
            return stmt.filter(col.is_(None))
        return stmt.filter(col == value)


class FilterNotEqual(BaseFilter):
    name = "Not Equal to"
    arg_name = "neq"

    def apply(stmt: Select, col: Column, value: Any) -> Select:
        if value == "NULL":
            return stmt.filter(col.isnot(None))
        return stmt.filter(col != value)


class FilterStartsWith(BaseFilter):
    name = "Starts with"
    arg_name = "sw"

    def apply(stmt: Select, col: Column, value: Any) -> Select:
        return stmt.filter(col.ilike(value + "%"))


class FilterNotStartsWith(BaseFilter):
    name = "Not Starts with"
    arg_name = "nsw"

    def apply(stmt: Select, col: Column, value: Any) -> Select:
        return stmt.filter(~col.ilike(value + "%"))


class FilterEndsWith(BaseFilter):
    name = "Ends with"
    arg_name = "ew"

    def apply(stmt: Select, col: Column, value: Any) -> Select:
        return stmt.filter(col.ilike("%" + value))


class FilterNotEndsWith(BaseFilter):
    name = "Not Ends with"
    arg_name = "new"

    def apply(stmt: Select, col: Column, value: Any) -> Select:
        return stmt.filter(~col.ilike("%" + value))


class FilterContains(BaseFilter):
    name = "Contains"
    arg_name = "ct"

    def apply(stmt: Select, col: Column, value: Any) -> Select:
        return stmt.filter(col.ilike("%" + value + "%"))


class FilterNotContains(BaseFilter):
    name = "Not Contains"
    arg_name = "nct"

    def apply(stmt: Select, col: Column, value: Any) -> Select:
        return stmt.filter(~col.ilike("%" + value + "%"))


class FilterGreater(BaseFilter):
    name = "Greater than"
    arg_name = "gt"

    def apply(stmt: Select, col: Column, value: Any) -> Select:
        return stmt.filter(col > value)


class FilterSmaller(BaseFilter):
    name = "Smaller than"
    arg_name = "lt"

    def apply(stmt: Select, col: Column, value: Any) -> Select:
        return stmt.filter(col < value)


class FilterGreaterEqual(BaseFilter):
    name = "Greater equal"
    arg_name = "ge"

    def apply(stmt: Select, col: Column, value: Any) -> Select:
        return stmt.filter(col >= value)


class FilterSmallerEqual(BaseFilter):
    name = "Smaller equal"
    arg_name = "le"

    def apply(stmt: Select, col: Column, value: Any) -> Select:
        return stmt.filter(col <= value)


class FilterIn(BaseFilter):
    name = "One of"
    arg_name = "in"

    def apply(stmt: Select, col: Column, value: Any) -> Select:
        return stmt.filter(col.in_(value))


class FilterRelationOneToOneOrManyToOneEqual(FilterEqual):
    arg_name = "rel_o_m"


class FilterRelationOneToOneOrManyToOneNotEqual(FilterNotEqual):
    arg_name = "nrel_o_m"


class FilterRelationOneToManyOrManyToManyIn(BaseFilter):
    name = "In"
    arg_name = "rel_m_m"

    def _apply_item(stmt: Select, col: Column, value: Any) -> Select:
        return stmt.filter(col.contains(value))

    def apply(stmt: Select, col: Column, value: Any) -> Select:
        if isinstance(value, list):
            for val in value:
                stmt = FilterRelationOneToManyOrManyToManyIn._apply_item(stmt, col, val)
        else:
            stmt = FilterRelationOneToManyOrManyToManyIn._apply_item(stmt, col, value)
        return stmt


class FilterRelationOneToManyOrManyToManyNotIn(BaseFilter):
    name = "Not In"
    arg_name = "nrel_m_m"

    def _apply_item(stmt: Select, col: Column, value: Any) -> Select:
        return stmt.filter(~col.contains(value))

    def apply(stmt: Select, col: Column, value: Any) -> Select:
        if isinstance(value, list):
            for val in value:
                stmt = FilterRelationOneToManyOrManyToManyNotIn._apply_item(
                    stmt, col, val
                )
        else:
            stmt = FilterRelationOneToManyOrManyToManyNotIn._apply_item(
                stmt, col, value
            )
        return stmt


class DateFilterEqual(FilterEqual):
    def apply(stmt: Select, col: Column, value: Any) -> Select:
        value = datetime.fromisoformat(value).date()
        return FilterEqual.apply(stmt, col, value)


class DateFilterNotEqual(FilterNotEqual):
    def apply(stmt: Select, col: Column, value: Any) -> Select:
        value = datetime.fromisoformat(value).date()
        return FilterNotEqual.apply(stmt, col, value)


class DateFilterGreater(FilterGreater):
    def apply(stmt: Select, col: Column, value: Any) -> Select:
        value = datetime.fromisoformat(value).date()
        return FilterGreater.apply(stmt, col, value)


class DateFilterSmaller(FilterSmaller):
    def apply(stmt: Select, col: Column, value: Any) -> Select:
        value = datetime.fromisoformat(value).date()
        return FilterSmaller.apply(stmt, col, value)


class DateFilterGreaterEqual(FilterGreaterEqual):
    def apply(stmt: Select, col: Column, value: Any) -> Select:
        value = datetime.fromisoformat(value).date()
        return FilterGreaterEqual.apply(stmt, col, value)


class DateFilterSmallerEqual(FilterSmallerEqual):
    def apply(stmt: Select, col: Column, value: Any) -> Select:
        value = datetime.fromisoformat(value).date()
        return FilterSmallerEqual.apply(stmt, col, value)


class DateFilterIn(FilterIn):
    def apply(stmt: Select, col: Column, value: Any) -> Select:
        value = [datetime.fromisoformat(v).date() for v in value]
        return FilterIn.apply(stmt, col, value)


class DateTimeFilterEqual(FilterEqual):
    def apply(stmt: Select, col: Column, value: Any) -> Select:
        value = datetime.fromisoformat(value).replace(tzinfo=None)
        return FilterEqual.apply(stmt, col, value)


class DateTimeFilterNotEqual(FilterNotEqual):
    def apply(stmt: Select, col: Column, value: Any) -> Select:
        value = datetime.fromisoformat(value).replace(tzinfo=None)
        return FilterNotEqual.apply(stmt, col, value)


class DateTimeFilterGreater(FilterGreater):
    def apply(stmt: Select, col: Column, value: Any) -> Select:
        value = datetime.fromisoformat(value).replace(tzinfo=None)
        return FilterGreater.apply(stmt, col, value)


class DateTimeFilterSmaller(FilterSmaller):
    def apply(stmt: Select, col: Column, value: Any) -> Select:
        value = datetime.fromisoformat(value).replace(tzinfo=None)
        return FilterSmaller.apply(stmt, col, value)


class DateTimeFilterGreaterEqual(FilterGreaterEqual):
    def apply(stmt: Select, col: Column, value: Any) -> Select:
        value = datetime.fromisoformat(value).replace(tzinfo=None)
        return FilterGreaterEqual.apply(stmt, col, value)


class DateTimeFilterSmallerEqual(FilterSmallerEqual):
    def apply(stmt: Select, col: Column, value: Any) -> Select:
        value = datetime.fromisoformat(value).replace(tzinfo=None)
        return FilterSmallerEqual.apply(stmt, col, value)


class DateTimeFilterIn(FilterIn):
    def apply(stmt: Select, col: Column, value: Any) -> Select:
        value = [datetime.fromisoformat(v).replace(tzinfo=None) for v in value]
        return FilterIn.apply(stmt, col, value)


class SQLAFilterConverter:
    """
    Helper class to get available filters for a column type.
    """

    conversion_table = (
        (
            "is_relation_one_to_one",
            [
                FilterRelationOneToOneOrManyToOneEqual,
                FilterRelationOneToOneOrManyToOneNotEqual,
            ],
        ),
        (
            "is_relation_many_to_one",
            [
                FilterRelationOneToOneOrManyToOneEqual,
                FilterRelationOneToOneOrManyToOneNotEqual,
            ],
        ),
        (
            "is_relation_one_to_many",
            [
                FilterRelationOneToManyOrManyToManyIn,
                FilterRelationOneToManyOrManyToManyNotIn,
            ],
        ),
        (
            "is_relation_many_to_many",
            [
                FilterRelationOneToManyOrManyToManyIn,
                FilterRelationOneToManyOrManyToManyNotIn,
            ],
        ),
        ("is_enum", [FilterEqual, FilterNotEqual, FilterIn]),
        ("is_boolean", [FilterEqual, FilterNotEqual, FilterIn]),
        (
            "is_text",
            [
                FilterEqual,
                FilterNotEqual,
                FilterStartsWith,
                FilterNotStartsWith,
                FilterEndsWith,
                FilterNotEndsWith,
                FilterContains,
                FilterNotContains,
                FilterIn,
            ],
        ),
        (
            "is_binary",
            [
                FilterEqual,
                FilterNotEqual,
                FilterStartsWith,
                FilterNotStartsWith,
                FilterEndsWith,
                FilterNotEndsWith,
                FilterContains,
                FilterNotContains,
                FilterIn,
            ],
        ),
        (
            "is_string",
            [
                FilterEqual,
                FilterNotEqual,
                FilterStartsWith,
                FilterNotStartsWith,
                FilterEndsWith,
                FilterNotEndsWith,
                FilterContains,
                FilterNotContains,
                FilterIn,
            ],
        ),
        (
            "is_json",
            [
                FilterEqual,
                FilterNotEqual,
                FilterStartsWith,
                FilterNotStartsWith,
                FilterEndsWith,
                FilterNotEndsWith,
                FilterContains,
                FilterNotContains,
                FilterIn,
            ],
        ),
        (
            "is_integer",
            [
                FilterEqual,
                FilterNotEqual,
                FilterGreater,
                FilterSmaller,
                FilterGreaterEqual,
                FilterSmallerEqual,
                FilterIn,
            ],
        ),
        (
            "is_float",
            [
                FilterEqual,
                FilterNotEqual,
                FilterGreater,
                FilterSmaller,
                FilterGreaterEqual,
                FilterSmallerEqual,
                FilterIn,
            ],
        ),
        (
            "is_numeric",
            [
                FilterEqual,
                FilterNotEqual,
                FilterGreater,
                FilterSmaller,
                FilterGreaterEqual,
                FilterSmallerEqual,
                FilterIn,
            ],
        ),
        (
            "is_date",
            [
                DateFilterEqual,
                DateFilterNotEqual,
                DateFilterGreater,
                DateFilterSmaller,
                DateFilterGreaterEqual,
                DateFilterSmallerEqual,
                DateFilterIn,
            ],
        ),
        (
            "is_datetime",
            [
                DateTimeFilterEqual,
                DateTimeFilterNotEqual,
                DateTimeFilterGreater,
                DateTimeFilterSmaller,
                DateTimeFilterGreaterEqual,
                DateTimeFilterSmallerEqual,
                DateTimeFilterIn,
            ],
        ),
    )
