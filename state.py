class state:
    # Here will be the instance stored.
    __instance = None
    state = False
    status = False
    silence = 0
    name = ""
    @staticmethod
    def getInstance():
        """ Static access method. """
        if state.__instance == None:
            state()

        return state.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if state.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            state.__instance = self