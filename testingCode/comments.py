# temp from online
# def take_photo(filename='photo.jpg', quality=0.8):
  
#   cam_port = 0
#   cam = cv2.VideoCapture(cam_port) 
    
#   # reading the input using the camera 
#   result, image = cam.read()
#   # image = cv2.imread("Metal_2.jpg") 
#   # img_gry = image
#   img_gry = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#   # img_gry = cv2.resize(img_gry,(256,256),interpolation=cv2.INTER_LANCZOS4)


#   # this detects anything but circles lmao
#   def lineDetector(path_to_img):
#     hori_line_mat = np.float32([[-1,-1,-1],
#                             [5,5,5],
#                             [-1,-1,-1]])
#     verti_line_mat = np.float32([[-1,5,-1],
#                             [-1,5,-1],
#                             [-1,5,-1]])
    
#     img = path_to_img
#     img_out = cv2.filter2D(img,-1,hori_line_mat) + cv2.filter2D(img,-1,verti_line_mat)
#     plt.figure(figsize=(20,10))
#     plt.subplot(121),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)),plt.title('Input',color='c')
#     plt.subplot(122),plt.imshow(cv2.cvtColor(img_out,cv2.COLOR_BGR2RGB)),plt.title('Transformed',color='c')
#     plt.show()
#     return img_out
  

#     # Line Detection
# def houghLineDetector(path_to_img):
#     img = cv2.imread(path_to_img)
#     img_edge = cv2.Canny(img,80,200)
#     lines = cv2.HoughLinesP(img_edge,5,np.pi/180,20,minLineLength=50,maxLineGap=10)
#     for line in lines:
#         x1,y1,x2,y2 = line[0]
#         cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)
#     plt.figure(figsize=(20,10))
#     plt.subplot(121),plt.imshow(cv2.cvtColor(img_edge,cv2.COLOR_BGR2RGB)),plt.title('Input',color='c')
#     plt.subplot(122),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)),plt.title('Output',color='c')
#     plt.show()
#     return



# more code
# img = cv2.GaussianBlur(img, (7, 7), 1.5)

    # cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    # circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.3, 30, param1=150, param2=70, minRadius=0, maxRadius=0)

    # circles = np.uint16(np.around(circles))

    # for c in circles[0, :]:
    #   cv2.circle(cimg, (c[0], c[1]), c[2], (0, 255, 0), 3)
    #   cv2.circle(cimg, (c[0], c[1]), 1, (0, 0, 255), 5)

    #   cv2.imshow('cimg', cimg)
    #   cv2.waitKey(0)
    #   cv2.imwrite('houghcircle.png', cimg)



    # vertImg = lineDetector(image, verti_line_mat)

  


  # min = np.amin(img_gry)
  # max = np.amax(img_gry)
  # img_normalized = cv2.normalize(img_gry, None, min, max, cv2.NORM_MINMAX, dtype=cv2.CV_32F)

  # cv2.imwrite("tes1t.png", img_gry)
  # cv2.imwrite("test.png", img_normalized)

  # print(img_normalized)
  # print(img_gry)

  # ret,img_bin = cv2.threshold(img_gry,127,255,cv2.THRESH_BINARY)
  # ret,img_bininv = cv2.threshold(img_gry,127,255,cv2.THRESH_BINARY_INV)
  # ret,img_Otsubin = cv2.threshold(img_gry,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

  # print(img_bin)
  # print(img_bininv)
  # print(img_Otsubin)

  # plt.imshow(img_Otsubin, interpolation='nearest')
  # plt.show()
  # plt.imshow(img_bininv, interpolation='nearest')
  # plt.show()

  # plt.imshow(img_bin, interpolation='nearest')
  # plt.show()


  # saving img_gry in local storage 
# cv2.imwrite("GeeksForGeeks.png", img_gry) 


# take_photo()