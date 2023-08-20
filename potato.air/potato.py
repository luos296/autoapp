# -*- encoding=utf8 -*-
__author__ = "luo"

from airtest.core.api import *

auto_setup(__file__, ['Android://127.0.0.1:5037/192.168.100.229:5555'])

wake()


def init_app():
    stop_app('com.iplay.potatoclash.taptap')
    start_app('com.iplay.potatoclash.taptap')
    sleep(25)


def up():
    swipe((540, 1800), (540, 600), duration=1, steps=6)
    sleep(1)


def down():
    swipe((540, 600), (540, 1800), duration=1, steps=6)
    sleep(1)


def sign():
    if exists(Template(r"tpl1691142414598.png", record_pos=(0.023, -0.484), resolution=(1080, 2340))):
        wait(Template(r"tpl1691142414598.png", record_pos=(0.023, -0.484), resolution=(1080, 2340)))
        sleep(3.0)
        if exists(Template(r"tpl1691142428909.png", record_pos=(0.019, 0.427), resolution=(1080, 2340))):
            touch(Template(r"tpl1691142428909.png", record_pos=(0.019, 0.427), resolution=(1080, 2340)))
        if exists(Template(r"tpl1691197836007.png", record_pos=(0.228, 0.43), resolution=(1080, 2340))):
            touch(Template(r"tpl1691197836007.png", record_pos=(0.228, 0.43), resolution=(1080, 2340)))
            ad()
        sleep(2)
        if exists(Template(r"tpl1691142449380.png", record_pos=(0.003, 0.64), resolution=(1080, 2340))):
            touch(Template(r"tpl1691142449380.png", record_pos=(0.003, 0.64), resolution=(1080, 2340)))
        touch(Template(r"tpl1691142535522.png", record_pos=(0.44, -0.531), resolution=(1080, 2340)))


def video_task():
    wait(Template(r"tpl1691149303069.png", record_pos=(0.253, -0.249), resolution=(1080, 2340)))
    touch(Template(r"tpl1691149303069.png", record_pos=(0.253, -0.249), resolution=(1080, 2340)))
    ad()
    wait(Template(r"tpl1691149519420.png", record_pos=(0.002, 0.629), resolution=(1080, 2340)))
    touch(Template(r"tpl1691149519420.png", record_pos=(0.002, 0.629), resolution=(1080, 2340)))
    wait(Template(r"tpl1691149544104.png", record_pos=(0.003, 0.64), resolution=(1080, 2340)))
    touch(Template(r"tpl1691149544104.png", record_pos=(0.003, 0.64), resolution=(1080, 2340)))


def box_click():
    wait(Template(r"tpl1691204848600.png", record_pos=(0.215, 0.362), resolution=(1080, 2340)))
    touch(Template(r"tpl1691204848600.png", record_pos=(0.215, 0.362), resolution=(1080, 2340)))
    ad()
    wait(Template(r"tpl1691204954139.png", record_pos=(0.006, 0.623), resolution=(1080, 2340)))
    touch(Template(r"tpl1691204954139.png", record_pos=(0.006, 0.623), resolution=(1080, 2340)))
    wait(Template(r"tpl1691204996891.png", record_pos=(0.005, 0.64), resolution=(1080, 2340)))
    touch(Template(r"tpl1691204996891.png", record_pos=(0.005, 0.64), resolution=(1080, 2340)))


def box():
    # 1
    if exists(Template(r"tpl1691204458677.png", record_pos=(-0.268, 0.621), resolution=(1080, 2340))):
        touch(Template(r"tpl1691204458677.png", record_pos=(-0.268, 0.621), resolution=(1080, 2340)))
        box_click()

    # 2
    if exists(Template(r"tpl1691217801511.png", record_pos=(-0.032, 0.623), resolution=(1080, 2340))):
        touch(Template(r"tpl1691217801511.png", record_pos=(-0.032, 0.623), resolution=(1080, 2340)))

    # 3
    if exists(Template(r"tpl1691204565381.png", record_pos=(0.206, 0.623), resolution=(1080, 2340))):
        touch(Template(r"tpl1691204565381.png", record_pos=(0.206, 0.623), resolution=(1080, 2340)))
        box_click()

    # 4
    if exists(Template(r"tpl1691204613326.png", record_pos=(0.445, 0.622), resolution=(1080, 2340))):
        touch(Template(r"tpl1691204613326.png", record_pos=(0.445, 0.622), resolution=(1080, 2340)))
        box_click()


