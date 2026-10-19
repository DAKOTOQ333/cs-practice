"""Прочитать имя журнала, вывести статистику и сохранить отчёт."""

from pathlib import Path

from logstats import count_levels, format_report, top_errors


def main():
    filename = input().strip()
    with open(filename, encoding="utf-8") as log:
        counts = count_levels(log)

    # Второй проход позволяет не хранить все строки журнала в памяти.
    with open(filename, encoding="utf-8") as log:
        errors = top_errors(log, 3)

    print(sum(counts.values()))
    print(counts.get("ERROR", 0))
    print(counts.get("BROKEN", 0))

    report_path = Path(__file__).resolve().with_name("report.txt")
    with open(report_path, "w", encoding="utf-8") as report:
        report.write(format_report(counts, errors))


if __name__ == "__main__":
    main()
