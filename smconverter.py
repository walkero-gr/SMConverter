#!/usr/bin/python

import sys, getopt, json
from pprint import pprint

ver = "0.1"

def introText():
	print "\nSession Manager Converter v" + ver
	print "Created by George Sokianos"
	
def helpText():
	introText()
	print "https://github.com/walkero-gr/SMConverter"
	print "This python script converts the Session Manager data to a plain list file\n"
	print "smconverter.py [-h,-v] -i <inputfile> [-o <outputfile>]\n"
	print "-h\t\tReturns this help text"
	print "-v|--verbose\tReturns more info in the output"
	print "-i|--ifile\tThe input file from Session Manager"
	print "-o|--ofile\tThe output file with the list of the url.\n\t\tCAUTION: Currently the script overrides the file, if it exists"


def parseData(rawdata):	
	introText()
	totalURLs = 0
	outputMessage = ""
	# @todo Add a check here if the file exists
	
	outputFileObj = open(outputfile, "w")	
	
	outputMessage += "Found " + str(len(rawdata["windows"])) + " Windows\n"
	
	for winidx, windows in enumerate(rawdata["windows"]):
		num_tabs = len(windows["tabs"])
		outputMessage += "Window: " + str(winidx + 1) + " has " + str(num_tabs+1) + " open tabs.\n"
		
		if verbose > 0:
			print "\n### Window " + str(winidx + 1) + " ================================================================"
		for rowidx, rows in enumerate(windows["tabs"]):
			try:
				url = rows["entries"][0]["url"]
				outputFileObj.write(url + '\n')
				totalURLs += 1
				if verbose > 0:
					print "Tab: " + str(rowidx) + " ----------> " + url
				
			except IndexError:
				pass
			
	# Close the output file
	outputFileObj.close()
	
	# Show final text after the conversion completed
	print "\nConversion Completed:"
	print outputMessage
	print "URLs saved at the file: " + outputfile + "\n"
	

def main(argv):
	global outputfile, verbose
	inputfile = ''
	outputfile = ''
	verbose = 0
	
	try:
		opts, args = getopt.getopt(argv,"hvi:o:",["verbose","ifile=","ofile="])
	except getopt.GetoptError:
		helpText()
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			helpText()
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg.strip()
		elif opt in ("-o", "--ofile"):
			outputfile = arg.strip()
		elif opt in ("-v", "--verbose"):
			verbose = 1
	if len(sys.argv) < 2:
		helpText()
		sys.exit()
	
	# Check if the user provided an input file name. If not show the helpText and exit
	if inputfile == "":
		helpText()
		sys.exit()
	else:
		if outputfile == "":
			outputfile = inputfile + "_export"

		try:
			inputFileObj = open(inputfile, "r")
			num_lines = sum(1 for line in inputFileObj)
			position = inputFileObj.seek(0, 0);
			cnt = 0;
			while (cnt < num_lines):
				fileLine = inputFileObj.readline()
				firstChar = fileLine[:1]
				if firstChar == '{':
					data = json.loads(fileLine)
					parseData(data)
				cnt += 1
			# Close the input file
			inputFileObj.close()
		except IOError:
			print "Error: can\'t find the file ", inputfile
	

if __name__ == "__main__":
	main(sys.argv[1:])

