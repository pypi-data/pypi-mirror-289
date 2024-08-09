# config_manager.py
from tinydb import TinyDB, Query
from typing import Dict, Any

class ConfigManager:
    def __init__(self, db_path: str = 'settings.json'):
        self.db = TinyDB(db_path)

    def add_item(self, table: str, item: Dict[str, Any]):
        table_instance = self.db.table(table)
        table_instance.insert(item)

    def update_item(self, table: str, item_id: str, updated_item: Dict[str, Any]):
        table_instance = self.db.table(table)
        Item = Query()
        table_instance.update(updated_item, Item.id == item_id)

    def get_item(self, table: str, item_id: str) -> Dict[str, Any]:
        table_instance = self.db.table(table)
        Item = Query()
        return table_instance.get(Item.id == item_id)

    def get_all_items(self, table: str) -> list:
        table_instance = self.db.table(table)
        return table_instance.all()

# Utilizzo
config_manager = ConfigManager()
