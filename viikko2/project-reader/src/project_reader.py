from urllib import request

import toml
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # print(content)

        spec = toml.loads(content)
        # print(spec)

        name = spec["tool"]["poetry"]["name"]
        desc = spec["tool"]["poetry"]["description"]
        license = spec["tool"]["poetry"]["license"]
        authors = spec["tool"]["poetry"]["authors"]
        dependencies = [name for name in spec["tool"]["poetry"]["dependencies"]]
        dev_dependencies = [name for name in spec["tool"]["poetry"]["group"]["dev"]["dependencies"]]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, authors, license, dependencies, dev_dependencies)
