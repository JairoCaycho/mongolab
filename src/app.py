from connector import lab_client, coll
from retriver import selector


def run():
    selector_result = selector(coll)
    for _ in selector_result:
        print(_)
    lab_client.close()