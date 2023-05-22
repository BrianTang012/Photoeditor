import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

def change_brightness(image, value):
    img = image.copy()
    img = image.astype("int16")
    for i in range (img.shape[0]):
        for j in range (img.shape[1]):
            for k in range (img.shape[2]):
                img[i][j][k]+=value
                
                if img[i][j][k] < 0:
                    img[i][j][k] = 0
                elif img[i][j][k] > 255:
                    img[i][j][k] = 255
                # error check to avoid result exceed parameter
    return img
  
def change_contrast(image, value):
    img = image.copy()
    img = image.astype("int16")
    F= (259*(value+255))/(255*(259-value))
    for i in range (img.shape[0]):
        for j in range (img.shape[1]):
            for k in range (img.shape[2]):
                img[i][j][k] = F*(img[i][j][k]-128) + 128
                
                if img[i][j][k] < 0:
                    img[i][j][k] = 0
                elif img[i][j][k] > 255:
                    img[i][j][k] = 255
                # error check to avoid result exceed parameter
    return img

def grayscale(image):
    img = image.copy()
    img = image.astype("int16")
    img2=img.copy()
    for i in range (img.shape[0]):
        for j in range (img.shape[1]):
            for k in range (img.shape[2]):
                img2[i][j][k] = 0.3*img[i][j][0] + 0.59*img[i][j][1] + 0.11*img[i][j][2]
                
                if img2[i][j][k] < 0:
                    img2[i][j][k] = 0
                elif img2[i][j][k] > 255:
                    img2[i][j][k] = 255
                # error check to avoid result exceed parameter
    return img2

def blur_effect(image):
    img = image.copy()
    img = image.astype("int16")
    img2 = img.copy()
    for i in range (1,img.shape[0]-1):
        for j in range (1,img.shape[1]-1):
           for k in range (img.shape[2]):
                img2[i][j][k] = 0.0625*img[i-1][j-1][k] + 0.125*img[i][j-1][k] + 0.0625*img[i+1][j-1][k] +\
                0.125*img[i-1][j][k] + 0.25*img[i][j][k] + 0.125*img[i+1][j][k] +\
                0.0625*img[i-1][j+1][k] + 0.125*img[i][j+1][k] + 0.0625*img[i+1][j+1][k]
                
                if img2[i][j][k] < 0:
                    img2[i][j][k] = 0
                elif img2[i][j][k] > 255:
                    img2[i][j][k] = 255
                # error check to avoid result exceed parameter
    return img2    

def edge_detection(image):
    img = image.copy()
    img = image.astype("int16")
    img2 = img.copy()
    for i in range (1,img.shape[0]-1):
        for j in range (1,img.shape[1]-1):
           for k in range (img.shape[2]):
                img2[i][j][k] = -1*img[i-1][j-1][k] -1*img[i-1][j][k] -1*img[i-1][j+1][k]\
                -1*img[i][j-1][k] + 8*img[i][j][k] -1*img[i][j+1][k] +\
                -1*img[i+1][j-1][k] -1*img[i+1][j][k] -1*img[i+1][j+1][k] +128
                
                if img2[i][j][k] < 0:
                    img2[i][j][k] = 0
                elif img2[i][j][k] > 255:
                    img2[i][j][k] = 255
                # error check to avoid result exceed parameter
    return img2    

def embossed(image):
    img = image.copy()
    img = image.astype("int16")
    img2 = img.copy()
    for i in range (1,img.shape[0]-1):
        for j in range (1,img.shape[1]-1):
           for k in range (img.shape[2]):
                img2[i][j][k] = -1*img[i-1][j-1][k] -1*img[i-1][j][k] +0*img[i-1][j+1][k]\
                -1*img[i][j-1][k] + 0*img[i][j][k] +1*img[i][j+1][k] +\
                0*img[i+1][j-1][k] +1*img[i+1][j][k] +1*img[i+1][j+1][k] +128
                
                if img2[i][j][k] < 0:
                    img2[i][j][k] = 0
                elif img2[i][j][k] > 255:
                    img2[i][j][k] = 255
                # error check to avoid result exceed parameter
    return img2    

