doc = {
    '$mul': {'radius': 1.60934}
}


def updater(coll):
    result = coll.update_many({}, doc)
    return result