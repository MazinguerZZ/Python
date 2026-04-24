def hero(bullets, dragons):
    if dragons * 2 <= bullets:
        return True
    else:
        return False

print(hero(10, 5))
print(hero(7, 4))