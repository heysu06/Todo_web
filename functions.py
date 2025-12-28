FILEPATH = 'user_tasks.txt'

def read_user_tasks(filepath=FILEPATH):
        """ Opens a text file on read mode and returns it's contents as a list."""
        with open(filepath , 'r') as file:
            user_tasks = file.readlines()
        return user_tasks    


def write_user_tasks( user_task_arg , filepath=FILEPATH):
        """ Writes the To-do items as a list inside of the text file."""
        with open(filepath , 'w') as file:
            file.writelines(user_task_arg)\
            



if __name__ == "__main__":
      print(read_user_tasks())