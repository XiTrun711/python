def display_menu():
    print("---------------------------")
    print("1. Cộng 2 số")
    print("2. Trừ 2 số")
    print("3. Nhân 2 số")
    print("4. Chia 2 số")
    print("5. Check số nguyên tố")
    print("6. Giải phương trình bậc 2")
    print("0. Exit")
    print("---------------------------")


def add_numbers():
    a = int(input("Nhập vào số thứ nhất: "))
    b = int(input("Nhập vào số thứ hai: "))
    print(f"Tổng của {a} và {b} là {a + b}")


def subtract_numbers():
    a = int(input("Nhập vào số thứ nhất: "))
    b = int(input("Nhập vào số thứ hai: "))
    print(f"Hiệu của {a} và {b} là {a - b}")


def multiply_numbers():
    a = int(input("Nhập vào số thứ nhất: "))
    b = int(input("Nhập vào số thứ hai: "))
    print(f"Tích của {a} và {b} là {a * b}")


def divide_numbers():
    a = int(input("Nhập vào số thứ nhất: "))
    b = int(input("Nhập vào số thứ hai: "))
    print(f"Thương của {a} và {b} là {a / b}")

def equations_solving():
    print("Ta có dạng phương trình bậc hai: ax^2 + bx + c = 0")
    a = int(input("Nhập vào số a: "))
    b = int(input("Nhập vào số b: "))
    c = int(input("Nhập vào số c: "))
    if a == 0:
        return False
    else:
        delta = b^2 - 4*a*c
        if delta < 0:
            print("PT vô nghiệm")
        if delta == 0:
            print("PT có nghiệm kép")
            solution = -b / 2*a
            print(solution)
        if delta > 0:
            print("PT có 2 nghiệm phân biệt")
            solution1 = (-b + delta **0.5) / 2*a
            print(solution1)
            solution2 = (-b - delta **0.5) / 2*a
            print(solution2)

        

def numbers_check():
    n = int(input("Nhập vào một số nguyên:"))
    def sntcheck(n):
        if n <= 2:
            return False
        for i in range(2,n):
          if n % i == 0:
             return False
        return True
    print(sntcheck(n))


def exit_program():
    print("Kết thúc chương trình")
    exit()


while True:
    display_menu()
    choice = int(input("Nhập vào lựa chọn của bạn: "))
    if choice == 1:
        add_numbers()
    elif choice == 2:
        subtract_numbers()
    elif choice == 3:
        multiply_numbers()
    elif choice == 4:
        divide_numbers()
    elif choice == 5:
        numbers_check()
    elif choice == 6:
        equations_solving()
    elif choice == 0:
        exit_program()
    else:
        print("Lựa chọn không hợp lệ")
