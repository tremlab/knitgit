# knitgit
app that calculates a sweater pattern based on user's parameters

knitgit_ui is the "main" file for this project. It imports from knitgit_functions & knitgit_classes.

Would love to get the python interacting with an HTML form and/or outputting to a text (or other) format...




Knitting - that fuddy-duddy, old-fashioned, bygone craft... is CODE. Pretty darn complex code.

This app will start with the most basic sweater design, but is infintely scalable over time to incorporate more and more complex structures as my skills (and investment of time) grows.

For ANY knitting project, the single most important factor for success is exactly measuring, and keeping consistent with, your GAUGE. Any stitch (simple/complex) any yarn (fat & fuzzy / threadlike) or needle (toothpicks/nunchucks) can be accomodated by this program, but it is imperative that the user take the time to knit a sample square, wash/iron/dry/stretch/whatever, and then carefully count how many stitches it takes to fill four inches over, and four inches up (N.B. stitches are NOT square).  KNOW YOUR GAUGE.

https://www.craftsy.com/blog/2013/05/how-to-measure-your-gauge-in-knitting/

The user will input stiches per 4 inches across, and up. These integer parameters (gauge_vert, gauge_horiz) will be used throughout the rest of the calculations.

Our basic sweater pattern will be a simple, scoopneck, boxy cut with a torso and 2 sleeves (identical) in one homogenous stitch (any the user chooses) knit in "in the round", i.e. seamless.

user will choose desired chest measurement in inches, full circumference = width (float parameter)
  size can be adjusted of course for the user's own body size, but also for desired fit - loose or snug.

user will choose desired length from top to bottom of body = length (float parameter)
  again, length can be adjusted for actual size, or desired fit - tunic to cropped
  
user will choose desired sleeve length, from shoulder seam to cuff = slv_length (float parameter)
  again by size and style - long sleeve, short sleeve or no sleeve at all :)



