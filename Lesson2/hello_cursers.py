import curses

def window(stdscr):

  (sh,sw)=stdscr.getmaxyx()

  #print the welcome message.
  msg = "hello somethng!"
  stdscr.addstr(sh//3, sw//3,msg)
  while True:
    userKey= stdscr.getch()
    stdscr.addstr("ASCII:{0}".format(userKey))
    if userKey == 27:
        break
  stdscr.getch()

curses.wrapper(window)
