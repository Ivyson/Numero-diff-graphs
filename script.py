import numpy as np
from matplotlib import pyplot as plt
dt = 0.2 # scale the small value of dt to be as small as possible
t = np.linspace(-2, 4, 60)
f = np.sin(t)
#Compute the derivative of this function 
dfdt = np.cos(t)  # This is the exact derivative
dfdtF = (np.sin(t+dt)-np.sin(t))/dt  #Forward Derivative
dfdtB = (np.sin(t)-np.sin(t-dt))/dt  #Backwards Derivative
dfdtC = (np.sin(t+dt)-np.sin(t-dt))/(2*dt) #CENTRAL DERIVATIVE 
#Plot the derivative graph on 
#Plot the Original Function 
plt.plot(t, f, 'k--', linewidth = 1.2) #Draw an actual Function sin(t)
plt.grid(True)
## Plot the Actual derivative
plt.plot(t, dfdt, 'k', linewidth = 3)
plt.plot(t, dfdtF, 'r', linewidth = 3)
plt.plot(t, dfdtB, 'b', linewidth = 3)
plt.plot(t, dfdtC, 'c', linewidth = 3)
plt.legend(["Function", "Exact Derivative","Forward Derivative", "Backwards Derivative", "Central Derivative"], fontsize = 12)
plt.xlim(-2, 4)
plt.ylim(-2, 2)
# hold on
plt.show()