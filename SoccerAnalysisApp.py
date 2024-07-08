import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import pandas as pd
from SoccerAnalysis import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    
class SoccerAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Soccer Ananlysis")
        
        self.filepath = None
        self.data = None
        self.visualizer = None
        
        # 创建一个顶部的框架来放置按钮
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)
        
        # 定义按钮宽度
        button_width = 20
        
        # 创建文件选择按钮
        self.file_button = tk.Button(self.button_frame, text="选择 CSV 文件", command=self.load_file, width=button_width)
        self.file_button.grid(row=0, column=0, padx=5)
        
        # 创建各个功能按钮
        self.ball_trace_button = tk.Button(self.button_frame, text="显示球的轨迹", command=self.show_ball_trace, state=tk.DISABLED, width=button_width)
        self.ball_trace_button.grid(row=0, column=1, padx=5)
        
        self.kick_line_button = tk.Button(self.button_frame, text="显示传球轨迹", command=self.show_kick_line, state=tk.DISABLED, width=button_width)
        self.kick_line_button.grid(row=0, column=2, padx=5)
        
        self.our_player_trace_button = tk.Button(self.button_frame, text="显示左边球员轨迹", command=self.show_our_player_trace, state=tk.DISABLED, width=button_width)
        self.our_player_trace_button.grid(row=0, column=3, padx=5)
        
        self.their_player_trace_button = tk.Button(self.button_frame, text="显示右边球员轨迹", command=self.show_their_player_trace, state=tk.DISABLED, width=button_width)
        self.their_player_trace_button.grid(row=0, column=4, padx=5)
        
        self.both_player_trace_button = tk.Button(self.button_frame, text="显示双方球员轨迹", command=self.show_both_player_trace, state=tk.DISABLED, width=button_width)
        self.both_player_trace_button.grid(row=0, column=5, padx=5)
        
        self.stamina_gap_button = tk.Button(self.button_frame, text="显示双方球员体力变化", command=self.show_stamina_gap, state=tk.DISABLED, width=button_width)
        self.stamina_gap_button.grid(row=1, column=0, padx=5)
        
        self.stamina_pie_button = tk.Button(self.button_frame, text="显示双方球员体力占比", command=self.show_stamina_pie, state=tk.DISABLED, width=button_width)
        self.stamina_pie_button.grid(row=1, column=1, padx=5)
        
        self.left_player_heatmap_button = tk.Button(self.button_frame, text="显示左边球员球场热力图", command=self.show_left_player_heatmap, state=tk.DISABLED, width=button_width)
        self.left_player_heatmap_button.grid(row=1, column=2, padx=5)
        
        self.right_player_heatmap_button = tk.Button(self.button_frame, text="显示右边球员球场热力图", command=self.show_right_player_heatmap, state=tk.DISABLED, width=button_width)
        self.right_player_heatmap_button.grid(row=1, column=3, padx=5)
        
        self.ball_heatmap_button = tk.Button(self.button_frame, text="显示球的热力图", command=self.show_ball_heatmap, state=tk.DISABLED, width=button_width)
        self.ball_heatmap_button.grid(row=1, column=4, padx=5)
        
        # 创建图片保存按钮
        self.picture_save_button = tk.Button(self.button_frame, text="保存图片文件", command=self.save_picture,state=tk.DISABLED, width=button_width)
        self.picture_save_button.grid(row=1, column=5, padx=5)
        
        # self.about_us_button = tk.Button(self.button_frame, text="关于", command=self.about_us,  width=button_width)
        # self.about_us_button.grid(row=1, column=5, padx=5)
        
        # 创建一个画布用于显示图表
        self.canvas_frame = tk.Frame(root,width=1200,height=800)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        # 创建底部状态栏
        self.status_bar = tk.Label(root, text="当前文件：未打开", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # 绑定关闭窗口事件
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def load_file(self):
        # 清空画布内容
        for widget in self.canvas_frame.winfo_children():
            widget.pack_forget()
        self.filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if self.filepath:
            self.data = pd.read_csv(self.filepath)
            self.visualizer = SoccerAnalysis(self.data)
            messagebox.showinfo("文件加载成功", f"已选择文件: {self.filepath}")
            self.enable_buttons()
            self.status_bar.config(text=f"当前文件：{self.filepath}")
        else:
            messagebox.showwarning("文件加载失败", "未选择文件")
            self.status_bar.config(text=f"当前文件：未打开")
        
    
    def enable_buttons(self):
        self.picture_save_button.config(state=tk.NORMAL)
        self.ball_trace_button.config(state=tk.NORMAL)
        self.kick_line_button.config(state=tk.NORMAL)
        self.our_player_trace_button.config(state=tk.NORMAL)
        self.their_player_trace_button.config(state=tk.NORMAL)
        self.both_player_trace_button.config(state=tk.NORMAL)
        self.stamina_gap_button.config(state=tk.NORMAL)
        self.stamina_pie_button.config(state=tk.NORMAL)
        self.left_player_heatmap_button.config(state=tk.NORMAL)
        self.right_player_heatmap_button.config(state=tk.NORMAL)
        self.ball_heatmap_button.config(state=tk.NORMAL)
        
    def display_plot(self):
        # 清空画布内容
        for widget in self.canvas_frame.winfo_children():
            widget.pack_forget()

        fig = plt.gcf()
        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
    def on_closing(self):
        plt.close("all")  # 关闭之前打开的图形窗口，否则容易出现内存警告
        self.root.destroy()
        
    def save_picture(self):
        fig = plt.gcf()
        ax = fig.gca()
        # 设置整个图片的标题
        suptitle = fig._suptitle.get_text() if fig._suptitle else ""
        title = suptitle if suptitle else (ax.get_title() if ax.get_title() else "plot")
        file_path = filedialog.asksaveasfilename(defaultextension=".png", initialfile=title, filetypes=[("PNG files", "*.png"), ("All files", "*.*")])

        if file_path:
            fig.savefig(file_path)
            messagebox.showinfo("保存成功",f"图片已保存至 {file_path}")
        else:
            messagebox.showwarning("保存失败", "未选择保存路径")
    
    def show_ball_trace(self):
        plt.close("all") 
        self.visualizer.ShowBallTrace()
        self.display_plot()
    
    def show_kick_line(self):
        plt.close("all")
        self.visualizer.ShowKickLine()
        self.display_plot()
    
    def show_left_player_heatmap(self):
        plt.close("all")
        unum = simpledialog.askinteger("输入", "请输入左方球员编号 (1-11):", minvalue=1, maxvalue=11)
        if unum is not None:
            self.visualizer.ShowLeftHeatMap(unum)
            self.display_plot()
        
    def show_right_player_heatmap(self):
        plt.close("all")
        unum = simpledialog.askinteger("输入", "请输入右方球员编号 (1-11):", minvalue=1, maxvalue=11)
        if unum is not None:
            self.visualizer.ShowRightHeatMap(unum)
            self.display_plot()
        
    def show_ball_heatmap(self):
        plt.close("all") 
        self.visualizer.ShowBallHeatMap()
        self.display_plot()
    
    def show_our_player_trace(self):
        plt.close("all")
        unum1 = simpledialog.askinteger("输入", "请输入第一个左方球员编号 (1-11):", minvalue=1, maxvalue=11)
        unum2 = simpledialog.askinteger("输入", "请输入第二个左方球员编号 (1-11):", minvalue=1, maxvalue=11)
        if unum1 or unum2 is None:
            messagebox.showwarning("输入错误", "未输入足够的球员编号")
        else:
            self.visualizer.ShowOurPlayerTrace(unum1, unum2)
            self.display_plot()
    
    def show_their_player_trace(self):
        plt.close("all")
        unum1 = simpledialog.askinteger("输入", "请输入第一个右方球员编号 (1-11):", minvalue=1, maxvalue=11)
        unum2 = simpledialog.askinteger("输入", "请输入第二个右方球员编号 (1-11):", minvalue=1, maxvalue=11)
        if unum1 or unum2 is None:
            messagebox.showwarning("输入错误", "未输入足够的球员编号")
        else:
            self.visualizer.ShowTheirPlayerTrace(unum1, unum2)
            self.display_plot()
    
    def show_both_player_trace(self):
        plt.close("all")
        unum1 = simpledialog.askinteger("输入", "请输入左方球员编号 (1-11):", minvalue=1, maxvalue=11)
        unum2 = simpledialog.askinteger("输入", "请输入右方球员编号 (1-11):", minvalue=1, maxvalue=11)
        if unum1 or unum2 is None:
            messagebox.showwarning("输入错误", "未输入足够的球员编号")
        else:
            self.visualizer.ShowBothPlayerTrace(unum1, unum2)
            self.display_plot()
    
    def show_stamina_gap(self):
        plt.close("all")
        unum1 = simpledialog.askinteger("输入", "请输入左方球员编号 (1-11):", minvalue=1, maxvalue=11)
        unum2 = simpledialog.askinteger("输入", "请输入右方球员编号 (1-11):", minvalue=1, maxvalue=11)
        if unum1 or unum2 is None:
            messagebox.showwarning("输入错误", "未输入足够的球员编号")
        else:
            self.visualizer.ShowStaminaGap(unum1, unum2)
            self.display_plot()
    
    def show_stamina_pie(self):
        plt.close("all")
        unum1 = simpledialog.askinteger("输入", "请输入左方球员编号 (1-11):", minvalue=1, maxvalue=11)
        unum2 = simpledialog.askinteger("输入", "请输入右方球员编号 (1-11):", minvalue=1, maxvalue=11)
        if unum1 or unum2 is None:
            messagebox.showwarning("输入错误", "未输入足够的球员编号")
        else:
            self.visualizer.ShowStaminaPie(unum1, unum2)
            self.display_plot()
            
    def about_us(self):
        messagebox.showinfo("About","Author: Zhang \n Version: 1.0 \n Copyright © 2024")
    
if __name__ == '__main__':
    root = tk.Tk()
    app = SoccerAnalysisApp(root)
    root.mainloop()
