# ==================================================================================
# IMPORT LIBRARIES
# ==================================================================================
# Objects
from matplotlib          import pyplot as plt
from pathlib             import Path
from typing              import Optional
from scipy.signal        import savgol_filter  # Para suavizado
from pyseestko.errors    import PlottingError
from pyseestko.utilities import pwl
from typing              import List

# Packages
import pandas as pd
import numpy  as np
# ==================================================================================
# MAIN FUNCTIONS CLASS
# ==================================================================================
def plotConfig(title:str, x = 19.2, y = 10.8, dpi = 100):
    fig = plt.figure(num=1, figsize=(x, y), dpi=dpi)
    ax = fig.add_subplot(1, 1, 1)
    ax.grid(True)
    ax.set_title(title)
    return fig, ax

def plotStatisticByReplicas(df:pd.DataFrame, statistic:str, title:str, ylabel:str,  x = 19.2, y = 10.8, dpi = 100):
    """
    This function plots the mean values of the replicas of the dataframe.
    It is supossed to use the getCummStatisticalDFs() functions to get the dataframes.
    So, df is supossed to have only a story as index, and the cummulative value of the drifts or spectra
    over the replicas as columns.
    As a example, the df could be like this:
    | Story | Replica 1 | Replica 2 | Replica 3 | ... | Replica 10 |
    |-------|-----------|-----------|-----------|-----|------------|
    | 1     | 0.001     | 0.002     | 0.003     | ... | 0.001      |
    | 2     | 0.002     | 0.003     | 0.004     | ... | 0.002      |
    | 3     | 0.003     | 0.004     | 0.005     | ... | 0.003      |
    | ...   | ...       | ...       | ...       | ... | ...        |
    | 10    | 0.010     | 0.011     | 0.012     | ... | 0.010      |
    
    Parameters
    ----------
    df : pd.DataFrame
        Dataframe with the mean values of the replicas.
    statistic : str
        Statistic to plot. The options are 'mean' and 'std'.
    title : str
        Title of the plot.  
    x : float, optional
        Width of the plot. The default is 19.2.
    y : float, optional
        Height of the plot. The default is 10.8.
    dpi : int, optional
        Dots per inch of the plot. The default is 100.
        
    Returns
    -------
    fig : plt.Figure
        Figure of the plot.
    ax : plt.Axes
        Axes of the plot.
    """
    # Check input
    if statistic not in ['mean', 'std']: raise ValueError(f'Statistic must be mean or std! Current: {statistic}')
    
    # Plot config
    fig, ax = plotConfig(title, x, y, dpi)
    
    # Plot the statistic value over the replicas for a given story
    for i in df.index:
        replicas  = [1,2,3,4,5,6,7,8,9,10]
        mean_vals = df.loc[i].values 
        plt.plot(replicas, mean_vals, label=f'Story {i}')
        
    # Set x values in [1,2,3,4,5,6,7,8,9,10]
    plt.xticks([1,2,3,4,5,6,7,8,9,10])
    plt.xlabel('Number of replicas')
    plt.ylabel(ylabel)
    
    # Write a vline segmented in red color in x=[3,5,10]
    plt.axvline(x=3, color ='black', linestyle=':')
    plt.axvline(x=5, color ='black', linestyle=':')
    plt.axvline(x=10, color='black', linestyle=':')
    
    # Set legend and grid
    plt.legend()
    plt.grid(True)
    plt.show()
    return fig, ax

