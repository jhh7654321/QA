
class Config:
    def __init__(self, env):

        # Browserstack or local
        SUPPORTED_BROWSER_LOCATIONS = ['local','bs']

        #if browserlocation.lower() not in SUPPORTED_BROWSER_LOCATIONS:
        #    raise Exception(f'{browserlocation} is not a supported browser location (Supported locations: {SUPPORTED_BROWSER_LOCATIONS})')
        #self.browserlocation = browserlocation

        # Test env, dev, prod, stage...
        SUPPORTED_ENVS = ['dev', 'prod', 'stage']

        if env.lower() not in SUPPORTED_ENVS:
            raise Exception(f'{env} is not a supported environment (Supported envs: {SUPPORTED_ENVS})')

        self.env = env

        self.base_url_gundrywellness = {
            'dev': 'https://dev.gundrywellness.com',
            'stage': 'https://staging.gundrywellness.com',
            'prod': 'https://gundrywellness.com'
        }[env]

        self.base_url_onetwocosmetics = {
            'dev': 'http://dev.onetwocosmetics.com',
            'stage': 'http://staging.onetwocosmetics.com',
            'prod': 'https://onetwocosmetics.com'
        }[env]

        self.base_url_brandx = {
            'dev': 'http://brandx-develop.goldenhippo.com',
            'stage': 'http://brandx-develop.goldenhippo.com',
            'prod': 'https://brandx.goldenhippo.com'
        }[env]

        self.base_url_nucific = {
            'dev': 'https://staging.nucific.com',
            'stage': 'https://staging.nucific.com',
            'prod': 'https://nucific.com'
        }[env]

        self.base_url_gundrymd = {
            'dev': 'https://staging.gundrymd.com',
            'stage': 'https://staging.gundrymd.com',
            'prod': 'https://gundrymd.com'
        }[env]