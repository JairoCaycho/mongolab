def selector(coll):
    equal = coll.find
    (
        {
            "hasRings": False,
            "mainAtmosphere": "Ar"
        }
    )
    # implicit and for compound query
    # and is the default logical operator when there are more than one criteria
    implicit_and = coll.find
    (
        {
            "surfaceTemperatureC.mean": {"$lt": 15},
            "surfaceTemperatureC.min": {"$gt": -100}
        }
    )
    # the logical operator has to be explicit when more than one  criteria is applied on the same field
    explicit_and = coll.find
    (
        {
            "$and": [
                {"orderFromSun": {"$gt": 2}},
                {"orderFromSun": {"$lt": 5}}
            ]
        }
    )
    explicit_or = coll.find(
        {
            "$or": [
                {"orderFromSun": {"$gt": 7}},
                {"orderFromSun": {"$lt": 2}}
            ]
        }
    )
    return explicit_or