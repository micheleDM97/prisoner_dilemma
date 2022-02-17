#Graph_functions
import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
from IPython.display import display
import it_pris_dil_func as pris_dil
import seaborn as sns


def graph_bar(media,unique,s):
    
    col = ['lime','red','cyan','saddlebrown','darkslategray','olive',
            'purple','navy','darkviolet','gold','darkgreen','darkorange',
            'royalblue','hotpink']
    col_1=[col[val] for val in unique]
    
    #col=[i for i in sns.color_palette("flare",n_colors=len(s_unique)) ] 
    
    def autolabel(rects):
        for idx,rect in enumerate(plot_bar):
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2.,
                    0.5*height, media[idx], ha='center',
                    va='center', rotation=0, fontdict=font)
    
    fig, ax = plt.subplots(figsize=(15.5,7))
    font = {'family': 'monospace',
            'color':  'black',
            'weight': 'medium'}
    s_unique = [s[val] for val in unique]   
    plot_bar=plt.bar(s_unique,media,color=col_1,width=0.8)
    
    return autolabel(plot_bar)

def graph_avarege(h,s_colors,val_ma,s,iterations):
    
    val_ma_graph = np.copy(val_ma)
    val_ma_graph[val_ma_graph == 0] = np.nan
        
    #fig, (ax1,ax2) = plt.subplots(nrows=1,ncols=2,figsize=(15,8.5))
    fig, ax2 = plt.subplots(nrows=1,ncols=1,figsize=(15,8.5))
    
    
    if np.shape(h) == (len(h.T),): #caso senza mutazione
        for i in range(len(s)):
            ax2.plot(0,val_ma_graph.T[i,0],'o',color='green')
            ax2.plot(np.arange(iterations)[-1],val_ma_graph.T[i,-1],'x',color='red',markeredgewidth=2)
            for j in range(len(val_ma_graph.T[i])):
                if np.isnan(val_ma_graph.T[i,j])==True: 
                    ax2.plot(np.arange(iterations)[j-1],val_ma_graph.T[i,j-1],'x',color='red',markeredgewidth=2)
            #ax1.plot(np.arange(iterations),n_ma3.T[i],color=s_colors[i])
            ax2.plot(np.arange(iterations),val_ma_graph.T[i],label=s[i],color=s_colors[i])
        ax2.set_title('Average points without mutation strategies',fontsize=14)
    else:#caso mutazioni
        s_mut = s[14:]
        for i in range(len(s_mut)):
            check_s_1 = s_mut[i][:-2]
            check_s_2 = s_mut[i][:-3]
            for j in range(len(s)):
                if s[j] == check_s_1:
                    shade = [col for col in sns.light_palette(s_colors[j],n_colors=100,reverse=True)]
                    s_2 = [l for l in s_mut[i]]
                    s_colors.append(shade[int(s_2[-1])])
            for j in range(len(s)):
                if s[j] == check_s_2:
                    shade = [col for col in sns.light_palette(s_colors[j],n_colors=100,reverse=True)]
                    s_2 = [l for l in s_mut[i]]
                    s_colors.append(shade[int(s_2[-2] + s_2[-1])])
        for i in range(len(val_ma.T)):
            k=np.where(val_ma.T[i]==0)[0]
            if len(k)>0:
                if k.max()==iterations-1: #caso morti prima
                    position_1=[k[y]-1 for y in range(1,len(k)) if k[y-1]+1!=k[y]]
                    if k.min()!=0:
                        ax2.plot(np.arange(iterations)[k.min()-1],
                                 val_ma_graph.T[i,k.min()-1],'x',color='red',
                                 markeredgewidth=2)#caso nati all'inizio 
                    if len(position_1)>0:
                        ax2.plot(np.arange(iterations)[position_1],
                                 val_ma_graph.T[i,position_1],
                                 'x',color='red',markeredgewidth=2) #caso nasce dopo   
                if k.min()==0: #caso nati dopo
                    position_2=[y+1 for y in range(len(k)-1) if k[y]+1!=k[y+1]] 
                    position_3=[w+1 for w in range(len(k)) if k.max()!=iterations-1]
                    if len(position_2)>0:
                        ax2.plot(position_2,
                                 val_ma_graph.T[i,position_2],'o',color='green')#caso morti 
                    if len(position_3)>0:
                        ax2.plot(max(position_3),
                                 val_ma_graph.T[i,max(position_3)],
                                 'o',color='green')#caso non morti

            ax2.plot(0,val_ma_graph.T[i,0],'o',color='green')    #caso nati all'inizio non morti 
            ax2.plot(np.arange(iterations)[-1],
                     val_ma_graph.T[i,-1],'x',color='red',markeredgewidth=2)#caso nati all'inizio non morti
            #ax1.plot(np.arange(iterations),n_ma4.T[i],color=s_colors_1[i])
            ax2.plot(np.arange(iterations),
                     val_ma_graph.T[i],label=s[i],color=s_colors[i])
        ax2.set_title('Average points mutation strategies',fontsize=14)




    #ax1.set_title('Population',fontsize=14) 
    #ax1.set_xlabel('Iteration')
    #ax1.set_ylabel('Population')
    
    ax2.set_xlabel('Iteration')
    ax2.set_ylabel('Average points')
    fig.legend(loc='center right')
    plt.show()
    return
    
def graph_population(n_ma,iterations,s,s_colors):
    fig,ax=plt.subplots(figsize=(15,8.5))
    ax.stackplot(np.arange(iterations),n_ma.T,labels=s,alpha=0.9,colors=s_colors);
    fig.legend(loc='center right')
    plt.xlim(range(iterations)[0],range(iterations)[-1])
    ax.set_title('Population') 
    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(.3)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(.3)
    plt.show()
    return