def get_coin():
    touch(v=(200, 800))
    sleep(1)
    if exists(Template(r"tpl1691208248383.png", record_pos=(0.002, 0.211), resolution=(1080, 2340))):
        touch(Template(r"tpl1691208248383.png", record_pos=(0.002, 0.211), resolution=(1080, 2340)))

    sleep(2)
    touch(Template(r"tpl1691208098809.png", record_pos=(0.005, 0.269), resolution=(1080, 2340)))
    ad()
    sleep(10)


def rune():
    wait(Template(r"tpl1691147881520.png", record_pos=(-0.234, 0.763), resolution=(1080, 2340)))
    touch(Template(r"tpl1691147881520.png", record_pos=(-0.234, 0.763), resolution=(1080, 2340)))
    ad()
    wait(Template(r"tpl1691142449380.png", record_pos=(0.003, 0.64), resolution=(1080, 2340)))
    touch(Template(r"tpl1691142449380.png", record_pos=(0.003, 0.64), resolution=(1080, 2340)))


def rainbow():
    touch(Template(r"tpl1691203338351.png", record_pos=(-0.319, 0.048), resolution=(1080, 2340)))
    wait(Template(r"tpl1691144926391.png", record_pos=(0.002, 0.213), resolution=(1080, 2340)))
    touch(Template(r"tpl1691144926391.png", record_pos=(0.002, 0.213), resolution=(1080, 2340)))
    wait(Template(r"tpl1691142449380.png", record_pos=(0.003, 0.64), resolution=(1080, 2340)))
    touch(Template(r"tpl1691142449380.png", record_pos=(0.003, 0.64), resolution=(1080, 2340)))
    sleep(2)
    touch(Template(r"tpl1691200133024.png", record_pos=(0.003, 0.859), resolution=(1080, 2340)))
    ad()
    sleep(10)


def video():
    touch(Template(r"tpl1691149282624.png", record_pos=(-0.4, -0.799), resolution=(1080, 2340)))
    for i in range(3):
        video_task()
    wait(Template(r"tpl1691198778535.png", record_pos=(0.427, -0.581), resolution=(1080, 2340)))
    touch(Template(r"tpl1691198778535.png", record_pos=(0.427, -0.581), resolution=(1080, 2340)))


def rank():
    touch(Template(r"tpl1691370915530.png", record_pos=(0.131, -0.943), resolution=(1080, 2340)))
    wait(Template(r"tpl1691370947886.png", record_pos=(0.137, -0.697), resolution=(1080, 2340)))
    touch(Template(r"tpl1691370947886.png", record_pos=(0.137, -0.697), resolution=(1080, 2340)))
    wait(Template(r"tpl1691370994442.png", record_pos=(-0.229, 0.007), resolution=(1080, 2340)))
    touch(Template(r"tpl1691370994442.png", record_pos=(-0.229, 0.007), resolution=(1080, 2340)))
    wait(Template(r"tpl1691371076104.png", record_pos=(0.002, 0.634), resolution=(1080, 2340)))
    touch(Template(r"tpl1691371076104.png", record_pos=(0.002, 0.634), resolution=(1080, 2340)))
    touch(Template(r"tpl1691371122229.png", record_pos=(0.209, 0.006), resolution=(1080, 2340)))
    wait(Template(r"tpl1691371076104.png", record_pos=(0.002, 0.634), resolution=(1080, 2340)))
    touch(Template(r"tpl1691371076104.png", record_pos=(0.002, 0.634), resolution=(1080, 2340)))
    touch(Template(r"tpl1691371146422.png", record_pos=(-0.015, 0.6), resolution=(1080, 2340)))
    wait(Template(r"tpl1691371076104.png", record_pos=(0.002, 0.634), resolution=(1080, 2340)))
    touch(Template(r"tpl1691371076104.png", record_pos=(0.002, 0.634), resolution=(1080, 2340)))
    touch(Template(r"tpl1691371178788.png", record_pos=(0.445, -0.689), resolution=(1080, 2340)))


def fight():
    # 签到
    task(sign)
    # 视频宝箱
    task(video)
    # 排行点赞
    task(rank)
    # 箱子加速
    task(box)


def store():
    # 领取符文
    touch(Template(r"tpl1691143170546.png", record_pos=(-0.419, 1.011), resolution=(1080, 2340)))
    wait(Template(r"tpl1692516234520.png", record_pos=(-0.119, -0.749), resolution=(1080, 2340)))
    touch(Template(r"tpl1692516234520.png", record_pos=(-0.119, -0.749), resolution=(1080, 2340)))
    for i in range(3):
        rune()
    # 特惠商店
    wait(Template(r"tpl1691143280953.png", record_pos=(-0.349, -0.744), resolution=(1080, 2340)))
    touch(Template(r"tpl1691143280953.png", record_pos=(-0.349, -0.744), resolution=(1080, 2340)))
    up()
    up()
    for i in range(3):
        get_coin()

    # 领取彩虹豆
    wait(Template(r"tpl1691144808706.png", record_pos=(0.119, -0.744), resolution=(1080, 2340)))
    touch(Template(r"tpl1691144808706.png", record_pos=(0.119, -0.744), resolution=(1080, 2340)))
    swipe(Template(r"tpl1691200103510.png", record_pos=(-0.322, 0.136), resolution=(1080, 2340)),
          vector=[-0.0088, -0.2712], duration=1)
    for i in range(3):
        rainbow()


