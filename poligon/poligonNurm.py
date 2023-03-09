from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import numpy as np
import matplotlib.pyplot as plt
import itertools
import math
import random




def tuple_to_np_array(poligon_coord): # получаем массив numpy, чтобы построить полигон
    xy = np.empty([len(poligon_coord),2])  
    for i,dot in enumerate(poligon_coord):
        x = dot[0][0]
        y = dot[1][0]
        xy[i] = np.array([x,y])
    return xy

def get_rotation_matrix(angle,x0,y0): #получаем матрицу поворота
    cos_a = math.cos(math.radians(angle))
    sin_a = math.sin(math.radians(angle))
    return np.array([[cos_a,-sin_a,-x0*(cos_a - 1)+y0*sin_a],[sin_a,cos_a,-y0*(cos_a-1) - x0*sin_a],[0,0,1]])    
  

def create_triangle(_x0,_y0,size,alpha = 1, angle=0): 
    '''
    _x0,_y0 первая точка фигуры; size/height-сторна; 
    alpha - соотшение сторон(у треугольника и шестиугольника всегда 1);
    angle - угол поворота фигуры
    '''
    rotation = get_rotation_matrix(angle,_x0,_y0)
    _x1 = _x0 + size/2
    _y1 = _y0 + math.sin(math.radians(60))*size
    _x2 = _x0 + size
    _y2 = _y0
    _point_a = np.array([[_x0],[_y0],[1]])
    _point_b = np.array([[_x1],[_y1],[1]])
    _point_c = np.array([[_x2],[_y2],[1]])
    point_a = rotation.dot(_point_a)
    point_b = rotation.dot(_point_b)
    point_c = rotation.dot(_point_c)
    point_a = point_a[:2] 
    point_b = point_b[:2]
    point_c = point_c[:2]
    return (point_a,point_b,point_c)


def create_hexagon(_x0,_y0,size,alpha = 1,angle=0):
    rotation = get_rotation_matrix(angle,_x0,_y0)
    _x1 = _x0 - size/2
    _y1 = _y0 + math.sin(math.radians(60))*size
    _x2 = _x0
    _y2 = _y1 + math.sin(math.radians(60))*size
    _x3 = _x2 + size
    _y3 = _y2
    _x4 = _x3 + size/2
    _y4 = _y1
    _x5 = _x3
    _y5 = _y0
    _point_a = np.array([[_x0],[_y0],[1]])
    _point_b = np.array([[_x1],[_y1],[1]])
    _point_c = np.array([[_x2],[_y2],[1]])
    _point_d = np.array([[_x3],[_y3],[1]])
    _point_e = np.array([[_x4],[_y4],[1]])
    _point_f = np.array([[_x5],[_y5],[1]])
    point_a = rotation.dot(_point_a)[:2]
    point_b = rotation.dot(_point_b)[:2]
    point_c = rotation.dot(_point_c)[:2]
    point_d = rotation.dot(_point_d)[:2]
    point_e = rotation.dot(_point_e)[:2]
    point_f = rotation.dot(_point_f)[:2]
    return (point_a,point_b,point_c,point_d,point_e,point_f)


def create_rectangle(_x0,_y0,height,alpha=1,angle=0):
    rotation = get_rotation_matrix(angle,_x0,_y0)
    width = height * alpha
    _x1 = _x0 
    _y1 = _y0 + height
    _x2 = _x1 + width
    _y2 = _y1
    _x3 = _x2
    _y3 = _y0
    _point_a = np.array([[_x0],[_y0],[1]])
    _point_b = np.array([[_x1],[_y1],[1]])
    _point_c = np.array([[_x2],[_y2],[1]])
    _point_d = np.array([[_x3],[_y3],[1]])
    point_a = rotation.dot(_point_a)[:2]
    point_b = rotation.dot(_point_b)[:2]
    point_c = rotation.dot(_point_c)[:2]
    point_d = rotation.dot(_point_d)[:2]
    return (point_a,point_b,point_c,point_d)

def create_trapeze(angle1,angle2,x0):
    k1 = math.tan(math.radians(angle1))
    k2 = math.tan(math.radians(angle2))
    x1 = x0*math.cos(math.radians(angle1))
    y1 = x1*k1 
    x2 = 2*x0*math.cos(math.radians(angle1))
    y2 = x2*k1
    x3 = 2*x0*math.cos(math.radians(angle2))
    y3 = x3*k2
    x4 = x0*math.cos(math.radians(angle2))
    y4 = x4*k2
    point_a = np.array([[x1],[y1]])
    point_b = np.array([[x2],[y2]])
    point_c = np.array([[x3],[y3]])
    point_d = np.array([[x4],[y4]])
    return (point_a,point_b,point_c,point_d)

list_figure = [create_hexagon,create_rectangle,create_triangle]


def line_generator(start_x,angle,distance,size,alpha):
    counter = 0
    k = math.tan(math.radians(angle))
    step = abs(size*alpha*2)*math.cos(math.radians(angle))
    x = start_x
    while True:
        x = start_x + counter*step    
        y = k*x + distance
        counter += 1
        yield x,y
           
