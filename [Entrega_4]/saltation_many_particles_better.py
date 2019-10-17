from matplotlib.pylab import *
import random
from time import time
start_time = time()
#unidades base SI (m, kg, s)

_m = 1.
_kg = 1.
_s = 1.
_mm = 1e-3*_m
_cm = 1e-2*_m
_gr = 1e-3*_kg
_in = 2.54 *_cm 

#masa de una particula 
g = 9.81 *_m/_s**2 #gravedad
d = 0.15*_mm #diametro 
rho_agua = 1000.*_kg/(_m**3)
rho_particula = 2650.*_kg/(_m**3)

dt = 0.0001*_s  #paso de tiempo
tmax = 2*_s #tiempo maximo de simulacion
ti = 0.*_s  #tiempo actual

tau_star = 0.067   # Tau star (Shear stress)

#importacion de condiciones iniciales
data = load("initial_condition.npz")
x0 = data["x0"]
y0 = data["y0"]
vx0 = data["vx0"]
vy0 = data["vy0"]
Nparticulas = data["Nparticulas"]
print "Numero de particulas:", Nparticulas

A = pi*(d/2)**2
V = (4./3.)*pi*(d/2)**3
m = rho_particula*V

W = array([0, -m*g])
#fB = array([0, rho_agua*V*g])

t = arange(0,tmax,dt)
Nt = len(t)

norm = lambda v: sqrt(dot(v,v))

Cd = 0.47 #para una particula
Cm = 0.5
CL = 0.2
Rp = 73.
R = (rho_particula/rho_agua -1)
alpha = 1/(1 + R + Cm)

ihat = array ([1,0]) #vectores unitarios
jhat = array ([0,1])

tau_cr = 0.22*Rp**(-0.6)+0.06*10**(-7*Rp**(-0.6))   # tau critico
ustar = sqrt(tau_star * g * Rp * d)		# uestrella de verdad

def velocity_field(x):
	z = x[1] /d
	if z > 1/30.:
		uf = ustar*log(30.*z)/0.41
		uf = uf * (uf > 0)
	else :
		uf = 0 
	return array ([uf,0])	

def fondo(x):
	x_mod_d = (x % d) - d/2
	y = sqrt((d/2)**2 - x_mod_d**2)
	return y

def fuerzas_hidrodinamicas(x,v,d,area,masa):
	xtop = x + (d/2)*jhat #posicion superior particulas
	xbot = x - (d/2)*jhat #posicion inferior particulas
	vf = velocity_field(x + 0*jhat)

	vrelf_top = abs(velocity_field(xtop)[0])
	vrelf_bot = abs(velocity_field(xbot)[0])

	vrel = vf - v

	Cd = 0.47
	fD = (0.5*Cd*alpha*rho_agua*norm(vrel)*area)*vrel

	fL = (0.5*CL*alpha*rho_agua*(vrelf_top - vrelf_bot)*area)*vrel[0]*jhat
	fW = (-masa*g)*jhat

	Fh = fW + fD + fL

	return Fh

elapsed_time1 = time() - start_time
print("Elapsed time1: %.10f seconds." % elapsed_time1)

vfx = velocity_field([0, 10*d])[0]
k_penal = 0.5*Cd*rho_agua*A*norm(vfx)**2/(d/20)

def particula(z,t):
	zp = zeros (4*Nparticulas)
	
	for i in range (Nparticulas):
		di = d
		xi = z[4*i:(4*i+2)]
		vi = z[4*i+2:(4*i+4)]

		Fh = fuerzas_hidrodinamicas(xi,vi, di, A, m)

		if xi[1] < fondo(xi[0]): #evaluo el choque con el piso
			if xi[1] > 0:
				xsuelo = round(xi[0]/d)*d+d/2
				rij = xi - [xsuelo, 0] #vector entre particulas
				if norm(rij) < d:
					delta = di - norm(rij)
					nij = rij /norm (rij)				

					Fh += k_penal*delta*nij 
			else: 
				Fh[1]+= k_penal*xi[1]

		zp[4*i:(4*i+2)] = vi
		zp[4*i+2:(4*i+4)] = Fh / m 
	
	for i in range (Nparticulas):
		xi = z[4*i:(4*i+2)] #calculo posicion de particula i 
		for j in range (Nparticulas):
			if i > j :
				xj = z[4*j : (4 * j+2)] #posicion de particula j 
				rij = xj - xi #vector diferencia entre posiciones i j 
				if norm (rij) < d: 
					delta = d - norm (rij)	
					nij = rij / norm (rij) #vector unitario q apunta de i hacia j 
					Fj = k_penal*delta*nij
					Fi = -k_penal*delta*nij
					zp [4*i+2:(4*i+4)] += Fi/m	
					zp [4*j+2:(4*j+4)] += Fj/m

	return zp 
elapsed_time2 = time() - start_time
print("Elapsed time2: %.10f seconds." % elapsed_time2)

from scipy.integrate import odeint
z0 = zeros (4*Nparticulas)
z0[0::4] = x0 
z0[1::4] = y0
z0[2::4] = vx0 
z0[3::4] = vy0

print "integrando"
z = odeint (particula, z0, t)
print "fin"

fig = figure ()
ax = gca() #linea suelo
for i in range(Nparticulas):
	xi = z[:, 4*i]
	yi = z[:, 4*i+1]
	col = rand(4)
	#for j in range(int(tmax/dt)): #marca cada 8 ptos la particula completa en rojo
		#if j%50 == 0: 
		#	circle = plt.Circle((xi[j], yi[j]), d/2, color=col, clip_on=True)
		#ax.add_artist(circle)	
		
#	plot (xi[0], yi[0], "o", color ="r")
	plot (xi/d,yi/d,"--.", color=col)
	#for x, y in zip(xi, yi):
	#	ax.add_artist(Circle(xy=(x,y),radius=d/2, color = col, alpha=0.7))

x = linspace(0, 1000*d,40000)
x_mod_d = (x % d) - d/2
y = sqrt((d/2)**2 - x_mod_d**2)

plot(x, y)


ax.axhline(d/2,color="k",linestyle="--")
plt.xlabel("x/d")
plt.ylabel("z/d")
plt.title("Movimiento de particulas (plano XY)")
plt.legend()

elapsed_time = time() - start_time
show ()
print("Elapsed time: %.10f seconds." % elapsed_time) 
