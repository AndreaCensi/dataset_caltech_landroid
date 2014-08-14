

def jobs_comptests(context):
    from conf_tools import GlobalConfig
    GlobalConfig.global_load_dirs(['dataset_caltech_landroid.configs'])

    # Our tests are its tests with our configuration
    from rawlogs import jobs_comptests
    jobs_comptests(context)