#NOTE:DEPRECATED
def plotValidation(drifts_df_lst, spectra_df_lst, base_shear_df_lst):
    # DRIFTS
    mean_drift_x_df, mean_drift_y_df, mean_drift_df = getReplicaCummStatisticDriftDFs(drifts_df_lst, statistic='mean')
    std_drift_x_df, std_drift_y_df, std_drift_df    = getReplicaCummStatisticDriftDFs(drifts_df_lst, statistic='std')

    # Plot the mean drifts
    fig1, ax = plotStatisticByReplicas(df=mean_drift_x_df, statistic='mean', ylabel='Drift', title='Number of replicas vs Mean Drift X')
    fig2, ax = plotStatisticByReplicas(df=mean_drift_y_df, statistic='mean', ylabel='Drift', title='Number of replicas vs Mean Drift Y')
    fig1.savefig('C:/Users/oioya/OneDrive - miuandes.cl/Escritorio/Git-Updated/Thesis-Project-Simulation-Data-Analysis/DataBase-Outputs/Analysis Output/Number of replicas vs Mean Drift X.png')
    fig2.savefig('C:/Users/oioya/OneDrive - miuandes.cl/Escritorio/Git-Updated/Thesis-Project-Simulation-Data-Analysis/DataBase-Outputs/Analysis Output/Number of replicas vs Mean Drift Y.png')

    # Plot the std drifts
    fig1, ax = plotStatisticByReplicas(df=std_drift_x_df, statistic='std', ylabel='Acceleration Spectra[m/s/s]', title='Number of replicas vs Std Drift X')
    fig2, ax = plotStatisticByReplicas(df=std_drift_y_df, statistic='std', ylabel='Acceleration Spectra[m/s/s]', title='Number of replicas vs Std Drift Y')
    fig1.savefig('C:/Users/oioya/OneDrive - miuandes.cl/Escritorio/Git-Updated/Thesis-Project-Simulation-Data-Analysis/DataBase-Outputs/Analysis Output/Number of replicas vs Std Drift X.png')
    fig2.savefig('C:/Users/oioya/OneDrive - miuandes.cl/Escritorio/Git-Updated/Thesis-Project-Simulation-Data-Analysis/DataBase-Outputs/Analysis Output/Number of replicas vs Std Drift Y.png')

    # SPECTRUMSS
    mean_spectra_x_df, mean_spectra_y_df, mean_spectra_df = getCummStatisticSpectraDFs(spectra_df_lst, statistic='mean')
    std_spectra_x_df, std_spectra_y_df, std_spectra_df    = getCummStatisticSpectraDFs(spectra_df_lst, statistic='std')

    # Plot the mean spectra
    fig1, ax = plotStatisticByReplicas(df=mean_spectra_x_df, statistic='mean', ylabel='Drift', title='Number of replicas vs Mean Spectra X')
    fig2, ax = plotStatisticByReplicas(df=mean_spectra_y_df, statistic='mean', ylabel='Drift', title='Number of replicas vs Mean Spectra Y')
    fig1.savefig('C:/Users/oioya/OneDrive - miuandes.cl/Escritorio/Git-Updated/Thesis-Project-Simulation-Data-Analysis/DataBase-Outputs/Analysis Output/Number of replicas vs Mean Spectra X.png')
    fig2.savefig('C:/Users/oioya/OneDrive - miuandes.cl/Escritorio/Git-Updated/Thesis-Project-Simulation-Data-Analysis/DataBase-Outputs/Analysis Output/Number of replicas vs Mean Spectra Y.png')

    # Plot the std spectra
    fig1, ax = plotStatisticByReplicas(df=std_spectra_x_df, statistic='std', ylabel='Acceleration Spectra[m/s/s]',title='Number of replicas vs Std Spectra X')
    fig2, ax = plotStatisticByReplicas(df=std_spectra_y_df, statistic='std', ylabel='Acceleration Spectra[m/s/s]',title='Number of replicas vs Std Spectra Y')
    fig1.savefig('C:/Users/oioya/OneDrive - miuandes.cl/Escritorio/Git-Updated/Thesis-Project-Simulation-Data-Analysis/DataBase-Outputs/Analysis Output/Number of replicas vs Std Spectra X.png')
    fig2.savefig('C:/Users/oioya/OneDrive - miuandes.cl/Escritorio/Git-Updated/Thesis-Project-Simulation-Data-Analysis/DataBase-Outputs/Analysis Output/Number of replicas vs Std Spectra Y.png')

    # SHEAR BASE
    max_shear_x_df, max_shear_y_df, max_shear_df = getReplicaCummStatisticBaseShearDFs(base_shear_df_lst, statistic='mean')

    # Plot the mean base shear
    fig1, ax = plotStatisticByReplicas(df=max_shear_x_df, statistic='mean', ylabel='Base Shear [kN]', title='Number of replicas vs Mean Base Shear X')
    fig2, ax = plotStatisticByReplicas(df=max_shear_y_df, statistic='mean', ylabel='Base Shear [kN]', title='Number of replicas vs Mean Base Shear Y')
    fig1.savefig('C:/Users/oioya/OneDrive - miuandes.cl/Escritorio/Git-Updated/Thesis-Project-Simulation-Data-Analysis/DataBase-Outputs/Analysis Output/Number of replicas vs Mean Base Shear X')
    fig2.savefig('C:/Users/oioya/OneDrive - miuandes.cl/Escritorio/Git-Updated/Thesis-Project-Simulation-Data-Analysis/DataBase-Outputs/Analysis Output/Number of replicas vs Mean Base Shear Y')

    # Plot the std base shear
    fig1, ax = plotStatisticByReplicas(df=max_shear_x_df, statistic='std', ylabel='Base Shear [kN]', title='Number of replicas vs Std Base Shear X')
    fig2, ax = plotStatisticByReplicas(df=max_shear_y_df, statistic='std', ylabel='Base Shear [kN]', title='Number of replicas vs Std Base Shear Y')
    fig1.savefig('C:/Users/oioya/OneDrive - miuandes.cl/Escritorio/Git-Updated/Thesis-Project-Simulation-Data-Analysis/DataBase-Outputs/Analysis Output/Number of replicas vs Std Base Shear X')
    fig2.savefig('C:/Users/oioya/OneDrive - miuandes.cl/Escritorio/Git-Updated/Thesis-Project-Simulation-Data-Analysis/DataBase-Outputs/Analysis Output/Number of replicas vs Std Base Shear Y')



