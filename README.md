# shredder

_eats an image and spits it out as spaghetti. shredded beyond recognition._

**Becareful, coz it turns images from this ...**
![from this](images/920x260_rgb_example.png)

**into this ... not a very nice thing to do!**
![into this](images/920x260_rgb_example_shredded.png)
(FIG1. default settings)

**... ah! it has done it again ...**
![or this](images/920x260_rgb_example_02.png)
(FIG2.  -o images/920x260_rgb_example_02.png -w 40 -b 80 -t 0.6)

**... sorry ... it was born this way**
![this again](images/920x260_rgb_example_03.png)
(FIG3.  -o images/920x260_rgb_example_03.png -w 5 -b 1 -t 0)

## Usage:

    ./shredder.py -i <input-image> [options]


## options

| argument           | type        | def  | comment
|--------------------|-------------|------|---------------------------------------------|
| -i, --input=*      | filename    |      | image file name (PNG recommended) 
| -o, --output=*     | filename    |      | input file name plus "_shredded" suffix
| -w, --width=*      | int (px)    | 20)  | width of the slices
| -b, --border=*     | int (px)    | 1    | width of the edge border
| -t, --tint=*       | float (0-1) | 0.9  | 0 = black, 1 = transparent


