from connector import lab_client, collection_planets, collection_comets
from retriver import selector
from inserter import writer
from modifier import updater, eraser


def run():
    selector_result = selector(collection_planets)
    for _ in selector_result:
        print(_)
    writer_result = writer(collection_comets)
    print(writer_result.inserted_ids)
    updater_result = updater(collection_comets)
    print(updater_result.modified_count)
    eraser_result = eraser(collection_comets)
    print(eraser_result.deleted_count)
    lab_client.close()