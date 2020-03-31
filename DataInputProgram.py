### TASK 1: Data Processing
import csv

def readFileCSV(path):
  rows = []
  with open(path) as csvfile:
    file_reader = csv.reader(csvfile)
    for row in file_reader:
      rows.append(list(row))
  return rows

def filter(f, seq):
  res = []
  for e in seq:
    if f(e):
      res.append(e)
  return res
def map(f, seq):
  res = []
  for e in seq:
    res.append(f(e))
    
  return res


### Task 1A: Summary
def filtyear(e):
      if(e[2]!= str(yearfilter)):
        return False
      else:
        return True
  
def filtyear2(e):
      if(e[2]!= yearfilter):
        return False
      else:
        return True
      
def mapcol(e):
 return e[colnum]
  
def summary(filename, year, c_name):
 
  arr=readFileCSV(filename)
  
  global filter_year
  filter_year = year
  filteredarr = filter(filtyear,arr)
  
  global colnum
  for x in range(len(arr[0])):
    if(arr[0][x]==c_name):
      colnum=x
  arr_after_mapping = map(mapcol,array_after_filtering)
 
  empty_counter = 0
 
  for x in range (len(arr_after_mapping)):
    if(arr_after_mapping[x]=='0'):
       arr_after_mapping[x]='0.0'
    elif(arr_after_mapping[x]==''):   
       empty_counter=empty_counter+1

       
  num_data=len(arr_after_mapping)-empty_counter
  array_with_float_val =[]
  for item in arr_after_mapping:
      try:
       array_with_float_val.append(float(item))
      except:
          continue
  try:         
      maxdata = float("{0:.2f}".format(max(array_with_float_val)))
      mindata = float("{0:.2f}".format(min(array_with_float_val)))
     
  except:
    maxdata = None
    mindata = None
  sum_data = float("{0:.2f}".format(sum(array_with_float_val)))
  if(sum_data == 0.0):
       sum_data = int(sum_data)
  return[num_data,maxdata,mindata,sum_data]
  
print(summary('Weather.csv', 2018, 'PRCP'))
print(summary('Weather.csv', 2019, 'TMIN'))
print(summary('Weather.csv', 2019, 'TMAX'))
print(summary('Weather.csv', 2020, 'TAVG'))


  
### Task 1B: Classification
def classify(filename, year):
  arrays=readFileCSV(filename)
  for x in range (len(arrays)):
    try:
     
      arrays[x][1] = int(arrays[x][1])
    except ValueError:
      arrays[x][1] = arrays[x][1]

  global filter_year
  filter_year = year
  array_after_filtering = filter(filtyear,arrays)
  global column_number
  column_number= 4
  arr_after_mapping_tavg = map(mapcol,array_after_filtering)
  column_number=1
  arr_after_mapping_month = map(mapcol,array_after_filtering)
  monthly_dailyavg ={}
  months = []
  for x in arr_after_mapping_month: 
        if x not in months: 
            months.append(x)
  montharr = []
  for x in reversed(range(len(arr_after_mapping_month)-1)):
    
    if(arr_after_mapping_month[x]==arr_after_mapping_month[x-1]):
            montharr.append(arr_after_mapping_tavg[x])
            for z in range(len(months)):
              if(months[z]==arr_after_mapping_month[x]):
                monthly_dailyavg[months[z]]=montharr
    else:
      montharr.append(arr_after_mapping_tavg[x])
      montharr = []
  for key in monthly_dailyavg.keys():
    val = monthly_dailyavg[key]
    float_monthly_dailyavg =[]
    for item in val:
      float_monthly_dailyavg.append(float(item))
    avg =  float("{0:.2f}".format(sum(float_monthly_dailyavg)))/(len(val))
    if(average_float<25):
      monthly_dailyavg[key] = 'COOL'
    elif(average_float>=25 and average_float<28):
      monthly_dailyavg[key] = 'WARM'
    elif(average_float>=28):
      monthly_dailyavg[key] = 'HOT'
  return monthly_dailyavg
print(classify('Weather.csv', 2017))
print(classify('Weather.csv', 2018))
print(classify('Weather.csv', 2019))
print(classify('Weather.csv', 2020))

def median(arrays):
  arrays.sort()
  if((len(arrays))%2==1):
      return arrays[int((len(arrays)/2))]
  if((len(arrays))%2==0):
    return arrays[int((len(arrays)/2))]