def rectangle_select(image, topleft, btmright):
    recmask= []
    for i in range(image.shape[0]):
        recmask.append([])
        for j in range(image.shape[1]):
            recmask[i].append(1)
            #create rectangle mask with 1s
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if i<int(topleft[0]) or i>int(btmright[0]) or j<int(topleft[1]) or j>int(btmright[1]):
                recmask[i][j]=0
    # change all corresponding values of the pixels outside of range to 0
    return np.array(recmask)
    

def magic_wand_select(image, x, thres):        
    magicmask=[]
    for i in range(image.shape[0]):
        magicmask.append([])
        for j in range(image.shape[1]):
            magicmask[i].append(0)
            #create magic mask with 0s
    queue=[[x[0],x[1]]]
    #Create queue for pixels to check. Pixels are checked first starting from given pixel.
    while len(queue)>0:
        if queue[0][0]<len(image) and queue[0][1]<len(image[0]) and queue[0][0]>=0 and queue[0][1]>=0 and magicmask[queue[0][0]][queue[0][1]]==0:
            
            dr=abs(int(image[x[0]][x[1]][0]-image[queue[0][0]][queue[0][1]][0]))
            dg=abs(int(image[x[0]][x[1]][1]-image[queue[0][0]][queue[0][1]][1]))
            db=abs(int(image[x[0]][x[1]][2]-image[queue[0][0]][queue[0][1]][2]))
            r=abs((int(image[x[0]][x[1]][0])+int(image[queue[0][0]][queue[0][1]][0]))/2)
            dist = math.sqrt( ((2+(r/256))*(dr**2)) + (4*(dg**2)) + ((2+((255-r)/256))*(db**2)))
            
            if dist<=thres:
                magicmask[queue[0][0]][queue[0][1]]=1
                if [queue[0][0]+1,queue[0][1]] not in queue:
                    queue.append([queue[0][0]+1,queue[0][1]])
                if [queue[0][0]-1,queue[0][1]] not in queue:
                    queue.append([queue[0][0]-1,queue[0][1]])
                if [queue[0][0],queue[0][1]+1] not in queue:
                    queue.append([queue[0][0],queue[0][1]+1])
                if [queue[0][0],queue[0][1]-1] not in queue:
                    queue.append([queue[0][0],queue[0][1]-1])
                queue.pop(0)
            else:
                queue.pop(0)
                #If threshold value is fulfilled, the corresponding index on magic mask is changed to 1,
                #then its four neighbouring pixels are added into queue.
                #If threshold value not fulfilled, the pixel is popped out from the queue directly.
        else:
            queue.pop(0)
            #If pixel is detected to be outside of picture boundary, it is popped out from the queue.
 
    return np.array(magicmask)

def compute_edge(mask):           
    rsize, csize = len(mask), len(mask[0]) 
    edge = np.zeros((rsize,csize))
    if np.all((mask == 1)): return edge        
    for r in range(rsize):
        for c in range(csize):
            if mask[r][c]!=0:
                if r==0 or c==0 or r==len(mask)-1 or c==len(mask[0])-1:
                    edge[r][c]=1
                    continue
                
                is_edge = False                
                for var in [(-1,0),(0,-1),(0,1),(1,0)]:
                    r_temp = r+var[0]
                    c_temp = c+var[1]
                    if 0<=r_temp<rsize and 0<=c_temp<csize:
                        if mask[r_temp][c_temp] == 0:
                            is_edge = True
                            break
    
                if is_edge == True:
                    edge[r][c]=1
            
    return edge

def save_image(filename, image):
    mpimg.imsave(filename,image)

def load_image(filename):
    img = mpimg.imread(filename)
    if len(img[0][0])==4: # if png file
        img = np.delete(img, 3, 2)
    if type(img[0][0][0])==np.float32:  # if stored as float in [0,..,1] instead of integers in [0,..,255]
        img = img*255
        img = img.astype(np.uint8)
    mask = np.ones((len(img),len(img[0]))) # create a mask full of "1" of the same size of the laoded image
    img = img.astype(int)
    return img, mask

