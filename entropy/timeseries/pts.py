import readdata

class Pts(object):
    """
    A Class that will holds the physiological/hormone time series data points. The data held 
    are: subject number, day number, time, the mean physiological concentration, variance model
    """
    def __init__(self, subject=None, day=None, time=None, mpc=None, sem=None,
                  replicates=None):
        self.subject = subject 
        self.day = day
        self.mpc = mpc
        self.sem = sem
        self.time= time
        self.replicates = replicates

