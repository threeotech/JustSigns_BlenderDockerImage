from azure.storage.blob import BlobServiceClient, ContentSettings
import os
import sys

blender_list = []
all_path = []
raw_path = sys.argv[1].split(",")
for path in raw_path:
    if path:
        all_path.append(path)
service = BlobServiceClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=virtualsignlanguage;AccountKey=H4EF5Nbwbd5STbeA5ztlSwBSphuvLBuFLEEs4uw0qmhaVGEO7xA2nydUJKGooSRghrWFyefP0folysk5WJo0hg==;EndpointSuffix=core.windows.net")
container_client = service.get_container_client("$web")
for url in all_path:
    container_client.delete_blob(blob=f"blender/{url}", delete_snapshots="include")
   