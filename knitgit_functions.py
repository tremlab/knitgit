#code actual!!!!

#github: tremlab
#Hackbright Intro 2016
 


####TORSO

# from knitgit_classes import Sweater

def torso_start(this_sweater):		
	#limits - max/min size?
	#is zero?

 
	print "\n\n\n\nBottoms up! Let's start building the torso.\n\n"
	print "Using the needles and yarn that you chose to achieve your gauge, cast on " + str(this_sweater.trs_stitches) + " stitches.\n"
	print """
REMINDER:  this pattern is in the round!
Loop around from your last cast on, back to your first.
Make sure to use a marker to keep track of where your row starts.
Start working in the pattern stitch you used to achieve your gauge.
SAVOR THIS MOMENT!!! IT'S GONNA BE ***GORGEOUS!!!***\n
	"""

	print "Continue working in your chosen stitch until work measures " + str(this_sweater.raw_trs_length) + " inches." #1 decimal???
	print "(Should be about " + str(this_sweater.trs_rows) + " rows, but do whatever feels right!)\n"
	print "Continue in your pattern stitch for " + str(this_sweater.trs_half) + " stitches.\n"
	print "We're halfway!! Cast off " + str(this_sweater.trs_armhole) + " stitches.\n"
	print "Continue the row in your pattern stitch for " + str(this_sweater.trs_half) + " stitches.\n"
	print "Again, cast off " + str(this_sweater.trs_armhole) + " stitches. Don't lose your marker! ;)"
	print "It may not look like much, but you just finished the biggest piece of this sweater!  You **so** got this!!\n"
	print "See? I TOLD you it would be gorgeous!! :*\n\n\n"
	#return stiches???????????

####SLEEVES

def sleeve_start(this_sweater):				#all inputs floats
	#limits - max/min size?
	#is zero?

	print "But, let's not rest on our laurels just yet. ;)"
	print "Set aside your (beautiful!) torso work, and lets get started on a sleeve.\n"
	print "Using the needles and yarn that you chose to achieve your gauge, cast on " + str(this_sweater.slv_stitches) + " stitches.\n"
	print "REMINDER: we're STILL working in the round. This is where you'll need a ninja star of double-pointed needles to work.\n"
	print "(REMINDER: you're totally a ninja!!)\n"
	print "Loop around from your last cast on, back to your first.\n"
	print "Make sure to use a marker to keep track of where your row starts.\n"
	print "Start working in the pattern stitch you used to achieve your gauge.\n"
	print "This is gonna go soooo much faster than the body! Rock your dance playlist.\n"
	print "Continue working in your chosen stitch until work measures %f(1) inches\n" % (this_sweater.raw_slv_length) #SYNTAX!!!!! 1 decimal! 2?
	print "(Should be about " + str(this_sweater.slv_rows) + " rows, but do whatever feels right!)"
	print "Continue in your pattern stitch until you reach the last " + str(this_sweater.trs_armhole) + " stitches.\n"	
	print "Cast off till the end of the row.\n"			
	print "Now you have the body *AND* a sleeve. Time for chocolate. or zinfandel... or bourbon.\n\n\n"
	print "But... we do need 2 sleeves. so repeat it all again, and make sure the lengths match each other exactly."

# ####NECK

def neck_start():		#no calculations here. tricky just getting everything lined up.

	print """


The good news: you've finished more than half or your knitting! Go you!!
The bad news: now it gets complicated...

The pattern so far has been pretty straightforward and chill, but now you have to start paying attention.

First, let's assemble all of our pieces into one big sweater-loop.
(REMINDER: you are Voltron!)




You will need 3 markers, all the same color, and 1 in a distinct color to mark the absolute row beginning.
Knit in your pattern stitch across the front of your torso, up to where you cast off for the first armhole.

---> Insert the first of your 3 markers.

Now bring your first sleeve, and line up the opening for the armhole, with the opening on the torso.
Continue to knit across from the torso directly onto the sleeve.
Knit all the way around the sleeve, and then...

---> Insert the second of your 3 markers.

Now continue to the back of your torso, knit all the way across to where you cast off for the seocnd armhole.

---> Insert the last of your 3 markers.

Bring your second sleeve, line up the armohole openings again, and knit around the armhole to the end.
We're back at the begining, now in one continuous loop!

---> Insert your 4th marker - unique color - to mark the row start.

Knitting this first row was probably very awkward, with your needles forced to turn around some pretty sharp curves.
The next few rows will continue to be awkward, but with each row it will level out into an easier round shape, so hang in there.
	"""

# def neck_finish(this_sweater):  #debug, test!!!!!! draft only

# 	row_count = 2 	#counter - first row, just working around once.  Second row is our first round of decreases.
# 	total_sts = this_sweater.total_stitches #just making shorter references
# 	final_sts = this_sweater.final_stitch_count
# 	buffer_sts = this_sweater.buffer_stitches

# 	print "Now, for the remainder of the work, you will be methodically decreasing stitches, so the body will taper off to a neckline.\n"
# 	print "You will need to pay attention to stitch and row count going forward.\n"
# 	print "Starting at the beginning of the row (your unique marker), knit " + buffer_sts + "."
# 	print "Knit 2 stitches together (decrease by one.)"
# 	print "Continue knitting until " + (buffer_sts + 2) + " before next marker.\n"
# 	print "Knit 2 together, knit " + buffer_sts + ", pass the marker, knit " + buffer_sts + ", and knit 2 together."
# 	print "Continue all the way around the row, decreasing once before, and once after, each marker, until you are back to the start."
	

# 	total_stitches -= 8

# 	print"""

# 	In plain English, you will be decreasing 8 stitches a row in this manner, every ??? rows,
# 	but the below chart will help you track exactly how many stitches and rows you should have at every point.
# 	N.B. this pattern will calculate a basic scoop neckline, but you can easily stop sooner, or continue past
# 	to create an open/off-the shoulder look, or funnel/turtleneck. Do what feels right!

# 	"""
# 	print "Row count = " + str(row_count) + ", Stitch count = " + str (total_sts)

# 	while total_sts > final_sts:
# 		print "Knit the next ???? rows as presented, without decreases."
# 		row_count += ???		#only execute decrease every ??? rows (not variable - slope is same no matter size).
# 		print "At row " + row_count + ", decrease as above - once before, and once after each marker."
# 		total_sts -= 8		#decreasing once before, once after each of the 4 markers.
# 		print "Row count = " + str(row_count) + ", Stitch count = " + str(total_sts)

# 	print "Now you should be at row " + str(row_count) + " with " + str(total_sts) + ".\n"

# 	print """

# Cast off all stitches.

# Sew closed the small armhole openings under each sleeve.

# Weave any loose ends back into the fabric.

# Block, iron, wash - whatever you did before to your swatch to achieve your gauge - 
# to make sure your sweater ends up the intended size.

# ********************************************
# ***  YOU JUST MADE A SWEATER!!!!!!!!!!!  ***
# ********************************************

# Do your happy dance!
# Rock your sweater for the whole world to see, and send pics to: 

# ninja@knitgit.com

# 	"""



	# print this_sweater.__dict__

	# torso_start(trs_width, gauge_st, trs_length, gauge_r)

#	variable_name?? = fun_call(parameters)!!!!!!!!! to go from one fun to the next, and carry over new data.

	# sleeve_start(trs_width, gauge_st, slv_length, gauge_r)

	# neck_start()

	# neck_finish(parammmm)

if __name__ == '__main__':
	main()