def league():
    wait(Template(r"tpl1691205594822.png", record_pos=(0.258, 1.004), resolution=(1080, 2340)))
    touch(Template(r"tpl1691205594822.png", record_pos=(0.258, 1.004), resolution=(1080, 2340)))
    wait(Template(r"tpl1691205661707.png", record_pos=(0.01, -0.939), resolution=(1080, 2340)))
    touch(Template(r"tpl1691205661707.png", record_pos=(0.01, -0.939), resolution=(1080, 2340)))
    wait(Template(r"tpl1691205694335.png", record_pos=(-0.002, -0.631), resolution=(1080, 2340)))
    touch(Template(r"tpl1691205694335.png", record_pos=(-0.002, -0.631), resolution=(1080, 2340)))
    wait(Template(r"tpl1691205726262.png", record_pos=(0.345, 0.696), resolution=(1080, 2340)))
    touch(Template(r"tpl1691205726262.png", record_pos=(0.345, 0.696), resolution=(1080, 2340)))
    wait(Template(r"tpl1691205765860.png", record_pos=(0.203, 0.303), resolution=(1080, 2340)))
    touch(Template(r"tpl1691205765860.png", record_pos=(0.203, 0.303), resolution=(1080, 2340)))
    ad()
    wait(Template(r"tpl1691205842087.png", record_pos=(0.002, 0.636), resolution=(1080, 2340)))
    touch(Template(r"tpl1691205842087.png", record_pos=(0.002, 0.636), resolution=(1080, 2340)))
    wait(Template(r"tpl1691205878201.png", record_pos=(0.438, -0.406), resolution=(1080, 2340)))
    touch(Template(r"tpl1691205878201.png", record_pos=(0.438, -0.406), resolution=(1080, 2340)))
    wait(Template(r"tpl1691205893655.png", record_pos=(0.461, -0.726), resolution=(1080, 2340)))
    touch(Template(r"tpl1691205893655.png", record_pos=(0.461, -0.726), resolution=(1080, 2340)))


