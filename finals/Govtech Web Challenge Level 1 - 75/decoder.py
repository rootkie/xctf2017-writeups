import requests

dict = {}

for i in range(32,127):
	r = requests.post('http://govtech-challenge.com/challenge/challenge1-first-puzzle.php', data = {'answer':chr(i)})
	matched_lines = [line for line in r.content.split('\n') if "Encoded" in line]
	print chr(i) + " - " + matched_lines[0][-4:]
	dict[matched_lines[0][-4:]] = chr(i)

todecode = "BCBCBADABCABBABDBDCDBDBABCBBBCADBCCABBDDBAACBCABBDADBCBBADBABDDB"

for i in range(len(todecode)/4):
	print(dict[todecode[i*4:(i*4)+4]])
