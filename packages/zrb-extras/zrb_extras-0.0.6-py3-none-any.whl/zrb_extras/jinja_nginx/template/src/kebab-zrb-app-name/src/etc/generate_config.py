import jinja2
import os

_CURRENT_DIR = os.path.dirname(__file__)

with open(os.path.join(_CURRENT_DIR, "start.d", 'default.conf'), 'r') as template_file:
    CONFIG_STR = template_file.read()

environment = jinja2.Environment()
template = environment.from_string(CONFIG_STR)
config = template.render(os=os)

with open('/etc/nginx/conf.d/default.conf', 'w') as config_file:
    config_file.write(config)
