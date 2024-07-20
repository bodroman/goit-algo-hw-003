import turtle

def koch_snowflake(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        koch_snowflake(length, depth-1)
        turtle.left(60)
        koch_snowflake(length, depth-1)
        turtle.right(120)
        koch_snowflake(length, depth-1)
        turtle.left(60)
        koch_snowflake(length, depth-1)

def draw_koch_snowflake(length, depth):
    for _ in range(3):
        koch_snowflake(length, depth)
        turtle.right(120)

def main():
    turtle.speed(0)  # Максимальна швидкість малювання
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()

    recursion_depth = int(input("Введіть рівень рекурсії: "))
    length = 400  # Довжина сторони сніжинки

    draw_koch_snowflake(length, recursion_depth)

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
