from __future__ import print_function
import argparse
import os
import subprocess

cur_dir = os.path.dirname(os.path.realpath(__file__))

def test_toy(timelimit):
	buggyprograms = []
	with open(cur_dir + '/toy_example_distrib/yield.txt') as f:
		line = f.readline()
		while line:
			words = line.split()
			if (len(words) == 2 and words[1] == 'succeeded'):
				buggyprograms.append(words[0])
			line = f.readline()

	for num in buggyprograms:
		with open(cur_dir + '/results/' + num + '.txt', "w") as f:
			subprocess.call(['smack', '--unroll', '2', '--time-limit', str(timelimit), '--only-check-valid-deref', cur_dir + '/toy_example_distrib/buggy/' + num + '/toy/toy.c'], stdout=f)

		file_string = ""

		with open(cur_dir + '/results/' + num + '.txt', "r") as f:
			file_string = f.read()
			print(num + ' ', end='')
			if 'SMACK found no errors' in file_string:
				print("No bug found")
			elif 'SMACK timed out' in file_string:
				print("Timed out")
			else:
				print("Bug found")

	
	# for num in buggyprograms:
	# 	if not os.path.isdir(cur_dir + '/toy_example_distrib/buggy/' + str(num)):
	# 		print("couldn't find: " + str(num))
	print(len(buggyprograms))
	# subprocess.call(['smack', '--time-limit', timelimit, '--only-check-valid-deref', cur_dir + '/toy_example_distrib/buggy/2/toy/toy.c'])

def test_1(timelimit):
	print("Benchmarking with LAVA-1 has not been implemented")

def test_M(timelimit):
	print("Benchmarking with LAVA-M has not been implemented")


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Benchmark SMACK against pieces of the LAVA corpora')
	parser.add_argument('--lavaset', default='toy', choices=['toy', '1', 'M'], help='LAVA dataset to analyze [default: toy]')
	parser.add_argument('--time-limit', dest='timelimit', default=1200, type=int, help='Time limit of each smack run in seconds. [default: 1200]')

	args = parser.parse_args()
	
	if args.lavaset == "toy":
		test_toy(args.timelimit)
	elif args.lavaset == "1":
		test_1(args.timelimit)
	elif args.lavaset == "M":
		test_M(args.timelimit)