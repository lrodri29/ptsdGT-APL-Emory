from skimage import filters
import numpy as np
import matplotlib.pyplot as plt
import intern
from intern.remote.boss import BossRemote
from PIL import Image
import os

#Define the Boss Remote with your API token
rmt = BossRemote({
    "protocol": "https",
    "host": "api.bossdb.org",
    "token": "9154f9b731940e65844ea3568a0d7daa94f06f8b",
})

#Define the data's location in the boss. 
COLL_NAME = 'OlfactoryBulbMicrogliaPlasticity'
EXP_NAME = 'PTSD'
CHAN_NAME = 'microgliaI'

# Grab the channel
chan = rmt.get_channel(CHAN_NAME, COLL_NAME, EXP_NAME)

#Grab the cutout from BOSS
rawMicroGlia = rmt.get_cutout(chan, 0,[460, 960], [1200, 1700], [700, 701],)
print("Data shape: " + str(rawMicroGlia.shape))

# # Show for sanity check
# plt.imshow(rawMicroGlia[0,:,:], cmap="gray")
# plt.show()

# Make use of the Otsu method

val = filters.threshold_otsu(rawMicroGlia)
mask = rawMicroGlia < val

# Show for sanity check
f, axarr = plt.subplots(1,2)
axarr[0].imshow(mask[0,:,:], cmap="gray")
axarr[1].imshow(rawMicroGlia[0,:,:], cmap="gray")
# plt.imshow(mask[0,:,:], cmap="gray")
plt.show()