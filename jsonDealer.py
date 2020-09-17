import json

def extract(startPath):
    #extract pose data
    with open(startPath, 'r') as startFile:
        allData = json.load(startFile)
        usefulData = allData["poses"]
        startFile.close()
    return usefulData

def poseLister(startPath):
    poses = extract(startPath)
    return poses