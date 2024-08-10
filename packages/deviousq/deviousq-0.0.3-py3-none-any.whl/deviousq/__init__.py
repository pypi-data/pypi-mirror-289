#!/usr/bin/env python3
from abc import ABC, abstractmethod
from contextlib import ExitStack
import sys
import os
import logging
from dateutil.tz import gettz
from datetime import datetime
import asyncio
import argparse
import aiohttp
from urllib.parse import urlencode, urlparse
from xml.etree import ElementTree as ET
from dateutil import parser as date_parser

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

__version__ = '0.0.3'

DEFAULT_ENDPOINT_BASE_URL = 'https://backend.deviantart.com/rss.xml'

# Mapping for order values.
ORDER_MAP = {
    'time': 5,
    'popularity': 9
}

# Reverse mapping for order values.
ORDER_REVERSE_MAP = {value: key for key, value in ORDER_MAP.items()}

# Mapping for common timezone abbreviations to their corresponding time zones.
TZINFOS = {
    'PST': gettz('US/Pacific'),
    'PDT': gettz('US/Pacific'),
    'EST': gettz('US/Eastern'),
    'EDT': gettz('US/Eastern'),
    'CST': gettz('US/Central'),
    'CDT': gettz('US/Central'),
    'MST': gettz('US/Mountain'),
    'MDT': gettz('US/Mountain'),
}

# Field names for CSV output.
FIELDNAMES = [
    'title',
    'link',
    'pub_date',
    'rating',
    'authors',
    'author',
    'avatar',
    'copyright',
    'content',
    'content_url',
    'content_filename',
    'content_blurred',
    'content_width',
    'content_height',
    'content_medium',
    'thumbnails',
    'thumbnail_urls',
    'thumbnail_url',
    'description'
]

class Endpoint:
    """Represents a DeviantArt RSS API endpoint."""

    def __init__(self, base_url=DEFAULT_ENDPOINT_BASE_URL):
        """
        Initializes an Endpoint instance with a base URL.

        Args:
            base_url (str): The base endpoint URL to build queries on.
        """
        self.base_url = base_url
        logging.debug(f'Initialized Endpoint with base_url: {self.base_url}')

    def build_query_url(self, search_terms=None, limit=10, order=9, offset=0, author=None, gallery=None):
        """
        Constructs a query URL based on provided parameters.

        Args:
            search_terms (str): Terms to search for.
            limit (int): Maximum number of results to return.
            order (int): Sorting order of results.
            offset (int): Offset to return results from.
            author (str): Author to query on.
            gallery (str): Gallery to query on.

        Returns:
            str: The constructed query URL.
        """
        params = {
            'type': 'deviation',
            'offset': offset,
            'limit': limit
        }

        if search_terms:
            params['q'] = ' '.join(search_terms)
        if author:
            params['q'] = (params.get('q', '') + f' by:{author}').strip()
        elif gallery:
            params['q'] = (params.get('q', '') + f' gallery:{gallery}').strip()
        elif order:
            params['order'] = order
            if order in ORDER_REVERSE_MAP:
                sort = ORDER_REVERSE_MAP[order]
                params['q'] = (params.get('q', '') + f' sort:{sort}').strip()

        url = f'{self.base_url}?{urlencode(params)}'
        logging.debug(f'Constructed query URL: {url}')
        return url

    async def __aenter__(self):
        logging.debug('Entering Endpoint context.')
        self.session = aiohttp.ClientSession()

    async def fetch(self, url):
        """
        Fetches data from a given URL.

        Args:
            url (str): The URL to fetch data from.

        Returns:
            str: The response content from the URL.
        """
        logging.debug(f'Fetching: {url}')
        try:
            async with self.session.get(url) as response:
                response.raise_for_status()
                logging.info(f'Response status: {response.status}')
                return await response.text()
        except aiohttp.ClientError as e:
            logging.error(f'Error fetching URL: {e}')
            return None

    async def query(self, search_terms, limit, order, offset, author, gallery):
        """
        Executes a query with the specified parameters against the endpoint.

        Args:
            search_terms (str): Terms to search for.
            limit (int): Maximum number of results to return.
            order (int): Sorting order of results.
            offset (int): Offset to return results from.
            author (str): Author to query on.
            gallery (str): Gallery to query on.

        Returns:
            dict, str: The arguments the function was invoked with and the query
            result data.
        """
        # Get the query parameters before defining any other locals.
        query_params = locals()
        url = self.build_query_url(search_terms, limit, order, offset, author, gallery)
        logging.info(f'Querying: {url}')
        pending_xml_data = self.fetch(url)
        xml_data = await pending_xml_data if pending_xml_data else None
        return query_params, xml_data

    async def __aexit__(self, exc_type, exc_value, traceback):
        logging.debug('Exiting Endpoint context.')
        await self.session.close()

