# services/example_service.py

def get_all_items(data_store):
    return data_store

def create_new_item(data_store, name, description):
    new_id = max(data_store.keys()) + 1 if data_store else 1
    data_store[new_id] = {'name': name, 'description': description}
    return new_id

def update_item(data_store, item_id, name, description):
    if item_id not in data_store:
        return False
    data_store[item_id] = {'name': name, 'description': description}
    return True

def delete_item(data_store, item_id):
    if item_id not in data_store:
        return False
    del data_store[item_id]
    return True
