
import win32com
import win32com.client


def makePPT(path):
    ppt = win32com.client.Dispatch("PowerPoint.Application")
    ppt.Visible = True
    pptFile = ppt.Presentations.Add()  # 增加一个文件

    page1 = pptFile.Slides.Add(1, 1)   # 创建页面，参数1页数（从第一页开始），参数2：类型
    t1 = page1.Shapes[0].TextFrame.TextRange  # 第一页，Shapes[0]
    t1.Text = "ssss"  # 写入的具体内容
    t2 = page1.Shapes[1].TextFrame.TextRange  # 第一页，Shapes[1]
    t2.Text = "hello"  # 写入的具体内容
    page2 = pptFile.Slides.Add(2, 1)  # 第二页
    t3 = page2.Shapes[0].TextFrame.TextRange  # 第二页，Shapes[0]
    t3.Text = "python"   # 写入的具体内容
    t4 = page2.Shapes[1].TextFrame.TextRange  # 第二页，Shapes[1]
    t4.Text = "haha"     # 写入的具体内容

    page2 = pptFile.Slides.Add(3, 2)
    pptFile.SaveAs(path)  # 保存
    pptFile.Close()  # 关闭文件
    ppt.Quit()

path = r"G:\dd.ppt"
makePPT(path)









