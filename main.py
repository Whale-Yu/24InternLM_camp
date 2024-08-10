# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import requests
url = 'https://ai.yunpengai.com/labelsysapi/dataset-clustering/submit'
data = {
    "algorithme": "kmeans",
    "clusterClass": "2",
    "modelName": "efficientnet-b3",
    "modelPath": "/data/html/dish.pth",
    "numsClass": "2306",
    "datasetId": "509",
    "labelId": "1013488",
    "groupId": "1811949036347392002"
}

resp=requests.post(url, data)
print(resp)

