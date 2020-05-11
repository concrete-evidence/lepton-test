import numpy as np
import matplotlib.pyplot as plt
from flirpy.camera.lepton import Lepton

camera = Lepton()
image = camera.grab(0) # Grab frame from camera 0
print(image)

plt.imshow(image) # Display raw temperature data as an image

camera.close()
