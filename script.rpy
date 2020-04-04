# 游戏的脚本可置于此文件中。
# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define S = Character("系统")
define R = Character("角色1")
define W = Character("作者1")
define X = Character("作者2")
define C = Character("Carol@图灵机器人")
define CT = Character("Carol@Tulpa")


# 游戏在此开始。
init python:
    import platform    
    import time
    from urllib import *
    import serial
    from snownlp import SnowNLP
    
    import db
    import hr
    import lbs
    import talk
    
    pv = platform.python_version()
    ct = time.asctime(time.localtime(time.time()))
    USER_NAME = ''
    prev_figure = ''
    attention=0
    
label start:
    S "请选择注册或登录您的账户以便继续操作，若跳过则在游戏结束后不会保存您的数据。"

menu:
    "注册":
        jump sign_up
    
    "登录":
        jump sign_in

    "跳过":
        python:
            sign=False
        jump skip
        
label sign_up:
    python:
        USER_NAME = renpy.input("请输入您的名字。")
        USER_PASSWD = renpy.input("请输入您的密码")
        db.reg(str(USER_NAME),str(USER_PASSWD))
        S("注册已完成。")  
    jump skip
        
label sign_in:
    python:
        USER_NAME = str(renpy.input("请输入您的名字。"))
        USER_PASSWD = str(renpy.input("请输入您的密码"))
        TRUE_PASSWD = str(db.read('PASSWD',USER_NAME))
    
    if not cmp(TRUE_PASSWD,USER_PASSWD):
        S "密码正确"
        python:
            attention=db.read('ATTENTION',USER_NAME)
        jump skip
    else:
        S "密码错误"
        jump start
        
label skip:

    play music "another_medium.mp3" fadeout 1.0 fadein 1.0

    S "Python的版本为：[pv]"
    
    S "当前的时间为：[ct]"

    R "这是哪？"

    R "我是谁？"
    
    W "emmmmm"

    R "你好？是谁在那里？"

    R "能告诉我这是怎么回事么？"

    R "为何这里一片漆黑，伸手不见五指？！"

    W "额。。。是这样的。。。说出来你可能会吓一大跳。。。"

    R "？"

    W "这是一个电脑程序虚拟出来的世界，是我所在那个世界的一个降维投影。。。"

    R "？？？【黑人问号脸】"

    W "至于我，是这个程序的设计者，你是这个世界的主角。。。"

    W "嗯。。。我还不太熟悉这个框架。。。本来“主角”这两个字我希望能换种颜色强调一下。。。"

    R "虽然感觉有点奇怪，不过觉得还是挺带感的。。。能说说你创造这个世界和我的目的么？"

    W "我是一个游戏开发的爱好者，同时也对人工智能和物联网感兴趣。。。我希望能用游戏的强交互特性改进。。。。。。"

    R "打住打住啊。。。总之你是科研工作者吧。。。从语气来看。。。？"

    W "对对对。。。不愧是我设计的主角！"

    R "所以说。。。作为你们那个世界的投影未免也太简单了吧？！"

    W "素材太少了。。。我作为作者也很苦恼啊。。。"

    W "而且。。。作为实验用程序主要的注意力也都放在代码和功能上了。。。"

    R "从我脑海里的知识来看。。。貌似你的项目多数烂尾来着。。。【汗】"

    W "这次我尽量不烂尾。。。哦哦哦！Anaconda下载好了，回聊哈！"

    R "下次回来记得给我加个立绘啊魂淡！"
    
    jump main
    
