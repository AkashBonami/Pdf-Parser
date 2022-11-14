import os
def name(loc):
    file = (os.path.basename(loc))
    file_name = os.path.splitext(file)[0]
    return(file_name)