from google.cloud import bigquery


PROJECT_ID = "diabot-b617c"
DATASET_ID = "test"
TABLE_ID = "margin_data"


from decimal import Decimal

client = bigquery.Client(project=PROJECT_ID)

def json_safe(value):
    if isinstance(value, Decimal):
        return float(value)
    return value

def get_margin_data(sku: str) -> dict:
    """
    Fetch margin data for a SKU from BigQuery.

    Use this tool whenever the user asks for revenue, cost,
    margin, or margin percentage for a SKU.

    Args:
        sku: SKU identifier, for example "SKU123".

    Returns:
        A JSON-serializable dictionary containing margin data.
    """

    print(f">>> get_margin_data called for SKU: {sku}", flush=True)

    client = bigquery.Client(project=PROJECT_ID)

    query = f"""
        SELECT
            sku,
            revenue,
            cost,
            margin,
            margin_percent
        FROM `{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}`
        WHERE UPPER(sku) = UPPER(@sku)
    """

    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter(
                "sku",
                "STRING",
                sku
            )
        ]
    )

    query_job = client.query(
        query,
        job_config=job_config
    )

    results = query_job.result()

    rows = []

    for row in results:
        row_data = {
            "sku": row.sku,
            "revenue": float(row.revenue)
            if row.revenue is not None
            else None,
            "cost": float(row.cost)
            if row.cost is not None
            else None,
            "margin": float(row.margin)
            if row.margin is not None
            else None,
            "margin_percent": float(row.margin_percent)
            if row.margin_percent is not None
            else None,
        }

        rows.append(row_data)

    if not rows:
        response = {
            "status": "not_found",
            "sku": sku,
            "message": f"No margin data found for {sku}",
            "data": []
        }

        print(">>> TOOL RETURN:", response, flush=True)

        return response

    response = {
        "status": "success",
        "sku": sku,
        "row_count": len(rows),
        "data": rows
    }

    print(">>> TOOL RETURN:", response, flush=True)

    return response