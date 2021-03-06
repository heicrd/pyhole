import yaml

class Config(object):
	def __init__(self, cdict):
		attrs = set(self.attrs) # copy and "unfreeze"
		for k, v in cdict.items():
			attrs.remove(k) # check if the key is allowed, mark it as present
			setattr(self, k, v)
		if len(attrs) != 0:
			raise KeyError('missing required bot config keys: %s' % attrs)

class WebConfig(Config):
	attrs = frozenset([
		'port',
		'websocket_host',
		'cookie_secret',
	])

class OAuthConfig(Config):
	attrs = frozenset([
		'client_id',
		'client_secret',
		'redirect_uri',
		'authorize_url',
		'access_token_url',
		'auth_user_url',
	])

__doc = yaml.load(open('config.yaml', 'r'))
web = WebConfig(__doc['web'])
oauth = OAuthConfig(__doc['oauth'])
