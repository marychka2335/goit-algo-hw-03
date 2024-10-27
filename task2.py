import turtle

def koch(size, level):
    if level == 0:
        turtle.forward(size)
    else:
        koch(size / 3, level - 1)
        turtle.left(60)
        koch(size / 3, level - 1)
        turtle.right(120)
        koch(size / 3, level - 1)
        turtle.left(60)
        koch(size / 3, level - 1)

def snowflake_koch(size, level):
    for _ in range(3):
        koch(size, level)
        turtle.right(120)

if __name__ == "__main__":
    turtle.speed(0)  
    turtle.hideturtle()  
    turtle.penup()
    turtle.goto(-200, 100)  
    turtle.pendown()
    try:
        recursion_level = int(input("Введіть рівень рекурсії (ціле число, максимум 10): "))
        if recursion_level > 10:
            print("Рівень рекурсії занадто високий, встановіть менше значення (максимум 10).")
        else:
            turtle.tracer(0, 0)  
            snowflake_koch(300, recursion_level)  
            turtle.update()  
    except ValueError:
        print("Неправильний ввід. Будь ласка, введіть дійсне ціле число для рівня рекурсії.")
    finally:
        print("Малювання завершено. Закрийте вікно для завершення програми.")
        turtle.done()  