# knitgit
app that calculates a sweater pattern based on user's parameters

registered knitgit.com  :D

Knitting - that fuddy-duddy, old-fashioned, bygone craft... is CODE. Pretty darn complex code.

This app will start with the most basic sweater design, but is infintely scalable over time to incorporate more and more complex structures as my skills (and investment of time) grows.

For ANY knitting project, the single most important factor for success is exactly measuring, and keeping consistent with, your GAUGE. Any stitch (simple/complex) any yarn (fat & fuzzy / threadlike) or needle (toothpicks/nunchucks) can be accomodated by this program, but it is imperative that the user take the time to knit a sample square, wash/iron/dry/stretch/whatever, and then carefully count how many stitches it takes to fill four inches over, and four inches up (N.B. stitches are NOT square).  KNOW YOUR GAUGE.

https://www.craftsy.com/blog/2013/05/how-to-measure-your-gauge-in-knitting/

The user will input stiches per 4 inches across, and up. These integer parameters (gauge_vert, gauge_horiz) will be used throughout the rest of the calculations.

Our basic sweater pattern will be a simple, scoopneck, boxy cut with a front & back (identical) and 2 sleeves (identical) in one homogenous stitch (any the user chooses)

user will choose desired chest measurement in inches, full circumference, divided by 2 = width (float parameter)
  size can be adjusted of course for the use'rs own body size, but also for desired fit - loose or snug.

user will choose desired length from top to bottom of body = length (float parameter)
  again, length can be adjusted for actual size, or desired fit - tunic to cropped
  
user will choose desired sleeve length, from shoulder seam to cuff = slv_length (float parameter)
  again by size and style - long sleeve, short sleeve or no sleeve at all :)


Now the calcualting begins!!!


BODY

The easy part, simply calculate the number of stiches needed to start (cast on) for front:
    width / 4 * gauge_horiz = cast_on (interger)

Calculate how long to knit until breaking for armhole:
    proportion of total length... output float inches

Calculate how to shape armhole:
    ratios and loops to create a parabolic curve... output integers (stiches per row, recurrence...)
    
Calculate when to break for neckline:
    proportion of total length... output float inches

Calculate how toshape neckline:
    ratios and loops to create a soft curve... output integers (stiches per row, recurrence...) 

cast off

Repeat all for back.


SLEEVE



    
    ......

