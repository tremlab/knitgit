class Sweater(object):
	def __init__(self, raw_gauge_st, raw_gauge_r, raw_trs_length, raw_trs_width, raw_slv_length):
		self.raw_gauge_st = int(raw_gauge_st)
		self.raw_gauge_r = int(raw_gauge_r)
		self.raw_trs_length = float(raw_trs_length)
		self.raw_trs_width = float(raw_trs_width)
		self.raw_slv_length = float(raw_slv_length)

		self.gauge_st = float(raw_gauge_st / 4)
		self.gauge_r = float(raw_gauge_r / 4)

		self.trs_stitches = int(trs_width * gauge_st)
		self.trs_rows = int(trs_length * gauge_r)
		self.trs_armhole = int((trs_stitches / 2) * 0.1)		#research this ratio!!! set max and min.
		self.trs_half = int((trs_stitches - trs_armhole) / 2)		#syntax?

		self.slv_stitches = int(trs_width * 0.4)	#research this ratio!! should be less than half of width.
		self.slv_rows = int(slv_length * gauge_r)
		#slv_armhole is just trs_armhole -- must be equal

		self.buffer_stitches = int(trs_stitches * 0.1) #???? calculate - definitely need max (10?) min(2)										
		self.final_stitch_count = int((trs_stitches + slv_stitches) * 2 * 0.3) ## .3?  calculate ratio, max/min.  front, back, 2 sleeves, then reduced to proportion.