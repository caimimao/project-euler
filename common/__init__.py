import datetime

__start__ = None
def time_start():
	global __start__
	__start__ = datetime.datetime.now()

def print_time_consume():
	global __start__
	now = datetime.datetime.now()
	print "The time used in this calculation is %s" % (now - __start__)

def print_head(number):

	print "---------------------------------------------"
	print "  Project Euler Solution for Problem %03d" % number
	print "        longwosion@gmail.com "
	print "---------------------------------------------"

	time_start()

def print_result(result, msg=None):
	if msg:
		print "%s %s" % (msg, result)
	else:
		print "Answer is %s" % result

	print_time_consume()

