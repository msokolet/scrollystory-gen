## Scrollystory generator ##

This is a wrapper for the [scrollama](https://github.com/russellgoldenberg/scrollama) library, the purpose of which is to create scrollystories with minimal effort. No knowledge of JS/CSS needed!

Requires Python 3 and the modules in requirements.txt.
 
Instructions:

* Download this repository.
* Create a new folder within it for your scrollystory, e.g. **`my_scrolly`**.
* Create a new subfolder **`my_scrolly/images`**, where you will place your images.
* Copy **`opts.json`** into **`my_scrolly`**.
* Open **`my_scrolly/opts.json`**.
* Choose a template (there are four choices: side, title, overlay, and wipe).
* Set the name, title, and description of your scrollystory.
* Set the text of each step, and add/remove steps as you wish.
* For each step, also set the name of the associated image.
* In the repository folder, run **`python gen.py my_scrolly`**.
* Your scrollystory will be outputted in **`my_scrolly/html`**.

For simple examples of scrollystories based on each of the four templates (as well as their associated **`opts.json`** and images folder), see **`examples`**. For a full blown example of a scrollystory based on the side template, see **`examples/side-full`**.
