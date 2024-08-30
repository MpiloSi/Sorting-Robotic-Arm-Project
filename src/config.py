import json
import os

# Load configuration from config.json
def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path) as config_file:
        return json.load(config_file)

# Load color ranges and shape templates
config = load_config()
COLOR_RANGES = config['color_ranges']
SHAPE_TEMPLATES = config['shape_templates']