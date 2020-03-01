import arcade

# Constants - These are values that do not change once they are set. If you know that you will reuse the same value repeately throughout the code, it will be beneficial to create a constant variable for that value.

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Ready, Set, Code: My First Python Game"

class MyGame(arcade.Window):
    """
    Main Game Application Class
    """

    def __init__(self):
      # Calls the parent class and sets up the window
      super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

      arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        # Set up the game here. Call this function to restart the game.
        pass
    
    def on_draw(self):
        # Renders the screen
        arcade.start_render()
        # Code to draw the screen goes here

def main():
    # Main Method
    window = MyGame()
    window.setup()
    window.run()

if __name__ == "__main__":
    main()