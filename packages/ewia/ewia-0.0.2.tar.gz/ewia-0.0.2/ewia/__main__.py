#!/usr/bin/env python3
#
#   ewia - A library to calculate astrophysical object positions
#   Copyright (C) 2017-2024 Johannes Bauer
#
#   This file is part of Ewia.
#
#    Ewia is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; this program is ONLY licensed under
#    version 2 of the License, later versions are explicitly excluded.
#
#    Ewia is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Ewia; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#   Johannes Bauer <JohannesBauer@gmx.de>

import sys
import ewia
import datetime
from .FriendlyArgumentParser import FriendlyArgumentParser

def main():
	parser = FriendlyArgumentParser()
	parser.add_argument("--json", action = "store_true", help = "Output data in JSON format.")
	parser.add_argument("-c", "--user-catalog", metavar = "filename", type = str, action = "append", default = [ ], help = "Specifies user catalogs to read after system catalogs have been read.")
	parser.add_argument("--no-system-catalog", action = "store_true", help = "Do not read system catalogs (by default, ~/.config/ewia/catalog.json and ./.catalog.json are tried)")
	parser.add_argument("-l", "--observer-location", metavar = "location", type = str, required = True, help = "Observer location on earth. Can be either a reference to the catalog or actual coordinates.")
	parser.add_argument("-t", "--observation-time", metavar = "timestamp", type = str, default = "now", help = "Time at which the observation is conducted. Accepts the special argument 'now', which reflects the current time. Otherwise, must be in format YYYY-mm-dd HH:MM:SS.")
	parser.add_argument("-z", "--observation-timezone", metavar = "tzone", type = str, default = "auto", help = "When a timestamp is given, this parameter influences at which timezone the timestamp is interpreted to be in. Can either be a timezone definition such as 'Europe/Berlin' or a static timezone such as 'utc' or 'Etc/GMT+8'. Alternatively, can be set to 'auto' in order to take the timezone that has been specified in the catalog for the observing location. Defaults to %(default)s.")
	parser.add_argument("-v", "--verbose", action = "count", default = 0, help = "Increase verbosity of output. Can be specified multiple times.")
	parser.add_argument("objects", metavar = "object", nargs = "+", help = "Object under observation. Must refer to the catalog.")
	args = parser.parse_args(sys.argv[1:])

	catalog = ewia.ObjectCatalog()
	if not args.no_system_catalog:
		for system_catalog_filename in [ "~/.config/ewia/catalog.json", ".catalog.json" ]:
			catalog.append_from_file(system_catalog_filename, fail_on_error = False)
	for user_catalog_filename in args.user_catalog:
		catalog.append_from_file(user_catalog_filename, fail_on_error = True)

	try:
		observer = catalog.get_observer(args.observer_location)
	except KeyError as e:
		print("No such observer location '%s' found in catalogs." % (args.observer_location))
		sys.exit(1)

	if args.observation_timezone == "auto":
		# Local time, take timezone form observer location timezone
		if observer.timezone is None:
			print("Cannot use timezone of observer location '%s', because it is not set in catalog." % (args.observer_location))
			sys.exit(1)
		timezone = observer.timezone
	else:
		timezone = args.observation_timezone

	if args.observation_time == "now":
		# Timezone automatically UTC
		obstime = ewia.Time(datetime.datetime.utcnow())
	else:
		timestamp = datetime.datetime.strptime(args.observation_time, "%Y-%m-%d %H:%M:%S")
		obstime = ewia.Time.from_localtime(timestamp, timezone)

	if args.verbose >= 1:
		print("Observation time: %s" % (obstime), file = sys.stderr)

	data_printer = ewia.DataPrinter(args.observer_location, observer, [ obstime ], timezone)
	for obs_object_name in args.objects:
		try:
			obs_object = catalog.get_object(obs_object_name)
		except KeyError:
			print("Cannot find object by name '%s' in catalogs." % (obs_object_name))
			sys.exit(1)

		data_printer.add_object(obs_object_name, obs_object)
	if args.json:
		print(data_printer.json())
	else:
		data_printer.dump()

if __name__ == "__main__":
	main()
