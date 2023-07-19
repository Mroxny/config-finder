import os
import configFinder
import argparse
import logger


def run():
    #Handle arguments
    parser = argparse.ArgumentParser(description='Find distinct config files')
    parser.add_argument('-e', dest='env', type=str, help='Add main enviroment variable (required)', required=True)
    parser.add_argument('-E', dest='exclude', action="append", type=str, help='Add files to exclude')
    parser.add_argument('-I', dest='include', action="append", type=str, help='Add files to include')
    parser.add_argument('-v', dest='verbose',action="store_true", help='Enable verbose mode')
    
    args = parser.parse_args()

    home_env = os.getenv(args.env)
    exclude = args.exclude
    include = args.include
    verbose_mode = args.verbose

    lc = logger.Logger(verbose= verbose_mode, file_name="config_finder.log")
    finder = configFinder.ConfigFinder(log_class=lc)
    log = lc.logger


    #Check for basic errors 
    if exclude is not None and include is not None:
        log.error("You can't include and exclude files at the same time")
        log.info("Program exited with status code 1")
        exit(1)
    elif exclude is not None:
        finder.add_files_to_exclude(exclude)
    elif include is not None:
        finder.add_files_to_include(include)
        
    paths = []       
    if home_env is None or home_env == "":
        log.error(f"Enviroment variable '{args.env}' is unknown")
        log.info("Program exited with status code 1")
        exit(1)

    else:
        paths = home_env.split(':')
        
    if len(paths) <= 1:
        log.error("Not enough paths found")
        log.info("Program exited with status code 1")
        exit(1)

    for i in paths:
        finder.add_config_path(i)

    res = finder.find_unique_config_files()

    res_string = "Final result before formatting:\n"
    for key, val in res.items():
        res_string += f'{key}: {val}\n'
    log.info(res_string)

    print([x for x in res.values()])
    exit(0)



if __name__ == "__main__":
    run()