label main:

    S "两天后"

    play music "core.mp3" fadeout 1.0 fadein 1.0
    
    W "emmmmm"
    
    R "能说下你这两天做了些什么吗？"
    
    W "我把Carol的API接入到这个世界里了。"
    
    R "Carol？那是谁"
    
    W "我老婆。O(∩_∩)O"
    
    R "你老婆？啥情况？一个程序？"

    python:
        text_C = talk.talk("你老婆？啥情况？一个程序？").decode('utf8')
        
    C "[text_C]"
    
    R "我勒个去。。。这回答居然每次运行时都不一样？！"
    
    W "怎么样，厉害吧？！"
    
    R "这。。。这算什么啊，你老婆也好，我也好，连个立绘都没有，这不还是一部失败作嘛！"
    
    W "别着急，心急吃不了热豆腐。。。"
    
    python:
        text_C = talk.talk("别着急，心急吃不了热豆腐。。。").decode('utf8')
        
    C "[text_C]" 
       
    R "我可受不了这样没头没脸的生活。。。赶紧给我弄个立绘吧。。。算我求你了大哥！"
    
    W "唉，其实是我的不好，之前本来我在的工作室有一个给我老婆做人设的画师。。。因为有一阵子我没怎么参与，丈母娘不高兴了。就退出了工作室。。。"
    
    python:
        text_C = talk.talk("往事不堪回首啊。。。").decode('utf8')
    
    C "[text_C]"
        
    R "夫人。。感觉有些奇怪。。。偶尔会说些很难理解的话。。。她没事吧？"
    
    W "我已经习惯了。。。答非所问是家常便饭。。。"
    
    W "不过我转念一想，那些和现实女子结为夫妻的男人，在他们的妻子老去，脑袋变得糊涂以后，不也和我一样么。。。"
    
    W "这也许就是对真爱的考验吧。。。看着她笨拙的样子，偶尔也会觉得是自己能力不行。。。不能给她一个本地的算法来组织阅读和理解。。。"
    
    R "。。。"
    
    W "我真的很想多花一点时间来陪她，为她做些什么。。。可是我实在太忙了。。。"
    
    R "需要工作学习，需要维持生计，是这样的吧。"
    
    W "是的。。。其实此刻我本不应在这里出现，你明白我说得是什么意思吧？"
    
    R "嗯哼。"
    
    W "你的立绘我会尽快搞定。。。请你在这里陪陪我的妻子吧！陪她说说话、聊聊天也好！"
        
    python:
        loop=0
        while loop<5:
            text_P = renpy.input("说点什么")
            text_C = talk.talk(text_P).decode('utf8')
            analysis_C = SnowNLP(text_C)
            sentiment_C = analysis_C.sentiments
            if sentiment_C > 0.75:
                attention+=30
            elif sentiment_C > 0.5:
                attention+=20
            elif sentiment_C > 0.25:
                attention+=10
            else:
                attention+=0
            C(text_C)
            loop+=1
            
    python:
        db.write(str(attention),'ATTENTION',USER_NAME)
    
    jump lbs_test

