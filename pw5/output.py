import curses

def make_curses():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    return stdscr

def menu(stdscr):
    stdscr.clear()
    stdscr.addstr("Menu:\n")
    stdscr.addstr("0. Input number of students\n")
    stdscr.addstr("1. Input number of courses\n")
    stdscr.addstr("2. Input student information\n")
    stdscr.addstr("3. Input course information\n")
    stdscr.addstr("4. Show courses\n")
    stdscr.addstr("5. Show students\n")
    stdscr.addstr("6. Input marks\n")
    stdscr.addstr("7. Exit\n")
    stdscr.addstr("Enter your choice (Do not enter character): ")


def close_curse(stdscr):
    stdscr.addstr("Thanks for using.")
    stdscr.refresh()
    curses.nocbreak()
    stdscr.keypadd(False)
    curses.echo()
    curses.endwin()