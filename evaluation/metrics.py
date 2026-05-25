import time

class MetricsTracker:

    def __init__(self):

        self.total_requests = 0
        self.successful_requests = 0
        self.failed_requests = 0

        self.total_latency = 0

        self.repair_count = 0

        self.failure_types = []

    def start_timer(self):

        return time.time()

    def end_timer(self, start_time):

        latency = time.time() - start_time

        self.total_latency += latency

        return latency

    def record_success(self):

        self.total_requests += 1
        self.successful_requests += 1

    def record_failure(self, error):

        self.total_requests += 1
        self.failed_requests += 1

        self.failure_types.append(str(error))

    def record_repair(self):

        self.repair_count += 1

    def get_metrics(self):

        avg_latency = 0

        if self.total_requests > 0:

            avg_latency = (
                self.total_latency /
                self.total_requests
            )

        success_rate = 0

        if self.total_requests > 0:

            success_rate = (
                self.successful_requests /
                self.total_requests
            ) * 100

        return {

            "total_requests": self.total_requests,

            "successful_requests":
                self.successful_requests,

            "failed_requests":
                self.failed_requests,

            "success_rate":
                round(success_rate, 2),

            "average_latency":
                round(avg_latency, 2),

            "repair_count":
                self.repair_count,

            "failure_types":
                self.failure_types
        }