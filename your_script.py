# your_script.py

import datetime

def main():
    # 获取当前日期和时间
    now = datetime.datetime.now()
    print(f"当前日期和时间: {now}")

    # 进行一些基本的数学计算
    a = 5
    b = 3
    sum_result = a + b
    product_result = a * b

    print(f"{a} + {b} = {sum_result}")
    print(f"{a} * {b} = {product_result}")

if __name__ == "__main__":
    main()
