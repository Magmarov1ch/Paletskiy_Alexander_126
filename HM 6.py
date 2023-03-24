def sub(x, y, z, cost):
    users = [("Алиса", x), ("Боб", y), ("Чарли", z)]
    users.sort(key=lambda user: user[1], reverse=True)
    for i in range(len(users)):
        for j in range(i + 1, len(users)):
            if users[i][1] + users[j][1] >= cost:
                return (users[i][0], users[j][0])
    return None
x = 100000 #победила в видео у MrBeast
y = 7.25
z = 3
cost = 19.99
result = sub(x, y, z, cost)
print(f"Купят подписку пользователи {result[0]} и {result[1]}")