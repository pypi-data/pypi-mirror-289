from troveclient import utils

class Extension(utils.HookableMixin):
    def __init__(self, name: str, module: str) -> None: ...
