import requests
import hashlib
import uuid

class UUIDFetcher:
    @staticmethod
    def get_player_uuid(username):
        online_uuid = UUIDFetcher.get_premium_uuid(username)
        offline_uuid = UUIDFetcher.offline_player_uuid(username)
        return online_uuid, offline_uuid

    @staticmethod
    def get_premium_uuid(username):
        try:
            response = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{username}')
            if response.status_code == 200:
                return response.json().get('id')
        except requests.RequestException:
            pass
        return None

    @staticmethod
    def offline_player_uuid(username):
        data = hashlib.md5(("OfflinePlayer:" + username).encode('utf-8')).digest()
        data = bytearray(data)
        data[6] = data[6] & 0x0f | 0x30
        data[8] = data[8] & 0x3f | 0x80
        return str(uuid.UUID(bytes=bytes(data)))

