#! /usr/bin/env python
# -*- coding: utf8 -*-

#Requires
import sys
import getopt

class Usage(Exception):
	"""
	Usage() exception class, which we catch in an except clause at the end of main()
	"""
	def __init__(self,msg):
		"A description of the Usage constructor"
		self.msg=msg

def main(argv=None):
	"""
	main() function to analyse the command line flags and arguments, and activate 
	further anlysis
	"""
	if argv is None:
		argv = sys.argv
	try:
		try:
			opts, args = getopt.getopt(argv[1:], "h", ["help"])
		except getopt.error, msg:
			 raise Usage(msg)
		# more code, unchanged
	except Usage, err:
		print >>sys.stderr, err.msg
		print >>sys.stderr, "for help use --help"
		return 2


if __name__ == "__main__":
	"""
	The main program collected into function main()
	"""
	sys.exit(main())

    
