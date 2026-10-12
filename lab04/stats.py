def parse_record(line):
    fields = line.split(";")

    if len(fields) != 3:
        raise ValueError("Должно быть ровно три поля")

    city = fields[0].strip()
    temp = fields[1].strip()
    date = fields[2].strip()

    if not city:
        raise ValueError("Город не должен быть пустым")

    if not date:
        raise ValueError("Дата не должна быть пустой")

    try:
        temperature = float(temp.replace(",", "."))
    except ValueError:
        raise ValueError("Температура должна быть числом")

    return {
        "city": city,
        "temperature": temperature,
        "date": date,
    }
def _means(records: list[dict]) -> dict:
    totals = {}
    counts = {}

    for record in records:
        city = record["city"]
        totals[city] = totals.get(city, 0.0) + record["temperature"]
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