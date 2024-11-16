import turtle


def draw_koch_segment(t, length, level):
    if level == 0:
        # Draw a straight line if we've reached the base level
        t.forward(length)
    else:
        # Divide the segment into four smaller segments and recursively apply the Koch pattern
        length /= 3.0
        draw_koch_segment(t, length, level - 1)  # First segment
        t.left(60)  # Turn left for the next segment
        draw_koch_segment(t, length, level - 1)  # Second segment
        t.right(120)  # Turn right for the third segment
        draw_koch_segment(t, length, level - 1)  # Third segment
        t.left(60)  # Turn left back to the original direction
        draw_koch_segment(t, length, level - 1)  # Fourth segment


def draw_koch_snowflake(t, length, level):
    for _ in range(3):
        draw_koch_segment(t, length, level)
        t.right(120)  # Turn to start the next side of the triangle


def main():
    level = int(input("Enter the recursion level for the Koch snowflake (e.g., 3): "))

    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Koch Snowflake Fractal")

    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    t.penup()
    t.goto(-200, 100)  # Position turtle to make the snowflake centered
    t.pendown()

    draw_koch_snowflake(t, 400, level)

    turtle.done()


if __name__ == "__main__":
    main()
