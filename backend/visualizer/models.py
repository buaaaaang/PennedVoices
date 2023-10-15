from django.db import models
import json
from .visualizer import visualizer
from .utils.pinata import Pinata

# Create your models here.

class Visualizer(models.Model):
    input = models.FileField()
    result = models.ImageField(blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "sound uploaded at {}".format(self.uploaded.strftime("%Y-%m-%d %H:%M:%S"))

    def save(self, *args, **kwargs):
        try:
            input = self.input
            result = visualizer(input)
            self.result.save('result.png', result, save=False)
            print('result saved')

            #temporary code for debug
            # pinata = Pinata()
            # print(self.result.path)
            # pinFileResult = pinata.pin_file_to_ipfs(self.result.path)
            # print(pinFileResult)
            # IPFS_image = "ipfs://" + pinFileResult["IpfsHash"]
            # metadata = {
            #     "name": "name", 
            #     "description": "description", 
            #     "image": IPFS_image+""}
            # print(metadata["image"])
            # pinJsonResult = pinata.pin_json_to_ipfs(metadata)
            # print("json pin result", pinJsonResult)

        except:
            print('failed')

        super().save(*args, **kwargs)

class Minter(models.Model):
    imageID = models.IntegerField(default=-1)
    name = models.TextField()
    description = models.TextField()
    IPFS_image = models.CharField(max_length=100,blank=True)
    tokenURI = models.CharField(max_length=100,blank=True)
    # static pinata class
    pinata = Pinata()

    def __str__(self):
        return "mint try for visualizer id " + str(self.imageID)

    def save(self, *args, **kwargs):
        try:
            visualizer = Visualizer.objects.get(id=self.imageID)
            pinFileResult = Minter.pinata.pin_file_to_ipfs(visualizer.result.path)
            print("file pin result", pinFileResult) 
            self.IPFS_image = "ipfs://" + pinFileResult["IpfsHash"]
            metadata = {
                "name": self.name+"", 
                "description": self.description+"", 
                "image": self.IPFS_image+""}
            pinJsonResult = Minter.pinata.pin_json_to_ipfs(metadata)
            print("json pin result", pinJsonResult)
            self.tokenURI = "https://gateway.pinata.cloud/ipfs/" + pinJsonResult["IpfsHash"]
        except:
            print('failed')
            self.tokenURI = ""
        super().save(*args, **kwargs)
