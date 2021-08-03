"""외계인 침공 게임에서는 플레이어가 화면 아래쪽 중앙에 나타나는 우주선을 조종한다.
플레이어는 화살표 키를 써서 우주선을 좌우로 움직일 수 있고, 스페이스 키를 눌러서 탄환을 발사할 수 있다.
게임이 시작하면 하늘을 가득 메운 외계인 함대가 좌우로 움직이며 점점 내려온다.
플레이어는 이 외계인들을 격추해야 한다. 플레이어가 외계인을 모두 물리치면 이전 함대보다 더 빨리 움직이는 새로운 함대가 나타난다.
외계인이 플레이어의 우주선과 부딪히거나 화면 아래쪽에 닿으면 플레이어는 우주선을 잃는다.
플레이어가 우주선 세 대를 잃으면 게임이 끝난다."""
import sys # 플레이어가 게임을 끝낼 때 필요한 도구가 있다.
import pygame  # 게임을 만드는 데 필요한 기능이 들어있다.

from settings import Settings

class AlienInvasion:
    """게임 전체의 자원과 동작을 관리하는 클래스"""

    def __init__(self):
        pygame.init() # 파이게임이 정상적으로 동작하기 위해 필요한 세팅을 초기화 한다. 
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height)) # pygame.display.set_mode()를 호출해 디스플레이 창을 생성. 매개변수 (1200,800)은 게임 창 크기를 정하는 튜플
        pygame.display.set_caption("Alien Invasion")
        
        # 배경색을 설정합니다.
        self.bg_color = (230, 230, 230)
    def run_game(self):
        """게임의 메인 루프를 시작합니다."""
        while True:
            #키보드와 마우스 이벤트를 주시합니다. 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #루프의 반복마다 화면을 다시 그립니다.
            self.screen.fill(self.settings.bg_color)
            
            #가장 최근에 그려진 화면을 표시합니다. 
            pygame.display.flip()

if __name__ == '__main__':
    # 게임 인스턴스를 만들고 게임을 실행합니다.
    ai = AlienInvasion()
    ai.run_game()            