doc = {
    '$mul': {'radius': 1.60934}
}

doc_del = {
    "orbitalPeriod": {
        "$gt": 5,
        "$lt": 85
    }
}

def updater(coll):
    result = coll.update_many({}, doc)
    return result

def eraser(coll):
    result = coll.delete_many(doc_del)
    return result