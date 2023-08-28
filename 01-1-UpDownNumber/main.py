import random

while True:
    correct_num = random.randint(1, 100)
    try_count = 0

    while True:
        input_text = input("1~100 사이의 숫자를 입력하세요: ")

        try:
            selected_num = int(input_text)
        except:
            print("올바른 입력이 아닙니다.")
            continue

        try_count = try_count + 1

        if selected_num == correct_num:
            print(f"축하합니다. {try_count}회 만에 맞췄습니다.")
            break

        if selected_num < correct_num:
            print("업")
        else:
            print("다운")

    input_text = input("다시 하시겠습니까? (Y/N): ")
    if input_text != "Y" and input_text != "y":
        break