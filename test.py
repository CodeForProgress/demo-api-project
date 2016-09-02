import urllib2
import json
import pprint

govTrack = "300001"

f = urllib2.urlopen('https://www.govtrack.us/api/v2/vote_voter?person=' + govTrack)
json_string = f.read()
parsed_json = json.loads(json_string)
govtrackObject = parsed_json
f.close()

# pprint.pprint(govtrackObject['objects'][1]['option']['value'])

for bill in govtrackObject['objects']:
	print bill['option']['value']
	
