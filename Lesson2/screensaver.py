import curses
import random

def window(stdscr):

  (sh,sw)=stdscr.getmaxyx()

  # setup colors
  curses.start_color()
  curses.use_default_colors()

  #initialize the color pairs
  for i in range (0, curses.COLORS):
    curses.init_pair(i+1, i, -1)
  #  stdscr.addstr(str(i + 1), curses.color_pair(i+1)) 
  #  i=i+1

  stdscr.nodelay(True)
  stdscr.timeout(100)

  while True:
    # get random letter 
    letter = random.randint(33,126)
    #get color
    color = random.randint(1,curses.COLORS+1)
    #GET LOCATION
    y = random.randint(0, sh-1)
    x = random.randint(0, sw-1)
    stdscr.addstr(y,x,chr(letter),curses.color_pair(color))
    if stdscr.getch() == 27:
      break
  

curses.wrapper(window)
