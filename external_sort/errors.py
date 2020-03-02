class LaunchParametersError(Exception):
    def __init__(self):
        self.txt = "You have entered unsupported quantities of parameters. Expected 3."


class MemoryStarvationError(Exception):
    def __init__(self):
        self.txt = "Not enough memory to process the string"

