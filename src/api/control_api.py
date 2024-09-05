class ControlAPI:
    def __init__(self):
        self.is_sorting = False

    def start_sorting(self):
        self.is_sorting = True
        print("Sorting process started")

    def stop_sorting(self):
        self.is_sorting = False
        print("Sorting process stopped")