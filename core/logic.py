#!/usr/bin/env python

import os,sys,random, re, time
base_dir=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_dir)
from config import settings
from log.play_logger import logger
from db import sql_api



class people(object):
    def __init__(self, name, power_value, rage_value=0, blood_value=settings.BLOOD_VALUE):
        self.name = name
        self.power = power_value
        self.rage = rage_value
        self.blood = blood_value

    def status(self, ot_object):
        time.sleep(0.5)
        print("          %s： 血量：%s  愤怒：%s <------------>%s： 血量：%s  愤怒：%s" \
              % (ot_object.name, ot_object.blood, ot_object.rage, self.name, self.blood, self.rage))
    def add_blood(self):
        if self.blood < 100:
            blood_list = settings.ADD_BLOOD_RANDOM
            blood_i = random.randrange(0, len(blood_list))
            self.blood += blood_list[blood_i]
            self.rage += blood_list[blood_i]
            time.sleep(1)
            print("          %s+自加血：  血量：+%s   愤怒：+%s  " % (self.name, blood_list[blood_i], blood_list[blood_i]))
            logger.warning("%s：  血量：+%s   愤怒：+%s  " % (self.name, blood_list[blood_i], blood_list[blood_i]))

    def say(self, word):
        logger.info("%s: %s" % (self.name, word))
        time.sleep(1.5)
        return "%s: %s" % (self.name, word)

    def answer(self, word):
        answer_word = sql_api.answer_say(word)
        time.sleep(0.5)
        logger.info("%s: %s" % (self.name, answer_word))
        return "        %s: %s" % (self.name, answer_word)

    def blow_hurt(self, ot_object):
        hurt_blood_num = settings.BLOW_BLOOD_VALUE
        ot_object.blood -= hurt_blood_num * self.power
        ot_object.rage += hurt_blood_num
        logger.warning("%s：  血量：-%s   愤怒：+%s  " % (ot_object.name, hurt_blood_num * self.power, hurt_blood_num))
        self.add_blood()
        self.status(ot_object)


    def foot_hurt(self, ot_object):
        hurt_blood_num = settings.FOOT_BLOOD_VALUE
        ot_object.blood -= settings.FOOT_BLOOD_VALUE * self.power
        ot_object.rage += settings.FOOT_BLOOD_VALUE
        logger.warning("%s：  血量：-%s   愤怒：+%s  " % (ot_object.name, hurt_blood_num * self.power, hurt_blood_num))
        self.add_blood()
        self.status(ot_object)


class monsters(people):
    def arms_hurt(self, ot_object):
        hurt_blood_num = settings.ARMS_BLOOD_VALUE
        ot_object.blood -= settings.ARMS_BLOOD_VALUE * self.power
        ot_object.rage += settings.ARMS_BLOOD_VALUE
        logger.warning("%s：  血量：-%s   愤怒：+%s  " % (ot_object.name, hurt_blood_num * self.power, hurt_blood_num))
        self.add_blood()
        self.status(ot_object)


    def rage_hurt(self,ot_object):
        hurt_blood_num = random.randrange(settings.RAGE_BLOOD_VALUE_START,settings.RAGE_BLOOD_VALUE_STOP)
        ot_object.blood -= hurt_blood_num * self.power
        ot_object.rage += hurt_blood_num
        logger.warning("%s：  血量：-%s   愤怒：+%s  " % (ot_object.name, hurt_blood_num * self.power, hurt_blood_num))
        self.add_blood()
        self.status(ot_object)


class gods(monsters):
    def help_gods(self, otname_o):
        p_k('二 郎 神', otname_o)


