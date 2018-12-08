import cv2
image = cv2.imread("images\\trex.png")
print("width: %d pixels" % image.shape[1])
print("height: %d pixels" % image.shape[0])
print("channels: %d" % image.shape[2])
cv2.imshow("Trex Image", image)

for r in range(image.shape[0]):
    image[r,150]=(0,0,0)

cv2.imshow("Trex with line image", image)

cv2.waitKey(0)
out_file_name = "trex_with_line.png"
cv2.imwrite(out_file_name, image)
