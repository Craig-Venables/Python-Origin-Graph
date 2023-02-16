#this is a file for adding into origin 
#git clone https://github.com/chrislauyc/PyWrapOrigin.git

import PyWrapOrigin.PyWrapOrigin as pw
import numpy as np
import pandas as pd

pwo = pw.PyWrapOrigin()
pwo.connect()


x1 = np.linspace(0,2)
y1 = np.exp(x1)
y2 = np.exp(2*x1)

data = {
    'x1':x1,
    'y1':y1,
    'y2':y2
}
df = pd.DataFrame(data)

ws = pwo.new_WorkSheet('sheet1','book0')
ws.from_df(df)

gp = pwo.new_GraphPage('Graph1')