class EndpointDry(Endpoint):
    """A 'dry-run' Endpoint that outputs constructed queries instead of
    executing them."""

    def __init__(self, base_url=DEFAULT_ENDPOINT_BASE_URL, out_stream=sys.stdout):
        """
        Initializes an EndpointDry instance with a base URL and an output
        stream.

        Args:
            base_url (str): The base endpoint URL to build queries on.
            out_stream (TextIO): Stream to output queries to.
        """
        super(EndpointDry, self).__init__(base_url)
        self.out_stream = out_stream

    async def __aenter__(self):
        logging.debug('Entering EndpointDry context.')
        pass

    def fetch(self, url):
        """
        Outputs the given URL to the configured output stream.

        Args:
            url (str): The URL to output.
        """

        self.out_stream.write(url + '\n')

    async def __aexit__(self, exc_type, exc_value, traceback):
        logging.debug('Exiting EndpointDry context.')
        pass

class PageProcessor(ABC):
    """Processes pages of RSS XML data from the DeviantArt RSS API endpoint.
    Each page is processed into results, which are then filtered according to
    the initialization parameters. The process_result method must be implemented
    by subclasses and is called for each result in the order they are
    encountered in the page."""

    # This constant signals to the user whether it is recommended that they
    # inject pages to this processor in order. For instance, for a processor
    # generating a JSON representation that is supposed to track the source data
    # closely it may be recommended, but for a processor just bulk downloading
    # files referenced by the source data there may be no recommendation either
    # way. For large sets of pages, there can be a performance benefit in
    # injecting them in whichever order they arrive in first, at the possible
    # expense of source fidelity.
    RECOMMENDS_INJECTING_DATA_IN_ORDER = True

    @staticmethod
    def filter_items(items, start_date_filter=None, end_date_filter=None, rating_filter=None, medium_filter=None, author_filter=None, min_width_filter=None, max_width_filter=None, min_height_filter=None, max_height_filter=None, no_blurred_content=False):
        namespaces = {
            'media': 'http://search.yahoo.com/mrss/'
        }

        filtered_items = []

        for item in items:
            pub_date_el = item.find('pubDate')
            pub_date = date_parser.parse(pub_date_el.text, tzinfos=TZINFOS) if pub_date_el is not None else None
            # Apply date filtering.
            if start_date_filter and (pub_date is None or pub_date < start_date_filter):
                logging.info(f'Skipping item due to start_date_filter: {pub_date}')
                continue
            if end_date_filter and (pub_date is None or pub_date > end_date_filter):
                logging.info(f'Skipping item due to end_date_filter: {pub_date}')
                continue

            # Apply rating filtering.
            rating_el = item.find('media:rating', namespaces)
            rating = rating_el.text if rating_el is not None else None
            if rating_filter and (rating is None or rating != rating_filter):
                logging.info(f'Skipping item due to rating_filter: {rating}')
                continue

            # Apply author filtering.
            authors = [credit.text for credit in item.findall("media:credit[@role='author']", namespaces)]
            if author_filter:
                author_filter_lower = author_filter.lower()
                if not any(author.lower() == author_filter_lower for author in authors):
                    logging.info(f'Skipping item due to author_filter: {authors}')
                    continue

            # Apply content filtering.
            content_el = item.find('media:content', namespaces)
            content = content_el.attrib if content_el is not None else None
            content_url = content['url'] if content is not None else None
            content_url_parsed = urlparse(content_url) if content_url is not None else None
            content_filename = os.path.basename(content_url_parsed.path) if content_url_parsed is not None else None
            content_dirname = os.path.dirname(content_url_parsed.path) if content_url_parsed is not None else None
            content_transform_parameters = os.path.basename(content_dirname) if content_dirname is not None else None
            content_blurred = 'blur_' in content_transform_parameters if content_transform_parameters is not None else None
            content_width_str = content.get('width', None) if content is not None else None
            content_width = int(content_width_str) if content_width_str is not None else None
            content_height_str = content.get('height', None) if content is not None else None
            content_height = int(content_height_str) if content_height_str is not None else None
            content_medium = content.get('medium', None) if content is not None else None
            if min_width_filter is not None and (content_width is None or content_width < min_width_filter):
                logging.info(f'Skipping item due to min_width_filter: {content_width}')
                continue
            if max_width_filter is not None and (content_width is None or content_width > max_width_filter):
                logging.info(f'Skipping item due to max_width_filter: {content_width}')
                continue
            if min_height_filter is not None and (content_height is None or content_height < min_height_filter):
                logging.info(f'Skipping item due to min_height_filter: {content_height}')
                continue
            if max_height_filter is not None and (content_height is None or content_height > max_height_filter):
                logging.info(f'Skipping item due to max_height_filter: {content_height}')
                continue
            if medium_filter is not None and (medium_filter is None or content_medium != medium_filter):
                logging.info(f'Skipping item due to medium_filter: {content_medium}')
                continue
            if no_blurred_content and content_blurred:
                logging.info(f'Skipping item due to no_blurred_content: {content_blurred}')
                continue

            # Extract additional details.
            author = authors[0] if authors else None
            avatar = authors[1] if authors and len(authors) >= 2 else None
            copyright_el = item.find('media:copyright', namespaces)
            copyright = copyright_el.text if copyright_el is not None else None

            thumbnail_els = item.findall('media:thumbnail', namespaces)
            thumbnails = [thumbnail_el.attrib for thumbnail_el in thumbnail_els]
            thumbnail_urls = [thumbnail['url'] for thumbnail in thumbnails]
            thumbnail_url = thumbnail_urls[0] if thumbnail_urls else None

            description_el = item.find('description', namespaces)
            description = description_el.text if description_el is not None else None

            filtered_items.append({
                'title': item.find('title').text,
                'link': item.find('link').text,
                'pub_date': pub_date,
                'rating': rating,
                'authors': authors,
                'author': author,
                'avatar': avatar,
                'copyright': copyright,
                'content': content,
                'content_url': content_url,
                'content_filename': content_filename,
                'content_blurred': content_blurred,
                'content_width': content_width,
                'content_height': content_height,
                'content_medium': content_medium,
                'thumbnails': thumbnails,
                'thumbnail_urls': thumbnail_urls,
                'thumbnail_url': thumbnail_url,
                'description': description
            })
        return filtered_items

    def __init__(self, out_stream=sys.stdout, start_date_filter=None, end_date_filter=None, rating_filter=None, medium_filter=None, author_filter=None, min_width_filter=None, max_width_filter=None, min_height_filter=None, max_height_filter=None, no_blurred_content=False):
        """
        Initializes a PageProcessor instance with specified filters and output
        settings.

        Args:
            out_stream (TextIO): Stream to output processed results to.
            start_date_filter (datetime): Start date to filter results by.
            end_date_filter (datetime): End date to filter results by.
            rating_filter (str): Rating to filter results by.
            medium_filter (str): Content medium to filter results by.
            author_filter (str): Author to filter results by.
            min_width_filter (int): Minimum width to filter results by.
            max_width_filter (int): Maximum width to filter results by.
            min_height_filter (int): Minimum height to filter results by.
            max_height_filter (int): Maximum height to filter results by.
            no_blurred_content (bool): Whether to exclude results with blurred content.
        """
        self.out_stream = out_stream
        self.start_date_filter = start_date_filter
        self.end_date_filter = end_date_filter
        self.rating_filter = rating_filter
        self.medium_filter = medium_filter
        self.author_filter = author_filter
        self.min_width_filter = min_width_filter
        self.max_width_filter = max_width_filter
        self.min_height_filter = min_height_filter
        self.max_height_filter = max_height_filter
        self.no_blurred_content = no_blurred_content

    async def __aenter__(self):
        logging.debug('Entering PageProcessor context.')
        pass

    @abstractmethod
    def process_result(self, result):
        """
        Abstract method invoked to process one query result item.

        Args:
            result (dict): The query result item to process.
        """
        pass

    def process_page(self, xml_data):
        """
        Extracts result items from a page of RSS XML data, filters them
        against configured filters, and submits them to processing.

        Args:
            xml_data (str): The RSS XML data to process.

        Returns:
            int: The number of items found in the XML data.
        """
        try:
            logging.info('Processing a new page of XML data.')
            root = ET.fromstring(xml_data)
            items = root.findall('channel/item')
            items_found = len(items)
            logging.debug(f'Number of items found in page: {items_found}')
            results = self.filter_items(items, self.start_date_filter, self.end_date_filter, self.rating_filter, self.medium_filter, self.author_filter, self.min_width_filter, self.max_width_filter, self.min_height_filter, self.max_height_filter, self.no_blurred_content)
            logging.debug(f'Number of results after filtering: {len(results)}')
            for result in results:
                self.process_result(result)
            return items_found
        except Exception as e:
            logging.error(f'Error processing page: {e}')
            raise

    async def __aexit__(self, exc_type, exc_value, traceback):
        logging.debug('Exiting PageProcessor context.')
        pass

