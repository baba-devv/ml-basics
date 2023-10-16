if __name__ == '__main__':
    print('Normal linear regression !!')

x_i = [2, 3]
y_i = [500, 700]
m = 2  # this is the number of learning inputs

w = -100
b = 100


# w = 200, b = 100 should be the actual values after the learning ends
# assuming the function is f(x) = wx + b

def sum_dj_dw_calc(w_curr, b_curr):
    temp_diff_sum = 0
    for i in range(0, m):
        x = x_i[i]
        y = y_i[i]
        temp_diff_sum += ((w_curr * x) + b_curr - y) * x
    return temp_diff_sum / m


def sum_dj_db_calc(w_curr, b_curr):
    temp_diff_sum = 0
    for i in range(0, m):
        x = x_i[i]
        y = y_i[i]
        temp_diff_sum += (w_curr * x) + b_curr - y
    return temp_diff_sum / m


sum_dj_dw = sum_dj_dw_calc(w, b)
sum_dj_db = sum_dj_db_calc(w, b)

print(f"sum_dj_dw is {sum_dj_dw}")
print(f"sum_dj_db is {sum_dj_db}")

a = 1e-1

while True:
    w_cur = w
    b_cur = b
    w_done = False
    b_done = False
    if not w_done:
        w -= a * sum_dj_dw_calc(w, b)
        print(f"Updating the value of w to {w}")
    if not b_done:
        b -= a * sum_dj_db_calc(w, b)
        print(f"Updating the value of b to {b}")

    w_done = abs(w_cur - w) < 1e-3
    b_done = abs(b_cur - b) < 1e-3
    if w_done and b_done:
        print("Breaking because the change in w & b is minimal.")
        break

print(f"Final values for w & b are {w} & {b} respectively !!")
