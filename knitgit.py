#code actual!!!!


#github: tremlab
#Hackbright Intro 2016

######variable formatting/verifying functions

#max/mins, 


######knitting functions
####TORSO

def torso_start(trs_width, gauge_st, trs_length, gauge_r):		#all inputs floats
	#limits - max/min size?
	#is zero?
	trs_stitches = int(trs_width * gauge_st)
	trs_rows = int(trs_length * gauge_r)
	trs_armhole = int((trs_stitches / 2) * 0.1)		#research this ratio!!! set max and min.
	trs_half = int((trs_stitches - trs_armhole) / 2)		#syntax?
 
	print "Bottoms up! Let's start building the torso.\n\n"
	print "Using the needles and yarn that you chose to achieve your gauge, cast on " + trs_stitches + " stitches.\n"
	print "REMINDER:  this pattern is in the round!\n"
	print "Loop around from your last cast on, back to your first.\n"
	print "Make sure to use a marker to keep track of where your row starts.\n"
	print "Start working in the pattern stitch you used to achieve your gauge.\n"
	print "SAVOR THIS MOMENT!!! IT'S GONNA BE ***GORGEOUS!!!***\n"
	print "Continue working in your chosen stitch until work measures %f(1) inches\n" (trs_length) #syntax???? 1 decimal!
	print "(Should be about " + trs_rows + " rows, but do whatever feels right!)"
	print "Continue in your pattern stitch for " + trs_half + " stitches.\n"
	print "We're halfway!! Cast off " + trs_armhole + " stitches.\n"
	print "Continue the row in your pattern stitch for " + trs_half + " stitches.\n"
	print "Again, cast off " + trs_armhole + " stitches. Don't lose your marker! ;)"
	print "It may not look like much, but you just finished the biggest piece of this sweater!  You **so** got this!!\n"
	print "See? I TOLD you it would be gorgeous!! :*\n\n\n"
	#return stiches???????????

####SLEEVES

def sleeve_start(trs_width, gauge_st, slv_length, gauge_r):				#all inputs floats
	#limits - max/min size?
	#is zero?
	slv_stitches = int(trs_width * 0.4)			#research this ratio!! shoudld be less than half of width.
	slv_rows - int(slv_length * gauge_r)
	trs_armhole = int((trs_stitches / 2) * 0.1)		#research this ratio!!! set max and min. 


	print "But, let's not rest on our laurels just yet. ;)"
	print "Set aside your (beautiful!) torso work, and lets get started on a sleeve.\n"
	print "Using the needles and yarn that you chose to achieve your gauge, cast on " + slv_stitches + " stitches.\n"
	print "REMINDER: we're STILL working in the round. This is where you'll need a ninja star of double-pointed needles to work.\n"
	print "(REMINDER: you're totally a ninja!!)\n"
	print "Loop around from your last cast on, back to your first.\n"
	print "Make sure to use a marker to keep track of where your row starts.\n"
	print "Start working in the pattern stitch you used to achieve your gauge.\n"
	print "This is gonna go soooo much faster than the body! Rock your dance playlist.\n"
	print "Continue working in your chosen stitch until work measures %f(1) inches\n" (slv_length) #syntax???? 1 decimal! 2?
	print "(Should be about " + slv_rows + " rows, but do whatever feels right!)"
	print "Continue in your pattern stitch until you reach the last " + trs_armhole + " stitches.\n"	
	print "Cast off till the end of the row.\n"			
	print "Now you have the body *AND* a sleeve. Time for chocolate. or zinfandel... or bourbon.\n\n\n"
	print "But... we do need 2 sleeves. so repeat it all again, and make sure the lengths match each other exactly."

####NECK