#def get_patch_args_old(n,angle,distance,height,alpha=1,center=None):
#    patch_args = []
#    if height>=0:
#        start = -height*alpha*n
#    else:
#        start = height*alpha*(n-1) 
#    if center:
#        rotation = get_rotation_matrix(angle,center[0],center[1])
#        point = np.array([[start],[center[1]],[1]])
#        point = rotation.dot(point)[:2]
#        start = point[0,0]
#    counter = 0
#    for x,y in line_generator(start,angle,distance,height,alpha):
#        single_arg = [x,y,height,alpha,angle]
#        patch_args.append(single_arg)#в списке лежит список аргументов для каждого полигона
#        counter +=1
#        if counter == n:
#            break
#    return patch_args

def get_patch_args(n,angle,distance,height,alpha=1,center=None,hom=False):
    patch_args = []
    if height>=0:
        start = -height*alpha*n*math.cos(math.radians(angle))
    else:
        start = height*alpha*(n-1)*math.cos(math.radians(angle))
    if center:
        start = start + center[0]
    if hom:
        start = 0
    counter = 0
    for x,y in line_generator(start,angle,distance,height,alpha):
        single_arg = [x,y,height,alpha,angle]
        patch_args.append(single_arg)#в списке лежит список аргументов для каждого полигона
        counter +=1
        if counter == n:
            break
    return patch_args

def homothety(single_shape,scale):
    proportion = np.array([[scale,0],[0,scale]])
    new_single_shape = []
    for point in single_shape:
        new_point = proportion.dot(point)
        new_single_shape.append(new_point)
    return new_single_shape

def create_strip(n,angle1,angle2):
    x1=np.linspace(-100,100,1000)
    line_1 = (x1,math.tan(math.radians(angle1))*x1)
    line_2 = (x1,math.tan(math.radians(angle2))*x1)
    x_mod = (-1,1)
    x = -1
    patches = []
    for i in range(2):
        for j in range(n):
            trapeze = create_trapeze(angle1,angle2,x)
            x = 2 * x + x_mod[i]
            xy = tuple_to_np_array(trapeze)
            sh_poly = Polygon(xy,True)
            patches.append(sh_poly)
        x=1
    return patches,[line_1,line_2]

def create_line(shape,n,angle,distance,height,alpha=1,center=None,hom = False):  
    patches = []
    patch_args = get_patch_args(n,angle,distance,height,alpha,center,hom)
    hom_counter = 0
    for single_shape in itertools.starmap(shape,patch_args):
        if hom:
            hom_counter += 2 
            single_shape = homothety(single_shape,hom_counter)           
        xy = tuple_to_np_array(single_shape)
        sh_poly = Polygon(xy,True)
        patches.append(sh_poly)      
    return patches    

def create_symmetry_line(s_angle,s_distance,shape,n,angle,distance,height,alpha=1):    
    new_angle = s_angle + (s_angle - angle)
    tan_old = math.tan(math.radians(angle))
    tan_s = math.tan(math.radians(s_angle))
    tan_new = math.tan(math.radians(new_angle))
    if new_angle == s_angle:
        new_distance = 2*s_distance - distance
        center = None
    else:
        x = (distance - s_distance) / (tan_s - tan_old)
        y = tan_s*x+s_distance
        center = (x,y)
        new_distance = y-x*tan_new
    line1 = create_line(shape,n,angle,distance,height,alpha=1,center = center)
    line2 = create_line(shape,n,new_angle,new_distance,-height,alpha=1,center = center)
    x1=np.linspace(-100,100,1000)
    line_s = (x1,tan_s*x1 + s_distance)
    return line1,line2,line_s
    #new_patches = []
    #new_height = (-1)*height
    #new_patch_args = get_patch_args(n,new_angle,new_distance,new_height,alpha)
    #for single_shape in itertools.starmap(shape,new_patch_args):
    #    xy = tuple_to_np_array(single_shape)
    #    sh_poly = Polygon(xy,True)
    #    new_patches.append(sh_poly)  
    
    #plt.plot(x1,tan_s*x1 + s_distance,'--r',label='symm')    
    #return line1,new_patches


def random_figure(n,angle,distance,height,alpha=1):
    callback_list = []
    patches = []
    hom_counter = 0
    for i in range(n):
        callback_list.append(random.choice(list_figure))
        patch_args = get_patch_args(n,angle,distance,height,alpha)    
    for callback,arg in zip(callback_list,patch_args):
        single_shape = callback(*arg)
        xy = tuple_to_np_array(single_shape)
        sh_poly = Polygon(xy,True)
        patches.append(sh_poly)
    return patches


def plot_polygons(patches,line_s=[]):    
    fig, ax = plt.subplots()
    ax.axis('equal')
    ax.set(xlim = (-8,8),ylim = (-8,8))
    p = PatchCollection(patches,alpha = 0.4)
    ax.add_collection(p)
    for line in line_s:
        plt.plot(line[0],line[1],'--b')
    plt.grid()
    plt.show()


#cимметрия
lines = []
line1, line2,line_s = create_symmetry_line(s_angle = 0,s_distance = 2,shape = create_triangle,n=10,angle = 0,distance=0,height=2,alpha=1)
lines.extend(line1)
lines.extend(line2)
plot_polygons(lines,line_s)


#фигура
#line = create_line(shape = create_rectangle,n = 30,angle = 45,distance = 0,height = 2,alpha=1,hom=True)
#plot_polygons(line)

#гомотетия
#strip,lines = create_strip(n = 5,angle1 = 15,angle2 = 30)
#plot_polygons(strip,lines)

#рандомные фигуры
#line = random_figure(7,angle = 45, distance = 0, height  = 1)
#plot_polygons(line)