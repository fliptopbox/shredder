#!/usr/bin/python3

import numpy as np
import cv2
import random
import sys
import getopt
import re


banner = """
   ____ .  .      ____ ___  ___  ____ ____ . ; . : . ,
   [__  |__| ---- |___ |  \ |  \ |___ |__/ | | | | | |
   ___] |  | |__/ |___ |__/ |__/ |___ |  \ | | | | | |
   +---------|--\----------------|-----------|---|---+
   | | | | | | | | | | | | | | | | | | | | | | | | | |
   | | | | | | | | | | | | | | | | | | | | | | | | | |
   | ! | | | | | ; | | | | | | | | | | | | | | | | | |
   |   | | | |     | ! | |   | '   ! | |   : |   ;   |


  %s -i <input-file> [options]

  [options]:

   -o --output=(filename)   output file name (..._shredded.png)
   -w --width=(integer)     width of slice column in pixels (20)
   -b --border=(integer)    pixel width of the border (1)
   -t --tint=(float)        opacity of the border (0.9 -- 0=black, 1=transparent)


  Usage examples: https://github.com/fliptopbox/shredder/


"""


def load_image(fn):

    img = cv2.imread(fn) # original
    img8 = (img).astype('uint8') # convert to 8bit
    imgN = (img8 / 256) # normalize to floating point

    return imgN


def shuffle_columns(array, column_width=10, border_color=0.9, border_width=1):

    # create a black image
    destination =  np.zeros(array.shape)

    # the original image's dimentions
    (height, width, channels) = array.shape

    # caluculate the iterations
    ubound = (width / column_width)

    # pre-shuffle the column output matrix
    sequence = np.arange(0, width, column_width)
    #print ("Sequential:", sequence)

    np.random.shuffle(sequence)
    #print ("Shuffled:", sequence)

    # Iterate and catenate the output columns
    column_index = 0
    for current_column in sequence:

        # Calulate the column's start & end
        start = current_column
        end = min(current_column + column_width, width)

        # How much to advance the index cursor
        # REMEMBER: cols are shuffled, and not all equal width)
        diff = end - start

        # Darken the right most edge of each 
        column_a = array[ 0:height, current_column:current_column + column_width ]
        column_a[ 0:height, -border_width:end ] *= border_color

        #print ("index:", column_index, "width:", diff)
        destination[ 0:height, column_index:(column_index + diff) ] = column_a

        column_index += diff

    return destination



def main(argv):

    # inflate the usage banner, injecting script name
    usage_message = banner % argv[0]

    # default variables
    filename = None
    save_as = None
    column_width = 10
    border_color = 0.9
    border_width = 1

    try:
        opts, args = getopt.getopt(argv[1:], "hi:o:w:t:b:", ["input=", "ouput=", "width=", "tint=", "border="])

    except getopt.GetoptError:
        print (usage_message)
        sys.exit(2)

    for opt, arg in opts:

        if opt == "-h":
            print (usage_message)
            sys.exit(2)

        if opt in ("-i", "--input"):
            filename = arg

        if opt in ("-o", "--output"):
            save_as = arg

        if opt in ("-w", "--width"):
            column_width = int(arg)

        if opt in ("-t", "--tint"):
            border_color = float(arg)

        if opt in ("-b", "--border"):
            border_width = int(arg)


    if filename == None:
        print (usage_message)
        sys.exit(2)

    if save_as == None:
        save_as = re.sub(r'\.([^\.]+)$', "_shredded.\\1", filename)

    input_array = load_image(filename)
    output_array = shuffle_columns(input_array, column_width, border_color, border_width)
    output_uint8 = output_array * 256
    cv2.imwrite(save_as, output_uint8)


if __name__ == "__main__":
    main(sys.argv)