class PageProcessorFlat(PageProcessor):
    """A PageProcessor which outputs the value of a specified field from each
    encountered result followed by a newline character."""

    def __init__(self, return_field='link', out_stream=sys.stdout, start_date_filter=None, end_date_filter=None, rating_filter=None, medium_filter=None, author_filter=None, min_width_filter=None, max_width_filter=None, min_height_filter=None, max_height_filter=None, no_blurred_content=False):
        """
        Initializes a PageProcessorFlat instance for the given result field,
        output stream and set of filters.

        Args:
            return_field (str): The field to output from each result.
            out_stream (TextIO): Stream to output the field of each result to.
            start_date_filter (datetime): Start date to filter results by.
            end_date_filter (datetime): End date to filter results by.
            rating_filter (str): Rating to filter results by.
            medium_filter (str): Content medium to filter results by.
            author_filter (str): Author to filter results by.
            min_width_filter (int): Minimum width to filter results by.
            max_width_filter (int): Maximum width to filter results by.
            min_height_filter (int): Minimum height to filter results by.
            max_height_filter (int): Maximum height to filter results by.
            no_blurred_content (bool): Whether to exclude results with blurred content.
        """

        super().__init__(out_stream, start_date_filter, end_date_filter, rating_filter, medium_filter, author_filter, min_width_filter, max_width_filter, min_height_filter, max_height_filter, no_blurred_content)
        self.return_field = return_field

    def process_result(self, result):
        """
        Extracts the value of the configured field from a given result and
        outputs it to the configured output stream.

        Args:
            result (dict): The query result item to process.
        """
        value = str(result[self.return_field] if result[self.return_field] is not None else '')
        self.out_stream.write(value + '\n')

