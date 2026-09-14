def get_forecast_data(sku: str) -> dict:
    """
    Retrieve forecast information for a SKU.
    """

    print(
        f">>> FORECAST TOOL CALLED: {sku}",
        flush=True
    )

    fake_data = {
        "SKU123": {
            "sku": "SKU123",
            "forecast_sales": 115000
        }
    }

    result = fake_data.get(sku.upper())

    if result is None:
        return {
            "status": "not_found",
            "domain": "forecast",
            "sku": sku
        }

    return {
        "status": "success",
        "domain": "forecast",
        "data": result
    }