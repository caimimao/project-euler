import datetime

__start__ = None

def time_start():
	global __start__
	__start__ = datetime.datetime.now()

def time_stop():
	global __start__
	now = datetime.datetime.now()
	return " %s" % (now - __start__)

__quite_mode__ = False

def enable_quite_mode():
	global __quite_mode__
	__quite_mode__ = True

def disable_quite_mode():
	global __quite_mode__
	__quite_mode__ = False

def print_time_consume():
	print "The time used in this calculation is %s" % time_stop()

def print_head(number, title=None):
	if title:
		print "\nProblem %03d: %s \n" % (number, title)
	else:
		print "\nProblem %03d \n" % number
	time_start()

def print_result(result, msg=None):
	if msg:
		print "%s %s" % (msg, result)
	else:
		print "Answer is %s" % result

	print_time_consume()

def log(s):
	if __quite_mode__ == False:
		print "> %s" % s

