class state:
    # Here will be the instance stored.
    __instance = None
    state = False
    status = False
    silence = 0
    name = ""
    @staticmethod
    def getInstance():
        if state.__instance is None:
            state()

        return state.__instance

    def __init__(self):
        if state.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            state.__instance = self
