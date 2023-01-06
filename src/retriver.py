def selector(collection):
    result = collection.find({"hasRings": False, "mainAtmosphere": "Ar"})
    return result