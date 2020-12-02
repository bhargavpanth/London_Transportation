from configparser import ConfigParser

config = ConfigParser()

config['settings'] = {
    'debug': 'true'
}

# Add config settings for Cassandra