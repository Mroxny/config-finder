import configFinder

finder = configFinder.ConfigFinder()
finder.add_config_path('a')
finder.add_config_path('b')
finder.add_config_path('c')

finder.add_files_to_include('config')
finder.add_files_to_include('yml')

finder.log.verbose_mode=True


res = finder.find_unique_config_files()
print([x for x in res.values()])


