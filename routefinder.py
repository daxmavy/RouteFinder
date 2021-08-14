import requests
import os
import shutil
import zipfile

if __name__ == "__main__":
    # Paths for downloads
    chunkSize = 1024*1024*10  # 10MB per chunk
    gtfsFolderPath = "./resources/sydney_gtfs"
    gtfsFilePath = "./resources/sydney_gtfs.zip"

    # Requesting transport data from NSW Transport
    headers = {
        "Accept": "application/x-zip-compressed",
        "Authorization": "apikey <ENTER KEY>"
    }
    r = requests.get(
        "https://api.transport.nsw.gov.au/v1/publictransport/timetables/complete/gtfs",
        headers=headers,
        stream=True
    )

    if os.path.isfile(gtfsFilePath):
        os.remove(gtfsFilePath)

    # Download the file
    with open(gtfsFilePath, 'wb') as fd:
        i = 0
        for chunk in r.iter_content(chunk_size=chunkSize):
            print("Downloading Chunk " + str(i))
            i += 1
            fd.write(chunk)
        print("Download Complete!")

    if os.path.isdir(gtfsFolderPath):
        shutil.rmtree(gtfsFilePath)

    # Unzip the zip file into a folder
    with zipfile.ZipFile(gtfsFilePath, 'r') as zip_ref:
        zip_ref.extractall(gtfsFolderPath)

    # TODO Safely grab API key
    # TODO PARSE CST's
    # TODO Visualise Parsed Data :)
