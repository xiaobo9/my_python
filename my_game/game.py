import sys
import pygame


class MoveImg:
    def __init__(self, _pygame, _screen, _image):
        # 加载logo图
        self.img = _pygame.image.load(_image)
        # 获取图像的位置
        self.position = self.img.get_rect()
        self.site = [0, 0]
        self.bg = (255, 255, 255)
        # 放置图片
        _screen.blit(self.img, self.position)

    def init_site(self):
        # 设置初始值
        self.site = [0, 0]

    def calc(self, _event):
        if _event.key == pygame.K_UP:
            self.site[1] -= 8
        if _event.key == pygame.K_DOWN:
            self.site[1] += 8
        if _event.key == pygame.K_LEFT:
            self.site[0] -= 8
        if _event.key == pygame.K_RIGHT:
            self.site[0] += 8

    def fill_back_ground(self, _screen):
        # 填充背景
        _screen.fill(self.bg)

    def move(self, _screen):
        # 计算新位置
        self.position = self.position.move(self.site)
        # 填充背景
        # _screen.fill(self.bg)
        # 放置图片
        _screen.blit(self.img, self.position)


class Some:
    def __init__(self):
        self.face = pygame.Surface((50, 50), flags=pygame.HWSURFACE)
        self.face.fill(color='pink')

        # 引入字体类型
        font = pygame.font.Font('C:/Windows/Fonts/simhei.ttf', 50)
        # 生成文本信息，第一个参数文本内容；第二个参数，字体是否平滑；第三个参数，RGB模式的字体颜色；第四个参数，RGB模式字体背景颜色；
        self.text = font.render("pygame", True, (255, 0, 0), (255, 255, 255))
        # 获得显示对象的rect区域坐标 设置显示对象居中 将准备好的文本信息，绘制到主屏幕 Screen 上。
        screen.blit(self.text, self.text.get_rect(center=(200, 200)))

    def blit(self):
        screen.blit(self.face, (100, 100))
        screen.blit(self.text, self.text.get_rect(center=(200, 200)))


if __name__ == '__main__':

    pygame.init()
    pygame.display.set_caption('hello world')

    # 设置主屏窗口
    screen = pygame.display.set_mode((400, 400))
    screen.fill('white')

    some = Some()

    move_image = MoveImg(pygame, screen, "peace.png")

    while True:
        move_image.init_site()
        # 循环获取事件，监听事件状态
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 图像移动 KEYDOWN 键盘按下事件 通过 key 属性对应按键
            if event.type == pygame.KEYDOWN:
                move_image.calc(event)

        move_image.fill_back_ground(screen)
        some.blit()
        move_image.move(screen)
        # 更新屏幕内容
        pygame.display.flip()
        # pygame.display.update()
