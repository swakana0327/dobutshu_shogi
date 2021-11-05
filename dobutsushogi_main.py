# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys
import dobutsushogi_module as dm


def main():
    dx=[]
    dy=[]
    pygame.init()                                               # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))                # 大きさ600*500の画面を生成
    pygame.display.set_caption("どうぶつしょうぎ　神戸大学大学院 若菜理志")                          # タイトルバーに表示する文字

    font1 = pygame.font.SysFont("hg正楷書体pro", 50)
    dm.setboard(screen)

        #普通に画像を表示する方法
    kirin = pygame.image.load("kirin.png")
    kirin = pygame.transform.scale(kirin, (100, 100))
    kirin_teki=pygame.transform.flip(kirin, True, True)
    minikirin=pygame.transform.scale(kirin, (50, 50))
        #一部の色を透明にする
    hiyoko = pygame.image.load("hiyoko.png")
    hiyoko = pygame.transform.scale(hiyoko, (100, 100))
    hiyoko_teki=pygame.transform.flip(hiyoko, True, True)
    minihiyoko=pygame.transform.scale(hiyoko, (50, 50))


    colorkey = hiyoko.get_at((0,0))
    hiyoko.set_colorkey(colorkey, RLEACCEL)
        
        #画像の大きさを変える
    lion = pygame.image.load("lion.png")
    lion = pygame.transform.scale(lion, (100, 100)) #200 * 130に画像を縮小
    lion_teki=pygame.transform.flip(lion, True, True)
    minilion=pygame.transform.scale(lion, (50, 50))

    zou  = pygame.image.load('ele.png')
    zou = pygame.transform.scale(zou, (100, 100))
    zou_teki=pygame.transform.flip(zou, True, True)
    minizou = pygame.transform.scale(zou, (50, 50))

    #自分の駒
    my_dict={0:8,1:12,2:10,3:11} #animal,areaの順

    #相手の駒
    your_dict={0:5,1:1,2:3,3:2}
    
    dm.setanimal(screen,zou,kirin,hiyoko,lion,my_dict)
    bdownlist=[]
    buplist=[]
    judge=False
    replaycount=0
    gamefinflag=0
    getkomalist=[]
    your_getkomalist=[]
    red_paint_area=[]
    red_area=-1
    minikoma=-1 #取った駒を盤面に置くかどうかのフラグ。基本的には-1 持ち駒を触ったときは0~4の値
    turn_count=1 #ターン数のカウント、奇数だと手前側、偶数だと奥側

    while (1):

        

        dm.setanimal(screen,zou,kirin,hiyoko,lion,my_dict)
        dm.setanimal(screen,zou_teki,kirin_teki,hiyoko_teki,lion_teki,your_dict)
        dm.showMykoma(screen,minizou,minikirin,minihiyoko,minilion,getkomalist)
        dm.showyourkoma(screen,minizou,minikirin,minihiyoko,minilion,your_getkomalist)
        dm.set_turn(turn_count,screen)
        

        gamefinflag=dm.checkWinner(my_dict,your_dict)
        if gamefinflag != 0:
            dm.setboard(screen)
            dm.setanimal(screen,zou,kirin,hiyoko,lion,my_dict)
            dm.setanimal(screen,zou_teki,kirin_teki,hiyoko_teki,lion_teki,your_dict)
            dm.showMykoma(screen,minizou,minikirin,minihiyoko,minilion,getkomalist)
            dm.showyourkoma(screen,minizou,minikirin,minihiyoko,minilion,your_getkomalist)
            text1 = font1.render(str(gamefinflag)+"P Win!!", True, (255,0,0))
            screen.blit(text1, (150,500))
            if judge==False:
                dm.setReplayButton(screen)
                judge=dm.judgePushButton(400,50,100,50,x,y)
                #if judge:

        if judge and gamefinflag!=0:
            #ゲームやり直し　dict,盤面,フラグ等全リセット
            dm.reset(my_dict,your_dict,gamefinflag,replaycount,judge,getkomalist,your_getkomalist)
            gamefinflag=0
            replaycount=0
            turn_count=1
            judge=False

        pygame.display.update()                                 # 画面を更新
        # イベント処理
        mouse_pressed = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type==MOUSEBUTTONDOWN:
                #print("turn_count="+str(turn_count))
                if turn_count%2==1:
                    x, y = event.pos
                    bdownlist.append(x)
                    bdownlist.append(y)
                    dm.animalCheck(my_dict,dm.getArea(x,y))
                    area=dm.getArea(x,y)
                    animal=dm.animalCheck(my_dict,area)
                    next=dm.getNext(animal,area,my_dict)
                    #print('---ミニコマの判定---')
                    #print(dm.judge_minikoma(x,y,getkomalist))
                    minikoma=dm.judge_minikoma(x,y,getkomalist)
                    for fact in next:
                        p=dm.AreatoPoint(fact)
                        #print(p)
                        dx.append(p[0])
                        dy.append(p[1])
                    if next:
                        for n in next:
                            p=dm.AreatoPoint(n)
                            pygame.draw.rect(screen,(0,80,0),Rect(p[0],p[1],100,100))
                    
                    if minikoma>=0: #持ち駒リストから参照
                        #print('red?area')
                        #print(red_area)
                        for n in dm.get_airarea(my_dict,your_dict):
                            if n!=red_area:
                                p=dm.AreatoPoint(n)
                                pygame.draw.rect(screen,(255,102,204),Rect(p[0],p[1],100,100))
                
                if turn_count%2==0:
                    x, y = event.pos
                    bdownlist.append(x)
                    bdownlist.append(y)
                    dm.animalCheck(your_dict,dm.getArea(x,y))
                    area=dm.getArea(x,y)
                    animal=dm.animalCheck(your_dict,area)
                    next=dm.getNext_your(animal,area,your_dict)
                    #print('---ミニコマの判定---')
                    #print(dm.judge_minikoma_your(x,y,your_getkomalist))
                    minikoma=dm.judge_minikoma_your(x,y,your_getkomalist)
                    for fact in next:
                        p=dm.AreatoPoint(fact)
                        #print(p)
                        dx.append(p[0])
                        dy.append(p[1])
                    if next:
                        for n in next:
                            p=dm.AreatoPoint(n)
                            pygame.draw.rect(screen,(0,80,0),Rect(p[0],p[1],100,100))
                    if judge==False and gamefinflag!=0:
                        judge=dm.judgePushButton(400,50,100,50,x,y)
                        if judge==True:
                            replaycount+=1
                    if minikoma>=0: #持ち駒リストから参照
                        #print('red?area')
                        #print(red_area)
                        for n in dm.get_airarea(your_dict,my_dict):
                            if n!=red_area:
                                p=dm.AreatoPoint(n)
                                pygame.draw.rect(screen,(255,102,204),Rect(p[0],p[1],100,100))
                
                
                        
            


                
                

            if event.type==MOUSEBUTTONUP:
                #print("turn_count="+str(turn_count))
                dm.setboard(screen)


                if turn_count%2==1:
                    #print("☟から来たよ")
                    #print(bdownlist)
                    x, y = event.pos
                    zahyo=[]
                    zahyo.append(x)
                    zahyo.append(y)
                    #print(zahyo)
                    comearea=dm.PointtoArea(bdownlist)
                    downarea=dm.PointtoArea(zahyo)
                    #print("downarea="+str(downarea))
                    #print('---')
                    #print('---')

                    if dm.animalCheck(my_dict,comearea) >=0:
                        
                        if downarea in next:
                            my_dict[dm.animalCheck(my_dict,comearea)]=downarea
                            catchnum=dm.catchanimal(your_dict,downarea)
                            if catchnum>=0:
                                your_dict.pop(catchnum)
                                getkomalist.append(catchnum)
                            turn_count+=1
                            continue
                             
                    
                    #取った駒を盤面に置くやつ。
                    if minikoma>=0:
                        set_area=dm.getArea(x,y)
                        #print('着地エリア'+str(set_area))
                        #print('---着地エリアが空かどうか判定---')
                        if set_area in dm.get_airarea(my_dict,your_dict): #着地エリアが空かどうか
                            my_dict[minikoma+10]=set_area
                            #取った駒を盤面に置いたら、持ち駒リストから削除
                            getkomalist.remove(minikoma)             
                            turn_count+=1
                            continue
                          
              
                    
                    dm.setboard(screen)
                    dx.clear()
                    dy.clear()
                    zahyo.clear()
                    bdownlist.clear()
                    next.clear()
                    

                if turn_count%2==0:
                    #print("☟から来たよ")
                    #print(bdownlist)
                    x, y = event.pos
                    zahyo=[]
                    zahyo.append(x)
                    zahyo.append(y)
                    #print(zahyo)
                    comearea=dm.PointtoArea(bdownlist)
                    downarea=dm.PointtoArea(zahyo)
                    #print("downarea="+str(downarea))
                    #print('---')
                    #print('---')

                    if dm.animalCheck(your_dict,comearea) >=0:
                        
                        if downarea in next:
                            your_dict[dm.animalCheck(your_dict,comearea)]=downarea
                            catchnum=dm.catchanimal(my_dict,downarea)
                            if catchnum>=0:
                                my_dict.pop(catchnum)
                                your_getkomalist.append(catchnum)
                            turn_count+=1
                            continue

                                  
                    
                    #取った駒を盤面に置くやつ。
                    if minikoma>=0:
                        set_area=dm.getArea(x,y)
                        #print('着地エリア'+str(set_area))
                        #print('---着地エリアが空かどうか判定---')
                        if set_area in dm.get_airarea(your_dict,my_dict): #着地エリアが空かどうか
                            your_dict[minikoma+10]=set_area
                            #取った駒を盤面に置いたら、持ち駒リストから削除
                            your_getkomalist.remove(minikoma)
                            turn_count+=1
                            continue

                                 

                    
                dm.setboard(screen)
                dx.clear()
                dy.clear()
                zahyo.clear()
                bdownlist.clear()
                next.clear()
        


            if event.type == QUIT:                              # 閉じるボタンが押されたら終了
                pygame.quit()                                   # Pygameの終了(画面閉じられる)
                sys.exit()
        


        
        

        

        


if __name__ == "__main__":
    main()