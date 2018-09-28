import sys
from api.docker_scheduler_api import DockerScheduler

def docker_scheduler_cli() :

    commands = ["list","create","run","help"]
    first_arg = get_argv(1)
    if first_arg not in commands:
        print("Incorrect Command, please try the 'help' command for assistance. Exiting")
        sys.exit()

    ds = DockerScheduler()
    if first_arg == "list" :
        list_commands = ["images", "containers"]
        second_arg = get_argv(2)
        if second_arg not in list_commands:
            print("Incorrect Command, please try the 'help' command for assistance. Exiting")
            sys.exit()
        if second_arg == "images" :
            print(ds.list_images())
        if second_arg == "containers" :
            print(ds.list_containers())

    if first_arg == "run":
        image = get_argv(2)
        command = get_argv(3)
        print(ds.run_container(image=image,command=command))

    if first_arg == "help":
       message = "Thank you for using docker_scheduler\n" \
                 "With this tool you can control docker containers\n" \
                 "Here is a list of available commands:\n" \
                 "=============================================\n" \
                 "list images - to list all the images available \n" \
                 "list containers - to list all the cointainers running \n" \
                 "run <image_type> <command> - to run an image with a specific command \n\n" \
                 "help - displays this output \n" \
                 "Example : \n" \
                 "python docker_scheduler_cli.py run 'ubuntu:latest' 'echo hello world'"

       print(message)



def get_argv(argv_index) :
    try :
        argv = sys.argv[argv_index]
    except Exception:
        print("Argument missing, please try the 'help' command for further assistance. Exiting")
        sys.exit()
    return argv

if __name__ == "__main__":
    docker_scheduler_cli()