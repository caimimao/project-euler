from optparse import OptionParser
from common import print_head, print_result
from common import time_start, time_stop
from common import enable_quite_mode


__version__ = """
Python solver for Project Euler
%prog 0.0.17
"""

def solve_one(module_name, quite=True, corrent_answer=None):
	try:
		mod = __import__(module_name, fromlist=['*'])
		title =  mod.__title__  if hasattr(mod, '__title__') else None
		if quite:
			time_start()
		else:
			print_head(int(module_name), title = title)

		result = mod.solve()
		if quite:
			if corrent_answer:
				ok =  "*" if (str(result) == corrent_answer) else ""
			
			time = time_stop()
			print "Problem %s - %s - %s - %s" % (module_name, result, ok, time)
		else:
			print_result(result)
	except ImportError as e:
		if not str(e).startswith('No module named'):
			import traceback
			traceback.print_exc()

def main():
	parser = OptionParser(usage="%prog [options] NO.PROBLEM", 
		version=__version__)
	parser.add_option("-t", "--time", 
			help="show consumed time infomration in every solution.",
			action="store_true", dest="show_time_log")  

	(options, args) = parser.parse_args() 

	if len(args)>0:

		if args[0] == "from" or args[0] == "all":
			from_no, to_no = 0, 5000
			if args[0] == "from":
				if len(args) != 4:
					return parser.print_help()
				else:
					from_no = int(args[1])
					to_no = int(args[3])

			from answer import answer
			enable_quite_mode()
			keys = answer.keys()
			keys.sort()
			for m in keys:
				if int(m)<=to_no and int(m)>=from_no:
					solve_one(m, quite=True, corrent_answer=answer[m])

		else:
			m = "%03d" % int(args[0])
			solve_one(m, quite=False)
	else:
		parser.print_help()
if __name__ == '__main__' :
	main()