#Importing libraries 
import numpy as np
import matplotlib.pyplot as plt


#Creating canvas
fig , ax = plt.subplots()


def curve(radio,rotation,LX,LY):
  '''
    Main function to plot the Gold Spiral curves

    It create a circular quadrant that is rotated and translated
  '''
  #Rotation cases in each quadrant
  rot = [(1,1),(1,-1),(-1,-1),(-1,1)]
  rotx , roty = rot[rotation%4]

  #Points that conform the circular quadrant
  X = np.linspace(0,radio,num=10000)
  Y = np.sqrt(radio**2-(X)**2)
  
  #Rotate the circular quadrant
  X *= rotx
  Y *= roty
  
  #Components of the curve's first point
  if rotation%4 == 1 or rotation%4 == 3:
    FX , FY = X[-1] , Y[-1]
  else:
    FX , FY = X[0] , Y[0]
  
  #Translating of the current curve using previous curve's 
  #last point and current curve's first point
  if rotation == 0:
    X , Y = X , Y
  else:
    X = X - FX + LX
    Y = Y - FY + LY
  
  #Plotting the curve with the same color
  plot = plt.plot(X,Y,c='blue')
  
  #Getting the current curve's last point
  if rotation%4 == 1 or rotation%4 == 3:
    rLX , rLY = X[0] , Y[0]
  else:
    rLX , rLY = X[-1] , Y[-1]

  return plot , rLX , rLY

if __name__ == '__main__':
    #Initial plotting and its aspect
    ax.set_aspect(2/(1+np.sqrt(5)))
    LX , LY = 0 , 0 
    fib = [1,1,2]

    #Number of curves to plot
    N = 10

    #Plotting of Golden Spiral with N curves 
    for i in range(N):
      if 3<=i:
        fib.append(fib[i-1]+fib[i-2])

      _ , LX , LY = curve(fib[i],i,LX,LY)

    plt.show()