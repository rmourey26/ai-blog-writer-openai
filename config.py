##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "7ghd7fls03kdnvud3jhgndolpdd4fdsghyu00p"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
