class state:
    # Here will be the status of recording stored.
    __instance = None
    state = False
    level = []
    recording_level = []
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
    def AddLevel(self, level):
        self.level.append(level)
        if len(self.level) > 50:
            self.level.remove(self.level[0])

    def AddrecordingLevel(self, level):
        self.recording_level.append(level)

    def GetRecordedLevel(self):
        import numpy as np
        if len(self.level) > 1:
            level = "{}dB".format(np.mean(self.recording_level))
            del self.recording_level[:]
            return level
        else:
            return "to few elemnts in table"

    def GetLevel(self):
        import numpy as np
        if len(self.level) > 1:
            return "{}dB".format(int(np.mean(self.level)))
        else:
            return "to few elemnts in table"
