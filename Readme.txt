<<<<<<< HEAD
#Auth:cyalu

1.游戏情景：
	唐僧和悟空师徒二人如今来到了平顶山，游山玩水之时唐僧被莲花洞的金角大王抓去了洞里。悟空为救师傅与金角大王几番苦战。
2.主要功能：
	人物对话：输入对话内容，系统回复。
	人物战斗：
			A，拳 攻击 
			B，脚 攻击
			C，武器 攻击
			D，愤怒 攻击
	人物策略：
			A，逃跑
			B，搬救兵
			C，继续战斗
	功能参数设置：
		#人物血量
		BLOOD_VALUE = 100
		#拳打伤害血量
		BLOW_BLOOD_VALUE = 2
		#脚踢伤害血量
		FOOT_BLOOD_VALUE = 2
		#武器伤害血量
		ARMS_BLOOD_VALUE = 5
		#愤怒杀害血量范围
		RAGE_BLOOD_VALUE_START = 6
		RAGE_BLOOD_VALUE_STOP = 10
		#使用武器的愤怒值限制
		ARMS_RAGE_VALUE = 20
		#暴击愤怒值限制
		RAGE_HURT_RAGE_VALUE = 40
		#可以搬救兵的血量下限
		HELP_BLOOD_VALUE = 20
		#人物随机自加血和愤怒值数据配置列表
		ADD_BLOOD_RANDOM = [0, 0, 0, 0, 0.1, 1, 1, 1, 2,  5, 10, 20]
		#人物战斗力对照数据配置
=======
1.游戏情景：
	唐僧和悟空师徒二人如今来到了平顶山，游山玩水之时唐僧被莲花洞的金角大王抓去了洞里。悟空为救师傅与金角大王几番苦战。
2.主要功能：
	人物对话：输入对话内容，系统回复。
	人物战斗：
			A，拳 攻击 
			B，脚 攻击
			C，武器 攻击
			D，愤怒 攻击
	人物策略：
			A，逃跑
			B，搬救兵
			C，继续战斗
	功能参数设置：
		#人物血量
		BLOOD_VALUE = 100
		#拳打伤害血量
		BLOW_BLOOD_VALUE = 2
		#脚踢伤害血量
		FOOT_BLOOD_VALUE = 2
		#武器伤害血量
		ARMS_BLOOD_VALUE = 5
		#愤怒杀害血量范围
		RAGE_BLOOD_VALUE_START = 6
		RAGE_BLOOD_VALUE_STOP = 10
		#使用武器的愤怒值限制
		ARMS_RAGE_VALUE = 20
		#暴击愤怒值限制
		RAGE_HURT_RAGE_VALUE = 40
		#可以搬救兵的血量下限
		HELP_BLOOD_VALUE = 20
		#人物随机自加血和愤怒值数据配置列表
		ADD_BLOOD_RANDOM = [0, 0, 0, 0, 0.1, 1, 1, 1, 2,  5, 10, 20]
		#人物战斗力对照数据配置
>>>>>>> c07a90accd37013244ea243538c2447ab39b8d91
		CHARACTER_POWER = {"唐 三 藏": 0, "孙 悟 空": 2, "二 郎 神": 1, "金角大王": 1}