import os


from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

# Config values will be given from environment variables and/or "default_settings" file.
# Also note that if we dont provide configuration file, the defaults act as development environment.
config = Config(os.path.abspath(os.path.join(os.path.dirname(__file__), 'default_settings')))

# for all other settings we first try to fetch them from etcd server. If not found/available
# we get them from project lvl environment variables.
clani = config('clani', cast=CommaSeparatedStrings, default=[])
github = config('github', cast=CommaSeparatedStrings, default=[])
travis = config('travis', cast=CommaSeparatedStrings, default=[])
dockerhub = config('dockerhub', cast=CommaSeparatedStrings, default=[])
opis_projekta = config('opis_projekta', cast=str, default="")
mikrostoritve = config('mikrostoritve', cast=CommaSeparatedStrings, default=[])
