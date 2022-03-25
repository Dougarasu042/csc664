class LocalDataBase: 
    binary_image_dict = {}
    grey_image_dict = {}

    def start(self):
        return self.binary_image_dict, self.grey_image_dict

    def Get_Image(self, hash, type):
        return 

    def Save_Image(self, hash, path, type):
        if type == 'binary':
            if hash not in self.binary_image_dict:
                self.binary_image_dict[hash] = []
            self.binary_image_dict[hash].append(path)
        else:
            if hash not in self.grey_image_dict:
                self.grey_image_dict[hash] = []
            self.grey_image_dict[hash].append(path)

    def __init__(self):
        self.binary_image_dict = self.binary_image_dict
        self.grey_image_dict = self.grey_image_dict
