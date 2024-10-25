#!/bin/bash

jpgfiles=$(ls -l ../pictures/*.jpg | wc -l)

# echo $jpgfiles (should display number of jpg files)


if [ "$jpgfiles" -eq 10 ]; then
  
  rm -f *.jpg 
  echo "Files were deleted."

else 
  
  echo "Files were not deleted."

fi

