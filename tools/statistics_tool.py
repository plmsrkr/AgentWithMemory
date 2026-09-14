import statistics


def analyze_series(
    values: list[float],
    current_value: float
) -> dict:
    """
    Perform basic statistical analysis of a numeric series.

    Use when the user asks whether a value is unusual,
    anomalous, statistically different, or outside normal range.
    """

    print(
        ">>> STATISTICS TOOL CALLED",
        flush=True
    )

    if len(values) < 2:
        return {
            "status": "insufficient_data"
        }

    mean = statistics.mean(values)
    std_dev = statistics.stdev(values)

    if std_dev == 0:
        z_score = 0
    else:
        z_score = (current_value - mean) / std_dev

    return {
        "status": "success",
        "mean": mean,
        "std_dev": std_dev,
        "current_value": current_value,
        "z_score": z_score,
        "is_unusual": abs(z_score) >= 2
    }