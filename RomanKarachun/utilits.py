class Colors:
    """"Adding possible colors"""
    def __init__(self, is_color: bool = False):
        if is_color:
            self.red = '\033[31m'
        else:
            self.red = ''
class ExceptionNotFoudNewsDate(Exception):
    """Exception for local storage"""
    pass
class ExceptionFormatDate(Exception):
    """Exception in Format Date"""
    pass