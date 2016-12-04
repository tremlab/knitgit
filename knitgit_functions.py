#code actual!!!!

#github: tremlab
#Hackbright Intro 2016

def print_intro():
	return """

vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
 v v v v v v v v v v v v v v v v v v v v v v v v v v v v
    vv     vv     o    vv     vv     o    vv     vv
    vvv   vvv          vvv   vvv          vvv   vvv
vvv vvvv vvvv vvv  vvv vvvv vvvv vvv  vvv vvvv vvvv vvv
 vvv vvv vvv vvv    vvv vvv vvv vvv    vvv vvv vvv vvv
  vvv vv vv vvv      vvv vv vv vvv      vvv vv vv vvv
        o                  o                  o
  vvv vv vv vvv      vvv vv vv vvv      vvv vv vv vvv  
 vvv vvv vvv vvv    vvv vvv vvv vvv    vvv vvv vvv vvv
vvv vvvv vvvv vvv  vvv vvvv vvvv vvv  vvv vvvv vvvv vvv
    vvv   vvv          vvv   vvv          vvv   vvv
    vv     vv    o     vv     vv     o    vv     vv 
 v v v v v v v v v v v v v v v v v v v v v v v v v v v v
vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
   
                    GIT YOUR KNIT ON

                   knitgit by tremlab
                     THE ROUNDABOUT

This app lets you use any stitch, yarn, and needle you'd like, 
to create a pattern for a straight-cut, scoopneck, raglan sleeve sweater
in whatever size you choose.

Make sure you are using a 'homogenous' stitch for the entire sweater
that can be tiled off of your 4" x 4" gauge swatch.

I just need a few measurements to get started.  Please enter numbers only!
	"""
 

def torso_start(this_sweater):		

	#is zero?

 	return """
******************* 
*** TORSO START ***
*******************

Bottoms up! Let's start building the torso.


Using the needles and yarn that you chose to achieve your gauge, cast on %i stitches.

---REMINDER:  this pattern is in the round!

Loop around from your last cast on, back to your first.
Make sure to use a marker to keep track of where your row starts.
Start working in the pattern stitch you used to achieve your gauge.

---SAVOR THIS MOMENT!!! IT'S GONNA BE ***GORGEOUS!!!***

Continue working in your chosen stitch until work measures %.1f inches. 
(Should be about %i rows, but do whatever feels right!)

Continue in your pattern stitch for %i stitches.
We're halfway!! Cast off %i stitches.
Continue the row in your pattern stitch for %i stitches.
Again, cast off %i stitches. Don't lose your marker! ;)

---It may not look like much, but you just finished the biggest piece of this sweater!  
---You **so** got this!!
""" % (	this_sweater.trs_stitches,
		this_sweater.raw_trs_length, #huzzah! figured out decimals.
		this_sweater.trs_rows,
		this_sweater.trs_half,
		this_sweater.trs_armhole,
		this_sweater.trs_half,
		this_sweater.trs_armhole
		)

####SLEEVES

def sleeve_start(this_sweater):				

	#is zero?
	return """
******************** 
*** SLEEVE START ***
********************

---But, let's not rest on our laurels just yet. ;)

Set aside your (beautiful!) torso work, and lets get started on a sleeve.

Using the needles and yarn that you chose to achieve your gauge, cast on %i stitches.

---REMINDER: we're STILL working in the round. 
---This is where you'll need a ninja star of double-pointed needles to work.
---(REMINDER: you're totally a ninja!!)

Loop around from your last cast on, back to your first.

Make sure to use a marker to keep track of where your row starts.

Start working in the pattern stitch you used to achieve your gauge.

---This is gonna go soooo much faster than the body! Rock your dance playlist.

Continue working in your chosen stitch until work measures %.1f inches.
(Should be about %i rows, but do whatever feels right!)

Continue in your pattern stitch until you reach the last %i stitches.

Cast off till the end of the row.

---Now you have the body *AND* a sleeve.
---Time for chocolate. or zinfandel... or bourbon.

But... we do need 2 sleeves. so repeat it all again, 
and make sure the lengths match each other exactly.

""" % (	this_sweater.slv_stitches,
		this_sweater.raw_slv_length,
		this_sweater.slv_rows,
		this_sweater.trs_armhole
	)

# ####NECK

