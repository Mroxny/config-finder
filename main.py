import sys
import os
import configFinder


def run():
    finder = configFinder.ConfigFinder()
    logger = finder.log
    home_env = ""
    paths = []

    #Handle arguments
    for i in range(len(sys.argv)):

        if sys.argv[i] == '-v':
            logger.verbose_mode = True
            logger.add_to_log("Program started with verbose mode")
        
        elif sys.argv[i] == '-e' or sys.argv[i] == '--env':
            env_name = sys.argv[i+1]
            logger.add_to_log(f"Set main enviroment variable: {env_name}")

            home_env = os.getenv(env_name)

        elif sys.argv[i] == '-E' or sys.argv[i] == '--Exclude':
            if len(finder.include) > 0 :
                logger.add_to_log("You cannot exclude files when includding", verbose=True)
                return
            
            file_to_exclude = sys.argv[i+1] 
            finder.add_files_to_exclude(file_to_exclude)


        elif sys.argv[i] == '-I' or sys.argv[i] == '--Include':
            if len(finder.exclude) > 0 :
                logger.add_to_log("You cannot include files when excludding", verbose=True)
                return
            
            file_to_include = sys.argv[i+1]
            finder.add_files_to_include(file_to_include)



    #Check for basic errors        
    if home_env is None or home_env == "":
        logger.add_to_log("Enviroment variable unknown", verbose=True)
        return
    else:
        paths = home_env.split(':')
        
    if len(paths) <= 1:
        logger.add_to_log("Not enough paths found", verbose=True)
        return            

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

