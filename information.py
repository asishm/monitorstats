import psutil

class InformationStatistics:

    def __init__(self):
        self.cpu_usage = psutil.cpu_percent()
        self.swap_mem_usage = psutil.swap_memory()[3]


    def get_cpu_usage(self):
        """ Get CPU utilization of the system """
        cpu_usage = psutil.cpu_percent(interval=None)
        return cpu_usage

    def get_swap_mem_usage(self):
        """ Get Swap mempry usage of the system"""
        swap_mem_usage = psutil.swap_memory()[3]
        return swap_mem_usage
