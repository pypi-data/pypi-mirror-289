from datetime import datetime

from SharepointConnect.Drives import Drives
from SharepointConnect.Lists import Lists
from SharepointConnect.PineconeOperations import PineconeOperations


def file_info(process_drives, found):
    files = []

    try:
        for link in found["links"]:
            files.append(process_drives.path(link["drive"]["id"], link["path"]))
    except:
        pass
    
    return files

def get_links(process_parts, root_site, page_ids):
    all_links = []

    for page_id in page_ids:
        parts = process_parts.page(root_site, page_id)
        links = process_parts.links(parts)
        all_links.extend(links)
    return all_links

def process_links(all_links, drives, lists):
    found = {"drives": set(), "lists": set(), "links": []}

    sites_start = 0; sites_left = 1

    while sites_start != sites_left:
        sites_start = len(all_links)

        for url in all_links:
            Drives.match_drives(all_links, drives, found, url)
            Lists.match_lists(all_links, lists, found, url)
            
        sites_left = len(all_links)
    return found

def Differential(rezolve, three_hours_ago, process_files, processed_files):
    pine_ops = PineconeOperations(rezolve)
    existing = pine_ops.get_sharepoint_data_by_namespace()

    existing_ids = list(set([file["identifier"] for file in existing]))
    new_ids = list(set([file["id"] for file in processed_files]))

    to_remove = [id for id in existing_ids if id not in new_ids]
    to_add = [id for id in new_ids if id not in existing_ids]

    recent_objects = [
        obj for obj in processed_files
        if datetime.fromisoformat(obj['modified'].replace('Z', '+00:00')) >= three_hours_ago
    ]

    recent_ids = [file['id'] for file in recent_objects]

    to_remove.extend(recent_ids)
    to_add.extend(recent_ids)

    remove_ids = [id['vector'] for id in existing if id['identifier'] in to_remove]
    add_files = [file for file in processed_files if file['id'] in to_add]

    if remove_ids:
        pine_ops.delete(remove_ids)
    
    if add_files:
        process_files.process(add_files, rezolve)