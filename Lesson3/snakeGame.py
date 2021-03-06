import curses
from curses import textpad

def board(stdscr):

  # turnoff the cursor
  curses.curs_set(0)
  # turn around no delay
  stdscr.nodelay(1)
  #set timout to 0.1 seconds
  stdscr.timeout(100)

  sh, sw = stdscr.getmaxyx()

  # define the game board
  box = [
    [1, 1],
    [sh - 2, sw - 2]
  ]
  # draw the game board
  textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1] )

  # define the snake body
  snake = [
    # head is the first item
    [sh // 2, sw // 2 + 1],
    # body
    [sh // 2, sw // 2],
    # tail
    [sh // 2, sw // 2-1]
  ]

  snake_ch = chr(9608)

  # draw the snake body

  for point in snake:
    stdscr.addstr(point[0], point[1], snake_ch)

  # set the directon for the snake
  direction = curses.KEY_RIGHT

  while True: 
    key = stdscr.getch()

    if key == 27:
      break;

    if key == curses.KEY_UP:
      direction = curses.KEY_UP
    elif key == curses.KEY_RIGHT:
      direction = curses.KEY_RIGHT
    elif key == curses.KEY_DOWN:
      direction = key
    elif key == curses.KEY_LEFT:
      direction = key

    # here is how we move the snake one cell to right
    # Step 1, figure out the new head.
    head = snake[0]
    # decide the direction based on user's input key:
    if direction == curses.KEY_UP:
      new_head = [head[0] - 1, head[1]]
    elif direction == curses.KEY_RIGHT:
      new_head = [head[0], head[1] + 1]
    elif direction == curses.KEY_DOWN:
      new_head = [head[0] + 1, head[1]]
    elif direction == curses.KEY_LEFT:
      new_head = [head[0], head[1] -1]
    # step 2, draw the new head on game board.
    stdscr.addstr(new_head[0], new_head[1], snake_ch)
    # add new head to snake
    snake.insert(0, new_head)
    # step 3, erase the tail from game board.
    stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
    # remove the tail cell from snake.
    snake.pop()

    #check if new snake head touch game border
    snake[0][0]
    snake[0][1]

  stdscr.getch()


curses.wrapper(board)