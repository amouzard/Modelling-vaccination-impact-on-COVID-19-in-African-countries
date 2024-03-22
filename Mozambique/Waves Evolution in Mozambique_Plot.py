import numpy as np
import matplotlib.pyplot as pyplot
pico=np.loadtxt('Waves Evolution in Mozambique_Data.txt',dtype=float)

pyplot.xlabel(r'Days Since the First Case')
pyplot.ylabel(r'Infectious (I)')
#pyplot.title('Time Series(TS) for the Population in Compartment I(t) in Mozambique')
#pyplot.text(15,7000, r'$(Cl\'audio \ Mois\acute{e}s \ Paulo \ , \ 2022)$')
#pyplot.text(15,5000, r'$(Updated: \ 16:22, \ 27/06/2022)$')


lines = pyplot.plot(pico[:,0],pico[:,1])
pyplot.setp(lines, color='r', linewidth=2.0)


pyplot.savefig('wave5MOZ.eps',format='eps',dpi=1200)
pyplot.savefig('wave5MOZ.png')
pyplot.show()
