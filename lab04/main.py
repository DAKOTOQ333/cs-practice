import sys

from stats import average_by_city, read_valid, warmest_city


def main() -> None:
    lines = sys.stdin.read().splitlines()

    records = read_valid(lines)

    nonempty_count = sum(
        1 for line in lines if line.strip()
    )
    skipped = nonempty_count - len(records)

    averages = average_by_city(records)
    city = warmest_city(records)

    print(len(records))
    print(skipped)

    if records:
        print(f"{averages[city]:.1f}")
    else:
        print("0.0")


if __name__ == "__main__":
    main()