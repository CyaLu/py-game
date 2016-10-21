#!/usr/bin/env python
import os, sys, json, random, re
base_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_dir)
data_dir = base_dir + '/db/say_data'
with open(data_dir, "r", encoding='utf-8') as f:
    say_data = json.load(f)

def answer_say(say_word):
    match_w = re.search(r"[a-zA-Z]+", say_word)
    match_song = re.search(r"~+", say_word)
    match_wy = re.search(r"[.。，‘、·]{2,}]", say_word)
    match_gt = re.search(r"[！啊呀][！啊呀]?", say_word)
    match_yg = re.search(r"[妖怪鬼]+", say_word)
    match_yg2 = re.search(r".*[去到]?.*[(看)(打探)]+", say_word)
    match_el = re.search(r"饿", say_word)
    match_wt = re.search(r"[？吗么]$", say_word)
    if match_w:
        say_word = '鸟语'
    elif match_yg or match_yg2:
        say_word = '妖怪'
    elif match_el:
        say_word = '饿了'
    elif match_wt:
        say_word = '？'

    elif match_song:
        say_word = '~'
    elif match_wy:
        say_word = '。。'
    elif match_gt:
        say_word = '！'
    if say_word not in list(say_data.keys()):
        say_word='无=语'
    return (say_data[say_word][random.randrange(0,len(say_data[say_word]))])

#answer_say("紧箍咒")
