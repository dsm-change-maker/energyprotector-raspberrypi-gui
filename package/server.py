# -*- coding: utf-8 -*-

from package.utils import get_project_root
from package.database import DataBase


class Token:
    def __init__(self):
        self.access = ""
        self.refresh = ""

        self.db = DataBase(get_project_root() + '/conf/energy_protector')
        self.db.execute(
            'CREATE TABLE IF NOT EXISTS token (access TEXT, refresh TEXT)')

        count = self.db.execute('SELECT COUNT(*) FROM token')[0][0]
        if count is 0:
            self.db.execute(
                'INSERT INTO token(access, refresh) values (?, ?)',
                (self.access, self.refresh)
            )
        else:
            self.load()

    def print(self):
        print("access token : '" + self.access + "'")
        print("refresh token : '" + self.refresh + "'")

    def load(self, access=True, refresh=True):
        data = self.db.execute('SELECT * FROM token LIMIT 1')[0]
        if access:
            self.access = data[0]
        if refresh:
            self.refresh = data[1]

    def write(self):
        self.db.execute(
            'UPDATE token SET access = ?, refresh = ?',
            (self.access, self.refresh))


class Server:
    def __init__(self):
        self.url = "https://energyprotector.run.goorm.io"
        self.token = Token()

    def print(self):
        print("URL : '" + self.url + "'")
        self.token.print()


def get_token(server_objs, apis):
    server_objs.token.load()
    if len(server_objs.token.access) is 0:
        res = apis.raspberry.connect()
        if res[0]:
            server_objs.token.access = res[2]['access_token']
            server_objs.token.write()
            return True
        return None
    return False


if __name__ == "__main__":
    server = Server()
    server.print()