# ==================================================================================
# PLOTTING METRICS CLASS
# ==================================================================================
"""
This class is used to perform the seismic analysis of the structure.
It's used to analyse quiclky the structure and get the results of the analysis.
You use it in the main after the results are uploaded to the database.

Parameters
----------
sim_type : int
    Simulation type of the model.
stories : int
    Number of stories of the model.
nsubs : int
    Number of subterrains of the model.
magnitude : float
    Magnitude of the earthquake.
    An example of the magnitude is 6.7.
iteration : int
    Iteration of the simulation.
rupture : int
    Rupture type of the earthquake.
    An example of the rupture is 1 for 'bl'.
station : int
    Station of the earthquake.
    An example of the station is 0.
"""
class Plotting:

    # ==================================================================================
    # INIT PARAMS
    # ==================================================================================
    def __init__(
            self, sim_type:int,
            stories:int, nsubs:int,
            magnitude:float, iteration:int,
            rupture:int, station:int, show_plots:bool = True):
        sim_type_map = {
            1: 'FB',
            2: 'AB',
            3: 'DRM',
        }
        rup_type_map = {
            1: 'BL',
            2: 'NS',
            3: 'SN'
        }
        self.sim_type  = sim_type_map.get(sim_type)
        self.stories   = stories
        self.magnitude = magnitude
        self.iteration = iteration
        self.rup_type  = rup_type_map.get(rupture)
        self.station   = station
        self.nsubs     = nsubs
        self.save_path = Path('')
        if not show_plots:
            plt.switch_backend('agg')
        else:
            plt.switch_backend('module://matplotlib_inline.backend_inline')

        self.file_name       = f'{self.sim_type}_{self.magnitude}_{self.rup_type}{self.iteration}_s{self.station}'
        self.id              = f'{self.sim_type} |  {self.magnitude} | {self.rup_type}{self.iteration} | Station {self.station} | {self.stories} stories - {self.nsubs} subs'
        self.drift_title     = f'Drift per story plot | {self.id}'
        self.spectrums_title = f'Story PSa plot | {self.id}'
        self.base_shear_ss_title = f'Base Shear Plot | {self.id}'

    def plotConfig(self, title:str, x = 19.2, y = 10.8, dpi = 100, grid:bool=False):
        """
        This function is used to configure the plot eather for a single metric or for a 
        grid metrics plot. Bewware that if you turn grid in on the plot will be a 3x3 grid
        and the axes will be returned as a 3x3 numpy array. That implies that you will have 
        to add plots in a way of axes[0,0].plot() instead of ax.plot().
        """
        if grid:
            fig, axes = plt.subplots(3, 3, figsize=(x, y), dpi=dpi)
            for ax in axes.flatten():
                ax.grid(True)
            fig.suptitle(title)  # Título para la figura completa
            return fig, axes
        else:
            fig = plt.figure(num=1, figsize=(x, y), dpi=dpi)
            ax = fig.add_subplot(1, 1, 1)
            ax.grid(True)
            ax.set_title(title)
            return fig, ax

    def plotSave(self, fig, file_type = 'png'):
        self.save_path.mkdir(parents=True, exist_ok=True)
        full_save_path = self.save_path / f'{self.file_name}.{file_type}'
        fig.savefig(full_save_path, dpi=100)
        # Mostrar figura solo si el backend no es 'Agg'
        if plt.get_backend() != 'agg':
            plt.show()
        plt.close(fig)  # Asegúrate de cerrar la figura para liberar memoria


    # ==================================================================================
    # PLOT METRICS FUNCTIONS
    # ==================================================================================
    def plotModelDrift(self, max_corner_x: list, max_center_x: list, max_corner_y: list, max_center_y:list, xlim_inf:float = 0.0, xlim_sup:float = 0.008,
                       ax:plt.Axes=None, save_fig:bool=True):
        # Input params
        fig, ax = self.plotConfig(self.drift_title) if ax is None else (ax.figure, ax)
        ax.set_yticks(range(1, self.stories))
        ax.set_xlabel('Interstory Drift Ratio (Drift/Story Height)')
        ax.set_ylabel('Story')
        ax.set_xlim(xlim_inf, xlim_sup)

        # Plot corner drift
        y = [i for i in range(1, self.stories+1)]
        ax.set_yticks(y)
        ax.plot(max_corner_x, y, label='max_corner_x', color='red')
        ax.plot(max_center_x, y, label='max_center_x',linestyle='--', color='green')

        # Plot center drift
        ax.plot(max_corner_y, y, label='max_corner_y', color='blue')
        ax.plot(max_center_y, y, label='max_center_y',linestyle='--', color='orange')

        # Plot NCH433 limits
        ax.axvline(x=0.002, color='black', linestyle='--', linewidth=2, alpha = 0.9, label='NCh433 Limit - 5.9.2 = 0.002')

        ax.legend()
        if save_fig:
            self.plotSave(fig)
        return ax

    def plotLocalStoriesSpectrums(self,
                            accel_df:pd.DataFrame, story_nodes_df:pd.DataFrame, direction:str, stories_lst:list[int],
                            save_fig:bool=True, ax:plt.Axes=None, soften:bool=False):   #linestyle:str='--'
        # Init params
        self.file_name = f'{self.sim_type}_{self.magnitude}_{self.rup_type}{self.iteration}_s{self.station}_{direction.upper()}'
        colors         = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'orange', 'purple', 'brown']
        line_styles    = ['-', '--', '-.', ':']  # Diferentes estilos de línea
        texts          = []
        method         = self.sim_type
        
        # Check input and raise errors
        if direction not in ['x', 'y', 'z']: raise PlottingError(f'Dir must be x, y or z! Current: {direction}')
        if len(stories_lst) > len(colors):   raise PlottingError(f'Not enough colors for the number of stories! Current: {len(stories_lst)}\n Try adding less stories.')

        # Plot config
        fig, ax = self.plotConfig(self.spectrums_title) if ax is None else (ax.figure, ax)
        self.spectrums_title = f'{method} {self.spectrums_title}' if ax is None else self.spectrums_title
        #if ax is None: fig, ax = self.plotConfig(self.spectrums_title)
        #else:
        #    self.spectrums_title = f'{method} {self.spectrums_title}'
        #    fig = ax.figure
        ax.set_xlabel('T (s)')
        ax.set_ylabel(f'Acceleration in {direction.upper()} (m/s/s)')
        nu = 0.05
        T = np.linspace(0.003, 2, 1000)
        w  = 2 * np.pi / np.array(T)
        spa_lst = []
        
        # Make plot spectrum
        for i, story in enumerate(stories_lst):
            # Setup color and linestyle
            color = colors[i % len(colors)]
            line_style = line_styles[i % len(line_styles)]

            # Obtain the spectrum
            df = accel_df[story_nodes_df.loc[story].index].copy()
            df.loc[:,'Average'] = df.mean(axis=1)
            adir = df.xs(direction, level='Dir')['Average'][::16]
            Spe = [max(max(u_x), abs(min(u_x))) * wi**2 for wi in w for u_x, _ in [pwl(adir.values, wi, nu)]]
            Spe = np.array(Spe)
            spa_lst.append(Spe)

            # Soften the spectrum
            if soften and len(Spe) > 50: Spe = savgol_filter(Spe, 51, 3)

            # Write the maximum values of the spectrum
            max_value = max(Spe)
            max_index = np.argmax(Spe)
            annotation = ax.annotate(f'{max_value:.2f}', xy=(T[max_index], max_value), textcoords="offset points", xytext=(0,10), ha='center')
            texts.append(annotation)
            ax.plot(T, Spe, label=f'Story {story}', linestyle=line_style, color=color)

        # Compute df
        spa_df = pd.DataFrame({f'Story {story}': spa for story, spa in zip(stories_lst, spa_lst)}, index=T)
        
        #NOTE: This is just an implementation to correct the pos of the comments in plot
        #adjust_text(texts, arrowprops=dict(arrowstyle='->', color='blue'), ax=ax)
        ax.legend()
        if save_fig:
            self.plotSave(fig)
        return ax, spa_df

    def plotShearBaseOverTime(self, time:np.ndarray, time_shear_fma:list[float], Qmin:float, Qmax:float, dir_:str):
        # Input params
        if dir_ not in ['x','X','y','Y']: raise ValueError(f'dir must be x, y! Current: {dir}')
        self.file_name = f'{self.sim_type}_{self.magnitude}_{self.rup_type}{self.iteration}_s{self.station}_{dir_.upper()}'

        fig, ax  = self.plotConfig(self.base_shear_ss_title)
        ax.axhline(y=Qmax,  color='red', linestyle='--', linewidth=2, alpha = 0.9, label='NCh433 Qmax - 6.3.7.1')
        ax.axhline(y=-Qmax, color='red', linestyle='--', linewidth=2, alpha = 0.9, label=None)

        ax.set_xlabel('Time (s)')
        ax.set_ylabel(f'Shear in {dir_.upper()} direction (kN)')
        ax.plot(time, time_shear_fma, label='Method: F=ma')
        ax.legend()
        self.plotSave(fig)

