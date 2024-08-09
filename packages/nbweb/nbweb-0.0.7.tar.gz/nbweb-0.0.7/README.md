# nbweb
nbweb is short for no bloat web

## description
nbweb extracts the clean information from websites removing all the bloat.

## installation
```sh
pip install nbweb
```

## usage
```sh
nbweb <url>

# return output in text format
nbweb --format=txt <url>

# return rss feed
nbweb --rss <url>

# check if website is supported
nbweb --supported <url>
```

## supported websites
list of supported websites can be found in the 'data.json' file

## features
* output as text or json 
* auto delete cache after 7 days
* return rss feed (only 1 website supported)
* checks if site is supported

## note
- this application is currently in experimental phase
