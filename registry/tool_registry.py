from ..tools.margin_tool import get_margin_data
from ..tools.sales_tool import get_sales_data
from ..tools.forecast_tool import get_forecast_data
from ..tools.statistics_tool import analyze_series
from ..tools.web_tool import search_external_context
from ..tools.skill_tool import load_skill_instruction

TOOL_REGISTRY = {
    "margin_data": get_margin_data,
    "sales_data": get_sales_data,
    "forecast_data": get_forecast_data,
    "statistics": analyze_series,
    "web_search": search_external_context,
    "skill_loader": load_skill_instruction,
}


def get_tools(tool_names: list[str]):
    return [
        TOOL_REGISTRY[name]
        for name in tool_names
    ]