def neck_start():		#no calculations here. tricky just getting everything lined up.

	print "The good news: you've finished more than half or your knitting! Go you!!"
	print "The bad news: now it gets complicated.\n"
	print "The pattern so far has been pretty straightforward and chill, but now you have to start paying attention.\n"
	print "First, let's assemble all of our pieces into one big sweater-loop."
	print "(REMINDER: you are Voltron!)\n"
	print "You will need 3 markers, all the same color, and 1 in a distinct color to mark the absolute row beginning.\n"
	print "Knit in your pattern stitch across the front of your torso, up to where you cast off for the first armhole.\n"
	print "Insert the first of your 3 markers.\n"
	print "Now bring your first sleeve, and line up the opening for the armhole, with the opening on the torso.\n"
	print "Continue to knit across from the torso directly onto the sleeve.\n"
	print "Knit all the way around the sleeve, and then insert the second of your 3 markers.\n"
	print "Now continue to the back of your torso, knit all the way across to where you cast off for the seocnd armhole.\n"
	print "Insert the last of your 3 markers.\n"
	print "Bring your second sleeve, line up the armohole openings again, and knit around the armhole to the end.\n"
	print "We're back at the begining, now in one continuous loop!\n"
	print "Insert your 4th marker - unique color - to mark the row start.\n"
	print "Knitting this first row was probably very awkward, with your needles forced to turn around some pretty sharp curves.\n"
	print "The next few rows will continue to be awkward, but with each row it will level out into an easier round shape, so hang in there.\n"


def neck_finish(trs_stitches_oneside, sl_stitches, gauge_st, gauge_r):
	buffer_stitches = int(trs_stitches * 0.1) #???? calculate - definitely need max (10?) min(2)
	total_stitches = 2 * (trs_stitches_oneside + sl)
	final_stitch_count = int((trs_stitches + slv_stitches) * 2 * 0.3) ## .3?  calculate ratio, max/min.  front, back, 2 sleeves, then reduced to proportion.
	row_count = 2 	#first row, just working around once.  Second row is our first round of decreases.


	print "Now, for the remainder of the work, you will be methodically decreasing stitches, so the body will taper off to a neckline.\n"
	print "You will need to pay attention to stitch and row count going forward.\n"
	print "Starting at the beginning of the row (your unique marker), knit " + buffer_stitches + "."
	print "Knit 2 stitches together (decrease by one.)"
	print "Continue knitting until " + (buffer_stitches + 2) + " before next marker.\n"
	print "Knit 2 together, knit " + buffer_stitches + ", pass the marker, knit " + buffer_stitches + ", and knit 2 together."
	print "Continue all the way around the row, decreasing once before, and once after, each marker, until you are back to the start."
	total_stitches -= 8
	print "In plain English, you will be decreasing 8 stitches a row in this manner, every ??? rows.\n"
	print "But the below chart will help you track exactly how many stitches and rows you should have at every point.\n"
	print "N.B. this pattern will calculate a basic neckline, but you can easily stop sooner, or continue past"
	print "to create an open/off-the shoulder look, or funnel/turtleneck. Do what feels right!\n\n\n"
	print "Row count = " + row_count + ", Stitch count = " + (total_stitches)

	while total_stitches > final_stitch_count:
		print "Knit the next ???? rows as presented, without decreases."
		row_count += ???		#only execute decrease every ??? rows (not variable - slope is same no matter size).
		print "At row " + row_count + ", decrease as above - once before, and once after each marker."
		total_stitches -= 8		#decreasing once before, once after each of the 4 markers.
		print "Row count = " + row_count + ", Stitch count = " + (total_stitches)

	print "Now you should be at row " + row_count + " with " + total_stitches + ".\n"
	print "Cast off all stitches.\n\n\n"

	print "YOU JUST MADE A SWEATER!!!!!!!!!!!"
	print "Do your happy dance first, and then take a moment to sew closed the small armhole openings under each sleeve.\n"
	print "Block, iron, wash - whatever you did before to your swtch to achieve your gauge.\n"
	print "Rock your sweater for the whole world to see, and send pics to: ninja@knitgit.com"











def main():
	print "git your knit on"

	torso_start(trs_width, gauge_st, trs_length, gauge_r)

#	variable_name?? = fun_call(parameters)!!!!!!!!! to go from one fun to the next, and carry over new data.

	sleeve_start(trs_width, gauge_st, slv_length, gauge_r)

	neck_start()

	neck_finish(parammmm)

if __name__ == '__main__':
	main()