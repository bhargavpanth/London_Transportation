from configparser import ConfigParser

config = ConfigParser()

config['settings'] = {
    'debug': 'true'
}

# Add config settings for Cassandra

# Add config settings for Kafka

with open('./config.ini', 'w') as f:
    config.write(f)