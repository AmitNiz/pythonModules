'''

###############################################
/ Creator:Amit Nizri                          /
/ Date: Jun 2019                              /
###############################################

Easy and simple module for creating message boxes for CLI.

                      **************
                      /   Borders  /
                      **************

'''
#///////////////TODO:///////////////////
#1.Add special boxes types.
#2.Add append mode for arrays.
#3.Add an option for box in a box mode.

class createBox:
    
    def __init__(self,width=1,height=1):

        '''
        Create new box:
        ---------------------------------------------------------------------
        width - the width of the box. 
        height - the height of the box.
        If the given dimensions doesn't fit to the size of the message,
        the box size will be adopted.
        ---------------------------------------------------------------------
        '''

        self.__width = width
        self.__height = height
        self.__content = []
        self.__horizontal_symbol = '*'
        self.__vertical_symbol = '*'
        self.__textAllign = '<' 
        self.__margin = 1
        self.__padding = 1
    def getDimensions(self):
        self.__updateDimensions
        '''Returns a tuples with the dimensions of the box.'''
        return (self.__width,self.__height)

    def __getMaxLineLen(self):
        max_len = 0
        for word in self.__content:
            max_len = len(word) if len(word) > max_len else max_len
        return max_len
    def __setAllignment(self,side):
        if side =='left':
            return '<'
        elif side =='right':
            return '>'
        elif side =='center':
            return '^'
        elif side is None:
            return None
        else:
            print('Wrong Allignment! Enter: left,right or center..')
            return None 
    def __updateDimensions(self): 
        line_width = self.__getMaxLineLen() + self.__margin*2 + len(self.__vertical_symbol*2)
        num_of_lines = len(self.__content)
        self.__height = self.__height if num_of_lines < self.__height else num_of_lines
        self.__width = self.__width if line_width < self.__width else line_width 
                      

    def style(self,width=None ,height= None,textAllign = None ,
                                            horizontal = None,vertical=None,
                                            padding =None,margin = None):
        '''
        Setting up the style of the box:
        widht - sets the width of the box.
        height - sets the height of the box.
        textAllign -Sets the text allignments. Options:'left', 'center', 'right'
        horizontal - Sets the horizontal symbols of the box. set to '*' by default
        vertical - Sets the vertical symbols of the box. set to '*' by default.
        padding - Sets the padding length.
        margin - Sets the margins length.
        '''
        self.__height = abs(int(height or self.__height))
        self.__width = abs(int(width or self.__width))
        self.__textAllign = self.__setAllignment(textAllign) or self.__textAllign
        self.__horizontal_symbol = horizontal or self.__horizontal_symbol
        self.__vertical_symbol = vertical or self.__vertical_symbol
        self.__margin = int(margin or self.__margin)
        self.__padding = int(padding or self.__padding)

    def append(self,string):
        '''Adds a new line to the box.'''
        self.__content.append(str(string))

    def pop(self,index=-1):
        '''Deletes a line from the box.'''
        try: 
            self.__content.pop(index)
        except IndexError: 
            print('IndexError: list index out of range') 

    def __len__(self):
        '''Returns the length of the message (by lines).''' 
        return len(self.__content)

    def __getitem__(self,i):
        '''Returns the string of a given line.'''
        try:
            return self.__content[i]
        except IndexError:
            print('IndexError: list index out of range')
    
    def __setitem__(self,index,string):
        '''Changes a given line content.'''
        try:
            self.__content[index] = str(string)
        except IndexError:
            print('IndexError: list indexo out of range')

    def getMessage(self):
        return self.__content.copy()

    def printBox(self):
        '''Prints the box.'''
        self.__updateDimensions()
        line_width=self.__width -2*self.__margin -2*len(self.__vertical_symbol)
        fmt = '{padding}{edge}{margin}{text:{allignSign}{width}}{margin}{edge}' 
        print(' '*self.__padding + self.__horizontal_symbol*(self.__width))
        for i in range(self.__height):
            line = '' if i >= len(self.__content) else self.__content[i]
            print(fmt.format(edge = self.__vertical_symbol,
                             margin =' '*self.__margin,
                             text = line,
                             padding =' '*self.__padding,
                             width = line_width,
                             allignSign = self.__textAllign))
            
        print(' '*self.__padding + self.__horizontal_symbol*(self.__width)) 
