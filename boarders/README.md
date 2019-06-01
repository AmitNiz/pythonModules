## What is it Boarders :question::confused:
Boarders is a python module, created especially for designing CLI tools.

With Boarders you can easily create and modify unique text boxes, and improve your tool's UI experiene.


##  :package:How to install Boarders?
#### Download the module:
```
  git clone https://github.com/AmitNiz/pythonModules.git
```
#### Installation:
```
cd boarders/
```
- __Option 1__: Use the installation file (linux/mac):
```
./install.sh
```
- __Option 2__: Move Manually boarders.py to your favorite module folder.


##  :notebook_with_decorative_cover:How to use Boarders:
#### Importing Boarders:
```
import boarders
```
#### Creating a Simple text box:
```
box = boarders.createBox() # you can also set a fixed size box by using createBox(width=X,height=X)
box.append('This is Boarders!')
box.printBox()
```
Results:
```
*******************
*This is Boarders!*
*******************
```

#### Changing the style of the box:
Using ```box.style()```
you can change the horizontal/vertical symbols of the box,change the dimensions,
add padding and margin and allign the text.

For example, lets change the symbols,add some margin and padding, and allign the text to the center.
```
box.style(hSymbol ='%%',vSymbol ='-',hMargin = 3,hPadding = 35,allign ='center')
```
Results:
```
                                   ---------------------------
                                   %%   This is Boarders!   %%
                                   ---------------------------
```
__Style Options__:
- width - sets the width of the box.
- height - sets the height of the box.
- allign - alligns the text to the right,left or center.
- vMargin - sets a vertical margin.
- hMargin - sets an horizontal margin.
- vPadding - sets a vertical padding.
- hPadding - sets an horizontal padding.
- vSymbol - sets the vertical symbols of the box.
- hSymbol - sets the horizontal symbols of the box.

#### Editing the text:
Editing the text inside the boxes is just like with lists.
you can use append,pop and get/set item using ```box[index]```.

Example:
```
box[0] = 'Changed line'
box.append('New Line')
box.style(hPadding = 40) # you can also make changes in the style (the untouched options will remain).
```

Results:
```
                                        ----------------------
                                        %%   Changed line   %%
                                        %%     New Line     %%
                                        ----------------------
```

#### Available methods:
- ```createBox()``` - creates a box instance. Optional arguments: ```width``` ```height```.
- ```getDimensions()``` - returns a tuple of the box dimensions.
- ```printBox()``` - prints the box.
- ```style()``` - sets the appearance of the box (all the arguments described above).
- ```getMessage()``` - returns a copy of the box's text as a list.


## Todos:
 :white_medium_small_square: Enable to create box inside a box.
 
 :white_medium_small_square: Add an option to set titles.
 
 :white_medium_small_square: Add auto line counting.
