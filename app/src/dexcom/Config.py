"""Class that encapsulates config data for the application. Based on the GarminDb config file structure by Tom Goetz."""

class Config():
    """Class that encapsulates config data for the dexcom."""

    db = {
        'type'                  : 'sqlite'
    }

    directories = {
        'relative_to_home'      : True,
        'config_dir'            : '.GarminDb',
        'base_dir'              : 'HealthData',
        'backup_dir'            : 'Backups',
        'plugins_dir'           : "Plugins",
        'fit_file_dir'          : 'FitFiles',
        'fitbit_file_dir'       : 'FitBitFiles',
        'mshealth_file_dir'     : 'MSHealth',
        'db_dir'                : 'DBs',
        'backup_dir'            : 'Backups',
        'sleep_files_dir'       : 'Sleep',
        'activities_file_dir'   : 'Activities',
        'monitoring_file_dir'   : 'Monitoring',
        'weight_files_dir'      : 'Weight',
        'rhr_files_dir'         : 'RHR'
    }

    config = {
        'metric'                : False
    }

    device_directories = {
        'base'                  : 'garmin',
        'activities'            : 'activity',
        'monitoring'            : 'monitor',
        'sleep'                 : 'sleep',
        'settings'              : 'settings'
    }

    graphs = {
        'size'                  : [16.0, 12.0],
        'steps'                 : {'period' : 'weeks', 'days' : 730},
        'hr'                    : {'period' : 'weeks', 'days' : 730},
        'itime'                 : {'period' : 'weeks', 'days' : 730},
        'weight'                : {'period' : 'weeks', 'days' : 730}
    }

    checkup = {
        'look_back_days'        : 90
    }