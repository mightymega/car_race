import curses
import random
import time

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 10, "Created by Brave")
    stdscr.addstr(2, 10, "Press any key to continue to the next screen...")
    stdscr.refresh()
    stdscr.getch()

    stdscr.clear()
    stdscr.addstr(0, 10, "Welcome to the Car Racing Game!")
    stdscr.addstr(2, 10, "Press any key to start the race...")
    stdscr.refresh()
    stdscr.getch()

def draw_window(stdscr, score):
    stdscr.clear()
    stdscr.border()
    stdscr.addstr(0, 2, f"Score: {score}")
    stdscr.refresh()

def game_over(stdscr, score):
    stdscr.clear()
    stdscr.addstr(0, 10, "Game Over!")
    stdscr.addstr(2, 10, f"Your score: {score}")
    stdscr.addstr(4, 10, "Press any key to exit...")
    stdscr.refresh()
    stdscr.getch()

def car_race_game(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    
    sh, sw = stdscr.getmaxyx()
    w = sw // 4
    car_x = sw // 2
    car_y = sh - 2

    obstacles = []
    score = 0

    while True:
        next_key = stdscr.getch()
        if next_key == curses.KEY_RIGHT and car_x < sw - 3:
            car_x += 1
        elif next_key == curses.KEY_LEFT and car_x > 1:
            car_x -= 1

        if random.randint(1, 100) > 98:
            obstacles.append([0, random.randint(1, sw - 2)])

        new_obstacles = []
        for obstacle in obstacles:
            obstacle[0] += 1
            if obstacle[0] < sh:
                new_obstacles.append(obstacle)
            if obstacle[0] == car_y and obstacle[1] == car_x:
                game_over(stdscr, score)
                return
        obstacles = new_obstacles

        draw_window(stdscr, score)
        stdscr.addstr(car_y, car_x, "C")

        for obstacle in obstacles:
            stdscr.addstr(obstacle[0], obstacle[1], "*")

        score += 1
        stdscr.refresh()

def main(stdscr):
    start_screen(stdscr)
    car_race_game(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)