def farm():
    wait(Template(r"tpl1691206218825.png", record_pos=(0.427, 0.995), resolution=(1080, 2340)))
    sleep(2)
    touch(Template(r"tpl1691206218825.png", record_pos=(0.427, 0.995), resolution=(1080, 2340)))

    sleep(2)
    if exists(Template(r"tpl1691206305555.png", record_pos=(-0.192, -0.558), resolution=(1080, 2340))):
        touch(Template(r"tpl1691206305555.png", record_pos=(-0.192, -0.558), resolution=(1080, 2340)))
        wait(Template(r"tpl1691206380730.png", record_pos=(-0.001, 0.127), resolution=(1080, 2340)))
        touch(Template(r"tpl1691206380730.png", record_pos=(-0.001, 0.127), resolution=(1080, 2340)))
        ad()
        sleep(2)
        touch(v=(770, 650))
        wait(Template(r"tpl1691206380730.png", record_pos=(-0.001, 0.127), resolution=(1080, 2340)))
        touch(Template(r"tpl1691206380730.png", record_pos=(-0.001, 0.127), resolution=(1080, 2340)))
        ad()
    if exists(Template(r"tpl1691405335155.png", record_pos=(-0.255, -0.207), resolution=(1080, 2340))):
        touch(Template(r"tpl1691405335155.png", record_pos=(-0.255, -0.207), resolution=(1080, 2340)))
        wait(Template(r"tpl1691405364034.png", record_pos=(0.205, 0.201), resolution=(1080, 2340)))
        touch(Template(r"tpl1691405364034.png", record_pos=(0.205, 0.201), resolution=(1080, 2340)))
        ad()
        wait(Template(r"tpl1691411641203.png", record_pos=(0.006, 0.633), resolution=(1080, 2340)))
        touch(Template(r"tpl1691411641203.png", record_pos=(0.006, 0.633), resolution=(1080, 2340)))
        sleep(1)
        touch(Template(r"tpl1691411698518.png", record_pos=(-0.245, -0.141), resolution=(1080, 2340)))
        sleep(2)
        swipe((540, 1500), (540, 900), duration=1, steps=6)
        touch(Template(r"tpl1691411819619.png", record_pos=(-0.106, 0.106), resolution=(1080, 2340)))
    if exists(Template(r"tpl1691411849672.png", record_pos=(0.253, -0.203), resolution=(1080, 2340))):
        touch(Template(r"tpl1691411849672.png", record_pos=(0.253, -0.203), resolution=(1080, 2340)))
        wait(Template(r"tpl1691405364034.png", record_pos=(0.205, 0.201), resolution=(1080, 2340)))
        touch(Template(r"tpl1691405364034.png", record_pos=(0.205, 0.201), resolution=(1080, 2340)))
        ad()
        wait(Template(r"tpl1691411641203.png", record_pos=(0.006, 0.633), resolution=(1080, 2340)))
        touch(Template(r"tpl1691411641203.png", record_pos=(0.006, 0.633), resolution=(1080, 2340)))
        sleep(1)
        touch(Template(r"tpl1691411952349.png", record_pos=(0.26, -0.127), resolution=(1080, 2340)))
        sleep(2)
        swipe((540, 900), (540, 1500), duration=1, steps=6)
        touch(Template(r"tpl1691412463628.png", record_pos=(0.099, -0.142), resolution=(1080, 2340)))
    if exists(Template(r"tpl1691412585752.png", record_pos=(-0.224, 0.178), resolution=(1080, 2340))):
        touch(Template(r"tpl1691412585752.png", record_pos=(-0.224, 0.178), resolution=(1080, 2340)))
        wait(Template(r"tpl1691405364034.png", record_pos=(0.205, 0.201), resolution=(1080, 2340)))
        touch(Template(r"tpl1691405364034.png", record_pos=(0.205, 0.201), resolution=(1080, 2340)))
        ad()
        wait(Template(r"tpl1691411641203.png", record_pos=(0.006, 0.633), resolution=(1080, 2340)))
        touch(Template(r"tpl1691411641203.png", record_pos=(0.006, 0.633), resolution=(1080, 2340)))
        sleep(1)
        touch(Template(r"tpl1691412662933.png", record_pos=(-0.218, 0.248), resolution=(1080, 2340)))
        sleep(2)
        touch(Template(r"tpl1691412690793.png", record_pos=(-0.106, 0.249), resolution=(1080, 2340)))
    if exists(Template(r"tpl1691412719006.png", record_pos=(0.23, 0.178), resolution=(1080, 2340))):
        touch(Template(r"tpl1691412719006.png", record_pos=(0.23, 0.178), resolution=(1080, 2340)))
        wait(Template(r"tpl1691405364034.png", record_pos=(0.205, 0.201), resolution=(1080, 2340)))
        touch(Template(r"tpl1691405364034.png", record_pos=(0.205, 0.201), resolution=(1080, 2340)))
        ad()
        wait(Template(r"tpl1691411641203.png", record_pos=(0.006, 0.633), resolution=(1080, 2340)))
        touch(Template(r"tpl1691411641203.png", record_pos=(0.006, 0.633), resolution=(1080, 2340)))
        sleep(1)
        touch(Template(r"tpl1691412868704.png", record_pos=(0.233, 0.256), resolution=(1080, 2340)))
        sleep(2)
        touch(Template(r"tpl1691412905574.png", record_pos=(0.305, 0.25), resolution=(1080, 2340)))


def ad():
    sleep(15)
    if exists(Template(r"tpl1691147046441.png", record_pos=(0.006, 0.51), resolution=(1080, 2340))):
        touch(Template(r"tpl1691147046441.png", record_pos=(0.006, 0.51), resolution=(1080, 2340)))
    sleep(10)
#     wait(Template(r"tpl1691145090649.png", record_pos=(0.405, -0.932), resolution=(1080, 2340)))
#     touch(Template(r"tpl1691145090649.png", record_pos=(0.405, -0.932), resolution=(1080, 2340)))
    wait(Template(r"tpl1691631186295.png", record_pos=(0.409, -0.927), resolution=(1080, 2340)))
    touch(Template(r"tpl1691631186295.png", record_pos=(0.409, -0.927), resolution=(1080, 2340)))
    sleep(1.0)

    if exists(Template(r"tpl1691197986546.png", record_pos=(0.405, -0.986), resolution=(1080, 2340))):
        touch(Template(r"tpl1691197986546.png", record_pos=(0.405, -0.986), resolution=(1080, 2340)))


def task(func):
    try:
        func()
    except:
        log(f"____________{func.__name__}执行失败_____________")
        init_app()


def run():
    init_app()
    task(fight)
    task(store)
    task(league)
    task(fight)
    farm()


if __name__ == '__main__':
    run()
    keyevent('POWER')