"""Построчная обработка журнала сервиса."""

LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}


def parse_event(line: str) -> dict:
    """Разобрать строку или вызвать ValueError при неверном формате."""
    parts = line.strip().split(maxsplit=2)
    if len(parts) != 3 or parts[1] not in LEVELS:
        raise ValueError("Ожидается строка: время уровень сообщение")
    time, level, message = parts
    return {"time": time, "level": level, "message": message}


def count_levels(lines) -> dict:
    """Подсчитать уровни, пропуская пустые строки."""
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            level = parse_event(line)["level"]
        except ValueError:
            level = "BROKEN"
        counts[level] = counts.get(level, 0) + 1
    return counts


def top_errors(lines, n: int) -> list[list]:
    """Вернуть наиболее частые ошибки; при равенстве — по алфавиту."""
    if n <= 0:
        return []
    counts = {}
    for line in lines:
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] == "ERROR":
            message = event["message"]
            counts[message] = counts.get(message, 0) + 1
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return [[message, count] for message, count in ordered[:n]]


def format_report(counts: dict, errors: list[list]) -> str:
    """Сформировать отчёт с завершающим переводом строки."""
    lines = ["Отчёт по журналу", ""]
    for level in sorted(counts):
        lines.append(f"{level}: {counts[level]}")
    lines.extend(["", "Частые ошибки:"])
    for message, count in errors:
        lines.append(f"- {message} — {count}")
    return "\n".join(lines) + "\n"
