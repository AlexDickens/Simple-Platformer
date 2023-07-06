import pygame



class homescreen:
        def homeScreen(self, screen, font):
                self.width = 800
                self.height = 400
                screen.fill((0,153,153))
                self.text1 = font.render("Alex Dickens Runner", False, (0,102,102))
                self.text1_rect = self.text1.get_rect(center = (self.width * 0.5, 100))
                
                
                self.homeImage = pygame.image.load("sprites/Player/player_walk_1.png")
                self.homeImage_rect = self.homeImage.get_rect(center = (self.width * 0.5, self.height * 0.5))
                self.restart = font.render("Press space to run", False, (0,102,102))
                self.restart_rect = self.restart.get_rect(center = (self.width * 0.5, 300))

                screen.blit(self.text1, self.text1_rect)
                
                screen.blit(self.homeImage, self.homeImage_rect)
                screen.blit(self.restart, self.restart_rect)
                
                