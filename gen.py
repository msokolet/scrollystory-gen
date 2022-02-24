# import modules
from jinja2 import Environment, FileSystemLoader
import os
import json

# load options
root = os.path.dirname(os.path.abspath(__file__))
opts_fname = os.path.join(root, 'opts.json')
f = open(opts_fname)
opts = json.load(f)

# load template
templates_dir = os.path.join(root, 'templates')
env = Environment( loader = FileSystemLoader(templates_dir) )
template = env.get_template(f'{opts["template"]}.html')

# generate html folder if it doesn't exist
html_dir = os.path.join(root, 'html')
if not os.path.exists(html_dir): os.makedirs(html_dir)

# generate html page
filename = os.path.join(html_dir, f'{opts["page_name"]}.html')
with open(filename, 'w') as fh:
    fh.write(template.render(
        page_title = opts['page_title'],
        page_desc = opts['page_desc'],
        steps = opts['steps']
    ))