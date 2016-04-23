#!/usr/bin/python

import time
import json
import logging
import os
import requests
from coorcal import generate_coordinate

logging.basicConfig(
    level=logging.INFO, format='%(levelname)s:%(message)s')

# Load config from file config.json
with open('config.json', 'r') as f:
    args = json.load(f)

# Get App Access Token
token = requests.get("https://graph.facebook.com/v2.5/oauth/access_token?client_id={0}&client_secret={1}&&grant_type=client_credentials".format(
    args["client_id"], args["client_secret"])).json()['access_token']


def get_page_ids(lat, lon):
    '''
    Get pages's ID from a location. Return a list of all ID.
    '''
    pages_id = requests.get("https://graph.facebook.com/v2.5/search?type=place&q={0}&center={1},{2}&distance={3}&limit={4}&fields=id&access_token={5}".format(
        args["keyword"],
        lat, lon,
        args["distance"],
        args["limit"],
        token)).json()
    # Create a list of all ID
    pages_id_list = [i['id'] for i in pages_id['data']]
    # Process Facebook API paging
    while pages_id['paging'].has_key('next'):
        pages_id = requests.get(pages_id["paging"]['next']).json()
        for a in pages_id['data']:
            pages_id_list.append(a['id'])

    return pages_id_list


def events_from_page_id(pageid):
    '''
    For each page ID, find all event (if have) of that Page from today.
    Return a dictionary of page's infos and it's events.
    '''
    events = requests.get("https://graph.facebook.com/v2.6/",
            params={
                "ids" : pageid,
                "fields" : "events.fields(id,name,start_time,description,place,type,category,ticket_uri,cover.fields(id,source),picture.type(large),attending_count,declined_count,maybe_count,noreply_count).since({0}),id,name,cover.fields(id,source),picture.type(large),location".format(time.strftime("%Y-%m-%d")),
                "access_token":token,
                }
            )

    return events.json()


if __name__ == '__main__':
    CIRCLE = (21.027875, 105.853654, 1000,)
    for point in generate_coordinate(*CIRCLE, scan_radius=args["distance"]):
        for page_id in get_page_ids(point[0], point[1]):
            logging.debug(page_id)
            event = events_from_page_id(page_id)[page_id]
            if event.has_key('events'):
                logging.info(event['events'])
            else:
                logging.debug(event['name'])



