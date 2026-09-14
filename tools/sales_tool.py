def get_sales_data(sku: str) -> dict:
    """
    Retrieve actual sales information for a SKU.
    """

    print(
        f">>> SALES TOOL CALLED: {sku}",
        flush=True
    )

    fake_data = {
        "SKU123": {
            "sku": "SKU123",
            "actual_sales": 125000,
            "previous_sales": 110000,
            "units": 1000
        }
    }

    result = fake_data.get(sku.upper())

    if result is None:
        return {
            "status": "not_found",
            "domain": "sales",
            "sku": sku
        }

    return {
        "status": "success",
        "domain": "sales",
        "data": result
    }