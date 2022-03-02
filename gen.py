# import modules
from jinja2 import Environment, FileSystemLoader
from typing import List, Tuple
import sys
import os
import json

# get folder func
def get_folders(root: str, args: List[str]) -> Tuple[str, str]:

    if len(args) < 2:
        print("Please specify the target subdirectory name.") 
        sys.exit()
    else:
        folder = args[1]

    # set html folder, or generate if it doesn't exit
    html_dir = os.path.join(root, folder, 'html')
    if not os.path.exists(html_dir): os.makedirs(html_dir)

    return folder, html_dir

# load options func
def load_opts(root: str, folder: str) -> dict:

    root = os.path.dirname(os.path.abspath(__file__))
    opts_fname = os.path.join(root, folder, 'opts.json')
    try:
        with open(opts_fname) as opts_file:
            opts = json.load(opts_file)
    except OSError:
        print("Could not open/read JSON file:", opts_fname)
        sys.exit()
    except ValueError:
        print("JSON file incorrectly formatted:", opts_fname)
        sys.exit()

    return opts

# load template func
def load_template(root: str, template_name: str) -> object:

    templates_dir = os.path.join(root, 'templates')

    try: 
        env = Environment( loader = FileSystemLoader(templates_dir) )
        template = env.get_template(f'{template_name}.html')
    except:
        print("Could load template from dir:", templates_dir)
        sys.exit()

    return template

# generate html page func
def generate_html(html_dir: str, opts: dict):

    try:
      html_fname = os.path.join(html_dir, f'{opts["page_name"]}.html')
    except KeyError:
        print("Please specify page name in opts.")
        sys.exit()

    try:
        with open(html_fname, 'w') as html_file:
            html_file.write(template.render(
                folder = folder,
                page_title = opts['page_title'],
                page_desc = opts['page_desc'],
                steps = opts['steps']
            ))
    except OSError:
        print("Could not write to HTML file:", html_fname)
        sys.exit()
    except KeyError as error:
        print("Could not read from opts:", error)
        sys.exit()

root = os.path.dirname(os.path.abspath(__file__)) # get root folder
folder, html_dir = get_folders(root, sys.argv) # get subfolder name
opts = load_opts(root, folder) # load options
template = load_template(root, opts["template"]) # load template
generate_html(html_dir, opts) # generate html page