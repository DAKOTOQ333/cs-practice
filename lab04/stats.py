def _means(records: list[dict]) -> dict:
    totals = {}
    counts = {}

    for record in records:
        city = record["city"]
        totals[city] = totals.get(city, 0.0) + record["temp"]
        counts[city] = counts.get(city, 0) + 1

    return {
        city: totals[city] / counts[city]
        for city in totals
    }


def average_by_city(records: list[dict]) -> dict:
    return {
        city: round(mean, 1)
        for city, mean in _means(records).items()
    }


def warmest_city(records: list[dict]) -> str:
    means = _means(records)

    if not means:
        return ""

    return min(
        means,
        key=lambda city: (-means[city], city),
    )
def _means(records: list[dict]) -> dict:
    totals = {}
    counts = {}

    for record in records:
        city = record["city"]
        totals[city] = totals.get(city, 0.0) + record["temp"]
        counts[city] = counts.get(city, 0) + 1

    return {
        city: totals[city] / counts[city]
        for city in totals
    }


def average_by_city(records: list[dict]) -> dict:
    return {
        city: round(mean, 1)
        for city, mean in _means(records).items()
    }


def warmest_city(records: list[dict]) -> str:
    means = _means(records)

    if not means:
        return ""

    return min(
        means,
        key=lambda city: (-means[city], city),
    )
def read_valid(lines: list[str]) -> list[dict]:
    records = []

    for line in lines:
        if not line.strip():
            continue

        try:
            record = parse_record(line)
        except ValueError:
            continue

        records.append(record)

    return records