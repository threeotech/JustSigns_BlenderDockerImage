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
    print(url)
    blender_list.append(container_client.get_blob_client(blob=f"blender/{url}"))
for blob_image in blender_list:
    print(blob_image.blob_name)
    download_file_path = os.path.join(blob_image.blob_name)
    print(download_file_path)
    with open(download_file_path, "wb") as download_file:
        try:
            download_file.write(blob_image.download_blob().readall())
        except Exception as e:
            print(f"Error loading {blob_image.blob_name}: {e}")