class Config(object):
    """
    Common configurations
    """
    MYSQL_DATABASE_USER = 'root'
    # MYSQL_DATABASE_PASSWORD = 'Muff4hire'
    # MYSQL_DATABASE_DB = 'ux_db'
    # MYSQL_DATABASE_HOST = 'localhost'
    # Put any configurations here that are common across all environments


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    MYSQL_DATABASE_USER = 'root'
    # 'MYSQL_DATABASE_PASSWORD' = 'Muff4hire'
    # 'MYSQL_DATABASE_DB' = 'ux_db'
    # 'MYSQL_DATABASE_HOST' = 'localhost'


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False
    MYSQL_DATABASE_PASSWORD = 'Muff4hire'

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
