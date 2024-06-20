from dateutil import parser
from dateutil.relativedelta import relativedelta
import json
from database import get_values_in_time_interval


def get_aggregated_salary_data(dt_from: str, dt_upto: str, group_type: str) -> str:
    """Serializes formed dictionary into json format"""
    dt_from = parser.parse(dt_from)
    dt_upto = parser.parse(dt_upto)
    
    aggregated_info = _get_formatted_dataset(dt_from, dt_upto, group_type)

    return json.dumps(aggregated_info)


def _get_formatted_dataset(dt_from: str, dt_upto: str, group_type: str) -> dict:
    """Formats the created dictionary for output"""
    data = list(get_values_in_time_interval(dt_from, dt_upto))

    interval_delta = _set_interval_data(group_type)

    aggregated_data = _calculate_aggregated_data(dt_from, dt_upto, interval_delta, data)

    dataset = list(aggregated_data.values())
    labels = [str(dt) for dt in aggregated_data.keys()]

    return {"dataset": dataset, "labels": labels}


def _set_interval_data(group_type):
    """Sets the time interval for formatting output"""
    interval_delta = None

    if group_type == "hour":
        interval_delta = relativedelta(hours=+1)
    elif group_type == "day":
        interval_delta = relativedelta(days=+1)
    elif group_type == "month":
        interval_delta = relativedelta(months=+1)
    else:
        raise ValueError("Unsupported group_type")
    
    return interval_delta


def _calculate_aggregated_data(dt_from: str, dt_upto: str, interval_delta, data: list) -> dict:
    """Creates a dictionary of aggregated data received from the database"""
    current_date = dt_from
    aggregated_data = {}

    while current_date <= dt_upto:
        next_interval_end = current_date + interval_delta
        sum_salary = 0
        for entry in data:
            if current_date <= entry['dt'] < next_interval_end:
                sum_salary += entry['value']

        aggregated_data[current_date.isoformat()] = sum_salary
        
        current_date = next_interval_end

    return aggregated_data
