import cv2
import numpy as np

def functions():
  def brightness(img, brightness_val):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    height, width, channels = hsv.shape
    for x in range(height):
      for y in range(width):
        if (hsv[x,y,2] + brightness_val) > 255:
          hsv[x,y,2] = 255 
        elif hsv[x,y,2] + brightness_val < 0:
          hsv[x,y,2] = 0 
        else:
          hsv[x,y,2] += brightness_val
    ret = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return ret 

  def blur(img, val):
    val = int(val)
    kernel = (val, val)
    ret = cv2.GaussianBlur(img, kernel, 0)
    return ret 

  def motion_blur(img, size):
    size = int(size)
    kernel = np.zeros((size, size))
    kernel[int((size-1)/2),:] = np.ones(size)
    kernel = kernel / size
    ret = cv2.filter2D(img, -1, kernel)
    return ret 

  def saturation(img, val):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    s = cv2.multiply(s, val)
    hsv = cv2.merge((h,s,v))
    ret = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return ret

  def sharpen(img, val):
    val = int(val)
    kernel = [[-1*val/9,-1*val/9,-1*val/9], [-1*val/9,val,-1*val/9], [-1*val/9,-1*val/9,-1*val/9]]
   # ret = cv2.filter2D(img, -1, kernel)
    ret = None
    return ret

  def flip(img, val):
    ret = cv2.flip(img, 1)
    return ret

  def gamma(img, gamma=1.0):
    invGamma = 1.0 / gamma
    table = np.array([((i/255.0)**invGamma)*255 for i in np.arange(0,256)]).astype("uint8")
    return cv2.LUT(img, table)

  def reduction(img, val):
    background = np.full(img.shape, 0, dtype=int)
    width = int(img.shape[1] * val)
    height = int(img.shape[0] * val)
    content = cv2.resize(img, dsize=(width, height), interpolation=cv2.INTER_CUBIC)
    ret = background.copy()
    ret[0:height,0:width] = content
    return ret

  return {"brightness":brightness, "blur":blur, "reduction":reduction, "motion_blur":motion_blur, \
          "saturation":saturation, "sharpen":sharpen, "flip":flip, "gamma":gamma, "reduction":reduction}
