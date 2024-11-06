class Project:
    def __init__(self, name, description, authors, license, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.authors = authors
        self.license = license
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_list(self, l):
        if len(l) < 1:
            return "-"
        s = ""
        for item in l:
            s += f"\n- {item}"
        return s

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n\nAuthors: {self._stringify_list(self.authors)}"
            f"\n\nDependencies: {self._stringify_list(self.dependencies)}"
            f"\n\nDevelopment dependencies: {self._stringify_list(self.dev_dependencies)}"
        )
