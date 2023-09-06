
#
# import cv2
#
# # Load the image
# image_path = 'image.jpeg'
# image = cv2.imread(image_path)
#
# # Display the image
# cv2.imshow('Image', image)
# cv2.waitKey(0)
#
#  Get coordinates
# def get_coordinates(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(f'Coordinates: ({x}, {y})')
#
# cv2.setMouseCallback('Image', get_coordinates)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# import cv2
# def image_crop(event,x,y,flags,params):
#     if event==cv2.EVENT_LBUTTONDOWN:
#         print(f"({x},{y}")
# if __name__=="__main__":
#     img=cv2.imread("waterfall.jpg",1)
#     cv2.imshow('image',img)
#     cv2.setMouseCallback("image",image_crop)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


# #
# import cv2
# # # to read image
# img=cv2.imread("waterfall.jpg",0)
# print(img)
# # # to show the image
# cv2.imshow("image",img)
# # # how many milliseconds to wait the image on screen
# cv2.waitKey(5000)
# # print(img.shape)
# # print(img.size)
# # print(img.dtype)
# cv2.destroyAllWindows()      # to close all windows open by opencv

#
# import cv2
# img=cv2.imread("waterfall.jpg")
# print(img.shape)
# #width,height=400,400
# #imgResize=cv2.resize(img,(width,height))
# #print(imgResize.shape)
# imgcropped=img[100:350,100:150]
#
# #cv2.imshow("image",img)iii
# #cv2.imshow("resized",imgResize)
# cv2.imshow("cropped",imgcropped)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


from PIL import Image, ImageDraw

#
# def crop_triangle(image_path, coordinates, output_path):
#     img = Image.open(image_path)
#     mask = Image.new("L", img.size, 0) # greyscale mode
#     draw = ImageDraw.Draw(mask)
#     draw.polygon(coordinates,fill=255)
#     result = Image.new("RGBA", img.size)
#     result.paste(img, mask=mask)
#     bbox = result.getbbox()
#     cropped_img = result.crop(bbox)
#     cropped_img.save(output_path)
# input_image_path = "waterfall.jpg"
# triangle_coordinates = [(10,700),(10,100),(200,10),(400,100),(400,700) ]
# output_image_path = "output_triangle.png"
# crop_triangle(input_image_path, triangle_coordinates, output_image_path)




from PIL import Image, ImageDraw, ImageFilter, ImageFont
img = Image.open('nature.jpeg').convert("RGBA")

background = Image.new("RGBA", img.size, 0)

mask = Image.new("RGBA", img.size, 0)
draw = ImageDraw.Draw(mask)
draw.regular_polygon((80,120,50), 5, rotation=360, fill='green', outline=None)

new_img = Image.composite(img, background, mask)
#
# base_img = Image.new("RGBA", (300,300))
# base_img.paste(new_img, (150,150), new_img)

new_img.show()
