import datetime

class TimeKeeper:
    def __init__(self, current_time):
        self.current_time = current_time
        self.time_last_watered = None
    
    def set_current_time(self, updated_time):
        self.current_time = updated_time

    def set_time_last_watered(self, updated_time):
        self.time_last_watered = updated_time

    @staticmethod
    def get_current_time():
        now = datetime.datetime.now()
        return now.strftime("%I:%M:%S %p")