def assemble_pieces():		#no calculations here. tricky just getting everything lined up.

	return """

***********************
*** ASSEMBLE PIECES ***
***********************

---The good news: you've finished more than half or your knitting! Go you!!
---The bad news: now it gets complicated...

---The pattern so far has been pretty straightforward and chill, 
---but now you have to start paying attention.

First, let's assemble all of our pieces into one big sweater-loop.

---(REMINDER: you are Voltron!)




You will need 3 markers, all the same color, plus 1 in a distinct color 
to mark the absolute row beginning.

Knit in your pattern stitch across the front of your torso, 
to where you cast off for the first armhole.

-> Insert the first of your 3 markers.

Now bring your first sleeve, and line up the opening for the armhole, 
with the opening on the torso.

Continue to knit across from the torso directly onto the sleeve.
Knit all the way around the sleeve, and then...

-> Insert the second of your 3 markers.

Now continue to the back of your torso, knit all the way across 
to where you cast off for the seocnd armhole.

-> Insert the last of your 3 markers.

Bring your second sleeve, line up the armohole openings again, 
and knit around the armhole to the end.
We're back at the begining, now in one continuous loop!

-> Insert your 4th marker - unique color - to mark the row start.

---Knitting this first row was probably very awkward, 
---with your needles forced to turn around some pretty sharp curves.
---The next few rows will continue to be awkward, 
---but with each row it will level out into an easier round shape, 
---so hang in there!!
"""

def neck_start(this_sweater):  #debug, test!!!!!! draft only
	buffer_st = this_sweater.buffer_stitches() #call method once, shorter name

	return """

***********************
*** RAGLAN DECREASE ***
***********************

Now, for the remainder of the work, 
you will be methodically decreasing stitches, 
so the body will taper off to a neckline.

You will need to pay attention to stitch and row count going forward!

Starting at the beginning of the row (your unique marker), knit %i stitches.

Knit 2 stitches together (decreasing by one.)

Continue knitting until %i stitches before next marker.

Knit 2 together, knit %i, pass the marker, knit %i, and knit 2 together.
Continue all the way around the row, decreasing once before, and once after, 
each marker, until you are back to the start of the row.

In plain English, you will be decreasing 8 stitches a row in this manner, 
every %i rows, but the below chart will help you track exactly how many  
stitches and rows you should have at every point.

---N.B. this pattern will calculate a basic scoop neckline, 
---but you can easily stop sooner to create an open/off-the shoulder look, 
---or continue past for a snug crew neck,
---or stop decreasing, but keep knitting for a funnel/turtleneck. 

---Do what feels right!

	""" % (buffer_st,
			buffer_st + 2, #um... can I do calculations in here? YEP! :D
			buffer_st,
			buffer_st,
			this_sweater.buffer_rows()
		)

def raglan_decrease(this_sweater):

	total_sts = this_sweater.total_stitches #just making shorter references
	final_sts = this_sweater.final_stitch_count
	buffer_r = this_sweater.buffer_rows()
#brand new var - just for counting through loop.
	row_count = 2 	#already knit 1 while assembling pieces, 2 while first row of decrease.
	total_sts -= 8 #already dropped 8 stitches in forest row of decrease.
#new var to hold strings from the upcoming loop
	raglan_instruction_list = []

	while total_sts > final_sts:
		raglan_instruction_list.append("Knit the next %i rows as presented, without decreases." % (buffer_r))
		row_count += buffer_r	#keeping row count in sync with knitting commands	
		raglan_instruction_list.append("At row %i, decrease as above - once before, and once after each marker." % (row_count))
		total_sts -= 8			#keeping stitch count in sync with knitting commands
		row_count += buffer_r	#keeping row count in sync with knitting commands	
		raglan_instruction_list.append("-> Row count = %i, Stitch count = %i" % (row_count, total_sts))
		raglan_instruction_list.append("\n\n")

	raglan_instr_string = ""

	for line in raglan_instruction_list:
		raglan_instr_string = raglan_instr_string + "\n" + line

	return raglan_instr_string		#yikes - orignially returned the list, but that messed up the file output. :()

def finish_sweater():

	return """

***************
*** FINISH! ***
***************


Loosely cast off all stitches.

Sew closed the small armhole openings under each sleeve.

Weave any loose ends back into the fabric.

Block, iron, wash - whatever you did before to your swatch to achieve your gauge - 
to make sure your sweater ends up the intended size.

********************************************
***  YOU JUST MADE A SWEATER!!!!!!!!!!!  ***
********************************************

Do your happy dance!

Rock your sweater for the whole world to see, 
and send pics to: 

knitgit@gmail.com

	"""





if __name__ == '__main__':
	main()