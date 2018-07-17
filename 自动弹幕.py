# @Author  : ShiRui

from selenium import webdriver
import time


class Automatic:

    def automaticBarrage(self):

        try:
            chrome.get("https://www.douyu.com/5132911") # 进入获取主播的房间
            chrome.maximize_window()    # 浏览器窗口最大化
            chrome.implicitly_wait(15)  # 隐式等待
            print(chrome.title)     # 打印主播的标题
            time.sleep(5)   # 有些平台是需要渲染时间的，为了不报错，我们设置一个睡眠时间。

            chrome.find_element_by_link_text("登录").click()  # 和爬虫差不多吧，找到文本元素，.click是点击意思。
            time.sleep(3)

            chrome.switch_to.frame("login-passport-frame")  # 切换窗口
            time.sleep(5)

            chrome.find_element_by_xpath("//*[@id='loginbox']/div[2]/div[2]/div[3]/div/span[2]").click()
            # import： 找到loginbox的id，采用绝对定位，找到密码登陆。 //表示当前目录，*表示不指定标签名，@id='loginbox'表示id属性，
            # div[2]表示第二个div，后面同理。

            time.sleep(3)
            chrome.find_element_by_xpath("//*[@id='loginbox']/div[3]/div[2]/div[2]/div[2]/a[1]").click()
            #   上面的那段代码是点击QQ登录，还是通过绝对定位来实现。
            time.sleep(3)

            handle = chrome.current_window_handle   # 获取窗口句柄。
            # ps：selenium执行时并不会自动切换到新开的页签或者窗口上，还会停留在之前的窗口中，
            # 所以两次打印的句柄都一样。新开窗口后必须通过脚本来进行句柄切换，才能正确操作相应窗口中的元素
            print(handle)   # 打印句柄。

            handles = chrome.window_handles  # 获取当前所有窗口句柄（窗口A、B）

            for newhandle in handles:  # 对窗口进行遍历

                if newhandle != handle:  # 筛选新打开的窗口B

                    chrome.switch_to_window(newhandle)  # 切换到新打开的窗口B
                    chrome.switch_to.frame("ptlogin_iframe")   # 在新打开的窗口B中操作
            time.sleep(3)

            ele = chrome.find_element_by_id("switcher_plogin").click()  # 同理找到登陆的元素，然后点击去
            chrome.find_element_by_xpath("//*[@id='u']").send_keys("你的qq")
            chrome.find_element_by_xpath("//*[@id='p']").send_keys("你的密码")
            time.sleep(3)
            chrome.find_element_by_xpath("//*[@id='login_button']").click()
            # 输入qq和密码然后登陆

            print("登录成功")

            self.sendBarrage()

        except Exception as e:
            print(e)

    def sendBarrage(self):

        try:
            while True:
                chrome.find_element_by_xpath("//*[@id='js-send-msg']/textarea").send_keys("这刀妹无敌")
                # 同理发送弹幕。
                time.sleep(3)
                chrome.find_element_by_xpath("//*[@id='js-send-msg']/div[1]").click()
                chrome.find_element_by_xpath("//*[@id='js-send-msg']/textarea").clear()
                # 清空缓冲,避免和原本的文本出现拼接。
                print("已发送第一条弹幕")
                time.sleep(3)

                chrome.find_element_by_xpath("//*[@id='js-send-msg']/textarea").send_keys("主播666")
                time.sleep(3)
                chrome.find_element_by_xpath("//*[@id='js-send-msg']/div[1]").click()
                chrome.find_element_by_xpath("//*[@id='js-send-msg']/textarea").clear()
                print("已发送第二条弹幕")
                time.sleep(3)

                chrome.find_element_by_xpath("//*[@id='js-send-msg']/textarea").send_keys("大家可以点点关注")
                time.sleep(3)
                chrome.find_element_by_xpath("//*[@id='js-send-msg']/div[1]").click()
                chrome.find_element_by_xpath("//*[@id='js-send-msg']/textarea").clear()
                print("已发送第三条弹幕")
                time.sleep(3)

                chrome.find_element_by_xpath("//*[@id='js-send-msg']/textarea").send_keys("喜欢这个主播")
                chrome.find_element_by_xpath("//*[@id='js-send-msg']/div[1]").click()
                chrome.find_element_by_xpath("//*[@id='js-send-msg']/textarea").clear()
                print("已发送第四条弹幕")

        except Exception as e:

            print(e)


if __name__ == '__main__':

    chrome = webdriver.Chrome(executable_path="D:\chromedriver\chromedriver")
    # 先要下载一个chromchromeiver，自己下载需要翻墙，我会上传。链接：http://npm.taobao.org/mirrors/chromedriver
    automatic = Automatic()
    automatic.automaticBarrage()
