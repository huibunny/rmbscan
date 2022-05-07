#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import pytesseract
import cv2
import numpy as np

#图像二值化
def otsu(img_o):
    blur = cv2.GaussianBlur(img_o,(3,3),0) #高斯滤波去除噪声
    #blur = cv2.equalizeHist(blur) #对比度暗的需要直方图均衡化增强对比度
    ret,img_OTSU = cv2.threshold(blur,120,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) #OTSU实现二值化分割
    return img_OTSU

#图像旋转修正
def rotated(img_OTSU):
    coords = np.column_stack(np.where(img_OTSU>0)) #求得代表纸币的白色点集
    angle = cv2.minAreaRect(coords)[-1] #求出最小外界矩形，返回的参数有三个：矩形的中心点、矩形的长和宽、矩形的旋转角度
    #print(angle)
    #确定用来修正的旋转角度
    if angle == 90:
        angle=0
    if angle < -45:
        angle = -(90+angle)
    if angle > 45:
        angle = 90-angle
    else:
        angle = -angle
    M = cv2.getRotationMatrix2D((w/2,h/2),angle,1.0)  #计算得到二维旋转矩阵
    img_rotated = cv2.warpAffine(img_OTSU,M,(w,h),flags = cv2.INTER_CUBIC,borderMode = cv2.BORDER_REPLICATE) #仿射变换实现旋转修正
    return img_rotated

#纸币裁剪
def cut(img_rotated):
    points = np.argwhere(img_rotated==255) #找到白色像素位置
    points = np.fliplr(points) #将得到的行列左边转换为(x,y)坐标
    x,y,w,h = cv2.boundingRect(points) #创建最小外接矩形，(x,y)为左上角起始点坐标，w和h为长度和高度
    img_cut = img_rotated[y:y+h, x:x+w] #裁剪
    return img_cut

#字符区域定位和提取
def local(img_cut):
    img_resize = cv2.resize(img_cut,(1000,800),interpolation=cv2.INTER_CUBIC) #将纸币统一为1000x800的图像
    img_local = img_resize[550:650,15:245]
    return img_local

#形态学处理
def result(img_local):
    s = np.ones((3,3),np.uint8) #结构元
    img_erode = cv2.erode(img_local,s) #膨胀运算
    return img_erode

#字符识别
def recog(img_erode):
    code = pytesseract.image_to_string(img_erode) #调用pytesseract进行字符识别
    code = ''.join(code.split()) #消除字符串之间的空格
    return code


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: python main.py <img filename>\n')
    else:
        file_name = sys.argv[1]
        # todo:
        # file not found here and exit.
        #读入图像灰度图
        img_o = cv2.imread(file_name,0)
        (h,w) = img_o.shape[:2] #获得高度和长度

        img_OTSU = otsu(img_o)
        img_rotated = rotated(img_OTSU)
        img_cut = cut(img_rotated)
        img_local = local(img_cut)
        img_erode = result(img_local)
        code = recog(img_erode)
        print(code)

        #cv2.imshow("Original Image",img_o)
        #cv2.imshow("Binarization",img_OTSU)
        #cv2.imshow("Rotation Correction",img_rotated)
        #cv2.imshow("Final Result",img_erode)
        #cv2.waitKey(0)

