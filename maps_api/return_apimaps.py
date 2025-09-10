import pandas as pd

def extract_data(data):
    routes_info = []
    for route in data.get('routes', []):
        for leg in route.get('legs', []):
            routes_info.append({
                'start_address': leg['start_address'],
                'end_address': leg['end_address'],
                'duration_text': leg['duration']['text'],
                'duration_value': leg['duration']['value'],
                'distance_text': leg['distance']['text'],
                'distance_value': leg['distance']['value'],
            })

    df_routes = pd.DataFrame(routes_info)

    return df_routes