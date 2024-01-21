class DictTransferrer:
    def __init__(self, dest, src):
        self.dist = dest
        self.src = src

    def transfer(self, *keys):
        if keys is None:
            raise ValueError(keys)
        for key in keys:
            self.dist[key] = self.src[key]
