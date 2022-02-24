## Scrollystory generator ##

This is a wrapper for the [scrollama](https://github.com/russellgoldenberg/scrollama) library, the purpose of which is to create scrollystories with minimal effort. No knowledge of JS/CSS needed!

Requires Python 3 and the modules in requirements.txt.
 
Instructions:

* Upload your images of choice to the images folder.
* Open **`opts.json`**.
* Set the name, title, and description of your scrollystory.
* Set the text of each step, and add/remove steps as you wish.
* For each step, also set the name of the associated image.
* Run **`gen.py`**.
* Your scrollystory will be outputted in the html folder.

For a simple example of an **`opts.json`** file and associated images folder, as well as the output html file, see **`examples/simple`**. For a full blown example, see **`examples/full`**.