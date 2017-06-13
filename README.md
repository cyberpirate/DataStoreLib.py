# DataStoreLib.py

Python Library to access the [DataStore API](https://github.com/cyberpirate/DataStore)

    #file: file to be passed to requests
    #mimeType: string mimeType
    #data: dictionary of metadata for the file
    DataStore.uploadFile(file, mimeType, data)
    #returns: True or False

    #conditions: array of conditions to pass to DataStore. Syntax in the DataStore documentation
    DataStore.getIds(conditions)
    #returns: array of urls to files passing the conditions