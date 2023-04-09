from item import Item, Session, engine

local_session = Session(bind=engine)

def insert(name):
    temp = Item(item_name = name)
    local_session.add(temp)
    local_session.commit()

def change_status(id):
    item = local_session.query(Item).filter_by(id = id).first()
    item.is_finish = not item.is_finish
    local_session.commit()

def delete(id):
    local_session.query(Item).filter_by(id = id).delete()
    local_session.commit()

def list_items():
    items = local_session.query(Item)
    return items