def dialogue(name, otname):
    '''
    对话函数
    :param name:
    :param otname:
    :return:
    '''
    name_o = people(name, settings.CHARACTER_POWER[name])
    otname_o = gods(otname, settings.CHARACTER_POWER[otname])
    say_word = 1
    print(name_o.say("悟空，这里风景秀丽我们是到了何处？"))
    print(otname_o.answer("到了何处"))
    print(name_o.say("小白龙你还在等啥呢，快......."))
    time.sleep(3)
    print("\n          这样师徒二人来到了平顶山上。")

    while say_word:
        say_word = input("%s(输入对话内容)：" % name).strip()
        name_o.say(say_word)
        if not say_word:
            say_word = "。。"
        answer_word = otname_o.answer(say_word)
        print('''
            %s
        ''' % (answer_word))
        match = re.search(r"(走也)$", answer_word)
        if match:
            # print(match.group())
            say_word = None
    time.sleep(2)
    print("孙悟空刚刚离开，唐三藏只觉眼前一黑就被妖怪带走了。。。。。")
    time.sleep(2)
    print("悟空跟随到了一个妖洞口外，随后并与妖怪打成了一团。")
#dialogue("唐三藏", "悟空")

help_count = 0
def p_k(name,otname):
    '''
    打斗函数
    :param name:
    :param otname:
    :return:
    '''
    global help_count
    name_o = gods(name, settings.CHARACTER_POWER[name])
    if isinstance(otname,monsters):
        otname_o = otname
    else:
        otname_o = monsters(otname, settings.CHARACTER_POWER[otname])
    while name_o.blood > 0 and otname_o.blood > 0:
        time.sleep(0.5)
        arm = input("A,拳  B,脚  C,武器  D,暴击：").strip().lower()

        if arm == 'a':
            name_o.blow_hurt(otname_o)
        elif arm == 'b':
             name_o.foot_hurt(otname_o)
        elif arm == 'c':
            if name_o.rage >= settings.ARMS_RAGE_VALUE:
                name_o.arms_hurt(otname_o)
            else:
                logger.error("你的愤怒值不够%s，还没有必要使用武器" % settings.ARMS_RAGE_VALUE)
        elif arm == 'd':
            if name_o.rage >= settings.RAGE_HURT_RAGE_VALUE:
                name_o.rage_hurt(otname_o)
            else:
                logger.error("你的愤怒值不够%s，你还没有被激怒" % settings.RAGE_HURT_RAGE_VALUE)
        else:
            logger.error("你放弃了一个绝佳的攻击机会")
        time.sleep(1)
        if otname_o.blood <= 0:
            logger.error("老妖%s 已被铲除！恭喜过关！" % otname_o.name)
            break
        print("%s攻击：" % otname_o.name)
        time.sleep(1)
        if otname_o.rage < settings.ARMS_RAGE_VALUE:
            otname_o.blow_hurt(name_o)
        elif otname_o.rage >= settings.ARMS_RAGE_VALUE and otname_o.rage < settings.RAGE_HURT_RAGE_VALUE:
            otname_o.arms_hurt(name_o)
        elif otname_o.rage >= settings.RAGE_HURT_RAGE_VALUE:
            otname_o.rage_hurt(name_o)
        if name_o.blood <= 0:
            if help_count == 0 or help_count == 2:
                time.sleep(0.8)
                logger.error("%s    已阵亡！！%s打算晚上就蒸了唐僧，游戏结束！" % (name, otname_o.name))
                break
            else:
                logger.error("%s    已阵亡！！还得自己来啊- -！" % name)
                time.sleep(1)
                help_count = 2
                print("\n           此时，悟空和%s又打斗成一团....." % otname_o.name)

        if name_o.blood < settings.HELP_BLOOD_VALUE and help_count == 0:
            step = input("看来这妖怪来头不小你的血量不足，走为上计：A,逃跑来日再战 B,去搬救兵 C,继续战斗(默认)：").strip().lower()
            if step == 'c':
                pass
            if step == 'a':
                help_count += 1
                logger.error("今天运气不好，改日再来降你！")
                time.sleep(2)
                print("         这一天，%s和%s 又开战了。。。不知唐三藏在妖洞里情况如何？" % (name, otname_o.name))
                return p_k(name, otname)
            elif step == 'b':
                print("\n         突然间一道闪光远方传来“汪汪汪”!!")
                time.sleep(1)
                print("二郎神前来助降！！")
                help_count += 1
                name_o.help_gods(otname_o)


#p_k("孙 悟 空", "金角大王")

def main_run():
    dialogue("唐 三 藏", "孙 悟 空")
    p_k("孙 悟 空", "金角大王")