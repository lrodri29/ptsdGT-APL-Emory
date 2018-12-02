import numpy as np
import matplotlib.pyplot as plt
import intern
from intern.remote.boss import BossRemote
from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt

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

# Ranges use the Python convention where the second number is the stop
# value.  

# You can specify ranges smaller than the full size image. 
x_rng = [0, 3638]
y_rng = [0, 3624]

i = 100
# You will need re-define this to point to the right tile location in the boss volume. 
#This example will replace the first image in the volume
while i < 470:
    z_rng = [i, i+1]

    fPath = "/Users/rodrilm2/Documents/APL/GeorgiaTech/PTSD/MOR23_control_OB_iba1_DAPI/MOR23_OB_iba1_DAPI_pilot(1)-stitched_T001_Z" + str(i) + ".tif"
    print("Uploading : " + fPath)
    # Note that the numpy matrix is in Z, Y, X order.
    data = np.array(Image.open(fPath))

    # Need to make the array three dimensional for intern to upload correctly
    data = data[:,:,1]
    data = np.expand_dims(data,axis=2)
    # C-contiguous array
    data = data.copy(order="C")

    # Make data match what was specified for the channel.
    data = data.astype(np.uint8)

    # # Upload the cutout to the channel.  The zero parameter specifies native
    # # resolution.
    rmt.create_cutout(chan, 0, x_rng, y_rng, z_rng, data)
    i+=1
