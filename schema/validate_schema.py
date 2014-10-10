#!/usr/bin/env python

"""validate_schema.py: validates the osm-thematic schema."""

__author__      = "Mathias Versichele"

import json
from jsonschema import *
#from jsonschema import Draft4Validator
from pprint import pprint

schema_data=open('osm-thematic.schema')
schema = json.load(schema_data)
try:
	Draft4Validator.check_schema(schema)
	print "Schema is valid!"
except SchemaError as e:
	print "Schema is invalid!"
	print e
schema_data.close()