class APIRequestError(Exception): 
    def __init__(self, message = ""):
        super().__init__(message)
    
class SchedulerError(Exception): 
    def __init__(self, message = "Schedule cannot start, Please enter (-eve -h) to learn how to use"):
        super().__init__(message)
        
class CredentialInvalid(Exception):
    def __init__(self, message):
        super().__init__(message)