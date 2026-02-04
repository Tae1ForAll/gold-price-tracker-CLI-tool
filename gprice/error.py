# custom errors
class APIRequestError(Exception): 
    def __init__(self, message = "[ERR] "):
        super().__init__(message)
    pass

    
class SchedulerError(Exception): 
    def __init__(self, message = "Schedule cannot start, Please enter (-eve -h) to learn how to use"):
        super().__init__(message)
        
class CredentialInvalid(Exception):
    def __init__(self, message):
        super().__init__(message)
# =======================================