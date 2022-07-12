import dropbox 

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
       
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx. file_upload(f.read(), dropbox_path, modeWriteMode('overwrite'))

def main():
    access_token = 'sl.BKrm3XW89icxpxb4OIodpgRGpwPEIqMsQwKBIU4f7v1LNIKqMWke051gEzyj1qkPVY4PLeROsu5wb0w6Xo8qgB_MLniNcQ5W3Zt1Djo3OdiyQCMyHtvpW0tbijx2tAKUmA2h5dnMlf0'
    transferData = TransferData(access_token)

    file_from = 'porject101.txt'
    file_to = '/101_dropbox/porject101.txt'  
    for root, dirs, files in os.walk(file_from)
    relative_path = os.path.relpath(file_from)
    dropbox_path = os.path.join(file_to)
    transferData.upload_file(file_from, file_to)
    print("uploading done!")

if __name__ == '__main__':
    main()