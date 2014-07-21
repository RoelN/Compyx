#!/usr/bin/python
import os
import glob

path = "*.svg"
for fname in glob.glob(path):

  print(fname)

  with open (fname, "r") as svgtje:
  	data=svgtje.readlines()

  colors = [ "8A46AE", "3E31A2", "7C70DA", "000000" ]

  for color in colors:

    newdata = []

    for line in data:
    	if not "polygon" in line:
    		newdata.append( line )
    	if "polygon" and color in line:
    		newdata.append( line )

    # with open ( fname+"-"+color+".svg" , "w") as svgwrite:

    with open ( color+"-"+fname , "w") as svgwrite:
      svgwrite.writelines(newdata)
