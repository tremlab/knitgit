#code actual!!!!


#github: tremlab
#Hackbright Intro 2016


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
	print "Starting working in the pattern stitch you used to achieve your gauge.\n"
	print "SAVOR THIS MOMENT!!! IT'S GONNA BE ***GORGEOUS!!!***\n"
	print "Continue working in your chosen stitch until work measures %f(1) inches\n" (trs_length) #syntax???? 1 decimal!
	print "(Should be about " + trs_rows + " rows, but do whatever feels right!)"
	print "Continue in your pattern stitch for " + trs_half + " stitches.\n"
	print "We're halfway!! Cast off " + trs_armhole + " stitches.\n"
	print "Continue the row in your pattern stitch for " + trs_half + " stitches.\n"
	print "Again, cast off " + trs_armhole + " stitches. Don't lost your marker! ;)"
	print "It may not look like much, but you just finished the biggest piece of this sweater!  You **so** got this!!\n"
	print "See? I TOLD you it would be gorgeous!! :*\n\n\n"
	#return stiches???????????

####SLEEVES

def sleeve_start(trs_width, gauge_st, slv_length, gauge_r):				#all inputs floats
	#limits - max/min size?
	#is zero?
	slv_stitches = int(trs_width * 0.4)			#research this ratio!! shoudld be less than half of width.
	slv_rows - int(slv_length * gauge_r)
	trs_armhole_half = int((trs_stitches / 2) * 0.05)		#research this ratio!!! set max and min. (50% of armhole drop.)
	trs_remainder = int(slv_stitches - (trs_armhole_half * 2))

	print "But, let's not rest on our laurels just yet. ;)"
	print "Set aside your (beautiful!) torso work, and lets get started on a sleeve."
	print "Using the needles and yarn that you chose to achieve your gauge, cast on " + slv_stitches + " stitches.\n"
	print "REMINDER: we're STILL working in the round. This is where you'll need a ninja star of double-pointed needles to work.\n"
	print "(REMINDER: you're totally a ninja!!)\n"
	print "Make sure to use a marker to keep track of where your row starts.\n"
	print "Starting working in the pattern stitch you used to achieve your gauge.\n"
	print "This is gonna go soooo much faster than the body! Rock your dance playlist.\n"
	print "Continue working in your chosen stitch until work measures %f(1) inches\n" (slv_length) #syntax???? 1 decimal! 2?
	print "(Should be about " + slv_rows + " rows, but do whatever feels right!)"
	print "Cast off " + trs_armhole_half + " stitches.\n"
	print "Continue in your pattern stitch for " + trs_remainder + " stitches.\n"	
	print "Now, if we did our math right, there are " + trs_armhole_half + " +/- 1 stitches left. Cast 'em, off!\n"
	print "Mark drop! Don't need that either.\n"
	print "Now you have the body *AND* a sleeve. Time for chocolate. or zinfandel... or bourbon.\n\n\n"
	print "But... we do need 2 sleeves. so repeat it all again, and make sure the lengths match each other exactly."

####NECK



def main():
	print "git your knit on"

	torso_start(trs_width, gauge_st, trs_length, gauge_r)

	sleeve_start(trs_width, gauge_st, slv_length, gauge_r)
#	neck_start.....

if __name__ == '__main__':
	main()