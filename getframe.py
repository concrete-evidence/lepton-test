import numpy as np
from flirpy.camera.lepton import Lepton
camera = Lepton()
image = camera.grab(0)
print(image)
camera.close()
