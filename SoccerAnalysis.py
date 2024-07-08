import matplotlib.pyplot as plt


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
        
    def ShowLeftHeatMap(self,unum=0):
        ax = self.init()
        right_player_x = self.right_data[self.right_data['player_num'] == unum]['player_x']
        right_player_y = self.right_data[self.right_data['player_num'] == unum]['player_y']
        extent = [-56.5, 56.5, -38, 38]
        ax.hexbin(right_player_x, right_player_y, gridsize=30, cmap='Reds',extent=extent, mincnt=1)
        ax.set_xlabel('Player X Position')
        ax.set_ylabel('Player Y Position')
        plt.title('{}_{} Player Heatmap'.format(self.left_team, str(unum)))
        
        # 添加颜色条
        cb = plt.colorbar(ax.collections[0], ax=ax)
        cb.set_label('Count')

    def ShowRightHeatMap(self,unum=0):
        ax = self.init()
        right_player_x = self.right_data[self.right_data['player_num'] == unum]['player_x']
        right_player_y = self.right_data[self.right_data['player_num'] == unum]['player_y']
        extent = [-56.5, 56.5, -38, 38]
        ax.hexbin(right_player_x, right_player_y, gridsize=30, cmap='Reds',extent=extent, mincnt=1)
        ax.set_xlabel('Player X Position')
        ax.set_ylabel('Player Y Position')
        plt.title('{}_{} Player Heatmap'.format(self.right_team, str(unum)))
        
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