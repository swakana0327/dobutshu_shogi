import math
import numpy as np
import pygame
from pygame.locals import *
import sys
def getDist(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def AreatoPoint(area):

    retlist=[]

    
    if area%3==0:
        retlist.append(250)
    elif area%3==1:
        retlist.append(50)
    elif area%3==2:
        retlist.append(150)
    
    if 1<=area and area<=3:
        retlist.append(50)
    elif  4<=area and area<=6:
        retlist.append(150)
    elif  7<=area and area<=9:
        retlist.append(250)
    elif  10<=area and area<=12:
        retlist.append(350)
        
    return retlist

def PointtoArea(point):
    if point[1]>=50 and point[1]<=150:
        if point[0]>=50 and point[0]<=150:
            return 1
        elif point[0]>=150 and point[0]<=250:
            return 2
        elif point[0]>=250 and point[0]<=350:
            return 3

    if point[1]>=150 and point[1]<=250:
        if point[0]>=50 and point[0]<=150:
            return 4
        elif point[0]>=150 and point[0]<=250:
            return 5
        elif point[0]>=250 and point[0]<=350:
            return 6    

    if point[1]>=250 and point[1]<=350:
        if point[0]>=50 and point[0]<=150:
            return 7
        elif point[0]>=150 and point[0]<=250:
            return 8
        elif point[0]>=250 and point[0]<=350:
            return 9

    if point[1]>=350 and point[1]<=450:
        if point[0]>=50 and point[0]<=150:
            return 10
        elif point[0]>=150 and point[0]<=250:
            return 11
        elif point[0]>=250 and point[0]<=350:
            return 12   
    
 

def getNext(animal,area,dict):

    if area==-1:
        return []


    cango=[]
    #cango...現エリアの周りすべてを格納（1マス差)
    for i in range(1,13):
        if i==area:
            continue
        p1=AreatoPoint(area)
        p2=AreatoPoint(i)
        if getDist(p1,p2)<150:
            cango.append(i)
    
    animalgo=getFlashLoad(area,animal)
    #animalgo...今の動物がいけるマス

    #print("指定エリアの周り")
    #print(cango)
    #print("この動物の行ける範囲")
    #print(animalgo)
    
    matched_list = []
    for tag in cango:
        for src in animalgo:
            if tag == src:
                matched_list.append(tag)
    for k,v in dict.items():
        if v in matched_list:
            matched_list.remove(v)
    
    return matched_list

def getNext_your(animal,area,dict):

    if area==-1:
        return []


    cango=[]
    #cango...現エリアの周りすべてを格納（1マス差)
    for i in range(1,13):
        if i==area:
            continue
        p1=AreatoPoint(area)
        p2=AreatoPoint(i)
        if getDist(p1,p2)<150:
            cango.append(i)
    
    animalgo=getFlashLoad_your(area,animal)
    #animalgo...今の動物がいけるマス

    #print("指定エリアの周り")
    #print(cango)
    #print("この動物の行ける範囲")
    #print(animalgo)
    
    matched_list = []
    for tag in cango:
        for src in animalgo:
            if tag == src:
                matched_list.append(tag)
    for k,v in dict.items():
        if v in matched_list:
            matched_list.remove(v)
    
    return matched_list


def setanimal(screen,zou,kirin,hiyoko,lion,dict):
        
        #敵陣
        #screen.blit(zou, (250, 50))
        #screen.blit(kirin, (50, 50))
        #screen.blit(hiyoko, (150,150))
        #screen.blit(lion, (150, 50))
        for k,v in dict.items():
            if k==0 or k==10:
                screen.blit(hiyoko, (AreatoPoint(v)[0],AreatoPoint(v)[1]))
                #print('ヒヨコ:'+str(v))
            if k==1 or k==11:
                screen.blit(kirin, (AreatoPoint(v)[0],AreatoPoint(v)[1]))
                #print('キリン:'+str(v))
            if k==2 or k==12:
                screen.blit(zou, (AreatoPoint(v)[0],AreatoPoint(v)[1]))
                #print('ゾウ:'+str(v))
            if k==3 or k==13:
                screen.blit(lion, (AreatoPoint(v)[0],AreatoPoint(v)[1]))
                #print('ライオン:'+str(v))

            
        

def setboard(screen):
    
    #将棋盤
    screen.fill((0,0,0))                                   
    for i in range(3):
        for j in range(4):
            pygame.draw.rect(screen,(0,80,0),Rect(50+100*i,50+100*j,100,100),5) 

    #自分の持ち駒　というテキストを表示
    font = pygame.font.SysFont("hg正楷書体pro", 25)
    text1 = font.render("1P koma", True, (255,0,191))
    text2 = font.render("2P koma", True, (255,0,191))

    screen.blit(text1, (450, 300))
    screen.blit(text2, (450, 100))


    #持ち駒スペース
    for i in range(6):
        pygame.draw.rect(screen,(255,255,0),Rect(400+50*i,350,50,50),2) 

    
    #持ち駒スペース
    for i in range(6):
        pygame.draw.rect(screen,(255,255,0),Rect(400+50*i,150,50,50),2) 
        


def getArea(x,y):
    if (50<=x and x<=150):
        if (50<=y and y<=150):
            return 1
        if (150<=y and y<=250):
            return 4
        if (250<=y and y<=350):
            return 7
        if (350<=y and y<=450):
            return 10
    
    if (150<=x and x<=250):
        if (50<=y and y<=150):
            return 2
        if (150<=y and y<=250):
            return 5
        if (250<=y and y<=350):
            return 8
        if (350<=y and y<=450):
            return 11
    
    if (250<=x and x<=350):
        if (50<=y and y<=150):
            return 3
        if (150<=y and y<=250):
            return 6
        if (250<=y and y<=350):
            return 9
        if (350<=y and y<=450):
            return 12
    #エリア外
    return -1            
    
def getFlashLoad(area,animal):
    flashlist=[]
    #area 1~12 int型
    # 
    # ---area--
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # 10 11 12

    # ---animal---
    # int型
    # 0:ひよこ
    # 1:キリン
    # 2:ゾウ
    # 3:ライオン
    # 4:ニワトリ(ひよこの裏面)
    if animal>=10:
        animal=animal-10

    if animal==0:
        flashlist.append(area-3)
    
    if animal==1:
        flashlist.extend([area-3,area-1,area+1,area+3])
    
    if animal==2:
        flashlist.extend([area-4,area-2,area+2,area+4])

    if animal==3:
        flashlist.extend([area-4,area-3,area-2,area-1,area+1,area+2,area+3,area+4])
    
    newlist = [e for e in flashlist if e >= 1 and e<=12]
    
    #print(newlist)
    return newlist

def getFlashLoad_your(area,animal):
    flashlist=[]
    #area 1~12 int型
    # 
    # ---area--
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # 10 11 12

    # ---animal---
    # int型
    # 0:ひよこ
    # 1:キリン
    # 2:ゾウ
    # 3:ライオン
    # 4:ニワトリ(ひよこの裏面)
    if animal>=10:
        animal=animal-10

    if animal==0:
        flashlist.append(area+3)
    
    if animal==1:
        flashlist.extend([area-3,area-1,area+1,area+3])
    
    if animal==2:
        flashlist.extend([area-4,area-2,area+2,area+4])

    if animal==3:
        flashlist.extend([area-4,area-3,area-2,area-1,area+1,area+2,area+3,area+4])
    
    newlist = [e for e in flashlist if e >= 1 and e<=12]
    
    #print(newlist)
    return newlist
    

def animalCheck(dict,area):
    for k, v in dict.items():
        if area==v:
            #print("0ヒヨコ 1キリン 2ゾウ 3ライオン　animal="+str(k))
            return k
    #print("no animal")
    return -1

def list_double_output(a,b):
    a_set=set(a)
    b_set=set(b)
    #aとbに共通するものを抽出
    c_set=a_set&b_set #3,30,103
    #結果をlistに変換
    c=list(c_set)
    #print(c)
    return c


def catchanimal(your_dict,downarea):
    for k,v in your_dict.items():
        if downarea==v:
            #print("相手の動物:"+str(k)+"を取れます")
            return k
    #取れるやつがないとき        
    return -1
       
def checkWinner(my_dict,your_dict):
    if 3 in my_dict and 3 in your_dict:
        return 0
    elif 3 in my_dict and 3 not in your_dict:
        #print('P1の勝利')
        return 1
    elif 3 not in my_dict and 3 in your_dict:
        #print("P2の勝利")
        return 2

def set_turn(turn_count,screen):
    font1 = pygame.font.SysFont("hg正楷書体pro", 50)
    if turn_count%2==1:
        #1pのターン
        text1 = font1.render("1P's turn", True, (255,0,0))
        screen.blit(text1, (150,500))
    if turn_count%2==0:
        #1pのターン
        text1 = font1.render("2P's turn", True, (255,0,0))
        screen.blit(text1, (150,500))

def setReplayButton(screen):
    shape1=400
    shape2=50
    len1=100
    len2=50
    font = pygame.font.SysFont("hg正楷書体pro", 25)
    text1 = font.render("Replay?", True, (0,0,0))
    pygame.draw.rect(screen,(255,255,0),Rect(shape1,shape2,len1,len2))
    screen.blit(text1, (420, 70))

def writePointatDis(x,y,screen,getkomalist):
    font = pygame.font.SysFont("hg正楷書体pro", 25)
    animal=getkomalist_area(x,y,getkomalist)
    text1 = font.render(str(x)+','+str(y) +' '+animal, True, (255,255,255))
    screen.blit(text1, (500, 100))

def getkomalist_area(x,y,getkomalist):
    anum=0
    if (350<=y and y<=400):
        if (400<=x and x<=450):
            anum = 1
        if (450<=x and x<=500):
            anum = 2
        if (500<=x and x<=550):
            anum = 3
        if (550<=x and x<=600):
            anum = 4
        if (600<=x and x<=650):
            anum = 5
        if (650<=x and x<=700):
            anum = 6
    if anum>=1:
        g=getkomalist[anum-1]
        return num_to_animal(g)
    else:
        return 'no'

def num_to_animal(num):
    if num==0:
        return 'ヒヨコ'
    elif num==1:
        return 'キリン'
    elif num==2:
        return 'ゾウ'
    elif num==3:
        return 'ライオン'
        

        
def judgePushButton(shape1,shape2,len1,len2,x,y):
    if x>=shape1 and x<=shape1+len1:
        if y>=shape2 and y<=shape2+len2:
            return True
    
    return False

def reset(my_dict,your_dict,gamefinflag,replaycount,judge,getkomalist,your_getkomalist):
    my_dict.clear()
    your_dict.clear()

    my_dict[0]=8
    my_dict[1]=12
    my_dict[2]=10
    my_dict[3]=11

    your_dict[0]=5
    your_dict[1]=1
    your_dict[2]=3
    your_dict[3]=2

    gamefinflag=0
    replaycount=0
    getkomalist.clear()
    your_getkomalist.clear()

    judge=False

def showMykoma(screen,zou,kirin,hiyoko,lion,getkomalist):
    count=0
    for i in getkomalist:
        if i==0:#ヒヨコ
            screen.blit(hiyoko, (400+count*50,350))
        if i==1:#キリン
            screen.blit(kirin, (400+count*50,350))
        if i==2:#ゾウ
            screen.blit(zou, (400+count*50,350))
        if i==3:#ライオン
            screen.blit(lion, (400+count*50,350))
        count+=1

def showyourkoma(screen,zou,kirin,hiyoko,lion,getkomalist):
    count=0
    for i in getkomalist:
        if i==0:#ヒヨコ
            screen.blit(hiyoko, (400+count*50,150))
        if i==1:#キリン
            screen.blit(kirin, (400+count*50,150))
        if i==2:#ゾウ
            screen.blit(zou, (400+count*50,150))
        if i==3:#ライオン
            screen.blit(lion, (400+count*50,150))
        count+=1


def judge_minikoma(x,y,getkomalist):
    length=len(getkomalist) #持ち駒の数
    #持ち駒のエリア
    if x>=400 and x<=400+length*50:
        if y>=350 and y<=400:
            #持ち駒の中
            if x>=400 and x<=450: #持ち駒リスト　エリア1
                return getkomalist[0]
            if x>=450 and x<=500: #持ち駒リスト　エリア1
                return getkomalist[1]
            if x>=500 and x<=550: #持ち駒リスト　エリア1
                return getkomalist[2]
            if x>=550 and x<=600: #持ち駒リスト　エリア1
                return getkomalist[3]
            if x>=600 and x<=650: #持ち駒リスト　エリア1
                return getkomalist[4]
            if x>=650 and x<=700: #持ち駒リスト　エリア1
                return getkomalist[5]
            #それぞれ数字を返す。0ヒヨコ 1キリン 2ゾウ 3ライオン
    
    return -1 #アニマルがない場合は-1


def judge_minikoma_your(x,y,getkomalist):
    length=len(getkomalist) #持ち駒の数
    #持ち駒のエリア
    if x>=400 and x<=400+length*50:
        if y>=150 and y<=200:
            #持ち駒の中
            if x>=400 and x<=450: #持ち駒リスト　エリア1
                return getkomalist[0]
            if x>=450 and x<=500: #持ち駒リスト　エリア1
                return getkomalist[1]
            if x>=500 and x<=550: #持ち駒リスト　エリア1
                return getkomalist[2]
            if x>=550 and x<=600: #持ち駒リスト　エリア1
                return getkomalist[3]
            if x>=600 and x<=650: #持ち駒リスト　エリア1
                return getkomalist[4]
            if x>=650 and x<=700: #持ち駒リスト　エリア1
                return getkomalist[5]
            #それぞれ数字を返す。0ヒヨコ 1キリン 2ゾウ 3ライオン
    
    return -1 #アニマルがない場合は-1

def get_airarea(my_dict,your_dict):#空きエリアリストを返す。
    air_area=[1,2,3,4,5,6,7,8,9,10,11,12]
    for k,v in my_dict.items():
        if v in air_area:
            air_area.remove(v)
    
    for k,v in your_dict.items():
        if v in air_area:
            air_area.remove(v)

    return air_area #空いているエリアリスト


    

