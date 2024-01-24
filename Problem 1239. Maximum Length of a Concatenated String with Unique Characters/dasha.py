import curses
import time
import math

def draw_dasha(stdscr, frame):
    # ASCII art frames for each letter
    frames = {
        'I': [
            "II",
            "II",
            "II",
            "II",
            "II "
        ],
        'D': [
            "DDDDD ",
            "D    D",
            "D    D",
            "D    D",
            "DDDDD "
        ],
        'A': [
            "  A   ",
            " A A  ",
            "AAAAA ",
            "A   A ",
            "A   A "
        ],
        'S': [
            " SSSS ",
            "S     ",
            " SSSS ",
            "     S",
            " SSSS "
        ],
        'Heart': [
            "  **  **  ",
            " **** **** ",
            "***********",
            " ********* ",
            "  *******  ",
            "   *****   ",
            "    ***    ",
            "     *     "
        ],
        'H': [
            "H   H ",
            "H   H ",
            "HHHHH ",
            "H   H ",
            "H   H "
        ],
    }

    # Animation properties
    amplitude = 2  # Vertical amplitude of the heart beat

    # Display each letter frame side by side with animation
    x = 5
    y = 5
    for element in ['I', 'Heart', 'D', 'A', 'S', 'H', 'A']:
        lines = frames[element]

        # Apply a smooth vertical oscillation to each element
        y_offset = int(amplitude * math.sin(frame * 0.2))

        # Adjust heart size based on time
        if element == 'Heart':
            size_multiplier = 1 + 0.5 * math.sin(frame * 0.3)
            lines = [line.replace('*', '*' * int(size_multiplier)) for line in lines]

        for i, line in enumerate(lines):
            stdscr.addstr(y + i + y_offset, x, line)

        x += len(lines[0]) + 2  # Add some space between elements

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)

    # Number of frames in the animation
    num_frames = 120

    # Main animation loop
    for frame in range(num_frames):
        stdscr.clear()

        # Draw the animated ASCII art for the word 'DASHA' with a beating heart
        draw_dasha(stdscr, frame)

        # Refresh the screen
        stdscr.refresh()

        # Pause for a short time to control animation speed
        time.sleep(0.05)

curses.wrapper(main)
