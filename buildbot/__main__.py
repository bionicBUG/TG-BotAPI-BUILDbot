from buildbot.mods import ALL_MODULES
 
for module_name in ALL_MODULES:
    imported_module = import_module("buildbot.mods." + module_name)
