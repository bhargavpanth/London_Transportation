from configparser import ConfigParser

config = ConfigParser()

config['settings'] = {
    'debug': 'true'
}

# Add config settings for Cassandra
config['cassandra'] = {
    'host': 'http://127.0.0.1',
    'port': 7000
}

# Add config settings for Kafka
config['kafka'] = {
    'host': 'http://127.0.0.1'
}

with open('./config.ini', 'w') as f:
    config.write(f)