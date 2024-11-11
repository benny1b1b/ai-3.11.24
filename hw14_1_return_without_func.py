
def ascending_my(a: int, b: int):
    """הפונקציה מדפיסה את המספרים בסדר עולה"""
    if a < b:
        print(a, b)
    if b < a:
        print(b, a)
ascending_my(7,-12)


def details_my(word: str):
    """הפונקציה מדפיסה את האות הראשונה האמצעית והאחרונה של המילה"""
    if word:
        print(word)
        print(word[0], end=" ")
        print(word[len(word)//2], end=" ")
        print(word[-1])

details_my("israel")
details_my("AI is the best")


import statistics



def bool_say(bool1: bool):
    """פונקציה שמקבלת ערך בוליאני ומדפיסה yes אם הערך True או no אם הערך False"""
    if bool1:
        print("yes")
    else:
        print("no")

bool_say(True)
bool_say(False)
bool_say(0)



def print_zugi(list1:list[int]):
    if list1:
        print(list1)
        print(["even" if num %2 == 0 else "odd" for num in list1])


print_zugi([14, 14, 15, 10, 2, 3, 5])


def my_statistics(score_list: list[int]):
    print(f"score list: {score_list}")
    print(f"the highest score in the list: {max(score_list)}")
    print(f"the lowest score: {min(score_list)}")
    print(f"the amount of score: {len(score_list)}")
    print(f"the grade point average: {statistics.mean(score_list):.2f}")

l_score: list[int] = []
SENTINEL: int = -99

while True:
    try:
        score: int = int(input("enter your score:"))
        if score == SENTINEL:
            break
        if 0 > score or score > 100:
            continue
        else:
            l_score.append(score)
    except ValueError as e:
        print(e)

print(l_score)

my_statistics([44, 55, 67, 87, 55, 44, 33, 77, 66, 55, 44, 87, 98, 56, 78, 65, 45])
