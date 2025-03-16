class LinksList:
    def __init__(self):
        self.data = []

    def add(self, to_value, link_value):
        self.data.append({'name': to_value, 'url': link_value})

    def get_all(self):
        return self.data


    def get_to(self, index):
        return self.data[index]

    def print(self):
        for i in range(len(self.data)):
            row = self.data[i]
            print(f"{i}: {row['name']}")