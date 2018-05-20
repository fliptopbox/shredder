#!/bin/bash


original=$1
stripewidth=$2


imagewidth=`identify -format '%w' $original`
imageheight=`identify -format '%h' $original`
count=$(( ( $imagewidth / $stripewidth ) - 1 ))

dest="${original}_slices"
mkdir $dest

clear

echo -e "\n\n"

echo "  ____ _  _ ____ ____ ___  ___  ____ ____ | | | | | | "
echo "  [__  |__| |__/ |___ |  \ |  \ |___ |__/ | | | | | | "
echo "  ___] |  | |  \ |___ |__/ |__/ |___ |  \ | | | | | | "
echo " The shredder starting up ..."
echo -e "\n\n"
echo " Image dimensions: $imagewidth x $imageheight"
echo " Slice width: $stripewidth - No of stripes: $count"
echo -e "\n\n"

for i in `seq 0 $count`;
do
    offset=$(( $i * $stripewidth ))
    prefix=$(( ( RANDOM % 888 ) + 111 ))
    name="$prefix-$i"

    filename="$dest/$name.png"

    echo "$i: $filename"

    convert  $original -crop "${stripewidth}x${imageheight}+${offset}+0" \
        -stroke black -strokewidth 2 \
        -draw "line ${stripewidth},${imageheight} ${stripewidth},0" \
        -strip $filename
done

# Rake up the shredded slices and glue the together
convert "${dest}/*.png" $original +append -strip -crop "${imagewidth}x${imageheight}+0+0" "sliced_$original"

# clean-up the mess
rm -R "$dest"


