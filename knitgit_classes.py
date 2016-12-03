class Sweater(object):
	def __init__(self, raw_gauge_st, raw_gauge_r, raw_trs_length, raw_trs_width, raw_slv_length):

#raw numbers

		self.raw_gauge_st = raw_gauge_st
		self.raw_gauge_r = raw_gauge_r
		self.raw_trs_length = raw_trs_length
		self.raw_trs_width = raw_trs_width
		self.raw_slv_length = raw_slv_length

#calculated gauge per inch

		self.gauge_st = float(self.raw_gauge_st / 4)
		self.gauge_r = float(raw_gauge_r / 4)

#calculated stitches for torso

		self.trs_stitches = int(self.raw_trs_width * self.gauge_st)
		self.trs_rows = int(self.raw_trs_length * self.gauge_r)
		self.trs_armhole = int((self.trs_stitches / 2) * 0.1)		#research this ratio!!! set min.
		self.trs_half = int((self.trs_stitches - self.trs_armhole) / 2)	

#calculated stitches for sleeve	

		self.slv_stitches = int(self.raw_trs_width * 0.4 * self.gauge_st)	#research this ratio!! should be less than half of width.
		self.slv_rows = int(self.raw_slv_length * self.gauge_r)
		#slv_armhole is just trs_armhole -- must be equal

#calculated stitches for finish/neck
	
		self.total_stitches = int(self.trs_stitches + (2 *self.slv_stitches) - (4 * self.trs_armhole))									
		self.final_stitch_count = int((self.trs_stitches + self.slv_stitches) * 2 * 0.3) ## .3?  calculate ratio, max/min.  front, back, 2 sleeves, then reduced to proportion.

	def buffer_stitches(self):
		if self.gauge_st/2 > 2:
			return int(self.gauge_st/2) #buffer should be about half-inch from each edge...
		else:
			return 2 	#but an absolute minimum of 2 stitches, or the pattern just won't work

	def buffer_rows(self):
		gauge_slope = self.raw_gauge_r/self.raw_gauge_st #more accurate at 4" count
		RAGLAN_SLOPE = 1.25 ###research!!!! 
		buffer_r = int(RAGLAN_SLOPE * gauge_slope)  # rows needed for each 1 stitch decrease = rows-per-inch / st-per-inch * desired slope
		if buffer_r > 1:
			return buffer_r
		else:
			return 1 	#but an absolute minimum of 1 row, or the pattern just won't work
		#if the gauge is too big horizontally (lots of stitches, few rows (like a cable stitch) in a square inch) 
		#raglan may not work -- will take forever to cast off enough stitches to close the neck.
		#validate gauge ratio???   ugh!! D:


