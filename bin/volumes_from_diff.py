#!/usr/bin/env python3

"""
Takes a list of XML files on STDIN, and prints all the volumes
within each of those files. e.g.,

    git diff --name-only master | ./bin/volumes_from_xml.py https://preview.aclanthology.org/BRANCH

Used to find the list of volumes to generate previews for.
"""

import sys
import argparse
import lxml.etree as etree
import subprocess


parser = argparse.ArgumentParser()
parser.add_argument("url_root")
args = parser.parse_args()

volumes = []
for line in sys.stdin:
    try:
        tree = etree.parse(xmlfile.rstrip())
    except:
        continue
    root = tree.getroot()
    collection_id = root.attrib["id"]
    for volume in root:
        volume_name = volume.attrib["id"]
        volume_id = f"{collection_id}-{volume_name}"
        volumes.append(f"[{volume_id}]({args.url_root}/{volume_id})")

print(", ".join(volumes))
