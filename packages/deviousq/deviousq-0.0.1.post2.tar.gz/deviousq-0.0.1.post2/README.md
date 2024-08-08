`deviousq` is a command-line utility for querying the RSS API endpoint of the
online art sharing community DeviantArt.

## Installation
To install from PyPI, run:

```
pip install deviousq
```

To clone the source repository, run:

```
git clone git@gitlab.com:afeder/deviousq.git
```

## Usage
```
usage: deviousq [-h] [-v] [-e ENDPOINT] [-q] [-l LIMIT] [-r ORDER] [-i OFFSET] [-p PAGE] [-P PAGES]
                [--start-date START_DATE] [--end-date END_DATE] [--rating RATING] [--category CATEGORY]
                [--author AUTHOR] [--gallery GALLERY] [--min-width MIN_WIDTH] [--max-width MAX_WIDTH]
                [--min-height MIN_HEIGHT] [--max-height MAX_HEIGHT] [--no-blurred-content] [--no-query-author]
                [-o OUTPUT_TO] [-t {flat,json,csv}] [-k RETURN_FIELD] [-d DOWNLOAD_TO]
                [--skip-download-exists]
                [search_terms ...]
```

By default, the utility queries the official DeviantArt endpoint for a list of
items ("deviations") related to zero or more search terms.

If the value of the `--order` option is 9 or "popularity", the list is ordered
by most popular first (this is the server-side default); if the value of
`--order` is 5 or "time", the list is ordered by newest first (this is forced
for queries on author or gallery).

An offset into the list may be specified with the `--offset` option, and an
upper limit on the number of items to return from the list per query (up to a
maximum of 60) may be specified with the `--limit` option.

If a page number is specified with the `--page` option, the effective offset is
increased by the page number multiplied by the limit. If a number of pages to
return is specified with the `--pages` option, the endpoint is queried up to
that number of times to return all items contained in that number of consecutive
pages.

The list of items to return may be reduced by applying any number of filters on
publication date (`--start-date` and `--end-date`), maturity rating
(`--rating`), category (`--category`), author username (`--author`), gallery
name (`--gallery`), and content width (`--min-width` and `--max-width`) and
height (`--min-height` and `--max-height`).

In default operation, a flat list with one URL representing each resulting
item, separated by newline characters, is output to `stdout`; if a field name
is specified with the `--return-field` option, then the value of the given
field is output for each result in flat mode. If a different output format
is specified with `--output-format`, a wider range of metadata is output for
each result in the given serialization format. If a download directory is
specified with the `--download-to` option, then the content URL of each result
is downloaded to that directory, and only the relative path to each
downloaded file is output. Finally if the `--return-query` flag is specified,
no queries are executed at all; instead only the URLs of the queries
corresponding to the input options are output.

If an output file is specified with `--output-to`, the generated output is
written to that file instead of `stdout`.

Run the command with the option `--help` for a list of descriptions of all
supported command-line options.

## Examples
Get a list of URLs of deviations related to the search term `ocean`, sorted
according to the server-side default (most popular first):

```
deviousq ocean
```

Get a list of URLs of deviations related to the search term `forest`, sorted by
newest first:

```
deviousq forest --order time
```

Get 5 pages of up to 30 results each with the URLs of deviations related to the
search term `landscapes`:

```
deviousq --pages 5 --limit 30 landscapes
```

Get a list of URLs of deviations posted by the user `spyed`, sorted according to
the only order supported by the server (newest first):

```
deviousq --author spyed
```

Get a list of URLs of deviations posted by the user `spyed` to their "Featured"
gallery (the gallery identifier was obtained manually by visiting the user's
web page on DeviantArt and looking at the address of the link to the gallery),
sorted according to the only order supported by the server (newest first):

```
deviousq --gallery spyed/4788
```

Get a list of URLs of the content media of deviations related to the search term
`portrait`:

```
deviousq --return-field content_url portrait
```

Download the content media of deviations related to the search term
`magicalrealms` to the directory `/tmp/downloads`:

```
deviousq --download-to /tmp/downloads magicalrealms
```

Get a list of deviations related to the search term `painting` and output their
metadata in JSON format to the file `/tmp/results.json`:

```
deviousq --output-format json --output-to /tmp/results.json painting
```
