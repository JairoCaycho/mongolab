from connector import lab_client, collection_planets, collection_comets
from retriver import selector
from inserter import writer


def run():
    selector_result = selector(collection_planets)
    writer_result = writer(collection_comets)
    for _ in selector_result:
        print(_)
    print(writer_result.inserted_ids)
    lab_client.close()