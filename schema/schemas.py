def individual_serial(country) -> dict:
    return {
        "id": str(country["_id"]),
        "name": country["name"],
        "population": country["population"],
    }

def list_serial(countries) -> list:
    return [individual_serial(country) for country in countries]

