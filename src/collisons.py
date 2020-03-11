import random

def how_many_before_collision(buckets, loops=1):
	"""
	How many rolls before collision?

	Run loops times
	"""

	for i in range(loops):
		tries = 0
		tried = set()

		tried_list = []

		while True:
			random_key = str(random.random())
			hash_index = hash(random_key) % buckets
			if hash_index not in tried:
				tried.add(hash_index)
				tries += 1
			
			else:
				break
		print(f"{buckets} buckets, {tries} hashes before collision. ({tries/buckets * 100:.1f}%)")

how_many_before_collision(10000, 10)