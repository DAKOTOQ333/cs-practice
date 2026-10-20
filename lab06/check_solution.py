"""Локальные проверки: python3 check_solution.py."""

from solution import count_by_extension, deepest_path, human_size


def main():
    paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]
    assert count_by_extension(paths) == {"pdf": 1, "txt": 1, "png": 1, "": 1}
    assert count_by_extension([]) == {}
    assert count_by_extension(["archive.tar.gz", ".gitignore", "PHOTO.JPG", "a.jpg"]) == {
        "gz": 1, "": 1, "jpg": 2
    }
    assert count_by_extension(["folder.v1/Makefile", "folder.txt/name."]) == {"": 2}
    assert count_by_extension([".gitignore", "config/.env", "..hidden"]) == {"": 3}
    assert count_by_extension([".config.JSON", "config/.env.local"]) == {"json": 1, "local": 1}
    assert deepest_path(paths) == "docs/img/logo.png"
    assert deepest_path(["x/y/z.txt", "a/b/c.txt"]) == "a/b/c.txt"
    assert deepest_path([]) == ""
    assert deepest_path(["z.txt", "a.txt"]) == "a.txt"
    assert deepest_path(["a/b/c.txt", "z.txt"]) == "a/b/c.txt"
    assert human_size(900) == "900 Б"
    assert human_size(1536) == "1.5 КБ"
    assert human_size(5 * 1024**2) == "5.0 МБ"
    assert human_size(0) == "0 Б"
    assert human_size(3 * 1024**3) == "3.0 ГБ"
    assert human_size(1023) == "1023 Б"
    assert human_size(1024) == "1.0 КБ"
    assert human_size(1024**2) == "1.0 МБ"
    assert human_size(1024**3) == "1.0 ГБ"
    assert human_size(1024**4) == "1.0 ТБ"
    assert human_size(1024**5) == "1024.0 ТБ"
    print("Все 22 проверки пройдены.")


if __name__ == "__main__":
    main()
