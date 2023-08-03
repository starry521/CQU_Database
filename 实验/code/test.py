import psycopg2
import tkinter as tk

#创建连接对象
conn=psycopg2.connect(database="db_2020_01", user="db_user2020_75", password="db_user@123", host="116.205.157.173", port=8000)

#创建指针对象
cur=conn.cursor()


# 登录按钮点击事件处理函数
def login():
    username = entry_username.get()
    password = entry_password.get()
    if username == 'admin' and password == '123456':

        lbl_result.config(text='登录成功！')

        # 销毁当前登录窗口
        root.destroy()

    else:
        
        lbl_result.config(text='用户名或密码错误！')


def submit():
    sql = SQL_input.get("1.0", tk.END)

    # 执行SQL语句
    cur.execute(sql)

    # 获取查询结果
    result = cur.fetchall()

    # 在结果标签中显示查询结果
    res_show.delete("1.0", tk.END)
    res_show.insert(tk.END, result)



# 创建主窗口
root = tk.Tk()
root.title('企业员工管理系统')

# 设置窗口尺寸
root.geometry('400x200+500+100')  # 设置宽度为400像素，高度为200像素

# 用户名
label_username = tk.Label(root, text='用户名：', width=10)
label_username.grid(row=0, column=1, padx=20)  # 放置在第0行第0列
entry_username = tk.Entry(root ,width=35)
entry_username.grid(row=0, column=2, pady=20)  # 放置在第0行第1列

# 创建密码标签和输入框
label_password = tk.Label(root, text='密码：', width=10)
label_password.grid(row=1, column=1)  # 放置在第1行第0列
entry_password = tk.Entry(root, width=35, show='*')  # 设置密码输入框为显示*字符
entry_password.grid(row=1, column=2 ,pady=30)  # 放置在第1行第0列

# 创建登录按钮
btn_login = tk.Button(root, text='登录', width=15, command=login)
btn_login.grid(row=2, column=2)

lbl_result = tk.Label(root, text='')
lbl_result.grid(row=3, column=2)

# 启动主循环
root.mainloop()

# 创建新的窗口
main_window = tk.Tk()
main_window.title('主窗口')

main_window.geometry('900x600+500+100')

SQL = tk.Label(main_window, text='SQL语句:', width=10)
SQL.grid(row=0, column=1)
SQL_input = tk.Text(main_window ,width=50, height=10)
SQL_input.grid(row=0, column=2, padx=2, pady=20)

btn_submit = tk.Button(main_window, text='提交', width=10, command=submit)
btn_submit.grid(row=0, column=3)

res_label = tk.Label(main_window, text='返回结果:', width=10)
res_label.grid(row=1, column=1, padx=20)

res_show = tk.Text(main_window ,width=85, height=25)
res_show.grid(row=2, column=2, pady=20)

# 运行主循环
main_window.mainloop()

conn.commit()
conn.close()