class PageProcessorJSON(PageProcessor):
    """A PageProcessor which collects all results and outputs them in JSON
    format when exited."""

    async def __aenter__(self):
        """Sets up the list to collect results in."""
        logging.debug('Entering PageProcessorJSON context.')
        self.results = []

    def process_result(self, result):
        """
        Appends a result to the list of results to be serialized to JSON.

        Args:
            result (dict): The query result item to collect.
        """
        self.results.append(result)

    async def __aexit__(self, exc_type, exc_value, traceback):
        """
        Finalizes the PageProcessorJSON context, dumping the JSON serialization
        of the collected results into the configured output stream.
        """
        logging.debug('Exiting PageProcessorJSON context.')
        import json
        json.dump(self.results, self.out_stream, default=str, indent=4)

class PageProcessorCSV(PageProcessor):
    """A PageProcessor which collects all results and outputs them in CSV
    format when exited."""

    async def __aenter__(self):
        """Sets up the list to collect results in."""
        logging.debug('Entering PageProcessorCSV context.')
        self.results = []

    def process_result(self, result):
        """
        Appends a result to the list of results to be serialized to CSV.

        Args:
            result (dict): The query result item to collect.
        """
        self.results.append(result)

    async def __aexit__(self, exc_type, exc_value, traceback):
        """
        Finalizes the PageProcessorCSV context, dumping the CSV serialization of
        the collected results into the configured output stream.
        """
        logging.debug('Exiting PageProcessorCSV context.')
        import csv
        writer = csv.DictWriter(self.out_stream, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(self.results)

class PageProcessorDownload(PageProcessor):
    """Asynchronously downloads the content URL of each result to a specified
    directory and outputs the path of each downloaded file."""

    RECOMMENDS_INJECTING_DATA_IN_ORDER = False

    def __init__(self, download_to, skip_download_exists=False, out_stream=sys.stdout, start_date_filter=None, end_date_filter=None, rating_filter=None, medium_filter=None, author_filter=None, min_width_filter=None, max_width_filter=None, min_height_filter=None, max_height_filter=None, no_blurred_content=False):
        """
        Initializes a PageProcessorDownload instance for the given download
        settings, output stream and set of filters.

        Args:
            download_to (str): Directory path to download content to.
            skip_download_exists (bool): Whether to skip downloading if the file already exists.
            out_stream (TextIO): Stream to output the JSON serialization of the results to.
            start_date_filter (datetime): Start date to filter results by.
            end_date_filter (datetime): End date to filter results by.
            rating_filter (str): Rating to filter results by.
            medium_filter (str): Content medium to filter results by.
            author_filter (str): Author to filter results by.
            min_width_filter (int): Minimum width to filter results by.
            max_width_filter (int): Maximum width to filter results by.
            min_height_filter (int): Minimum height to filter results by.
            max_height_filter (int): Maximum height to filter results by.
            no_blurred_content (bool): Whether to exclude results with blurred content.
        """
        super().__init__(out_stream, start_date_filter, end_date_filter, rating_filter, medium_filter, author_filter, min_width_filter, max_width_filter, min_height_filter, max_height_filter, no_blurred_content)
        self.download_to = download_to
        self.skip_download_exists = skip_download_exists

    async def __aenter__(self):
        """
        Creates an asynchronous HTTP client session and initializes a list to
        collect download tasks in.
        """
        logging.debug('Entering PageProcessorDownload context.')
        self.session = aiohttp.ClientSession()
        self.download_tasks = []

    async def download_content(self, content_url, path):
        """
        Downloads content from a given URL and saves it to a specified path.

        Args:
            content_url (str): The URL to download content from.
            path (str): The path of the file to save the content to.

        Raises:
            IOError: If there is an issue writing the content to the file.
        """
        if self.skip_download_exists and os.path.exists(path):
            logging.info(f'Skipping download for existing file: {path}')
            return
        try:
            logging.info(f'Downloading file from {content_url}')
            async with self.session.get(content_url) as response:
                response.raise_for_status()
                with open(path, 'wb') as f:
                    f.write(await response.read())
                logging.info(f'Downloaded and saved file: {path}')
                self.out_stream.write(os.path.relpath(path) + '\n')
        except aiohttp.ClientError as e:
            logging.error(f'Error downloading file from {content_url}: {e}\n')

    def process_result(self, result):
        """
        Collects an asynchronous download task for the content URL of the given
        query result item.

        Args:
            result (dict): The query result item to process.
        """
        if result['content_url']:
            filename = os.path.join(self.download_to, os.path.basename(urlparse(result['content_url']).path))
            task = asyncio.create_task(self.download_content(result['content_url'], filename))
            self.download_tasks.append(task)

    async def __aexit__(self, exc_type, exc_value, traceback):
        """
        Finalizes the PageProcessorDownload context, waiting for all download
        tasks to complete, and then closing the asynchronous HTTP client
        session.
        """
        logging.debug('Exiting PageProcessorDownload context.')
        await asyncio.gather(*self.download_tasks)
        logging.info('All download tasks completed.')
        await self.session.close()

async def run(search_terms, endpoint_base_url, return_query, limit, order, offset, page, pages, start_date, end_date, rating, content_medium, author, gallery, min_width, max_width, min_height, max_height, no_blurred_content, no_query_author, output_to, output_format, return_field, download_to, skip_download_exists):
    """Initializes and executes the main querying and processing flow of the
    program."""
    with ExitStack() as stack:
        out_stream = sys.stdout
        if output_to:
            out_stream = stack.enter_context(open(output_to, 'w'))

        endpoint = None
        if return_query:
            endpoint = EndpointDry(endpoint_base_url, out_stream)
        else:
            endpoint = Endpoint(endpoint_base_url)

        processor = None
        if download_to:
            processor = PageProcessorDownload(
                download_to,
                skip_download_exists,
                out_stream,
                start_date,
                end_date,
                rating,
                content_medium,
                author,
                min_width,
                max_width,
                min_height,
                max_height,
                no_blurred_content
            )
        elif output_format == 'flat':
            processor = PageProcessorFlat(
                return_field,
                out_stream,
                start_date,
                end_date,
                rating,
                content_medium,
                author,
                min_width,
                max_width,
                min_height,
                max_height,
                no_blurred_content
            )
        elif output_format == 'json':
            processor = PageProcessorJSON(
                out_stream,
                start_date,
                end_date,
                rating,
                content_medium,
                author,
                min_width,
                max_width,
                min_height,
                max_height,
                no_blurred_content
            )
        elif output_format == 'csv':
            processor = PageProcessorCSV(
                out_stream,
                start_date,
                end_date,
                rating,
                content_medium,
                author,
                min_width,
                max_width,
                min_height,
                max_height,
                no_blurred_content
            )

        async with endpoint:
            async with processor:
                ordered_query_tasks = []
                try:
                    for page_num in range(pages):
                        page_offset = offset + (page_num * limit)
                        logging.info(f'Querying page {page_num} with offset {page_offset}.')
                        query_task = asyncio.create_task(endpoint.query(search_terms, limit, order, page_offset, None if no_query_author else author, gallery))
                        ordered_query_tasks.append(query_task)
                except Exception as e:
                    logging.exception(f'An unexpected error occurred during querying: {e}')
                    sys.exit(1)
                try:
                    injecting_in_order = processor.RECOMMENDS_INJECTING_DATA_IN_ORDER
                    tasks = ordered_query_tasks if injecting_in_order else asyncio.as_completed(ordered_query_tasks)
                    # The maximum number of results the server may return
                    # (before client-side filtering) over all pages is equals to
                    # the limit (the maximum number of results per page)
                    # multiplied by the number of pages requested.
                    total_server_results_upper_bound = limit * pages
                    total_server_results_processed = 0
                    for task in tasks:
                        query_params, xml_data = await task
                        if xml_data:
                            page_server_results = processor.process_page(xml_data)
                            # If the page contained less than limit server
                            # results, that means it crossed the boundary of the
                            # total number of server results, so we can try to
                            # calculate a better upper bound from its
                            # parameters.
                            if page_server_results < query_params['limit']:
                                total_server_results_upper_bound = min(total_server_results_upper_bound, query_params['offset'] + page_server_results)
                            # Increment the count of server results processed
                            # by the number of server results contained in the
                            # page.
                            total_server_results_processed += page_server_results
                            # If the total number of server results processed
                            # now exceeds or is equal to the upper bound of the
                            # total number of server results, then any lingering
                            # pages will be past the boundary and thus empty, so
                            # we can safely abort processing without losing out
                            # on any results.
                            if total_server_results_processed >= total_server_results_upper_bound:
                                break


                except Exception as e:
                    logging.exception(f'An unexpected error occurred during processing: {e}')
                    sys.exit(1)

def main():
    """
    Entry point of the utility. Parses command-line arguments and starts the
    querying and processing flow of the program.
    """
    description = 'Query the DeviantArt RSS API endpoint.'
    epilog = """By default, the utility queries the official DeviantArt endpoint
    for a list of items ("deviations") related to zero or more search terms. If
    the value of the --order option is 9 or "popularity", the list is ordered
    by most popular first (this is the server-side default); if the value of
    --order is 5 or "time", the list is ordered by newest first (this is forced
    for queries on author or gallery). An offset into the list may be specified
    with the --offset option, and an upper limit on the number of items to
    return from the list per query (up to a maximum of 60) may be specified with
    the --limit option. If a page number is specified with the --page option,
    the effective offset is increased by the page number multiplied by the limit.
    If a number of pages to return is specified with the --pages option, the
    endpoint is queried up to that number of times to return all items contained
    in that number of consecutive pages. The list of items to return may be
    reduced by applying any number of filters on publication date (--start-date
    and --end-date), maturity rating (--rating), content medium (--medium),
    author username (--author), gallery name (--gallery), and content width
    (--min-width and --max-width) and height (--min-height and --max-height).
    In default operation, a flat list with one URL representing each resulting
    item, separated by newline characters, is output to stdout; if a field name
    is specified with the --return-field option, then the value of the given
    field is output for each result in flat mode. If a different output format
    is specified with --output-format, a wider range of metadata is output for
    each result in the given serialization format. If a download directory is
    specified with the --download-to option, then the content URL of each result
    is downloaded to that directory, and only the relative path to each
    downloaded file is output. Finally if the --return-query flag is specified,
    no queries are executed at all; instead only the URLs of the queries
    corresponding to the input options are output. If an output file is
    specified with --output-to, the generated output is written to that file
    instead of stdout."""
    parser = argparse.ArgumentParser(description=description, epilog=epilog)

    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}')

    # Group for endpoint options.
    group_endpoint = parser.add_argument_group('endpoint options')
    group_endpoint.add_argument('-e', '--endpoint', type=str, default=DEFAULT_ENDPOINT_BASE_URL, help='base URL of endpoint to query (default: the official endpoint base URL)')
    group_endpoint.add_argument('-q', '--return-query', action='store_true', help='output the URL of each generated query instead of fetching results')

    # Group for query options.
    group_query = parser.add_argument_group('query options', 'basic parameters of the query')
    group_query.add_argument('search_terms', help='search terms to query for; has no effect for queries on author or gallery', nargs='*', default=[])
    group_query.add_argument('-l', '--limit', type=int, default=60, help='number of results to return per page (default: 60)')
    group_query.add_argument('-r', '--order', type=str, default=None, help='order of results: 5 or "time" for newest first, or 9 or "popularity" for most popular first (default: None); has no effect for queries on author or gallery')
    group_query.add_argument('-i', '--offset', type=int, default=0, help='base offset for pagination (default: 0)')
    group_query.add_argument('-p', '--page', type=int, default=0, help='number of first page to fetch relative to offset (default: 0)')
    group_query.add_argument('-P', '--pages', type=int, default=1, help='number of pages to fetch (default: 1)')

    # Group for filter options.
    current_date = datetime.now().date().strftime("%Y-%m-%d")
    group_filter = parser.add_argument_group('filter options', 'control which results to return')
    group_filter.add_argument('--start-date', type=str, help='start date to filter results by (e.g. "2017-06-15")', required=False)
    group_filter.add_argument('--end-date', type=str, help=f'end date to filter results by (e.g. "{current_date}")', required=False)
    group_filter.add_argument('--rating', type=str, help='maturity rating to filter results by (e.g. "nonadult")', required=False)
    group_filter.add_argument('--medium', type=str, help='content medium to filter results by (e.g. "image")', required=False)
    group_filter.add_argument('--author', type=str, help='author to filter results by (e.g. "spyed")', required=False)
    group_filter.add_argument('--gallery', type=str, help='gallery to filter results by (e.g. "spyed/4788")', required=False)
    group_filter.add_argument('--min-width', type=int, help='minimum content width to filter results by', required=False)
    group_filter.add_argument('--max-width', type=int, help='maximum content width to filter results by', required=False)
    group_filter.add_argument('--min-height', type=int, help='minimum content height to filter results by', required=False)
    group_filter.add_argument('--max-height', type=int, help='maximum content height to filter results by', required=False)
    group_filter.add_argument('--no-blurred-content', action='store_true', help='exclude results whose content has been blurred (for-pay content)')
    group_filter.add_argument('--no-query-author', action='store_true', help='don\'t query on author if one is given, only apply the filter on client side')

    # Group for processing options.
    group_processing = parser.add_argument_group('processing options', 'control how results are processed')
    group_processing.add_argument('-o', '--output-to', type=str, help='save the generated output to the specified file', required=False)
    group_processing.add_argument('-t', '--output-format', type=str, choices=['flat', 'json', 'csv'], default='flat', help='format to output results in (default: "flat")')
    group_processing.add_argument('-k', '--return-field', type=str, default='link', help='key of field to output for each result in flat mode (default: "link")')
    group_processing.add_argument('-d', '--download-to', type=str, help='download the content URL of each result to the specified directory and output filename of each downloaded file', required=False)
    group_processing.add_argument('--skip-download-exists', action='store_true', help='skip downloading files whose filename already exists in the download directory')

    args = parser.parse_args()
    logging.info(f'Starting with parameters: {args}')

    # Clamp limit to a maximum value of 60.
    args.limit = min(args.limit, 60)

    # Translate order argument.
    if args.order is not None:
        if args.order in ORDER_MAP:
            args.order = ORDER_MAP[args.order]
        else:
            try:
                args.order = int(args.order)
            except ValueError:
                logging.error(f'Invalid value for --order: {args.order}\n')
                sys.exit(1)

    # Convert start_date and end_date to offset-aware datetime if they are provided.
    if args.start_date:
        args.start_date = datetime.strptime(args.start_date, '%Y-%m-%d').replace(tzinfo=gettz('UTC'))
    else:
        args.start_date = None

    if args.end_date:
        args.end_date = datetime.strptime(args.end_date, '%Y-%m-%d').replace(tzinfo=gettz('UTC'))
    else:
        args.end_date = None

    # If a download directory was specified, ensure it exists.
    if args.download_to and not os.path.exists(args.download_to):
        os.makedirs(args.download_to)

    asyncio.run(run(
        args.search_terms,
        args.endpoint,
        args.return_query,
        args.limit,
        args.order,
        args.offset,
        args.page,
        args.pages,
        args.start_date,
        args.end_date,
        args.rating,
        args.medium,
        args.author,
        args.gallery,
        args.min_width,
        args.max_width,
        args.min_height,
        args.max_height,
        args.no_blurred_content,
        args.no_query_author,
        args.output_to,
        args.output_format,
        args.return_field,
        args.download_to,
        args.skip_download_exists
    ))

    logging.info('Program complete.')

if __name__ == '__main__':
    logging.info('Program started.')
    try:
        main()
    except Exception as e:
        logging.exception(f'An unexpected error occurred: {e}')
        sys.exit(1)
