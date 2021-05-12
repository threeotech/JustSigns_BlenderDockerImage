import json
import os
import sys
from azure.storage.blob import BlobServiceClient, ContentSettings

service = BlobServiceClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=virtualsignlanguage;AccountKey=H4EF5Nbwbd5STbeA5ztlSwBSphuvLBuFLEEs4uw0qmhaVGEO7xA2nydUJKGooSRghrWFyefP0folysk5WJo0hg==;EndpointSuffix=core.windows.net")


def upload_images(file_path):
    container_client = service.get_container_client("$web")
    image_content_setting = ContentSettings(content_type='application/x-blender')
    with open(file_path[0], "rb") as data:
        container_client.upload_blob(name=file_path[1], data=data, overwrite=True, content_settings=image_content_setting)

upload_images(["ภาคใต้.blend","blender/ภาคใต้.blend"])