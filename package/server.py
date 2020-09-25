from package.utils import get_project_root
import os


class Token:
    def __init__(self):
        self.access = ""
        self.refresh = ""

    def print(self):
        print("access token : '" + self.access + "'")
        print("refresh token : '" + self.refresh + "'")

    def write(self):
        conf_path = str(get_project_root()) + "/conf"
        if not os.path.isdir(conf_path):
            os.mkdir(conf_path)
        f = open(conf_path + "/tokens.txt", "w")
        f.write(str(self.access) + '\n')
        f.write(str(self.refresh) + '\n')
        f.close()


class Server:
    def __init__(self):
        self.url = "https://energyprotector.run.goorm.io"
        self.token = Token()

    def print(self):
        print("URL : '" + self.url + "'")
        self.token.print()


if __name__ == "__main__":
    server = Server()
    server.print()
