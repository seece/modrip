
class TrackerSong:
	"""A self-contained tracker song."""
	PROTRACKER = "MOD"
	UNKNOWN = "???"

	def __init__(self):
		#self.fmt = Song.PROTRACKER
		self.name = ""
		self.bpm = 0
		self.num_patterns = 0
		self.orderlist = []
		self.num_channels = 0
		self.patterns = []
		self.instruments = []

class Pattern:
	def __init__(self):
		self.length = 0 # length in rows
		self.rows = [] # each row is a list of lists of notes

class Note:
	def __init__(self):
		self.pitch = 0
		self.volume = 0
		self.volume_effect = 0
		self.effect = 0
		self.parameters = 0
		self.instrument = 0

class Instrument:
	def __init__(self, sample):
		self.sample = sample

class Sample:
	def __init__(self):
		self.name = ""
		self.length = 0 # length in bytes 
		self.volume = 0
		self.finetune = 0
		self.repeat = 0
		self.repeat_length = 0
		self.data = bytes()