### Task 1C: Grouping
def grouping(filename):
 
  arrays=readFileCSV(filename)
  temporary_array = []
  for y in range( len(arrays[0])):
         temporary_array.append(arrays[0][y])

      
  del(arrays[0])
  arrays= sorted(arrays, key = lambda x: (x[2],x[1]))
  
  for z in range(len(arrays)):
    if(arrays[z][2]==''):
     arrays[z] = [x for x in arrays[z]if x != '']

  arrays =  [x for x in arrays if x != []]
 
 
  for x in range (len(arrays)):
      arrays[x][4] = float(arrays[x][4])
      arrays[x][2] = int(arrays[x][2])
      arrays[x][1] = int(arrays[x][1])
  


  arrays.insert(0,temporary_array)
  
  years_avg={}
  years = []
  global column_number
  global filter_year
  column_number=2
  arr_after_mapping_year = map(mapcol,arrays)
  for x in arr_after_mapping_year: 
        if x not in years:
          try:
            int(x)
            years.append(x)
          except ValueError:
             continue
     
  for x in  range(len(arrays)-1):
    for z in years:
      if(z == arrays[x][2]):
       filter_year = z
       array_after_filtering = filter(filtyear2,arrays)
       column_number=4 
       arr_after_mapping = map(mapcol,array_after_filtering)
       years_avg[z] = arr_after_mapping
  years_avg_median ={}
  
  for key in years_avg.keys():
    values = years_avg[key]
    column_number = 1
    filter_year = key
    array_after_filtering = filter(filtyear2,arrays)
    arr_after_mapping = map(mapcol,array_after_filtering)
    months = []
    for x in arr_after_mapping: 
          if x not in months: 
              months.append(x)
    months.append(0) 
    
    arr_y_m_avg ={}
    monthly_avg = []
    months.sort()

    for y in range(len(months)-1):
     for x in range(len(arr_after_mapping)):
      if(arr_after_mapping[x]==months[y]):
              monthly_avg.append(values[x])
              for z in range(len(months)):
                if(months[z]==arr_after_mapping[x]):
                  arr_y_m_avg[months[z]]=monthly_avg
      else:
       
        monthly_avg = []    
         
   
    for x in arr_y_m_avg.keys():
     
      values = arr_y_m_avg[x]
   
      arr_y_m_avg[x]=median(values)
      
    arr_y_avg_med[key] = arr_y_m_avg




  allmonths=[]
  final_months_array = []
  final_array={}
  for years in arr_y_avg_med.keys():
      values = arr_y_avg_med[years]
      for months in values.keys():
        allmonths.append(months)
        
  
  for x in allmonths: 
          if x not in final_months_array: 
              final_months_array.append(x)
  for x in reversed(final_months_array):
    final_array[x]={}


  inversearr = []   
  for x in range(len(final_months_array)):
    for years in arr_y_avg_med.keys():
      inversearr.append(years)

  inversed_array = inversed_array[::-1]  

  for x in range(len(final_months_array)):
    yearsmonths={}
    for years in arr_y_avg_med.keys():
     for year_inversed in inversed_array:
      values = arr_y_avg_med[year_inversed]       
      for months in values.keys():

           if(final_months_array[x] == months):
               yearsmonths[year_inversed]= values[final_months_array[x]]
               final_array[months]=yearsmonths

  return final_array
  

print(grouping('Weather.csv'))

 



### Task 2: Grayscale
from imageio import imread
import numpy as np
import matplotlib.pyplot as plt

def read_image(path):
  img = imread(path)
  res = []
  for row in img:
    ln = []
    for R,G,B,*_ in row:
      ln.append([R,G,B])
    res.append(ln)
  return res

def show_image(image):
  img = np.array(image)
  plt.figure(1)
  plt.imshow(img)
  plt.show()


### Task 2A: Median Color
def convert_bw_median(path):


 arrays = read_image(path)

 for x in range (len(arrays)):
     for y in range (len(arrays[x])):
         for z in range (len(arrays[x][y])):
             arrays[x][y][z]=arrays[x][y][1]
                  
 return arrays


show_image(convert_bw_median('cat.jpg'))
show_image(convert_bw_median('dog.jpg'))


