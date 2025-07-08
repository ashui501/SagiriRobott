class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 21758143
    API_HASH = "154769775792944f6cd51a77b54c57a7"

    CASH_API_KEY = ""  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgresql://neondb_owner:npg_s9chAgJZRWp4@ep-damp-dew-a8fpypno-pooler.eastus2.azure.neon.tech/neondb?sslmode=require&channel_binding=require"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002655322719)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://tiwarireeta004:peqxLEd36RAg7ors@cluster0.furypd3.mongodb.net/?retryWrites=true&w=majority"  # Get this value from cloud.mongodb.com

    REDIS_URL = ""  #Get this value from redis.com

    # Telegraph link of the image which will be shown at start command.
    PHOTO = "https://te.legra.ph/file/31077a464a4ca165eb8bc.jpg"

    SUPPORT_CHAT = "ogapexmainchat"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "7770778661:AAGdLJtw3iBNsZILLWVk-WNkBN5bKKgcarA"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "hagT777"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 8176785590  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
