import os, datetime
class Cmd:
    def __init__(self):
        self.base = os.getcwd()

    os.chdir("/home/fazil/Desktop")
    core_dir = os.getcwd()



    def ls(self):
        for x in os.listdir(os.getcwd()):

            c_time = os.path.getctime(x)
            
            dt_c = datetime.datetime.fromtimestamp(c_time)
            print(f'''{x}                              Created on:{dt_c}''')

    def cd(self, newpath) -> str:
        this_path = f'{os.getcwd()}/{newpath}'
        os.chdir(this_path)
        return this_path


    def cd_go_back(self):
        os.chdir('..')



    def mkdir(self, name: str):
        directory = name
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, directory)
        try:
            if os.path.exists(name):
                os.mkdir(path)
                print(f"Directory with name {directory} already exists")
            else:
                os.mkdir(path)
                print("Directory '% s' created" % directory)
        except OSError as error:
            print(error)
            print(f"Directory {directory} can not be created" )



    def rmdir(self, name: str):
        directory = name
        parent = os.getcwd()
        path = os.path.join(parent, directory)
        try:
            os.rmdir(path)
            print(f"Directory {directory} has been removed successfully")
        except OSError as error:
            print(error)
            print(f"Directory {directory} can not be removed")

    def create_file(self, filename):  # touch
        if os.path.exists(filename):
            print(f"file with name {filename} already exists")
        else:
            parent_directory = self.base

            with open(os.path.join(parent_directory, filename), 'w') as file:
                scan = input("Do you want to write smthing in file  Y/N:" )
                if scan == "Y" or "y":
                    scan2 = input("Enter you text:")
                    file.write(scan2)
                else:
                    pass


    def open_file(self, filename):  #less
        if os.path.exists(filename):
            with open(f"{filename}") as file:
                print(file.read())

        else:
            print(f"file with name {filename} does not exist")

    @staticmethod
    def help_of():
        print("""
[cd] - To navigate through the Linux files and directories, use the cd command. Depending on your current working directory, it requires either the full path or the directory name.
Running this command without an option will take you to the home folder. Keep in mind that only users with sudo privileges can execute it.
Let’s say you’re in /home/username/Documents and want to go to Photos, a subdirectory of Documents. To do so, enter the following command:
cd Photos.
If you want to switch to a completely new directory, for example, /home/username/Movies, you have to enter cd followed by the directory’s absolute path:
cd /home/username/Movies
Here are some shortcuts to help you navigate:
cd ~[username] goes to another user’s home directory.
cd .. moves one directory up.

[ls] - The ls command lists files and directories within a system. Running it without a flag or parameter will show the current working directory’s content.
To see other directories’ content, type ls followed by the desired path. For example, to view files in the Documents folder, enter:
ls /home/username/Documents

[mkdir] - Use the mkdir command to create one or multiple directories at once and set permissions for each of them. The user executing this command must have the privilege to make a new folder in the parent directory, or they may receive a permission denied error.
Here’s the basic syntax:
mkdir [option] directory_name
For example, you want to create a directory called Music:
mkdir Music
To make a new directory called Songs inside Music, use this command:
mkdir Music/Songs

[rmdir] - To permanently delete an empty directory, use the rmdir command. Remember that the user running this command should have sudo privileges in the parent directory.
For example, you want to remove an empty subdirectory named personal1 and its main folder mydir:
rmdir -p mydir/personal1

[touch] - The touch command is a standard program for Unix/Linux operating systems, that is used to create, change and modify timestamps of a file

[less] - On Linux systems, less is a command that displays file contents or command output one page at a time in your terminal. 
less is most useful for viewing the content of large files or the results of commands that produce many lines of output. 
The content displayed by less can be navigated by entering keyboard shortcuts""")







