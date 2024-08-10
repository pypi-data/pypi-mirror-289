from sqlitedict import SqliteDict
import os


class UserIdStorage:
    # Responsible for getting user id by messenger and uid
    def __init__(self, data_path:str = "data/"):
        self.users_count = 0
        self.messengers_stores = {}
        os.makedirs(f"{data_path}messengers_store", exist_ok=True)
        for storage_name in os.listdir(f"{data_path}messengers_store/"):
            messenger = storage_name.replace("_id_storage.db", "")
            self.messengers_stores[messenger] = SqliteDict(
                f"{data_path}messengers_store/{messenger}_id_storage.db", autocommit=True
            )
            self.users_count += self.messengers_stores[messenger].__len__()
        self.data_path = data_path

    def get_user_id(self, messenger_name: str, messenger_user_id):
        messenger_user_id = str(messenger_user_id)

        if messenger_name not in self.messengers_stores.keys():
            self.messengers_stores[messenger_name] = SqliteDict(
                f"{self.data_path}{messenger_name}_id_storage.db", autocommit=True
            )
            self.users_count += self.messengers_stores[messenger_name].__len__()

        if messenger_user_id not in list(self.messengers_stores[messenger_name].keys()):
            self.users_count += 1
            self.messengers_stores[messenger_name][messenger_user_id] = self.users_count
        return self.messengers_stores[messenger_name][messenger_user_id]

    def set_authorization(self, messenger_id, value: bool):
        # Need a suitable user database.
        return NotImplementedError

    # def _create_full_user_id_database(self):
    # self.users_storage = SqliteDict("user_id_storage.db", autocommit=True)
    #     for storage_name in self.messengers_stores.keys():
    #         for user in self.messengers_stores[storage_name].keys():
    #             self.users_storage[str(self.messengers_stores[storage_name][user])] = {
    #                 "messenger_name": storage_name,
    #                 "messenger_user_id": user,
    #             }