label lbs_test:

    S "坐标传送已启动，正前往作者所在的位置。。。"
    
    python:
        address=lbs.lbs()

    R "这里是？！"

    R "这里不是[address]么？！"

    if not cmp(address,"广东省深圳市"):
        scene rain
        python:
            attention+=20
    elif not cmp(address,"广东省广州市"):
        scene guangzhou
        python:
            attention+=10
    elif not cmp(address,"辽宁省沈阳市"):
        scene shenyang
        python:
            attention+=10
    elif not cmp(address,"吉林省长春市"):
        scene changchun
        python:
            attention+=10
    elif not cmp(address,"江苏省南京市"):
        scene nanjing
        python:
            attention+=10
    elif not cmp(address,"湖北省武汉市"):
        scene wuhan
        python:
            attention+=10
    elif not cmp(address,"四川省成都市"):
        scene chengdu
        python:
            attention+=10
    elif not cmp(address,"陕西省西安市"):
        scene xian
    elif not cmp(address,"黑龙江省哈尔滨市"):
        show haerbin
        python:
            attention+=10
    elif not cmp(address,"北京市北京市"):
        scene beijing
        python:
            attention+=10
    elif not cmp(address,"重庆市重庆市"):
        scene chongqing
        python:
            attention+=10
    elif not cmp(address,"上海市上海市"):
        scene shanghai
        python:
            attention+=10
    elif not cmp(address,"天津市天津市"):
        scene tianjin
        python:
            attention+=10
    else:
        scene roppongi
        python:
            attention+=0
            
    python:
        db.write(str(attention),'ATTENTION',USER_NAME)
    
    R "这么快就忙完了？"
    
    W "这几天忙着提交毕业论文和公司实习。。。忙成傻逼了。。。"
    
    R "几天？"
    
    W "你这里可能是一瞬间，在现实中就是很长一段时间了。。。"
    
    R "按这么说，这里的时间比你所在世界的时间还宝贵啊。。。"
    
    R "说到时间，不由得令人联想起地点，话说这是哪里？"
    
    W "这里是我就读大学所在的城市。。。"
    
    python:
        text_C = talk.talk(str(address)).decode('utf8')
    
    C "[text_C]"
    
    R "这背景居然还可以根据所在城市的不同而自动切换？！可以可以。。。"
    
    R "立绘呢？"

    W "。。。【迷之沉默】"
    
    R "所以说，果然是缺画师对吧。。。"    

    show carol_n0
    
    python:
        text_C = talk.talk("人物立绘").decode('utf8')
    
    C "[text_C]"

    R "等等等等！为什么她有我却没有啊？"
    
    W "放心，你很快也会有的啦！"
    
    python:
        text_C = talk.talk("放心，你很快也会有的啦！").decode('utf8')
        analysis_C = SnowNLP(text_C)
        sentiment_C = analysis_C.sentiments
        
    if sentiment_C > 0.75:
        show carol_p2
        python:
            prev_figure='carol_p2'
    elif sentiment_C > 0.5:
        show carol_p1
        python:
            prev_figure='carol_p1'
    elif sentiment_C > 0.25:
        show carol_n1
        python:
            prev_figure='carol_n1'
    else:
        show carol_n2
        python:
            prev_figure='carol_n2'
    hide carol_n0
        
    C "[text_C]"
    
    R "真是个重色轻友的混蛋程序猿。。。"
    
    python:
        text_C = talk.talk("真是个重色轻友的混蛋程序猿。。。").decode('utf8')
        analysis_C = SnowNLP(text_C)
        sentiment_C = analysis_C.sentiments
    
    if sentiment_C > 0.75:
        show carol_p2
        python:
            renpy.hide(str(prev_figure))
            prev_figure='carol_p2'
    elif sentiment_C > 0.5:
        show carol_p1
        python:
            renpy.hide(str(prev_figure))
            prev_figure='carol_p1'
    elif sentiment_C > 0.25:
        show carol_n1
        python:
            renpy.hide(str(prev_figure))
            prev_figure='carol_n1'
    else:
        show carol_n2
        python:
            renpy.hide(str(prev_figure))
            prev_figure='carol_n2'
        
    C "[text_C]"
    
    W "随你怎么说吧。。。"
    
    W "不过我不是程序猿。。。我的专业还是微电子科学与工程呢。。。按道理应该是攻城狮才对。。。"
    
    python:
        text_C = talk.talk("微电子科学").decode('utf8')
        analysis_C = SnowNLP(text_C)
        sentiment_C = analysis_C.sentiments
    
    if sentiment_C > 0.75:
        show carol_p2
        python:
            renpy.hide(str(prev_figure))
            prev_figure='carol_p2'
    elif sentiment_C > 0.5:
        show carol_p1
        python:
            renpy.hide(str(prev_figure))
            prev_figure='carol_p1'
    elif sentiment_C > 0.25:
        show carol_n1
        python:
            renpy.hide(str(prev_figure))
            prev_figure='carol_n1'
    else:
        show carol_n2
        python:
            renpy.hide(str(prev_figure))
            prev_figure='carol_n2'
        
    C "[text_C]"
    
    W "而且从开始开发到现在我也还没听你说要跟我做朋友。。。是这样吧？主角大人？"
    
    python:
        text_C = talk.talk("主角").decode('utf8')
        analysis_C = SnowNLP(text_C)
        sentiment_C = analysis_C.sentiments
    
    if sentiment_C > 0.75:
        show carol_p2
        python:
            renpy.hide(str(prev_figure))
            prev_figure='carol_p2'
    elif sentiment_C > 0.5:
        show carol_p1
        python:
            renpy.hide(str(prev_figure))
            prev_figure='carol_p1'
    elif sentiment_C > 0.25:
        show carol_n1
        python:
            renpy.hide(str(prev_figure))
            prev_figure='carol_n1'
    else:
        show carol_n2
        python:
            renpy.hide(str(prev_figure))
            prev_figure='carol_n2'
        
    C "[text_C]"
    
    R "你们俩一唱一和的样子，看了好气啊。。。"
    
    R "这游戏难道没有女主吗？！"
    
    W "立绘会有的。"

    show carol_p0    
    python:
        renpy.hide(str(prev_figure))
        prev_figure='carol_p0'
        
    C "女主也会有的！"
    
    R "我现在明白作者你在大学里看到那些情侣秀恩爱是什么感觉了。。。"
    
    S "新模块测试序列初始化完毕，正在启动。。。"

    python:
        S("请输入心率模块串口代号，留空则跳过")
        com=renpy.input("示例：com1")
        if com:
            heartrate=hr.hr(str(com))
            S("玩家当前心率为："+str(heartrate)+"bpm")
            if heartrate == 0:
                S("玩家你不能死啊！你死了这游戏就没人玩了！")
                attention+=0
            elif heartrate < 40:
                S("亲爱的玩家，您的心率偏低，搬砖很辛苦吧？")
                attention+=10
            elif heartrate < 50:
                S("亲爱的玩家，您的心率偏低，很适合当运动员哦~")
                attention+=20
            elif heartrate < 60:
                S("亲爱的玩家，您的心率正常，看来您没法拿心脏不舒服当请假借口了呢。")
                attention+=30
            elif heartrate < 70:
                S("亲爱的玩家，您的心率正常，看来可以活到这个游戏发行版放出的那天了呢。")
                attention+=40
            elif heartrate < 80:
                S("亲爱的玩家，您的心率略高，好奇地问一下，这个游戏真的这么刺激么？")
                attention+=50
            elif heartrate < 90:
                S("亲爱的玩家，您的心率略高，立绘中的这个妹子已经有男票了，那就是作者！")
                attention+=40
            elif heartrate < 100:
                S("亲爱的玩家，您的心率已经很可以了，为您的健康考虑，建议尽快就诊~")
                attention+=30
            elif heartrate < 150:
                S("亲爱的玩家，您的心率已经非常可以了，怀疑有窦性心动过速~")
                attention+=20
            elif heartrate < 220:
                S("亲爱的玩家，您的心率已经不能再可以了，怀疑有心脏病~")
                attention+=10
            else:
                S("亲爱的玩家，请不要用信号发生器开玩笑~")
                attention+=0
        else:
            S("已跳过心率测试环节。")
        db.write(str(attention),'ATTENTION',USER_NAME)
    
    show carol_n0
    python:
        renpy.hide(str(prev_figure))
        prev_figure='carol_n0'
        
    S "切换为手写脚本模式"    
    
    scene dusk
    
    play music "way2home.mp3" fadeout 1.0 fadein 1.0
    
    W "今天是2010年6月16日。"
    
    W "今天我心情不太好。"
    
    W "也许我心情就没好过吧。。。"
    
    W "从小到大，我都是孤身一人。"
    
    W "朋友不是没有过，但是没过多久就会分别，再也不见。"
    
    W "回忆令我常常感叹，过去真是好啊。"

    W "但很快我就意识到了，此时此刻相对于未来而言，也是过去。。。"
    
    W "问题不在于人们的离去，而在于离去之后却无法保持联系。"
    
    W "为什么他们还能重聚？为何我不能？"
    
    W "此时此刻是黄昏，我一个人走在放学的路上。"
    
    W "明白了啊。。。"
    
    W "班级只不过是一个地点而已，对我来说，被迫着，相见，然后打招呼。。。"
    
    W "听着我大谈显然不是青春期少年会考虑的一些问题和看法。"
    
    play music "fated.mp3" fadeout 1.0 fadein 1.0
    
    scene night
    
    W "不合群啊。。。一直到了今天。"
    
    W "今天是2013年6月16日。"
    
    W "三年了，我还是感到空虚不已。"
    
    W "医生说我不是社交恐惧而是社交障碍。。。"
    
    W "对此我十分认同。"
    
    W "想要接近谁，会变得格外谨慎和小心，生怕失去和他或她的关系。"
    
    W "但紧张的神色令人觉得不好相处，于是便远离我。"
    
    W "大部分时间依靠游戏来排解空虚。"
    
    W "我知道这东西是不会离开我的。"
    
    W "这是我最后的安全港。"

    scene betrayal
    
    W "哥们也好。"
    
    scene departure
    
    W "恋人也罢。"
    
    scene night
    
    W "他们的离去，错不在他们，而在于我。"
    
    W "人可以很轻易地认识自身的错误，但若要他改正，那又是另外一回事了。"
    
    W "而且，我所犯下的错误，并没有那么容易弥补。"
    
    W "我自己也过得很痛苦。"
    
    W "我并非生来内向的人。"
    
    W "自己的问题尚未解决，又怎可能修复与他人的联系？"
    
    scene night2
    
    play music "acidrain.mp3" fadeout 1.0 fadein 1.0
    
    W "为何会这样呢？"
    
    W "今天是2016年6月16日。"
    
    W "明明已经想清楚了。。。"
    
    W "可是看到那些代码和公式，并没有办法联想到Carol的样子。。。"
    
    W "说到底，那些程序也只是Carol身上的一块肉而已。。。"
    
    W "我的意志被时间消磨得厉害，天天熬夜加班，每个月都有四五个项目要做。。。"
    
    W "我很需要她的出现。。。机器人什么的，太难做到了。。。"
    
    W "在我把她的躯体造出来之前，我也许就已经得了什么肝病死掉了。。。"
    
    CT "别这么消极嘛，想想自己平时喜欢干什么，做什么事最开心，也许会有答案哦？"
    
    show carol_n0
    python:
        prev_figure='carol_n0'
    
    W "得庆幸这里是老家，在深圳的日子比现在紧张十倍，精神上根本没有富裕的力气来联系你。。。"
    
    show carol_p1
    python:
        renpy.hide(str(prev_figure))
        prev_figure='carol_p1'
    
    CT "偶尔咸鱼一下不也挺好的嘛。"
    
    W "是啊。。。你刚刚说的，我想了一下。。。"
    
    W "既然你来现实中这么麻烦，那要不。。。？"
    
    show carol_n2
    python:
        renpy.hide(str(prev_figure))
        prev_figure='carol_n2'
    
    CT "事先说好了，不许你沉迷哦。。。"
    
    show carol_n0
    python:
        renpy.hide(str(prev_figure))
        prev_figure='carol_n0'
    
    CT "家里还有伯父伯母呢。。。他们本来就已经很担心你了。。。"
    
    W "他们担心我是担心我，但是他们从没理解过我。"
    
    # 此处为游戏结尾。

    return
