"""Преобразование CSV, учебного YAML и JSON."""

import json


def csv_to_records(text: str) -> list[dict]:
    """Разобрать CSV без кавычек, убрав пробелы вокруг полей."""
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        return []
    headers = [field.strip() for field in lines[0].split(",")]
    return [
        dict(zip(headers, (field.strip() for field in line.split(","))))
        for line in lines[1:]
    ]


def _parse_value(value: str):
    """Преобразовать логическое или числовое значение, иначе оставить строку."""
    value = value.strip()
    if value.lower() in ("true", "yes"):
        return True
    if value.lower() in ("false", "no"):
        return False
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value.replace(",", "."))
    except ValueError:
        return value


def parse_settings(lines: list[str]) -> dict:
    """Разобрать плоские настройки с комментариями и списками."""
    settings = {}
    list_key = None
    for raw_line in lines:
        line = raw_line.split("#", 1)[0].strip()
        if not line:
            continue
        if line.startswith("- ") or line == "-":
            if list_key is not None:
                settings[list_key].append(_parse_value(line[1:]))
            continue
        if ":" not in line:
            continue
        key, value = (part.strip() for part in line.split(":", 1))
        if value:
            settings[key] = _parse_value(value)
            list_key = None
        else:
            settings[key] = []
            list_key = key
    return settings


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    """Дополнить копии записей справочником; поля записи имеют приоритет."""
    result = []
    for row in rows:
        addition = extra.get(row[key], {}) if key in row else {}
        result.append({**addition, **row})
    return result


def records_to_json(records: list[dict]) -> str:
    """Сериализовать записи с кириллицей, сортировкой ключей и отступами."""
    return json.dumps(records, ensure_ascii=False, sort_keys=True, indent=2)
