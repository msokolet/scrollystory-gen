# import modules
from jinja2 import Environment, FileSystemLoader
import sys
import os
import json

# extract subdirectory name
if len(sys.argv) < 2:
    print("Please specify the target subdirectory name.") 
    sys.exit()
else:
    folder = sys.argv[1]

# load options
root = os.path.dirname(os.path.abspath(__file__))
opts_fname = os.path.join(root, folder, 'opts.json')
try:
    f = open(opts_fname)
except OSError:
    print("Could not open/read file:", opts_fname)
    sys.exit()
opts = json.load(f)

# load template
templates_dir = os.path.join(root, 'templates')
env = Environment( loader = FileSystemLoader(templates_dir) )
template = env.get_template(f'{opts["template"]}.html')

# set html folder, or generate if it doesn't exit
html_dir = os.path.join(root, folder, 'html')
if not os.path.exists(html_dir): os.makedirs(html_dir)

# generate html page
filename = os.path.join(html_dir, f'{opts["page_name"]}.html')
with open(filename, 'w') as fh:
    fh.write(template.render(
        folder = folder,
        page_title = opts['page_title'],
        page_desc = opts['page_desc'],
        steps = opts['steps']
    ))