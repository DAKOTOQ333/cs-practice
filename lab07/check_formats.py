"""Запуск локальных проверок: python3 lab07/check_formats.py."""

from copy import deepcopy
from formats import csv_to_records, parse_settings, merge_by_key, records_to_json


def main():
    assert csv_to_records("id,город\n1,Азов\n2,Шахты\n") == [
        {"id": "1", "город": "Азов"}, {"id": "2", "город": "Шахты"}
    ]
    assert csv_to_records("город, цена \n Азов , 100 \n") == [{"город": "Азов", "цена": "100"}]
    assert csv_to_records("") == []
    assert csv_to_records(" \n\t\n") == []
    assert csv_to_records("id,name\n") == []
    assert csv_to_records("id,value\r\n001,\r\n\r\n") == [{"id": "001", "value": ""}]
    assert parse_settings(["title: Отчёт за март", "decimals: 1", "active: true",
                           "columns:", "  - город", "  - цена"]) == {
        "title": "Отчёт за март", "decimals": 1, "active": True, "columns": ["город", "цена"]
    }
    assert parse_settings(["# только комментарий", " ", "name: Азов # город"]) == {"name": "Азов"}
    assert parse_settings(["rate: 3,5 # с запятой", "enabled: yes", "disabled: no"]) == {
        "rate": 3.5, "enabled": True, "disabled": False
    }
    assert parse_settings([]) == {}
    assert parse_settings(["a: -12", "b: 3.5", "c: false", "d: текст"]) == {
        "a": -12, "b": 3.5, "c": False, "d": "текст"
    }
    assert parse_settings(["values:", " - 12", " - 3,5", " - yes", " - no", " - город"]) == {
        "values": [12, 3.5, True, False, "город"]
    }
    assert parse_settings(["empty:", "title: Отчёт", "url: https://example.org"]) == {
        "empty": [], "title": "Отчёт", "url": "https://example.org"
    }
    assert parse_settings(["a:", " - один", "", "# комментарий", " - два", "b:", " - три"]) == {
        "a": ["один", "два"], "b": ["три"]
    }
    rows = [{"id": "1", "город": "Азов", "регион": "свой"}, {"id": "9"}]
    extra = {"1": {"регион": "из справочника", "страна": "Россия"}}
    before = deepcopy((rows, extra))
    merged = merge_by_key(rows, extra)
    assert merged == [{"id": "1", "город": "Азов", "регион": "свой", "страна": "Россия"}, {"id": "9"}]
    assert (rows, extra) == before
    assert merged[0] is not rows[0] and merged[1] is not rows[1]
    assert merge_by_key([{"code": "A"}], {"A": {"name": "Азов"}}, "code") == [{"code": "A", "name": "Азов"}]
    assert merge_by_key([], extra) == []
    assert merge_by_key([{"город": "Азов"}], extra) == [{"город": "Азов"}]
    assert records_to_json([{"б": 2, "а": 1}]) == '[\n  {\n    "а": 1,\n    "б": 2\n  }\n]'
    assert records_to_json([]) == "[]"
    print("Все 22 проверки пройдены.")


if __name__ == "__main__":
    main()
