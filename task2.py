import turtle

def koh(size, level):
    """
    Рекурсивна функція для малювання кривої Коха.
    """
    if level == 0:
        turtle.forward(size)
    else:
        koh(size / 3, level - 1)
        turtle.left(60)
        koh(size / 3, level - 1)
        turtle.right(120)
        koh(size / 3, level - 1)
        turtle.left(60)
        koh(size / 3, level - 1)

def snowflake_koh(size, level):
    """
    Малює фрактал сніжинка Коха.
    """
    for _ in range(3):
        koh(size, level)
        turtle.right(120)

if __name__ == "__main__":
    turtle.speed(0)  # Найшвидша швидкість малювання
    turtle.hideturtle()  # Приховати курсор черепахи
    turtle.penup()
    turtle.goto(-200, 100)  # Початкова позиція
    turtle.pendown()
    level_recurse = int(input("Введіть рівень рекурсії (ціле число): "))
    
    turtle.tracer(0, 0)  # Контроль частоти оновлення екрану
    snowflake_koh(300, level_recurse)  # Малюємо сніжинку
    turtle.update()  # Оновлюємо екран після завершення малювання
    
    print("Малювання завершено. Закрийте вікно для завершення програми.")
    turtle.done()  # Залишаємо вікно відкритим, поки користувач не закриє його
