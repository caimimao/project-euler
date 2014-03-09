from optparse import OptionParser

def main():
	from os import path
	import os.path

	parser = OptionParser(usage="%prog [options] NO.PROBLEM")

	(options, args) = parser.parse_args() 

	if len(args)>0:
		filename = "%03d.py" % int(args[0])
		folder = "%03d/" % (int(args[0]) // 100 * 100 + 100)
		if path.isfile(folder+filename):
			print "ERROR, python file %s already exist." % filename
		else:
			f = open(folder+filename, "w")
			f.write('# -*- coding: utf-8 -*-\n\n')
			f.write('__title__ = ""\n\n')
			f.write('def solve():\n')
			f.write('    pass\n')
			f.close()
	else:
		parser.print_help()
if __name__ == '__main__' :
	main()