from .uuid_fetcher import UUIDFetcher

def print_uuids(username, online_uuid, offline_uuid):
    print(f'Username: {username}')
    print(f'Premium UUID: {online_uuid or "None"}')
    print(f'Cracked/Offline UUID: {offline_uuid}')

def get_uuid_from_user():
    return input("Enter Minecraft username: ").strip()

def uuid_command(username):
    try:
        online_uuid, offline_uuid = UUIDFetcher.get_player_uuid(username)
        print_uuids(username, online_uuid, offline_uuid)
    except KeyboardInterrupt:
        print('\nOperation interrupted.')
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    username = get_uuid_from_user()
    uuid_command(username)
