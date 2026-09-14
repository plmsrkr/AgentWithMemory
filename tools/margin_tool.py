def get_margin_data(
    sku: str,
    start_year: int | None = None,
    end_year: int | None = None,
) -> dict:
    """
    Mock margin data for a SKU across multiple fiscal years.

    Use this tool whenever revenue, cost, margin,
    margin percentage, or units are required.
    """

    print(
        f">>> MARGIN TOOL CALLED: sku={sku}, "
        f"start_year={start_year}, end_year={end_year}",
        flush=True,
    )

    mock_data = {
        "SKU123": [
            {
                "fiscal_year": 2025,
                "revenue": 120000.0,
                "cost": 84000.0,
                "margin": 36000.0,
                "margin_percent": 30.0,
                "units": 1100,
            },
            {
                "fiscal_year": 2026,
                "revenue": 125000.0,
                "cost": 90000.0,
                "margin": 35000.0,
                "margin_percent": 28.0,
                "units": 1000,
            },
        ],
        "SKU456": [
            {
                "fiscal_year": 2025,
                "revenue": 90000.0,
                "cost": 63000.0,
                "margin": 27000.0,
                "margin_percent": 30.0,
                "units": 800,
            },
            {
                "fiscal_year": 2026,
                "revenue": 82000.0,
                "cost": 64000.0,
                "margin": 18000.0,
                "margin_percent": 21.95,
                "units": 700,
            },
        ],
    }

    sku_key = sku.upper()

    if sku_key not in mock_data:
        return {
            "status": "not_found",
            "sku": sku,
            "data": [],
        }

    rows = mock_data[sku_key]

    if start_year is not None:
        rows = [
            row for row in rows
            if row["fiscal_year"] >= start_year
        ]

    if end_year is not None:
        rows = [
            row for row in rows
            if row["fiscal_year"] <= end_year
        ]

    response = {
        "status": "success",
        "domain": "margin",
        "sku": sku_key,
        "data": rows,
    }

    print(">>> MARGIN TOOL RETURN:", response, flush=True)

    return response


# from google.cloud import bigquery


# PROJECT_ID = ""
# DATASET_ID = ""
# TABLE_ID = ""

### bq way
# def get_margin_data(sku: str) -> dict:
#     """
#     Retrieve current margin data for a SKU.

#     Use when margin, cost, revenue or margin percentage
#     information is required.
#     """

#     print(
#         f">>> MARGIN TOOL CALLED: {sku}",
#         flush=True
#     )

#     client = bigquery.Client(project=PROJECT_ID)

#     query = f"""
#         SELECT
#             sku,
#             revenue,
#             cost,
#             margin,
#             margin_percent
#         FROM `{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}`
#         WHERE UPPER(sku) = UPPER(@sku)
#     """

#     job_config = bigquery.QueryJobConfig(
#         query_parameters=[
#             bigquery.ScalarQueryParameter(
#                 "sku",
#                 "STRING",
#                 sku
#             )
#         ]
#     )

#     results = client.query(
#         query,
#         job_config=job_config
#     ).result()

#     rows = []

#     for row in results:
#         rows.append({
#             "sku": row.sku,
#             "revenue": float(row.revenue)
#             if row.revenue is not None else None,

#             "cost": float(row.cost)
#             if row.cost is not None else None,

#             "margin": float(row.margin)
#             if row.margin is not None else None,

#             "margin_percent": float(row.margin_percent)
#             if row.margin_percent is not None else None,
#         })

#     if not rows:
#         return {
#             "status": "not_found",
#             "sku": sku,
#             "data": []
#         }

#     return {
#         "status": "success",
#         "domain": "margin",
#         "data": rows
#     }