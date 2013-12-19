import struct
from struct import unpack
from lib.modtag.format import ModuleFormat, ProtrackerFormat

formats = []
formats.append(ProtrackerFormat())

class InvalidModuleException(Exception):
	pass

def detect_module_format(modulebytes):
	for f in formats:
		if f.identify(modulebytes):
			return f

	return None

def load_module(modulebytes, options=None):
	f = detect_module_format(modulebytes)

	if f == None:
		raise InvalidModuleException()

	return f.load_module(modulebytes, options)

def get_pattern_string(song, pnum):
	pattern = song.patterns[pnum]
	print("Pattern #" + str(pnum))
	print("len: " + str(pattern.length))
	print("channels: " + str(song.num_channels))

	for r in range(pattern.length-1):
		for c in range(song.num_channels-1):
			#print("pos {0} {1}", c, r)
			note = pattern.rows[c][r]
			print("\t|", note.pitch, hex(note.effect), hex(note.parameters), end="")
		print()



