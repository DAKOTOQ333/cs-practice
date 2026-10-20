"""Функции для обработки путей и размеров файлов."""


def count_by_extension(paths: list[str]) -> dict[str, int]:
    """Подсчитать расширения по последней точке в имени файла."""
    counts = {}
    for path in paths:
        filename = path.rsplit("/", 1)[-1]
        extension = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
        counts[extension] = counts.get(extension, 0) + 1
    return counts


def deepest_path(paths: list[str]) -> str:
    """Выбрать самый вложенный путь, при равенстве — по алфавиту."""
    return min(paths, key=lambda path: (-path.count("/"), path), default="")


def human_size(n_bytes: int) -> str:
    """Перевести размер в Б, КБ, МБ, ГБ или ТБ."""
    units = ("Б", "КБ", "МБ", "ГБ", "ТБ")
    size = n_bytes
    unit_index = 0
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1
    if unit_index == 0:
        return f"{n_bytes} Б"
    return f"{size:.1f} {units[unit_index]}"