### Task 2B: Gamma Value
def convert_bw_gamma(path):
    arrays = read_image(path)
    for x in range (len(arrays)):
     for y in range (len(arrays[x])):
         
    
             arrays[x][y][0]= (arrays[x][y][0]/255)
             arrays[x][y][1]= (arrays[x][y][1]/255)
             arrays[x][y][2]= (arrays[x][y][2]/255)

             if( arrays[x][y][0]<=0.04045):
                  arrays[x][y][0]= arrays[x][y][0]/12.92
             else:
                  arrays[x][y][0]=((arrays[x][y][0]+0.055)/1.055)**2.4


             if( arrays[x][y][1]<=0.04045):
                  arrays[x][y][1]= arrays[x][y][1]/12.92
             else:
                  arrays[x][y][1]=((arrays[x][y][1]+0.055)/1.055)**2.4
                  
             if( arrays[x][y][2]<=0.04045):
                  arrays[x][y][2]= arrays[x][y][2]/12.92
             else:
                  arrays[x][y][2]=((arrays[x][y][2]+0.055)/1.055)**2.4

             LY = (0.2126*arrays[x][y][0])+ (0.7152*arrays[x][y][1])+ (0.0722*arrays[x][y][2])

             if(LY <= 0.0031308):
                  arrays[x][y][0]=LY*12.92
                  arrays[x][y][1]=LY*12.92
                  arrays[x][y][2]=LY*12.92
             else:
                  arrays[x][y][0]=1.055*(LY**(1/2.4))-0.055
                  arrays[x][y][1]=1.055*(LY**(1/2.4))-0.055
                  arrays[x][y][2]=1.055*(LY**(1/2.4))-0.055

             arrays[x][y][0]= (arrays[x][y][0]*255)
             arrays[x][y][1]= (arrays[x][y][1]*255)
             arrays[x][y][2]= (arrays[x][y][2]*255)

             arrays[x][y][0] = int(round(arrays[x][y][0],0))
             arrays[x][y][1] = int(round(arrays[x][y][1],0))
             arrays[x][y][2] = int(round(arrays[x][y][2],0))
             
             
             
    return arrays
              
     
show_image(convert_bw_gamma('garfield.jpg'))





### Task 3: Maze
def m_print(maze):
  for row in maze:
    for e in row:
      print(e, end='')
    print()


### Task 2A: Median Color
def count_areas(diag_maze_array):

  counter = 0
  if(len(diag_maze_array) < 1 or diag_maze_array== None ):
      return counter

  max_x =  len(diag_maze_array)-1
  max_y=   len(diag_maze_array[0])-1
  
  
          
  if(diag_maze_array[max_x][max_y]=="/"):#corner
              counter=counter+1      
     
  if(diag_maze_array[max_x][0] == "\\"  ):#corner
          counter=counter+1
 
  if(diag_maze_array[0][0] == "/"):#corner
         counter=counter+1
         
  if(diag_maze_array[0][max_y] == "\\"):#corner
         counter=counter+1
         
  for y in range(max_y):#last and first row /\
        if(diag_maze_array[max_x][y]=="/" and diag_maze_array[max_x][y+1]=="\\"):
              counter=counter+1
        if(diag_maze_array[0][y]=="\\" and diag_maze_array[0][y+1]=="/"):
              counter=counter+1
        if(diag_maze_array[0][y]==diag_maze_array[0][y+1] and diag_maze_array[0][y]!=diag_maze_array[0][y+2]):
          counter = counter+1

  for x in range(max_x):#3 diagonal lines box
    for y in range(max_y):
        if(diag_maze_array[x][y]==diag_maze_array[x+1][y+1] and diag_maze_array[x][y] != diag_maze_array[x][y+1] and diag_maze_array[x][y+1]!=diag_maze_array[x+1][y] and diag_maze_array[x][y]==diag_maze_array[x+1][y] and diag_maze_array[x+1][y]!=diag_maze_array[max_x][y] ):
            counter=counter+1
  

  for x in range(max_x):#diamond
     for y in range(max_y):
        
       if(diag_maze_array[x][y]== "/" and diag_maze_array[x][y+1]== "\\" and diag_maze_array[x+1][y]== "\\" and diag_maze_array[x+1][y+1]== "/"):
          counter=counter+1
          
  for x in range(max_x):# sides > <
    if(diag_maze_array[x][0]=="\\" and diag_maze_array[x+1][0]=="/"):
          counter=counter+1
          
    if(diag_maze_array[x][max_y]=="/" and diag_maze_array[x+1][max_y]=="\\"):
          counter=counter+1
  
  return counter


print(count_areas(["\//\\\\/", "\///\\\\", "//\\\\/\\", "\/\///"]))      
print(count_areas(["\/", "/\\"]))
print(count_areas(["/\\", "\/"]))
print(count_areas([]))


