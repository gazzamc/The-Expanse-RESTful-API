"""
    Returns a hardcoded directory of API and filters.
"""

import json
from flask import request, current_app


def endpoint_dir():
    '''
    Returns API endpoints and filters in JSON object.

            Parameters:
                    None

            Returns:
                    JSON Object: JSON response
    '''
    response = {
        "base_url": request.base_url,
        "endpoints": [
            {
                "people": [
                    request.base_url + "/people",
                    request.base_url + "/people/{id}",
                    {
                        "filters": [
                            request.base_url + "/people?offset={offset}",
                            request.base_url + "/people?name={name}",
                            request.base_url + "/people?status={status}",
                            request.base_url + "/people?gender={gender}"
                        ]
                    }
                ],
                "systems":[
                    request.base_url + "/systems",
                    request.base_url + "/systems/{id}",
                    {
                        "filters": [
                            request.base_url + "/systems?offset={offset}",
                            request.base_url + "/systems?name={name}"
                        ]
                    }
                ],
                "locations":[
                    request.base_url + "/locations",
                    request.base_url + "/locations/{id}",
                    {
                        "filters": [
                            request.base_url + "/people?offset={offset}",
                            request.base_url + "/people?name={name}",
                            request.base_url + "/people?system={system}"
                        ]
                    }
                ]
            }
        ]
    }

    return current_app.response_class(
                json.dumps(
                    response,
                    indent=4,
                    sort_keys=False
                    ), mimetype="application/json")