def display_image(image, mask):
    # if using Spyder, please go to "Tools -> Preferences -> IPython console -> Graphics -> Graphics Backend" and select "inline"
    tmp_img = image.copy()
    edge = compute_edge(mask)
    for r in range(len(image)):
        for c in range(len(image[0])):
            if edge[r][c] == 1:
                tmp_img[r][c][0]=255
                tmp_img[r][c][1]=0
                tmp_img[r][c][2]=0
 
    plt.imshow(tmp_img)
    plt.axis('off')
    plt.show()
    print("Image size is",str(len(image)),"x",str(len(image[0])))

def menu():
    
    img = mask = np.array([])  
    maskchanged=False
    compare12=[]
    for i in range(-255,256):
        compare12.append(str(i))
    # maskchanged boolean variable to determine if mask has been applied
    # compare12 used to error check for input value of brightness and contrast
    
    newimg=[]
    
    print("Welcome! What do you want to do?")
    print("e - exit")
    print("l - load a picture")
    ch=str(input(""))
    
    while True:
        if ch=="e":
            print("")
            print("Thank you for using this program!")
            break
        
        elif ch=="l":
            filname=str(input("Enter filename: "))
            while True:
                try:
                    img, mask = load_image(filname)
                    break
                except:
                    filname=input("File not found, please retype: ")
            break
            # try and except statement to error check for filename
        
        else:
            print("Input not recognised, try again.")
            ch=str(input("Insert: "))
            continue
        
    if ch=="e":
        return 0

    while True:
        print("")
        print("What do you want to do next?")
        print("e - exit")
        print("l - load a picture")
        print("s - save the current picture")
        print("1 - adjust brightness")
        print("2 - adjust contrast")
        print("3 - apply grayscale")
        print("4 - apply blur")
        print("5 - edge detection")
        print("6 - embossed")
        print("7 - rectangle select")
        print("8 - magic wand select")
        print("d - display image")
        ch1=str(input(""))
        
        while ch1!='e'and ch1!='l' and ch1!='1' and ch1!='2' and ch1!='3' and ch1!='4' and ch1!='5' and ch1!='6' and ch1!='7' and ch1!='8' and ch1!='d' and ch1!='s':
                print("Input not recognised, try again.")
                ch1=str(input("Insert: ")) 

        if ch1=="e":
            print("")
            print("Thank you for using this program!")
            break
        
        elif ch1=="l":
            filname=str(input("Enter filename: "))
            while True:
                try:
                    img, mask = load_image(filname)
                    break
                except:
                    filname=input("File not found, please retype: ")
            continue
            # try and except statement to error check for filename
        elif ch1=="s":
            filname=str(input("Enter filename: "))
            img = img.astype("uint8")
            while True:
                try:
                    save_image(filname, img)
                    break
                except:
                    filname=input("Invalid name, please retype: ")
            continue
        #img as type uint8 to ensure no errors on saving
        # try and except statement to error check for saving filename
        
        elif ch1=="1":
            brival=input("Insert value for brightness change: ")
            while brival not in compare12:
                brival=input("Input error, insert another value for contrast change: ")
            brival=int(brival)
            # error check for brightness value            
            if maskchanged==False:
                img=change_brightness(img, brival)
            else:
                newimg=change_brightness(img, brival)
                for i in range(len(mask)):
                    for j in range(len(mask[0])):
                        if mask[i][j]==1:
                            img[i][j]=newimg[i][j]
            # check if mask is changed by rectangle or magic wand select, same for functions 2-6
            continue
        
        elif ch1=="2":
            conval=input("Insert value for contrast change: ")
            while conval not in compare12:
                conval=input("Input error, insert another value for contrast change: ")
            conval=int(conval)
            #error check for contrast value
            if maskchanged==False:
                img=change_contrast(img, conval)
            else:
                newimg=change_contrast(img, conval)
                for i in range(len(mask)):
                    for j in range(len(mask[0])):
                        if mask[i][j]==1:
                            img[i][j]=newimg[i][j]
            continue
        
        elif ch1=="3":
            if maskchanged==False:
                img=grayscale(img)
            else:
                newimg=grayscale(img)
                for i in range(len(mask)):
                    for j in range(len(mask[0])):
                        if mask[i][j]==1:
                            img[i][j]=newimg[i][j]
            continue
        
        elif ch1=="4":
            if maskchanged==False:
                img=blur_effect(img)
            else:
                newimg=blur_effect(img)
                for i in range(len(mask)):
                    for j in range(len(mask[0])):
                        if mask[i][j]==1:
                            img[i][j]=newimg[i][j]
            continue
        
        elif ch1=="5":
            if maskchanged==False:
                img=edge_detection(img)
            else:
                newimg=edge_detection(img)
                for i in range(len(mask)):
                    for j in range(len(mask[0])):
                        if mask[i][j]==1:
                            img[i][j]=newimg[i][j]
            continue
        
        elif ch1=="6":
            if maskchanged==False:
                img=embossed(img)
            else:
                newimg=embossed(img)
                for i in range(len(mask)):
                    for j in range(len(mask[0])):
                        if mask[i][j]==1:
                            img[i][j]=newimg[i][j]
            continue
        
        elif ch1=="7":
            comparey=[]
            comparex=[]
            for i in range(1,len(img)+1):
                comparey.append(str(i))
            for j in range(1,len(img[0])+1):
                comparex.append(str(j))
            #create list for error checking
            while True:
                print("")
                print('Insert the y position of the top left pixel, within range 1 to',len(img),': ')
                ytl=input("")
                while ytl not in comparey:
                    ytl=input("Input error, insert another value for y of top left: ")
                print("")
                print('Insert the x position of the top left pixel, within range 1 to',len(img[0]),': ')
                xtl=input("")
                while xtl not in comparex:
                    xtl=input("Input error, insert another value for x of top left: ")
                print("")
                print('Insert the y position of the bottom right pixel, within range 1 to',len(img),': ')
                ybr=input("")
                while ybr not in comparey:
                    ybr=input("Input error, insert another value for y of bottom right: ")
                print("")
                print('Insert the x position of the bottom right pixel, within range 1 to',len(img[0]),': ')
                xbr=input("")
                while xbr not in comparex:
                    xbr=input("Input error, insert another value for x of bottom right: ")
                #error check for the pixel values
                ytl=int(ytl)-1
                xtl=int(xtl)-1
                ybr=int(ybr)-1
                xbr=int(xbr)-1
                #since program starts from 0 but people start from 1 in normal day life, input altered to fit common usage
                if ytl>ybr or xtl>xbr:
                    print("Values for top left and bottom right contradict. Please retype.")
                    continue
                else:
                    break
                #error check if top left and bottom right contradicts
            recx=(ytl,xtl)
            recy=(ybr,xbr)
            mask=rectangle_select(img, recx, recy)
            maskchanged=True
            continue
        
        elif ch1=="8":
            comparey=[]
            comparex=[]
            for i in range(1,len(img)+1):
                comparey.append(str(i))
            for j in range(1,len(img[0])+1):
                comparex.append(str(j))
            # create list for error checking 
                
            while True:
                print("")
                print('Insert the x position of the target pixel, within range 1 to',len(img[0]),': ')
                magx=input("")
                while magx not in comparex:
                    magx=input("Input error, insert another value for x position of target pixel: ")
                print("")
                print('Insert the y position of the target pixel, within range 1 to',len(img[0]),': ')
                magy=input("")
                while magy not in comparey:
                    magy=input("Input error, insert another value for y position of target pixel: ")
                #error check for values of x and y position of target pixel
                
                thres=input("Insert threshold:")
                while True:
                    while True:
                        try:
                            thres=float(thres)
                            break
                        except:
                            thres=input("Input error, insert another value for threshold: ")
                    if thres<=0 or thres>math.sqrt( ((2+(255/(2*256)))*(255**2)) + (4*(255**2)) + ((2+((255-(255/2))/256))*(255**2))):
                        thres=input("Input error, insert another value for threshold: ")
                    else:
                        break
                break
            #try and except to determine if input is a number, then if statement to regulate the range
            magy=int(magy)-1
            magx=int(magx)-1
            thres=float(thres)
            #since program starts from 0 but people start from 1 in normal day life, input altered to fit common usage        
            #since max value of threshold is float (764.83...), threshold kept as float type
            posta=(magy,magx)
            mask=magic_wand_select(img, posta, thres)
            maskchanged=True
            continue
        
        elif ch1=="d":
            display_image(img,mask)
            continue
        

  
       
if __name__ == "__main__":
    menu()






