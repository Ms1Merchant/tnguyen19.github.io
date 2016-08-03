import matplotlib.pyplot as plt
import os.path

#Naming the current directory
directory = os.path.dirname(os.path.abspath(__file__))  

#Initializing empty lists for x and y values
years1=[]
landline_yes1=[]
cell_yes1=[]
landline_frequency=[]
cell_frequency=[]


#Open the date file for that year
filename = os.path.join(directory, 'CELLPHONE_LANDLINE.csv')
datafile = open(filename,'r') # 'r' means 'read only'
#For each line in the file
for line in datafile:
    #Split the line into the six separate pieces of info
    YEAR, LANDLINE_YES, LANDLINE_NO, CELL_YES, CELL_NO, FREQUENCY = line.split(',')
    years1.append(YEAR)
    landline_yes1.append(LANDLINE_YES)
    cell_yes1.append(CELL_YES)
    landline_frequency.append(float(LANDLINE_YES)/float(FREQUENCY)*100)
    cell_frequency.append(float(CELL_YES)/float(FREQUENCY)*100)
datafile.close()
    
fig, ax = plt.subplots(1,2)
ax[0].plot(years1, landline_yes1,'#FF0000')
ax[0].plot(years1, landline_yes1,'ro')
ax[0].plot(years1, cell_yes1,'#00FF00')
ax[0].plot(years1, cell_yes1,'gs')
ax[0].minorticks_on() 

ax[0].set_title('Landline(RED) vs Cellphone(GREEN) RAW DATA (2004-2015)')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of U.S. Families')

ax[1].plot(years1, landline_frequency, '#FF0000')
ax[1].plot(years1, landline_frequency, 'ro')
ax[1].plot(years1, cell_frequency, '#00FF00')
ax[1].plot(years1, cell_frequency, 'gs')
ax[1].set_ylim(0,100)

ax[1].minorticks_on() 

ax[1].set_title('Decline of Landline Phones & Rise of Cellphones')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Frequency (%)')

fig.show()
