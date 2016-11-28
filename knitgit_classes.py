class Sweater(object):
	def __init__(self, raw_gauge_st, raw_gauge_r, raw_trs_length, raw_trs_width, raw_slv_length):
		self.raw_gauge_st = raw_gauge_st
		self.raw_gauge_r = raw_gauge_r
		self.raw_trs_length = raw_trs_length
		self.raw_trs_width = raw_trs_width
		self.raw_slv_length = raw_slv_length

	# def gauge_st(self):							# I don't think methods are needed, as the contstants will never change.
	# 	gauge_st = float(self.raw_gauge_st / 4)
	# 	return gauge_st

		self.gauge_st = float(self.raw_gauge_st / 4)
		self.gauge_r = float(raw_gauge_r / 4)

		self.trs_stitches = int(self.raw_trs_width * self.gauge_st)
		self.trs_rows = int(self.raw_trs_length * self.gauge_r)
		self.trs_armhole = int((self.trs_stitches / 2) * 0.1)		#research this ratio!!! set max and min.
		self.trs_half = int((self.trs_stitches - self.trs_armhole) / 2)		#syntax?

		self.slv_stitches = int(self.raw_trs_width * 0.4 * self.gauge_st)	#research this ratio!! should be less than half of width.
		self.slv_rows = int(self.raw_slv_length * self.gauge_r)
		#slv_armhole is just trs_armhole -- must be equal

		self.buffer_stitches = int(self.trs_stitches * 0.1) #???? calculate - definitely need max (10?) min(2)	
		self.total_stitches = int(self.trs_stitches + (2 *self.slv_stitches) - (4 * self.trs_armhole))									
		self.final_stitch_count = int((self.trs_stitches + self.slv_stitches) * 2 * 0.3) ## .3?  calculate ratio, max/min.  front, back, 2 sleeves, then reduced to proportion.

# first_sweater = Sweater(20, 22, 20.5, 38, 12)


# first_sweater.raw_gauge_st = 100
# print first_sweater.__dict__