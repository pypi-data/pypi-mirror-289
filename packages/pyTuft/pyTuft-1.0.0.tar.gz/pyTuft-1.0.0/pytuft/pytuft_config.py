import os

# Default configuration
BLOCKCHAIN_URL = 'http://eaies_net/'
DEPLOYER_ADDRESS = None

# Load user-specific configuration if it exists
user_config_path = os.path.join(os.path.dirname(__file__), 'pyTuft_user_config.py')
if os.path.exists(user_config_path):
    user_config = {}
    with open(user_config_path, 'r') as f:
        exec(f.read(), user_config)
    BLOCKCHAIN_URL = user_config.get('BLOCKCHAIN_URL', BLOCKCHAIN_URL)
    DEPLOYER_ADDRESS = user_config.get('DEPLOYER_ADDRESS', DEPLOYER_ADDRESS)

if not DEPLOYER_ADDRESS:
    raise ValueError("DEPLOYER_ADDRESS must be set in pyTuft_user_config.py or as an environment variable.")
