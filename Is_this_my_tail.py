def correct_tail(body, tail):
    for i in range(len(body)):
        if body[-1] == tail:
            return True
        return False
print(correct_tail("Emu", "t"))