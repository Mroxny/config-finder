import os
import configFinder
import argparse


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

    finder = configFinder.ConfigFinder()
    logger = finder.log

    #Check for basic errors 
    if exclude is not None and include is not None:
        print("You can't include and exclude files at the same time")
        exit(1)
    elif exclude is not None:
        finder.add_files_to_exclude(exclude)
    elif include is not None:
        finder.add_files_to_include(include)
        
    paths = []       
    if home_env is None or home_env == "":
        logger.add_to_log(f"Enviroment variable '{args.env}' is unknown", verbose=True)
        exit(1)

    else:
        paths = home_env.split(':')
        
    if len(paths) <= 1:
        logger.add_to_log("Not enough paths found", verbose=True)
        exit(1)

    for i in paths:
        finder.add_config_path(i)

    res = finder.find_unique_config_files()

    res_string = "Final result before formatting:\n"
    for key, val in res.items():
        res_string += f'{key}: {val}\n'
    logger.add_to_log(res_string)
    
    print([x for x in res.values()])



if __name__ == "__main__":
    run()

