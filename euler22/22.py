print sum([(i * sum([ord(k) - ord('A') + 1 for k in j])) for (i, j) in zip(xrange(1,1000000), sorted(open("names.txt").readline().replace('"','').split(",")))])
