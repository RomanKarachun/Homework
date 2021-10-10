class File71:
    def __init__(self, file_name, method="r"):
        self.file_name = file_name
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        print("Exception")
        self.file_obj.close()
        return True
with File71("test71", "w") as op_file:
    op_file.write("Python has released version 3.10")
    
    
