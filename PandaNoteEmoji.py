
from PIL import Image, ImageDraw, ImageFont
import math

#熊猫日记生成器
class Panda_Note_Emoji:
    """
    熊猫日记表情生成器
    """
    """初始化数据"""
    def __init__(self):
        self.panda_img=self.__get_panda_img()
    
    """获取熊猫图片"""
    def __get_panda_img(self):
        img=Image.open('./images/panda.png')
        self.panda_width, self.panda_height=img.size
        self.font=ImageFont.truetype('./images/xiaowanzi.ttf', 12)
        return img
    
    #图片生成算法(不完善，有漏洞，如果是汉字还行，有英文字符会捉襟见肘)
    def __get_note_img(self,str):
        lenContent=len(str) #日记字数
         #第一行是有空格，只能输入21个汉子
        if(lenContent<21):
        #只有一行，也就是说图片的高度就是12px，高的两边加点距离给20px
            note_height=1*20
            #创建画布
            note_img=Image.new('RGB', (self.panda_width, note_height), (255, 255, 255))
            #作画
            draw=ImageDraw.Draw(note_img)
            #写字
            draw.text((20, 0), str, (0, 0, 0), font=self.font)
            #出图
            note_img.save('./images/panda_note.png', 'png')
        else:
            #超过21个汉字，需要算法计算高度()
            #计算日记内容行数
            note_rows=math.ceil((lenContent-21)/22)+1
            #计算日记图片高度
            note_height=note_rows*22
            #循环给每行加字幕
            pixel=0  #每行像素
            count=-1 #记录行数
            content_one=21 #第一行是21个汉字
            content_other=22 #其他行的汉字为23个
            content_number=0
        
            #创建画布
            note_img=Image.new('RGB', (self.panda_width, note_height), (255, 255, 255))
            #作画
            draw=ImageDraw.Draw(note_img)
            #循环给每行写字
            while(count<note_rows):
                if(count<0):
                    #第一行写21个汉子
                    sub_index=content_one-1
                    draw.text((30, pixel), str[0:sub_index], (0, 0, 0), font=self.font)
                    count=count+1
                    pixel=20
                    content_number=content_number+content_one
                else:
                    #其他行数汉字个数
                    #截取index
                    sub_index_next=(content_number+content_other)-1
                    draw.text((8, pixel), str[sub_index:sub_index_next], (0, 0, 0), font=self.font)
                    count+=1
                    pixel+=20
                    sub_index=sub_index_next
                    content_number=content_number+content_other

            #创一个块行的画布，宽度等于熊猫图片的宽度，高度=熊猫图片的高度+日记内容图片的高度
            panda_note_img=Image.new('RGB', ((self.panda_width), (self.panda_height+note_height)), (255, 255, 255))
            #拼接哪张图Image.paste
            #首先拼接熊猫图
            panda_note_img.paste(self.panda_img, box=(0, 0))
            #拼接日记图片
            panda_note_img.paste(note_img, box=(0, self.panda_height))
            #出图
            self.panda_note_img=panda_note_img
            #return panda_note_img
            #panda_note_img.save('./images/panda_note.png', 'png')
    
    def get_note_img(self, str):
        self.__get_note_img(str)
 
 
#p=Panda_Note_Emoji()
#print('panda_width:%d'%p.panda_width)
#str='我是一个大水比，啊哈哈！天气不是很好，燥热。工地砖头烫手，完全不想干活。但是包工头来监工了，只有硬着头皮干了。'
#p.get_note_img(str)
#p.panda_note_img.save('./images/panda_note.png', 'png')
