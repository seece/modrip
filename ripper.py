#!/usr/bin/python
# At least python 3.3 required

import argparse
import hashlib
import string
import wave
from lib.modtag.modtag import load_module


parser = argparse.ArgumentParser(description='Rip samples from Amiga modules')
parser.add_argument('module', help='The module where to rip samples from')
parser.add_argument('--output', help='Where to save the resulting samples', default='.')
parser.add_argument('--verbose', action='store_true')
parser.add_argument('--rate', default=8000)

args = parser.parse_args()

valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)

f = open(args.module, "rb")
songbytes = f.read()
f.close()

mod = load_module(songbytes, {'verbose': args.verbose})
rate = args.rate 

for ins in mod.instruments:
	s = ins.sample
	if s.length == 0:
		continue

	name = ''.join(c for c in ins.sample.name if c in valid_chars)
	
	if len(name) == 0:
		# use md5 hash of the sample data if no name given
		# not tested
		m = hashlib.md5(s.data)
		name = m.hexdigest()

	w = wave.open(args.output + name + ".wav", 'w')
	w.setparams((1, 2, int(rate), 0, 'NONE', 'not compressed'))
	w.writeframes(s.data)
	w.close()

