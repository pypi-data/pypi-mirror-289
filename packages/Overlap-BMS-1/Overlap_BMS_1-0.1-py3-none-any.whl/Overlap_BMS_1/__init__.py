

import pandas as pd
import numpy as np
from IPython.display import display
from datetime import datetime
from ipywidgets import interact, interact_manual, widgets



def Overlap_Summary(Id, Month, Sales, Tactic, Start_Month, End_Month):
    Required_Cube_Data = pd.DataFrame(Cube_Data[[Id, Month, Sales, Tactic]])
    Required_Cube_Data[Month] = pd.to_datetime(Required_Cube_Data[Month]).dt.strftime('%Y%m')
    Required_Cube_Data[Month] = Required_Cube_Data[Month].astype(int)
    
    Start_Month = datetime.strptime(Start_Month, '%Y-%m-%d')
    Start_Month = Start_Month.strftime('%Y%m')
    Start_Month = int(Start_Month)
    
    End_Month = datetime.strptime(End_Month, '%Y-%m-%d')
    End_Month = End_Month.strftime('%Y%m')
    End_Month = int(End_Month)
    
    Required_Cube_Data_1 = Required_Cube_Data[(Required_Cube_Data[Month] >= Start_Month) & (Required_Cube_Data[Month] <= End_Month)]
    
    Summary_Data = Required_Cube_Data_1.groupby([Id,Month]).sum().reset_index()
    Summary_Data['Overlap_Type'] = "Not_Defined"
    
    for row_num in range(len(Summary_Data.index)):
        if ((Summary_Data.at[row_num,Sales] + Summary_Data.at[row_num,Tactic]) == 0):
            Summary_Data.at[row_num,'Overlap_Type'] = "No Activity & No Sales"
        else:
            if ((Summary_Data.at[row_num,Sales] > 0) & (Summary_Data.at[row_num,Tactic] > 0)):
                Summary_Data.at[row_num,'Overlap_Type'] = "Activity & Sales"
            else:
                if ((Summary_Data.at[row_num,Sales] > 0) & (Summary_Data.at[row_num,Tactic] == 0)):
                    Summary_Data.at[row_num,'Overlap_Type'] = "No Activity & Sales"
                else:
                    Summary_Data.at[row_num,'Overlap_Type'] = "Activity & No Sales"
    
    Summary_Data_1 = Summary_Data.groupby([Id, 'Overlap_Type']).sum().reset_index()
    Summary_Data_1['HCP_Count'] = 1
    Summary_Data_2 = Summary_Data_1.drop([Id, Month], axis=1)
    Summary_Data_3 = Summary_Data_2.groupby(['Overlap_Type']).sum().reset_index()
    
    Summary_Data_4 = Summary_Data_3[['Overlap_Type', 'HCP_Count', Sales, Tactic]]
    
    display(Summary_Data_4)


def Load_Cube(Cube_Location, Id_Current, Month_Current, Sales_Current):
    Cube_Data = pd.read_csv(Cube_Location)
    
    
    interact_manual(
        Overlap_Summary,  
        Start_Month = widgets.Dropdown(options=['Select Month'] + list(Cube_Data[Month_Current].unique()), value="Select Month", description='Start Month: ',disabled=False),
        End_Month = widgets.Dropdown(options=['Select Month'] + list(Cube_Data[Month_Current].unique()), value="Select Month", description='End Month: ',disabled=False),
        Tactic = widgets.Dropdown(options=['Select Tactic'] + Cube_Data.columns.tolist(), value='Select Tactic', description='Tactic: ',disabled=False), 
        Month = Month_Current,
        Id = Id_Current,
        Sales = Sales_Current
    )

interact_manual(
    Load_Cube,
    Cube_Location = widgets.Text(value="", placeholder="Enter Cube Location",description="Cube Location: ",disabled=False),
    Id_Current = widgets.Text(value="", placeholder='ID Column Name', description='ID Column Name:',disabled=False),
    Month_Current = widgets.Text(value='', placeholder='Type here', description='Month Column Name',disabled=False),
    Sales_Current = widgets.Text(value='', placeholder='Type here', description='Sales Column Name',disabled=False),
)

