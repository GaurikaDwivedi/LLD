class StatsResponse:
    def __init__(self, avg_read_time, avg_write_time, usages):
        self.avg_read_time = avg_read_time
        self.avg_write_time = avg_write_time
        self.usages = usages