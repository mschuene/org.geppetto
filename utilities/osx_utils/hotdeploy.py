#!/usr/bin/python

#
#	Deploys built artifacts to $SERVER_HOME/pickup
#

import os, sys, json, distutils.core, shutil, glob
from subprocess import call

serverHome = os.environ['SERVER_HOME']

def copyext(targetdir, extension):
	files = glob.iglob(os.path.join(targetdir,'*.'+extension))
	for file in files:
	    if os.path.isfile(file):
	        shutil.copy2(file, serverHome+'/pickup/')

def main(argv):
	serverHome = os.environ['SERVER_HOME']
	targetdir = os.path.join(os.path.realpath('./target'))
	copyext(targetdir, 'jar')
	copyext(targetdir, 'war')
	copyext(targetdir+'/classes/lib', 'jar')
	copyext(targetdir+'/classes/lib', 'war')

	#shutil.copy2(os.path.realpath(sourcesdir+'/org.geppetto/geppetto.plan'), serverHome+'/pickup')
	print 'Geppetto build deployed to virgo'

if __name__ == "__main__":
	main(sys.argv[1:])
