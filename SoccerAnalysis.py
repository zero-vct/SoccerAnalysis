import matplotlib.pyplot as plt
<<<<<<< Updated upstream
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
        
        # 创建图片保存按钮
        self.picture_save_button = tk.Button(self.button_frame, text="保存图片文件", command=self.save_picture,state=tk.DISABLED, width=button_width)
        self.picture_save_button.grid(row=0, column=1, padx=5)
        
        # 创建各个功能按钮
        self.ball_trace_button = tk.Button(self.button_frame, text="显示球的轨迹", command=self.show_ball_trace, state=tk.DISABLED, width=button_width)
        self.ball_trace_button.grid(row=0, column=2, padx=5)
        
        self.kick_line_button = tk.Button(self.button_frame, text="显示传球轨迹", command=self.show_kick_line, state=tk.DISABLED, width=button_width)
        self.kick_line_button.grid(row=0, column=3, padx=5)
        
        self.our_player_trace_button = tk.Button(self.button_frame, text="显示左边球员轨迹", command=self.show_our_player_trace, state=tk.DISABLED, width=button_width)
        self.our_player_trace_button.grid(row=0, column=4, padx=5)
        
        self.their_player_trace_button = tk.Button(self.button_frame, text="显示右边球员轨迹", command=self.show_their_player_trace, state=tk.DISABLED, width=button_width)
        self.their_player_trace_button.grid(row=0, column=5, padx=5)
        
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
        
        self.about_us_button = tk.Button(self.button_frame, text="关于", command=self.about_us,  width=button_width)
        self.about_us_button.grid(row=1, column=5, padx=5)
        
        # 创建一个画布用于显示图表
        self.canvas_frame = tk.Frame(root,width=1200,height=800)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        # 创建底部状态栏
        self.status_bar = tk.Label(root, text="当前文件：未打开", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # 绑定关闭窗口事件
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def load_file(self):
        self.filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if self.filepath:
            self.data = pd.read_csv(self.filepath)
            self.visualizer = SoccerAnalysis(self.data)
            messagebox.showinfo("文件已加载", f"已选择文件: {self.filepath}")
            self.enable_buttons()
        self.status_bar.config(text=f"当前文件：{self.filepath}")
    
    def enable_buttons(self):
        self.picture_save_button.config(state=tk.NORMAL)
        self.ball_trace_button.config(state=tk.NORMAL)
        self.kick_line_button.config(state=tk.NORMAL)
        self.our_player_trace_button.config(state=tk.NORMAL)
        self.their_player_trace_button.config(state=tk.NORMAL)
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
            print(f"图片已保存至 {file_path}")
    
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
        self.visualizer.ShowLeftHeatMap()
        self.display_plot()
        
    def show_right_player_heatmap(self):
        plt.close("all")
        self.visualizer.ShowRightHeatMap()
        self.display_plot()
        
    def show_ball_heatmap(self):
        plt.close("all") 
        self.visualizer.ShowBallHeatMap()
        self.display_plot()
    
    def show_our_player_trace(self):
        plt.close("all")
        unum1 = simpledialog.askinteger("输入", "请输入第一个左方球员编号 (1-11):", minvalue=1, maxvalue=11)
        unum2 = simpledialog.askinteger("输入", "请输入第二个左方球员编号 (1-11):", minvalue=1, maxvalue=11)
        if unum1 is not None:
            self.visualizer.ShowOurPlayerTrace(unum1, unum2)
            self.display_plot()
    
    def show_their_player_trace(self):
        plt.close("all")
        unum1 = simpledialog.askinteger("输入", "请输入第一个右方球员编号 (1-11):", minvalue=1, maxvalue=11)
        unum2 = simpledialog.askinteger("输入", "请输入第二个右方球员编号 (1-11):", minvalue=1, maxvalue=11)
        if unum1 is not None:
            self.visualizer.ShowTheirPlayerTrace(unum1, unum2)
            self.display_plot()
    
    def show_stamina_gap(self):
        plt.close("all")
        unum1 = simpledialog.askinteger("输入", "请输入左方球员编号 (1-11):", minvalue=1, maxvalue=11)
        unum2 = simpledialog.askinteger("输入", "请输入右方球员编号 (1-11):", minvalue=1, maxvalue=11)
        if unum1 is not None and unum2 is not None:
            self.visualizer.ShowStaminaGap(unum1, unum2)
            self.display_plot()
    
    def show_stamina_pie(self):
        plt.close("all")
        unum1 = simpledialog.askinteger("输入", "请输入左方球员编号 (1-11):", minvalue=1, maxvalue=11)
        unum2 = simpledialog.askinteger("输入", "请输入右方球员编号 (1-11):", minvalue=1, maxvalue=11)
        if unum1 is not None:
            self.visualizer.ShowStaminaPie(unum1, unum2)
            self.display_plot()
            
    def about_us(self):
        messagebox.showinfo("About","Author: Zhang \n Version: 1.0 \n Copyright © 2024")
=======
>>>>>>> Stashed changes

class SoccerAnalysis:
    def __init__(self, data):
        self.data = data
        self.left_team = self.data.iloc[1, :]['team_name']
        self.right_team = self.data.iloc[12, :]['team_name']
        self.left_data = self.data[self.data['team_name'] == self.left_team]
        self.right_data = self.data[self.data['team_name'] == self.right_team]

    def init(self):
        fig, ax = plt.subplots(1, 1, figsize=(12, 8))
        plt.xlim(-56.5, 56.5)
        plt.ylim(-38, 38)
        ax.set_xticks([-52.5, -36, -20, 0, 20, 36, 52.5])
        ax.set_yticks([34, 20, 7, 0, -7, -20, -34])
        ax.plot([-52.5, -52.5], [-34, 34], color="k", linestyle="-", linewidth=1)
        ax.plot([52.5, 52.5], [-34, 34], color="k", linewidth=1)
        ax.plot([52.5, -52.5], [-34, -34], color="k", linewidth=1)
        ax.plot([52.5, -52.5], [34, 34], color="k", linewidth=1)
        ax.plot([0, 0], [34, -34], color="k", linewidth=0.5)
        ax.plot([36, 52.5], [-20, -20], color="k", linewidth=0.5)
        ax.plot([36, 52.5], [20, 20], color="k", linewidth=0.5)
        ax.plot([36, 36], [-20, 20], color="k", linewidth=0.5)
        ax.plot([52.5, 52.5], [7, -7], color='k', linewidth=1.0)
        ax.plot([54.5, 52.5], [7, 7], color='k', linewidth=1.0)
        ax.plot([54.5, 52.5], [-7, -7], color='k', linewidth=1.0)
        ax.plot([54.5, 54.5], [7, -7], color='k', linewidth=1.0)
        ax.plot([-36, -52.5], [-20, -20], color="k", linewidth=0.5)
        ax.plot([-36, -52.5], [20, 20], color="k", linewidth=0.5)
        ax.plot([-36, -36], [-20, 20], color="k", linewidth=0.5)
        ax.plot([-52.5, -52.5], [7, -7], color='k', linewidth=1.0)
        ax.plot([-54.5, -52.5], [7, 7], color='k', linewidth=1.0)
        ax.plot([-54.5, -52.5], [-7, -7], color='k', linewidth=1.0)
        ax.plot([-54.5, -54.5], [7, -7], color='k', linewidth=1.0)
        plt.title(self.left_team + ' vs ' + self.right_team)
        return ax
    
    def init_stamina(self):
        fig, ax = plt.subplots(1, 1, figsize=(12, 8))
        plt.xlim(0, 6000)
        plt.ylim(0, 8000)
        ax.set_xticks([0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000])
        ax.set_yticks([0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000])
        plt.title(self.left_team + ' vs ' + self.right_team)
        return ax

    def ShowStaminaGap(self, unum1=0, unum2=0):
        ax = self.init_stamina()
        cycle = self.left_data[self.left_data['player_num']==unum1]['cycle']
        stamina = self.left_data[self.left_data['player_num']==unum1]['stamina']
        ax.plot(cycle, stamina, color="b", alpha=0.5, label='{}_{}'.format(self.left_team, str(unum1)))
        if unum2 != 0:
            cycle2 = self.right_data[self.right_data['player_num']==unum2]['cycle']
            stamina2 = self.right_data[self.right_data['player_num']==unum2]['stamina']
            ax.plot(cycle2, stamina2, color="r", alpha=0.5, label='{}_{}'.format(self.right_team, str(unum2)))
        plt.title('{}_{} vs {}_{} Stamina Gap'.format(self.left_team,str(unum1), self.right_team, str(unum2)))
        ax.legend(loc='best')
        
    def ShowBallTrace(self):
        ax = self.init()
        ball_x = self.data['ball_x']
        ball_y = self.data['ball_y']
        plt.title('Ball Trace')
        ax.plot(ball_x, ball_y, color="r", linewidth=0.5, linestyle="-", alpha=1)

    def ShowOurPlayerTrace(self, unum1=0, unum2=0):
        ax = self.init()
        player1_x = self.left_data[self.left_data['player_num'] == unum1]['player_x']
        player1_y = self.left_data[self.left_data['player_num'] == unum1]['player_y']
        ax.plot(player1_x, player1_y, color="r", linewidth=0.5, label='{}_{}'.format(self.left_team, str(unum1)))
        if unum2 != 0:
            player2_x = self.left_data[self.left_data['player_num'] == unum2]['player_x']
            player2_y = self.left_data[self.left_data['player_num'] == unum2]['player_y']
            ax.plot(player2_x, player2_y, color="b", linewidth=0.5, label='{}_{}'.format(self.left_team, str(unum2)))
        plt.title('{} Player {} And {} Trace'.format(self.left_team,str(unum1), str(unum2)))
        ax.legend(loc='upper left')

    def ShowTheirPlayerTrace(self, unum1=0, unum2=0):
        ax = self.init()
        player1_x = self.right_data[self.right_data['player_num'] == unum1]['player_x']
        player1_y = self.right_data[self.right_data['player_num'] == unum1]['player_y']
        ax.plot(player1_x, player1_y, color='r', linewidth=0.5, label='{}_{}'.format(self.right_team, str(unum1)))
        if unum2 != 0:
            player2_x = self.right_data[self.right_data['player_num'] == unum2]['player_x']
            player2_y = self.right_data[self.right_data['player_num'] == unum2]['player_y']
            ax.plot(player2_x, player2_y, color='b', linewidth=0.5, label='{}_{}'.format(self.right_team, str(unum2)))
        plt.title('{} Player {} And {} Trace'.format(self.right_team,str(unum1), str(unum2)))
        ax.legend(loc='upper left')

    def ShowKickLine(self):
        ax = self.init()
        left_kick = self.left_data[self.left_data['kick'].notnull()]
        right_kick = self.right_data[self.right_data['kick'].notnull()]
        ax.plot(left_kick['ball_x'], left_kick['ball_y'], marker='.', alpha=0.3, color='r', label=self.left_team)
        ax.plot(right_kick['ball_x'], right_kick['ball_y'], marker='.', alpha=0.3, color='b', label=self.right_team)
        plt.title('Kick Line')
        ax.legend(loc='upper left')
        
    def ShowStaminaPie(self, unum1=0, unum2=0):
        left_player_data = self.left_data[(self.left_data['player_num'] == unum1)]
        right_player_data = self.right_data[(self.right_data['player_num'] == unum2)]
        
        left_stamina = left_player_data['stamina']
        right_stamina = right_player_data['stamina']
        cycles = 6000

        stand = 4800
        left_below_4800 = (left_stamina < stand).sum() / cycles
        right_below_4800 = (right_stamina < stand).sum() / cycles

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 8))

        labels = ['Below {}'.format(stand), 'Above {}'.format(stand)]
        colors = ['#ff9999','#66b3ff']
        explode = (0.1, 0) 

        ax1.pie([left_below_4800, 1-left_below_4800], colors = colors, explode = explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
        ax1.set_title('{}_{} Stamina Below {}'.format(self.left_team, str(unum1), stand))

        ax2.pie([right_below_4800, 1-right_below_4800], colors = colors, explode = explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
        ax2.set_title('{}_{} Stamina Below {}'.format(self.right_team, str(unum2), stand))
        
        plt.suptitle('{}_{} vs {}_{} Stamina Pie'.format(self.left_team, str(unum1), self.right_team, str(unum2)))
        plt.tight_layout()
        
    def ShowLeftHeatMap(self):
        ax = self.init()
        left_player_x = self.left_data['player_x']
        left_player_y = self.left_data['player_y']

        ax.hexbin(left_player_x, left_player_y, gridsize=30, cmap='Reds')
        ax.set_title('{} Player Heatmap'.format(self.left_team))
        ax.set_xlabel('Player X Position')
        ax.set_ylabel('Player Y Position')
        plt.title('{} Player Heatmap'.format(self.left_team))
        
        # 添加颜色条
        cb = plt.colorbar(ax.collections[0], ax=ax)
        cb.set_label('Count')

    def ShowRightHeatMap(self):
        ax = self.init()
        right_player_x = self.right_data['player_x']
        right_player_y = self.right_data['player_y']

        ax.hexbin(right_player_x, right_player_y, gridsize=30, cmap='Reds')
        ax.set_title('{} Player Heatmap'.format(self.right_team))
        ax.set_xlabel('Player X Position')
        ax.set_ylabel('Player Y Position')
        plt.title('{} Player Heatmap'.format(self.right_team))
        
        cb = plt.colorbar(ax.collections[0], ax=ax)
        cb.set_label('Count')
        
    def ShowBallHeatMap(self):
        ax = self.init()
        ball_x = self.data['ball_x']
        ball_y = self.data['ball_y']

        ax.hexbin(ball_x, ball_y, gridsize=30, cmap='Reds')
        ax.set_title('Ball Heatmap')
        ax.set_xlabel('Ball X Position')
        ax.set_ylabel('Ball Y Position')
        plt.title('Ball Heatmap')
        
        cb = plt.colorbar(ax.collections[0], ax=ax)
        cb.set_label('Count')