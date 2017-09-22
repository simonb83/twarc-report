#!/usr/bin/env python            

import json
import optparse
from profiler import Profiler # local module
import dateutil.parser # $ pip install python-dateutil
# import sparkline

opt_parser = optparse.OptionParser()
opt_parser.add_option("-o", "--output", dest="output", type="str", 
    help="text | json (default: text)", default="text")
opts, args = opt_parser.parse_args()

profiler = Profiler({"extended": True, "blocks": ["all"]})

profiler.gettweets(opts, args)

data = profiler.report()

if (opts.output == "json"):
    print(json.dumps(data))
else:
    print ("Count:            " + "{:>9}".format(str(data["count"])))
    print ("Users:            " + "{:>9}".format(str(data["usercount"])))
    print ("User percentiles: " + str(data["userspercentiles"]))
    print ("                  " + str(data["userspercentiles"]))
    print ("Has hashtag:      " + "{:>9}".format(str(data["hashtagcount"])) + " (" + str("%.2f" % (float(data["hashtagcount"]) / float(data["count"]) * 100.0)) + "%)")
    print ("Hashtags:         " + "{:>9}".format(str(data["hashtags"])))
    print ("Hashtags percentiles: " + str(data["hashtagspercentiles"]))
    print ("                  " + str(data["hashtagspercentiles"]))
    print ("Has URL:          " + "{:>9}".format(str(data["urlcount"])) + " (" + str("%.2f" % (float(data["urlcount"]) / float(data["count"]) * 100.0)) + "%)")
    print ("URLs:             " + "{:>9}".format(str(data["urls"])))
    print ("URLs percentiles: " + str(data["urlspercentiles"]))
    print ("                  " + str(data["urlspercentiles"]))
    print ("Has Image URL:    " + "{:>9}".format(str(data["imageurlcount"])) + " (" + str("%.2f" % (float(data["imageurlcount"]) / float(data["count"]) * 100.0)) + "%)")
    print ("Image URLs:       " + "{:>9}".format(str(data["imageurls"])))
    print ("Image URLs percentiles: " + str(data["imageurlspercentiles"]))
    print ("                  " + str(data["imageurlspercentiles"]))
    print ("Retweets:         " + "{:>9}".format(str(data["retweetcount"])) + " (" + str("%.2f" % (float(data["retweetcount"]) / float(data["count"]) * 100.0)) + "%)")
    print ("Geo:              " + "{:>9}".format(str(data["geocount"])) + " (" + str("%.2f" % (float(data["geocount"]) / float(data["count"]) * 100.0)) + "%)")
    print ("Earliest:         " + str(data["earliest"]))
    print ("Latest:           " + str(data["latest"]))
    print ("Duration:         " + str(dateutil.parser.parse(data["latest"]) - dateutil.parser.parse(data["earliest"])))

    print ("Top users:        " + str([u["value"] for u in data["topusers"]]))
    for user in data["topusers"]:
        print ("{:>7}".format(str(user["value"])) + " " + user["name"])
    print ("Top hashtags:     " + str([u["value"] for u in data["tophashtags"]]))
    for hashtag in data["tophashtags"]:
        print ("{:>7}".format(str(hashtag["value"])) + " " + hashtag["name"])
    print ("Top URLs:         " + str([u["value"] for u in data["topurls"]]))
    for url in data["topurls"]:
        print ("{:>7}".format(str(url["value"])) + " " + url["name"])
    print ("Top Image URLs:   " + str([u["value"] for u in data["topimageurls"]]))
    for imageurl in data["topimageurls"]:
        print ("{:>7}".format(str(imageurl["value"])) + " " + imageurl["name"])
