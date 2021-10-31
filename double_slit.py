import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider


#Definimos los valores iniciales:
X = np.arange(-0.005,0.005,0.00001)
ancho_rendija= 100*(10**-6)
long_onda = 500*(10**-9)
distancia_pantalla = 50*(10**-2)
dist_entre_rendijas= 1*10**-3

#Definimos la funcion:
def doble_rendija_diff_intens(ancho_rendija, long_onda, distancia_pantalla, dist_entre_rendijas,  X) :
  """
    Coge los valores de ancho_rendija, long_onda, distancia pantalla, distancia entre las dos rendijas y una matriz numpy X (distancias del centro).
    Devuelve una matriz de intensidades normalizadas correspondiente a X.
  """
  return (((np.sin((np.pi*ancho_rendija*X)/(long_onda*distancia_pantalla)))/((np.pi*ancho_rendija*X)/(long_onda*distancia_pantalla)))**2)*((np.cos((np.pi*dist_entre_rendijas*X)/(long_onda*distancia_pantalla)))**2)

#Utilizamos la funcion:
Y = doble_rendija_diff_intens(ancho_rendija, long_onda, distancia_pantalla, dist_entre_rendijas, X)
plot, = plt.plot(X,Y)
plt.xlabel("Distancia del centro")
plt.ylabel("Intensidad")

#Definimos los ejes:
ejes=(plt.axes([0.75, 0.75, 0.14, 0.05]))
ejes2 = (plt.axes([0.75,0.65, 0.14, 0.05]))
ejes3 = (plt.axes([0.75,0.55, 0.14, 0.05]))
ejes4 = (plt.axes([0.75,0.45, 0.14, 0.05]))

long_onda_slider = Slider(ejes,'Longitudonda(nm)',100, 1000,valinit=long_onda*10**9)
slit_width_slider = Slider(ejes2, "Distancia Rendijas(micrometros)", 10, 1000, valinit=ancho_rendija*10**6)
distancia_pantalla_slider = Slider(ejes3, "Distancia Pantalla(cm)", 10, 100, valinit= distancia_pantalla*10**2)
dist_entre_rendijas_slider = Slider(ejes4, "Distancia b/w rendijas(mm)", 0.1, 10, valinit=dist_entre_rendijas*10**3) 




#Definimos la funcion:
def update(val) :
  long_onda = long_onda_slider.val*(10**-9)
  ancho_rendija = slit_width_slider.val*(10**-6)
  distancia_pantalla = distancia_pantalla_slider.val*(10**-2)
  dist_entre_rendijas = dist_entre_rendijas_slider.val*(10**-3)
  Y = doble_rendija_diff_intens(ancho_rendija, long_onda, distancia_pantalla, dist_entre_rendijas, X)
  plot.set_ydata(Y)

long_onda_slider.on_changed(update)
slit_width_slider.on_changed(update)
distancia_pantalla_slider.on_changed(update)
dist_entre_rendijas_slider.on_changed(update)

plt.show()
