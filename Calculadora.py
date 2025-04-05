from scipy.special import comb
from scipy import stats
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")


#Se cambia el tema de la calculadora
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

#Se crea la ventana de inicio de la calculadora
inicio = ctk.CTk()
inicio.title('Calculadora de Distribuciones')
inicio.geometry('500x300')
inicio.resizable(False, False)
inicio.lift()
inicio.attributes('-topmost', True)
centrar_ventana(inicio, 500, 300)

#Se crea label de titulo en el inicio
lbl_titulo = ctk.CTkLabel(inicio, text='Calculadora de Distribuciones', bg_color= 'transparent', font=('Arial', 20))
lbl_titulo.place(relx=0.5, rely=0.1, anchor = tk.CENTER)

#Se crea combobox en el inicio
combobox = ctk.CTkComboBox(inicio, values=['Distribucion Binomial', 'Distribucion Poisson', 'Distribucion Normal','Distribucion Hipergeometrica'], 
                           state='readonly')
combobox.set('-Seleccione-')
combobox.place(relx=0.5, rely=0.5, anchor = tk.CENTER)

#Se crea label en el inicio
lbl = ctk.CTkLabel(inicio, text='Seleccione una distribución')
lbl.place(relx=0.5, rely=0.4, anchor = tk.CENTER)

#Se crea una función que se ejecuta al presionar el botón iniciar
def press_i():
    if combobox.get() == 'Distribucion Binomial':
        inicio.withdraw()
        dist_binomial.deiconify()
    elif combobox.get() == 'Distribucion Poisson':
        inicio.withdraw()
        dist_poisson.deiconify()
    elif combobox.get() == 'Distribucion Hipergeometrica':
        inicio.withdraw()
        dist_hipergeometrica.deiconify()
    elif combobox.get() == 'Distribucion Normal':
        inicio.withdraw()
        dist_normal.deiconify()
    else:
        messagebox.showerror('Error', 'Seleccione una distribución')

#Se crea funcion para volver a la ventana de inicio
def press_v():
    dist_binomial.withdraw()
    dist_poisson.withdraw()
    dist_hipergeometrica.withdraw()
    dist_normal.withdraw()
    inicio.deiconify()

#Se crea funcion para cerrar la ventana de inicio
def press_cerrar():
    inicio.quit()

#Se crea boton en el inicio
btn_i = ctk.CTkButton(inicio, text='Iniciar', command = press_i)
btn_i.place(relx=0.35, rely=0.7, anchor = tk.CENTER)

#Se crea boton cerrar en el inicio
btn_cerrar = ctk.CTkButton(inicio, text='Cerrar', command = press_cerrar)
btn_cerrar.place(relx=0.65, rely=0.7, anchor = tk.CENTER)

#Se la ventana de la distribución binomial
dist_binomial = ctk.CTk()
dist_binomial.title('Distribución Binomial')
dist_binomial.geometry('800x600')
dist_binomial.resizable(False, False)
centrar_ventana(dist_binomial, 800, 600)

#Se crea una función que se ejecuta al presionar el botón calcular
def press_cbin():
    if txt_n.get() == '':
        messagebox.showerror('Error', 'Ingrese un valor para n')
    elif txt_k.get() == '':
        messagebox.showerror('Error', 'Ingrese un valor para k')
    elif txt_p.get() == '':
        messagebox.showerror('Error', 'Ingrese un valor para p')

    #Se obtienen los valores de los textbox
    #Bucle para validar que p sea un valor entre 0 y 1
    while True:
        if float(txt_p.get()) < 0 or float(txt_p.get()) > 1:
            messagebox.showerror('Error', 'Ingrese un valor entre 0 y 1 para p')
            break
        else:
            break
    k = int(txt_k.get())
    n = int(txt_n.get()) 
    p = float(txt_p.get())
    xi = k
    if txt_xj.get() != '':
        xj = int(txt_xj.get())


    # Distribución para P(X=k)
    distribucion_binom = stats.binom.pmf(k, n, p)

    # Distribución para P(X<k)
    distribucion_binom_menor = stats.binom.cdf(k-1, n, p)

    # Distribución para P(X>k)
    distribucion_binom_mayor = 1 - stats.binom.cdf(k, n, p)

    # Distribución para P(X<=k)
    distribucion_binom_menor_igual = stats.binom.cdf(k, n, p)

    # Distribución para P(X>=k)
    distribucion_binom_mayor_igual = 1 - stats.binom.cdf(k-1, n, p)

    if txt_xj.get() != '':
        # Distribución para P(x_i < X < x_j)
        distribucion_binom_entre = stats.binom.cdf(xj-1, n, p) - stats.binom.cdf(xi, n, p)

        # Distribución para P(x_i <= X <= x_j)
        distribucion_binom_entre_igual = stats.binom.cdf(xj, n, p) - stats.binom.cdf(xi-1, n, p)

    #Se muestran los resultados en los textbox
    txt_r_XK.configure(state='normal')
    txt_r_XK.delete(0, tk.END)
    txt_r_XK.insert(0, f'{distribucion_binom:.4}')
    txt_r_XK.configure(state='readonly')
    
    txt_r_XK_menor.configure(state='normal')
    txt_r_XK_menor.delete(0, tk.END)
    txt_r_XK_menor.insert(0, f'{distribucion_binom_menor:.4}')
    txt_r_XK_menor.configure(state='readonly')
        
    txt_r_XK_mayor.configure(state='normal')
    txt_r_XK_mayor.delete(0, tk.END)
    txt_r_XK_mayor.insert(0, f'{distribucion_binom_mayor:.4}')
    txt_r_XK_mayor.configure(state='readonly')
    
    txt_r_XK_menor_igual.configure(state='normal')
    txt_r_XK_menor_igual.delete(0, tk.END)
    txt_r_XK_menor_igual.insert(0, f'{distribucion_binom_menor_igual:.4}')
    txt_r_XK_menor_igual.configure(state='readonly')
    
    txt_r_XK_mayor_igual.configure(state='normal')
    txt_r_XK_mayor_igual.delete(0, tk.END)
    txt_r_XK_mayor_igual.insert(0, f'{distribucion_binom_mayor_igual:.4}')
    txt_r_XK_mayor_igual.configure(state='readonly')
    
    #Condicion en caso de que no se haya ingresado un valor para xj
    if txt_xj.get() != '':
        txt_r_Xi_Xj.configure(state='normal')
        txt_r_Xi_Xj.delete(0, tk.END)
        txt_r_Xi_Xj.insert(0, f'{distribucion_binom_entre:.4}')
        txt_r_Xi_Xj.configure(state='readonly')
    
        txt_r_Xi_Xj_igual.configure(state='normal')
        txt_r_Xi_Xj_igual.delete(0, tk.END)
        txt_r_Xi_Xj_igual.insert(0, f'{distribucion_binom_entre_igual:.4}')
        txt_r_Xi_Xj_igual.configure(state='readonly')
    else:
        txt_r_Xi_Xj.configure(state='normal')
        txt_r_Xi_Xj.delete(0, tk.END)
        txt_r_Xi_Xj.insert(0, 'No ingresado')
        txt_r_Xi_Xj.configure(state='readonly')
    
        txt_r_Xi_Xj_igual.configure(state='normal')
        txt_r_Xi_Xj_igual.delete(0, tk.END)
        txt_r_Xi_Xj_igual.insert(0, 'No ingresado')
        txt_r_Xi_Xj_igual.configure(state='readonly')


#Se crea una función que se ejecuta al presionar el botón limpiar
def press_l():
    txt_k.delete(0, tk.END)
    txt_n.delete(0, tk.END)
    txt_p.delete(0, tk.END)
    txt_xj.delete(0, tk.END)
    
    txt_r_XK.configure(state='normal')
    txt_r_XK.delete(0, tk.END)
    txt_r_XK.configure(state='readonly')
    
    txt_r_XK_menor.configure(state='normal')
    txt_r_XK_menor.delete(0, tk.END)
    txt_r_XK_menor.configure(state='readonly')
    
    txt_r_XK_mayor.configure(state='normal')
    txt_r_XK_mayor.delete(0, tk.END)
    txt_r_XK_mayor.configure(state='readonly')
    
    txt_r_XK_menor_igual.configure(state='normal')
    txt_r_XK_menor_igual.delete(0, tk.END)
    txt_r_XK_menor_igual.configure(state='readonly')
    
    txt_r_XK_mayor_igual.configure(state='normal')
    txt_r_XK_mayor_igual.delete(0, tk.END)
    txt_r_XK_mayor_igual.configure(state='readonly')
    
    txt_r_Xi_Xj.configure(state='normal')
    txt_r_Xi_Xj.delete(0, tk.END)
    txt_r_Xi_Xj.configure(state='readonly')
    
    txt_r_Xi_Xj_igual.configure(state='normal')
    txt_r_Xi_Xj_igual.delete(0, tk.END)
    txt_r_Xi_Xj_igual.configure(state='readonly')

def press_l_p():
    txt_mu.delete(0, tk.END)
    txt_k_p.delete(0, tk.END)
    txt_xj_p.delete(0, tk.END)
    
    txt_r_XK_p.configure(state='normal')
    txt_r_XK_p.delete(0, tk.END)
    txt_r_XK_p.configure(state='readonly')
    
    txt_r_XK_menor_p.configure(state='normal')
    txt_r_XK_menor_p.delete(0, tk.END)
    txt_r_XK_menor_p.configure(state='readonly')
    
    txt_r_XK_mayor_p.configure(state='normal')
    txt_r_XK_mayor_p.delete(0, tk.END)
    txt_r_XK_mayor_p.configure(state='readonly')
    
    txt_r_XK_menor_igual_p.configure(state='normal')
    txt_r_XK_menor_igual_p.delete(0, tk.END)
    txt_r_XK_menor_igual_p.configure(state='readonly')
    
    txt_r_XK_mayor_igual_p.configure(state='normal')
    txt_r_XK_mayor_igual_p.delete(0, tk.END)
    txt_r_XK_mayor_igual_p.configure(state='readonly')
    
    txt_r_Xi_Xj_p.configure(state='normal')
    txt_r_Xi_Xj_p.delete(0, tk.END)
    txt_r_Xi_Xj_p.configure(state='readonly')
    
    txt_r_Xi_Xj_igual_p.configure(state='normal')
    txt_r_Xi_Xj_igual_p.delete(0, tk.END)
    txt_r_Xi_Xj_igual_p.configure(state='readonly')

def press_l_h():
    txt_k_h.delete(0, tk.END)
    txt_n_h.delete(0, tk.END)
    txt_N.delete(0, tk.END)
    txt_x.delete(0, tk.END)
    txt_xj_h.delete(0, tk.END)
    
    txt_r_XK_h.configure(state='normal')
    txt_r_XK_h.delete(0, tk.END)
    txt_r_XK_h.configure(state='readonly')
    
    txt_r_XK_menor_h.configure(state='normal')
    txt_r_XK_menor_h.delete(0, tk.END)
    txt_r_XK_menor_h.configure(state='readonly')
    
    txt_r_XK_mayor_h.configure(state='normal')
    txt_r_XK_mayor_h.delete(0, tk.END)
    txt_r_XK_mayor_h.configure(state='readonly')
    
    txt_r_XK_menor_igual_h.configure(state='normal')
    txt_r_XK_menor_igual_h.delete(0, tk.END)
    txt_r_XK_menor_igual_h.configure(state='readonly')
    
    txt_r_XK_mayor_igual_h.configure(state='normal')
    txt_r_XK_mayor_igual_h.delete(0, tk.END)
    txt_r_XK_mayor_igual_h.configure(state='readonly')
    
    txt_r_Xi_Xj_h.configure(state='normal')
    txt_r_Xi_Xj_h.delete(0, tk.END)
    txt_r_Xi_Xj_h.configure(state='readonly')
    
    txt_r_Xi_Xj_igual_h.configure(state='normal')
    txt_r_Xi_Xj_igual_h.delete(0, tk.END)
    txt_r_Xi_Xj_igual_h.configure(state='readonly')

def press_l_n():
    txt_mu_n.delete(0, tk.END)
    txt_sigma.delete(0, tk.END)
    txt_k_n.delete(0, tk.END)
    txt_xj_n.delete(0, tk.END)
    
    txt_r_XK_menor_igual_n.configure(state='normal')
    txt_r_XK_menor_igual_n.delete(0, tk.END)
    txt_r_XK_menor_igual_n.configure(state='readonly')
    
    txt_r_XK_mayor_igual_n.configure(state='normal')
    txt_r_XK_mayor_igual_n.delete(0, tk.END)
    txt_r_XK_mayor_igual_n.configure(state='readonly')
    
    txt_r_Xi_Xj_n.configure(state='normal')
    txt_r_Xi_Xj_n.delete(0, tk.END)
    txt_r_Xi_Xj_n.configure(state='readonly')

#Funcion para validar que lo que se escribe en los textbox sean solo numeros
def validar_num(action, txt):
    if action == '1':  # Acción de insertar
        if txt == "" or txt == "-" or txt == ".":
            return True
        if txt.count("-") > 1 or txt.count(".") > 1:
            messagebox.showerror('Error', 'El caracter ingresado no está permitido')
            return False
        if txt.replace("-", "").replace(".", "").isdigit():
            return True
        else:
            messagebox.showerror('Error', 'El caracter ingresado no está permitido')
            return False
    return True  # Permitir otras acciones como borrar

vcmd = (dist_binomial.register(validar_num), '%d', '%P')

#Se crean textbox en la ventana para ingresar los valores de n, k y p
txt_n = ctk.CTkEntry(dist_binomial)
txt_n.place(relx=0.25, rely=0.2, anchor = tk.CENTER)
txt_n.configure(validate='key', validatecommand=vcmd)

txt_k = ctk.CTkEntry(dist_binomial)
txt_k.place(relx=0.5, rely=0.2, anchor = tk.CENTER)
txt_k.configure(validate='key', validatecommand=vcmd)

txt_p = ctk.CTkEntry(dist_binomial)
txt_p.place(relx=0.75, rely=0.2, anchor = tk.CENTER)  
txt_p.configure(validate='key', validatecommand=vcmd)

txt_xj = ctk.CTkEntry(dist_binomial)
txt_xj.place(relx=0.5, rely=0.3, anchor = tk.CENTER)
txt_xj.configure(validate='key', validatecommand=vcmd)

#Se crea label de titulo en la ventana
lbl_titulo_bin = ctk.CTkLabel(dist_binomial, text='Distribucion Binomial', bg_color= 'transparent', font=('Arial', 20))
lbl_titulo_bin.place(relx=0.5, rely=0.05, anchor = tk.CENTER)

#Se crean labels en la ventana para indicar los campos de n, k y p
lbl_n = ctk.CTkLabel(dist_binomial, text='n', bg_color= 'transparent')
lbl_n.place(relx=0.25, rely=0.15, anchor = tk.CENTER)

lbl_k = ctk.CTkLabel(dist_binomial, text='k', bg_color= 'transparent')
lbl_k.place(relx=0.5, rely=0.15, anchor = tk.CENTER)

lbl_p = ctk.CTkLabel(dist_binomial, text='p', bg_color= 'transparent')
lbl_p.place(relx=0.75, rely=0.15, anchor = tk.CENTER)

lbl_xj = ctk.CTkLabel(dist_binomial, text='xj', bg_color= 'transparent')
lbl_xj.place(relx=0.5, rely=0.25, anchor = tk.CENTER)

#Se crea boton calcular
btn_c = ctk.CTkButton(dist_binomial, text='Calcular', command = press_cbin)
btn_c.place(relx=0.4, rely=0.4, anchor = tk.CENTER)

#Se crea boton limpiar
btn_l = ctk.CTkButton(dist_binomial, text='Limpiar', command = press_l)
btn_l.place(relx=0.6, rely=0.4, anchor = tk.CENTER)

#Se crea boton volver
btn_v = ctk.CTkButton(dist_binomial, text='Volver', command = press_v)
btn_v.place(relx=0.9, rely=0.9, anchor = tk.CENTER)

lbl_resultados = ctk.CTkLabel(dist_binomial, text='Resultados', bg_color= 'transparent', font=('Arial', 20))
lbl_resultados.place(relx=0.5, rely=0.5, anchor = tk.CENTER)

#Se crean textbox en la ventana para mostrar los resultados
txt_r_XK = ctk.CTkEntry(dist_binomial)
txt_r_XK.place(relx=0.25, rely=0.65, anchor = tk.CENTER)
txt_r_XK.configure(state='readonly')

txt_r_XK_menor = ctk.CTkEntry(dist_binomial)
txt_r_XK_menor.place(relx=0.5, rely=0.65, anchor = tk.CENTER)
txt_r_XK_menor.configure(state='readonly')

txt_r_XK_mayor = ctk.CTkEntry(dist_binomial)
txt_r_XK_mayor.place(relx=0.75, rely=0.65, anchor = tk.CENTER)
txt_r_XK_mayor.configure(state='readonly')

txt_r_XK_menor_igual = ctk.CTkEntry(dist_binomial)
txt_r_XK_menor_igual.place(relx=0.25, rely=0.75, anchor = tk.CENTER)
txt_r_XK_menor_igual.configure(state='readonly')

txt_r_XK_mayor_igual = ctk.CTkEntry(dist_binomial)
txt_r_XK_mayor_igual.place(relx=0.5, rely=0.75, anchor = tk.CENTER)
txt_r_XK_mayor_igual.configure(state='readonly')

txt_r_Xi_Xj = ctk.CTkEntry(dist_binomial)
txt_r_Xi_Xj.place(relx=0.75, rely=0.75, anchor = tk.CENTER)
txt_r_Xi_Xj.configure(state='readonly')

txt_r_Xi_Xj_igual = ctk.CTkEntry(dist_binomial)
txt_r_Xi_Xj_igual.place(relx=0.5, rely=0.85, anchor = tk.CENTER)
txt_r_Xi_Xj_igual.configure(state='readonly')

#Se crean labels en la ventana para indicar los campos de los resultados
lbl_XK = ctk.CTkLabel(dist_binomial, text='P(X=k)', bg_color= 'transparent')
lbl_XK.place(relx=0.25, rely=0.6, anchor = tk.CENTER)

lbl_XK_menor = ctk.CTkLabel(dist_binomial, text='P(X<k)', bg_color= 'transparent')
lbl_XK_menor.place(relx=0.5, rely=0.6, anchor = tk.CENTER)

lbl_XK_mayor = ctk.CTkLabel(dist_binomial, text='P(X>k)', bg_color= 'transparent')
lbl_XK_mayor.place(relx=0.75, rely=0.6, anchor = tk.CENTER)

lbl_XK_menor_igual = ctk.CTkLabel(dist_binomial, text='P(X<=k)', bg_color= 'transparent')
lbl_XK_menor_igual.place(relx=0.25, rely=0.7, anchor = tk.CENTER)

lbl_XK_mayor_igual = ctk.CTkLabel(dist_binomial, text='P(X>=k)', bg_color= 'transparent')
lbl_XK_mayor_igual.place(relx=0.5, rely=0.7, anchor = tk.CENTER)

lbl_Xi_Xj = ctk.CTkLabel(dist_binomial, text='P(xi<X<xj)', bg_color= 'transparent')
lbl_Xi_Xj.place(relx=0.75, rely=0.7, anchor = tk.CENTER)

lbl_Xi_Xj_igual = ctk.CTkLabel(dist_binomial, text='P(xi<=X<=xj)', bg_color= 'transparent')
lbl_Xi_Xj_igual.place(relx=0.5, rely=0.8, anchor = tk.CENTER)

#Se crea la ventana de distribución poisson
dist_poisson = ctk.CTk()
dist_poisson.title("Distribucion Poisson")
dist_poisson.geometry('800x600')
dist_poisson.resizable(False, False)
centrar_ventana(dist_poisson, 800, 600)

#Se crea una función que se ejecuta al presionar el botón calcular
def press_cpoisson():
    if txt_mu.get() == '':
        messagebox.showerror('Error', 'Ingrese un valor para mu')
    elif txt_k_p.get() == '':
        messagebox.showerror('Error', 'Ingrese un valor para k')

    #Se obtienen los valores de los textbox
    mu = float(txt_mu.get())
    k = int(txt_k_p.get())
    xi = k
    if txt_xj_p.get() != '':
        xj = int(txt_xj_p.get())

    # Distribución para P(X=k)
    distribucion_poisson = stats.poisson.pmf(k, mu)

    # Distribución para P(X<k)
    distribucion_poisson_menor = stats.poisson.cdf(k-1, mu)

    # Distribución para P(X>k)
    distribucion_poisson_mayor = 1 - stats.poisson.cdf(k, mu)

    # Distribución para P(X<=k)
    distribucion_poisson_menor_igual = stats.poisson.cdf(k, mu)

    # Distribución para P(X>=k)
    distribucion_poisson_mayor_igual = 1 - stats.poisson.cdf(k-1, mu)

    if txt_xj_p.get() != '':
        # Distribución para P(x_i < X < x_j)
        distribucion_poisson_entre = stats.poisson.cdf(xj-1, mu) - stats.poisson.cdf(xi, mu)

        # Distribución para P(x_i <= X <= x_j)
        distribucion_poisson_entre_igual = stats.poisson.cdf(xj, mu) - stats.poisson.cdf(xi-1, mu)

    #Se muestran los resultados en los textbox
    txt_r_XK_p.configure(state='normal')
    txt_r_XK_p.delete(0, tk.END)
    txt_r_XK_p.insert(0, f'{distribucion_poisson:.4}')
    txt_r_XK_p.configure(state='readonly')
    
    txt_r_XK_menor_p.configure(state='normal')
    txt_r_XK_menor_p.delete(0, tk.END)
    txt_r_XK_menor_p.insert(0, f'{distribucion_poisson_menor:.4}')
    txt_r_XK_menor_p.configure(state='readonly')
    
    txt_r_XK_mayor_p.configure(state='normal')
    txt_r_XK_mayor_p.delete(0, tk.END)
    txt_r_XK_mayor_p.insert(0, f'{distribucion_poisson_mayor:.4}')
    txt_r_XK_mayor_p.configure(state='readonly')
    
    txt_r_XK_menor_igual_p.configure(state='normal')
    txt_r_XK_menor_igual_p.delete(0, tk.END)
    txt_r_XK_menor_igual_p.insert(0, f'{distribucion_poisson_menor_igual:.4}')
    txt_r_XK_menor_igual_p.configure(state='readonly')
    
    txt_r_XK_mayor_igual_p.configure(state='normal')
    txt_r_XK_mayor_igual_p.delete(0, tk.END)
    txt_r_XK_mayor_igual_p.insert(0, f'{distribucion_poisson_mayor_igual:.4}')
    txt_r_XK_mayor_igual_p.configure(state='readonly')
    
    #Condicion en caso de que no se haya ingresado un valor para xj
    if txt_xj_p.get() != '':
        txt_r_Xi_Xj_p.configure(state='normal')
        txt_r_Xi_Xj_p.delete(0, tk.END)
        txt_r_Xi_Xj_p.insert(0, f'{distribucion_poisson_entre:.4}')
        txt_r_Xi_Xj_p.configure(state='readonly')
    
        txt_r_Xi_Xj_igual_p.configure(state='normal')
        txt_r_Xi_Xj_igual_p.delete(0, tk.END)
        txt_r_Xi_Xj_igual_p.insert(0, f'{distribucion_poisson_entre_igual:.4}')
        txt_r_Xi_Xj_igual_p.configure(state='readonly')
    else:
        txt_r_Xi_Xj_p.configure(state='normal')
        txt_r_Xi_Xj_p.delete(0, tk.END)
        txt_r_Xi_Xj_p.insert(0, 'No ingresado')
        txt_r_Xi_Xj_p.configure(state='readonly')
    
        txt_r_Xi_Xj_igual_p.configure(state='normal')
        txt_r_Xi_Xj_igual_p.delete(0, tk.END)
        txt_r_Xi_Xj_igual_p.insert(0, 'No ingresado')
        txt_r_Xi_Xj_igual_p.configure(state='readonly')


#Se crea boton volver
btn_v_p = ctk.CTkButton(dist_poisson, text='Volver', command = press_v)
btn_v_p.place(relx=0.9, rely=0.9, anchor = tk.CENTER)

vcmd_p = (dist_poisson.register(validar_num), '%d', '%P')

#Se crea txb para mu
txt_mu = ctk.CTkEntry(dist_poisson)
txt_mu.place(relx=0.25, rely=0.25, anchor = tk.CENTER)
txt_mu.configure(validate='key', validatecommand=vcmd_p)

#Se crea texbox para k
txt_k_p = ctk.CTkEntry(dist_poisson)
txt_k_p.place(relx=0.5, rely=0.25, anchor = tk.CENTER)
txt_k_p.configure(validate='key', validatecommand=vcmd_p)

#Se crea texbox para xj
txt_xj_p = ctk.CTkEntry(dist_poisson)
txt_xj_p.place(relx=0.75, rely=0.25, anchor = tk.CENTER)
txt_xj_p.configure(validate='key', validatecommand=vcmd_p)

#Se crea label de titulo en la ventana
lbl_titulo_poisson = ctk.CTkLabel(dist_poisson, text='Distribucion Poisson', bg_color= 'transparent', font=('Arial', 20))
lbl_titulo_poisson.place(relx=0.5, rely=0.05, anchor = tk.CENTER)

#Se crean labels en la ventana para indicar los campos de mu y k
lbl_mu = ctk.CTkLabel(dist_poisson, text='mu', bg_color= 'transparent')
lbl_mu.place(relx=0.25, rely=0.20, anchor = tk.CENTER)

lbl_k_p = ctk.CTkLabel(dist_poisson, text='k', bg_color= 'transparent')
lbl_k_p.place(relx=0.5, rely=0.20, anchor = tk.CENTER)

lbl_xj_p = ctk.CTkLabel(dist_poisson, text='xj', bg_color= 'transparent')
lbl_xj_p.place(relx=0.75, rely=0.20, anchor = tk.CENTER)

#Se crea boton calcular
btn_c_p = ctk.CTkButton(dist_poisson, text='Calcular', command = press_cpoisson)
btn_c_p.place(relx=0.35, rely=0.4, anchor = tk.CENTER)

#Se crea boton limpiar
btn_l_p = ctk.CTkButton(dist_poisson, text='Limpiar', command=press_l_p)
btn_l_p.place(relx=0.65, rely=0.4, anchor = tk.CENTER)

#Se crea label de resultados
lbl_resultados_p = ctk.CTkLabel(dist_poisson, text='Resultados', bg_color= 'transparent', font=('Arial', 20))
lbl_resultados_p.place(relx=0.5, rely=0.5, anchor = tk.CENTER)

#Se crean textbox en la ventana para mostrar los resultados
txt_r_XK_p = ctk.CTkEntry(dist_poisson)
txt_r_XK_p.place(relx=0.25, rely=0.65, anchor = tk.CENTER)
txt_r_XK_p.configure(state='readonly')

txt_r_XK_menor_p = ctk.CTkEntry(dist_poisson)
txt_r_XK_menor_p.place(relx=0.5, rely=0.65, anchor = tk.CENTER)
txt_r_XK_menor_p.configure(state='readonly')

txt_r_XK_mayor_p = ctk.CTkEntry(dist_poisson)
txt_r_XK_mayor_p.place(relx=0.75, rely=0.65, anchor = tk.CENTER)
txt_r_XK_mayor_p.configure(state='readonly')

txt_r_XK_menor_igual_p = ctk.CTkEntry(dist_poisson)
txt_r_XK_menor_igual_p.place(relx=0.25, rely=0.75, anchor = tk.CENTER)
txt_r_XK_menor_igual_p.configure(state='readonly')

txt_r_XK_mayor_igual_p = ctk.CTkEntry(dist_poisson)
txt_r_XK_mayor_igual_p.place(relx=0.5, rely=0.75, anchor = tk.CENTER)
txt_r_XK_mayor_igual_p.configure(state='readonly')

txt_r_Xi_Xj_p = ctk.CTkEntry(dist_poisson)
txt_r_Xi_Xj_p.place(relx=0.75, rely=0.75, anchor = tk.CENTER)
txt_r_Xi_Xj_p.configure(state='readonly')

txt_r_Xi_Xj_igual_p = ctk.CTkEntry(dist_poisson)
txt_r_Xi_Xj_igual_p.place(relx=0.5, rely=0.85, anchor = tk.CENTER)
txt_r_Xi_Xj_igual_p.configure(state='readonly')

#Se crea label en la ventana para indicar el campo de los resultados
lbl_XK_p = ctk.CTkLabel(dist_poisson, text='P(X=k)', bg_color= 'transparent')
lbl_XK_p.place(relx=0.25, rely=0.6, anchor = tk.CENTER)

lbl_XK_menor_p = ctk.CTkLabel(dist_poisson, text='P(X<k)', bg_color= 'transparent')
lbl_XK_menor_p.place(relx=0.5, rely=0.6, anchor = tk.CENTER)

lbl_XK_mayor_p = ctk.CTkLabel(dist_poisson, text='P(X>k)', bg_color= 'transparent')
lbl_XK_mayor_p.place(relx=0.75, rely=0.6, anchor = tk.CENTER)

lbl_XK_menor_igual_p = ctk.CTkLabel(dist_poisson, text='P(X<=k)', bg_color= 'transparent')
lbl_XK_menor_igual_p.place(relx=0.25, rely=0.7, anchor = tk.CENTER)

lbl_XK_mayor_igual_p = ctk.CTkLabel(dist_poisson, text='P(X>=k)', bg_color= 'transparent')
lbl_XK_mayor_igual_p.place(relx=0.5, rely=0.7, anchor = tk.CENTER)

lbl_Xi_Xj_p = ctk.CTkLabel(dist_poisson, text='P(xi<X<xj)', bg_color= 'transparent')
lbl_Xi_Xj_p.place(relx=0.75, rely=0.7, anchor = tk.CENTER)

lbl_Xi_Xj_igual_p = ctk.CTkLabel(dist_poisson, text='P(xi<=X<=xj)', bg_color= 'transparent')
lbl_Xi_Xj_igual_p.place(relx=0.5, rely=0.8, anchor = tk.CENTER)

#Se crea la ventana de distribución hipergeometrica
dist_hipergeometrica = ctk.CTk()
dist_hipergeometrica.title("Distribucion Hipergeometrica")
dist_hipergeometrica.geometry('800x600')
dist_hipergeometrica.resizable(False, False)
centrar_ventana(dist_hipergeometrica, 800, 600)

#Se crea una función que se ejecuta al presionar el botón calcular
def press_ch():
    if txt_k_h.get() == '':
        messagebox.showerror('Error', 'Ingrese un valor para k')
    elif txt_n_h.get() == '':
        messagebox.showerror('Error', 'Ingrese un valor para n')
    elif txt_N.get() == '':
        messagebox.showerror('Error', 'Ingrese un valor para N')
    elif txt_x.get() == '':
        messagebox.showerror('Error', 'Ingrese un valor para x')

    #Se obtienen los valores de los textbox
    k = int(txt_k_h.get())
    n = int(txt_n_h.get())
    N = int(txt_N.get())
    x = int(txt_x.get())
    xi = k
    if txt_xj_h.get() != '':
        xj = int(txt_xj_h.get())

    # Distribución para P(X=k)
    distribucion_hipergeometrica = stats.hypergeom.pmf(k, N, n, x)

    # Distribución para P(X<k)
    distribucion_hipergeometrica_menor = stats.hypergeom.cdf(k-1, N, n, x)

    # Distribución para P(X>k)
    distribucion_hipergeometrica_mayor = 1 - stats.hypergeom.cdf(k, N, n, x)

    # Distribución para P(X<=k)
    distribucion_hipergeometrica_menor_igual = stats.hypergeom.cdf(k, N, n, x)

    # Distribución para P(X>=k)
    distribucion_hipergeometrica_mayor_igual = 1 - stats.hypergeom.cdf(k-1, N, n, x)

    if txt_xj_h.get() != '':
        # Distribución para P(x_i < X < x_j)
        distribucion_hipergeometrica_entre = stats.hypergeom.cdf(xj-1, N, n, x) - stats.hypergeom.cdf(xi, N, n, x)

        # Distribución para P(x_i <= X <= x_j)
        distribucion_hipergeometrica_entre_igual = stats.hypergeom.cdf(xj, N, n, x) - stats.hypergeom.cdf(xi-1, N, n, x)
        
    #Se muestran los resultados en los textbox
    txt_r_XK_h.configure(state='normal')
    txt_r_XK_h.delete(0, tk.END)
    txt_r_XK_h.insert(0, f'{distribucion_hipergeometrica:.4}')
    txt_r_XK_h.configure(state='readonly')
    
    txt_r_XK_menor_h.configure(state='normal')
    txt_r_XK_menor_h.delete(0, tk.END)
    txt_r_XK_menor_h.insert(0, f'{distribucion_hipergeometrica_menor:.4}')
    txt_r_XK_menor_h.configure(state='readonly')
    
    txt_r_XK_mayor_h.configure(state='normal')
    txt_r_XK_mayor_h.delete(0, tk.END)
    txt_r_XK_mayor_h.insert(0, f'{distribucion_hipergeometrica_mayor:.4}')
    txt_r_XK_mayor_h.configure(state='readonly')
    
    txt_r_XK_menor_igual_h.configure(state='normal')
    txt_r_XK_menor_igual_h.delete(0, tk.END)
    txt_r_XK_menor_igual_h.insert(0, f'{distribucion_hipergeometrica_menor_igual:.4}')
    txt_r_XK_menor_igual_h.configure(state='readonly')
    
    txt_r_XK_mayor_igual_h.configure(state='normal')
    txt_r_XK_mayor_igual_h.delete(0, tk.END)
    txt_r_XK_mayor_igual_h.insert(0, f'{distribucion_hipergeometrica_mayor_igual:.4}')
    txt_r_XK_mayor_igual_h.configure(state='readonly')
    
    #Condicion en caso de que no se haya ingresado un valor para xj
    if txt_xj_h.get() != '':
        txt_r_Xi_Xj_h.configure(state='normal')
        txt_r_Xi_Xj_h.delete(0, tk.END)
        txt_r_Xi_Xj_h.insert(0, f'{distribucion_hipergeometrica_entre:.4}')
        txt_r_Xi_Xj_h.configure(state='readonly')
    
        txt_r_Xi_Xj_igual_h.configure(state='normal')
        txt_r_Xi_Xj_igual_h.delete(0, tk.END)
        txt_r_Xi_Xj_igual_h.insert(0, f'{distribucion_hipergeometrica_entre_igual:.4}')
        txt_r_Xi_Xj_igual_h.configure(state='readonly')
    else:
        txt_r_Xi_Xj_h.configure(state='normal')
        txt_r_Xi_Xj_h.delete(0, tk.END)
        txt_r_Xi_Xj_h.insert(0, 'No ingresado')
        txt_r_Xi_Xj_h.configure(state='readonly')
    
        txt_r_Xi_Xj_igual_h.configure(state='normal')
        txt_r_Xi_Xj_igual_h.delete(0, tk.END)
        txt_r_Xi_Xj_igual_h.insert(0, 'No ingresado')
        txt_r_Xi_Xj_igual_h.configure(state='readonly')

#Se crea label de titulo para la ventana
lbl_titulo_hipergeometrica = ctk.CTkLabel(dist_poisson, text='Distribucion Hipergeometrica', bg_color= 'transparent', font=('Arial', 20))
lbl_titulo_hipergeometrica.place(relx=0.5, rely=0.05, anchor = tk.CENTER)

vcmd_h = (dist_hipergeometrica.register(validar_num), '%d', '%P')

#Se crean los textbox en la ventana para ingresar los valores de k, n, N y x
txt_k_h = ctk.CTkEntry(dist_hipergeometrica)
txt_k_h.place(relx=0.25, rely=0.2, anchor = tk.CENTER)
txt_k_h.configure(validate='key', validatecommand=vcmd_h)

txt_n_h = ctk.CTkEntry(dist_hipergeometrica)
txt_n_h.place(relx=0.5, rely=0.2, anchor = tk.CENTER)
txt_n_h.configure(validate='key', validatecommand=vcmd_h)

txt_N = ctk.CTkEntry(dist_hipergeometrica)
txt_N.place(relx=0.75, rely=0.2, anchor = tk.CENTER)
txt_N.configure(validate='key', validatecommand=vcmd_h)

txt_x = ctk.CTkEntry(dist_hipergeometrica)
txt_x.place(relx=0.35, rely=0.3, anchor = tk.CENTER)
txt_x.configure(validate='key', validatecommand=vcmd_h)

txt_xj_h = ctk.CTkEntry(dist_hipergeometrica)
txt_xj_h.place(relx=0.65, rely=0.3, anchor = tk.CENTER)
txt_xj_h.configure(validate='key', validatecommand=vcmd_h)

#Se crean labels en la ventana para indicar los campos de k, n, N y x
lbl_k_h = ctk.CTkLabel(dist_hipergeometrica, text='k', bg_color= 'transparent')
lbl_k_h.place(relx=0.5, rely=0.15, anchor = tk.CENTER)

lbl_n_h = ctk.CTkLabel(dist_hipergeometrica, text='n', bg_color= 'transparent')
lbl_n_h.place(relx=0.35, rely=0.25, anchor = tk.CENTER)

lbl_N = ctk.CTkLabel(dist_hipergeometrica, text='N', bg_color= 'transparent')
lbl_N.place(relx=0.75, rely=0.15, anchor = tk.CENTER)

lbl_x = ctk.CTkLabel(dist_hipergeometrica, text='x', bg_color= 'transparent')
lbl_x.place(relx=0.25, rely=0.15, anchor = tk.CENTER)

lbl_xj_h = ctk.CTkLabel(dist_hipergeometrica, text='xj', bg_color= 'transparent')
lbl_xj_h.place(relx=0.65, rely=0.25, anchor = tk.CENTER)

#Se crea el boton para volver
btn_v_h = ctk.CTkButton(dist_hipergeometrica, text='Volver', command = press_v)
btn_v_h.place(relx=0.9, rely=0.9, anchor = tk.CENTER)

#Se crea el boton limpiar
btn_l_h = ctk.CTkButton(dist_hipergeometrica, text='Limpiar', command = press_l_h)
btn_l_h.place(relx=0.65, rely=0.4, anchor = tk.CENTER)

#Se crea el boton calcular
btn_c_h = ctk.CTkButton(dist_hipergeometrica, text='Calcular', command = press_ch)
btn_c_h.place(relx=0.35, rely=0.4, anchor = tk.CENTER)

#Se crean textbox en la ventana para mostrar los resultados
txt_r_XK_h = ctk.CTkEntry(dist_hipergeometrica)
txt_r_XK_h.place(relx=0.25, rely=0.65, anchor = tk.CENTER)
txt_r_XK_h.configure(state='readonly')

txt_r_XK_menor_h = ctk.CTkEntry(dist_hipergeometrica)
txt_r_XK_menor_h.place(relx=0.5, rely=0.65, anchor = tk.CENTER)
txt_r_XK_menor_h.configure(state='readonly')

txt_r_XK_mayor_h = ctk.CTkEntry(dist_hipergeometrica)
txt_r_XK_mayor_h.place(relx=0.75, rely=0.65, anchor = tk.CENTER)
txt_r_XK_mayor_h.configure(state='readonly')

txt_r_XK_menor_igual_h = ctk.CTkEntry(dist_hipergeometrica)
txt_r_XK_menor_igual_h.place(relx=0.25, rely=0.75, anchor = tk.CENTER)
txt_r_XK_menor_igual_h.configure(state='readonly')

txt_r_XK_mayor_igual_h = ctk.CTkEntry(dist_hipergeometrica)
txt_r_XK_mayor_igual_h.place(relx=0.5, rely=0.75, anchor = tk.CENTER)
txt_r_XK_mayor_igual_h.configure(state='readonly')

txt_r_Xi_Xj_h = ctk.CTkEntry(dist_hipergeometrica)
txt_r_Xi_Xj_h.place(relx=0.75, rely=0.75, anchor = tk.CENTER)
txt_r_Xi_Xj_h.configure(state='readonly')

txt_r_Xi_Xj_igual_h = ctk.CTkEntry(dist_hipergeometrica)
txt_r_Xi_Xj_igual_h.place(relx=0.5, rely=0.85, anchor = tk.CENTER)
txt_r_Xi_Xj_igual_h.configure(state='readonly')

#Se crean labels en la ventana para indicar los campos de los resultados
lbl_XK_h = ctk.CTkLabel(dist_hipergeometrica, text='P(X=k)', bg_color= 'transparent')
lbl_XK_h.place(relx=0.25, rely=0.6, anchor = tk.CENTER)

lbl_XK_menor_h = ctk.CTkLabel(dist_hipergeometrica, text='P(X<k)', bg_color= 'transparent')
lbl_XK_menor_h.place(relx=0.5, rely=0.6, anchor = tk.CENTER)

lbl_XK_mayor_h = ctk.CTkLabel(dist_hipergeometrica, text='P(X>k)', bg_color= 'transparent')
lbl_XK_mayor_h.place(relx=0.75, rely=0.6, anchor = tk.CENTER)

lbl_XK_menor_igual_h = ctk.CTkLabel(dist_hipergeometrica, text='P(X<=k)', bg_color= 'transparent')
lbl_XK_menor_igual_h.place(relx=0.25, rely=0.7, anchor = tk.CENTER)

lbl_XK_mayor_igual_h = ctk.CTkLabel(dist_hipergeometrica, text='P(X>=k)', bg_color= 'transparent')
lbl_XK_mayor_igual_h.place(relx=0.5, rely=0.7, anchor = tk.CENTER)

lbl_Xi_Xj_h = ctk.CTkLabel(dist_hipergeometrica, text='P(xi<X<xj)', bg_color= 'transparent')
lbl_Xi_Xj_h.place(relx=0.75, rely=0.7, anchor = tk.CENTER)

lbl_Xi_Xj_igual_h = ctk.CTkLabel(dist_hipergeometrica, text='P(xi<=X<=xj)', bg_color= 'transparent')
lbl_Xi_Xj_igual_h.place(relx=0.5, rely=0.8, anchor = tk.CENTER)

#Se crea la ventana de Distribución normal
dist_normal = ctk.CTk()
dist_normal.title("Distribucion Normal")
dist_normal.geometry('800x600')
dist_normal.resizable(False, False)
centrar_ventana(dist_normal, 800, 600)

#Se crea una función que se ejecuta al presionar el botón calcular
def press_cn():
    if txt_mu_n.get() == '':
        messagebox.showerror('Error', 'Ingrese un valor para mu')
    elif txt_sigma.get() == '':
        messagebox.showerror('Error', 'Ingrese un valor para sigma')
    elif txt_k_n.get() == '':
        messagebox.showerror('Error', 'Ingrese un valor para k')

    #Se obtienen los valores de los textbox
    mu = float(txt_mu_n.get())
    sigma = float(txt_sigma.get())
    k = float(txt_k_n.get())
    if txt_xj_n.get() != '':
        xj = float(txt_xj_n.get())
    xi = k
    
    # Distribución para P(X<=k)
    distribucion_normal_menor = stats.norm.cdf(k, mu, sigma)
    
    # Distribución para P(X>=k)
    distribucion_normal_mayor = 1 - stats.norm.cdf(k, mu, sigma)
    
    if txt_xj_n.get() != '':
        # Distribución para P(xi<X<xj)
        distribucion_normal_entre = stats.norm.cdf(xj, mu, sigma) - stats.norm.cdf(xi, mu, sigma)
    
    #Se muestran los resultados en los textbox
    txt_r_XK_menor_igual_n.configure(state='normal')
    txt_r_XK_menor_igual_n.delete(0, tk.END)
    txt_r_XK_menor_igual_n.insert(0, f'{distribucion_normal_menor:.4}')
    txt_r_XK_menor_igual_n.configure(state='readonly')
    
    txt_r_XK_mayor_igual_n.configure(state='normal')
    txt_r_XK_mayor_igual_n.delete(0, tk.END)
    txt_r_XK_mayor_igual_n.insert(0, f'{distribucion_normal_mayor:.4}')
    txt_r_XK_mayor_igual_n.configure(state='readonly')
    
    if txt_xj_n.get() != '':
        txt_r_Xi_Xj_n.configure(state='normal')
        txt_r_Xi_Xj_n.delete(0, tk.END)
        txt_r_Xi_Xj_n.insert(0, f'{distribucion_normal_entre:.4}')
        txt_r_Xi_Xj_n.configure(state='readonly')
    else:
        txt_r_Xi_Xj_n.configure(state='normal')
        txt_r_Xi_Xj_n.delete(0, tk.END)
        txt_r_Xi_Xj_n.insert(0, 'No ingresado')
        txt_r_Xi_Xj_n.configure(state='readonly')

vcmd_n = (dist_normal.register(validar_num), '%d', '%P')

#Se crean los txtbox para ingresar los valores de mu, sigma, k y x_j
txt_mu_n = ctk.CTkEntry(dist_normal)
txt_mu_n.place(relx=0.25, rely=0.2, anchor = tk.CENTER)
txt_mu_n.configure(validate='key', validatecommand=vcmd_n)

txt_sigma = ctk.CTkEntry(dist_normal)
txt_sigma.place(relx=0.5, rely=0.2, anchor = tk.CENTER)
txt_sigma.configure(validate='key', validatecommand=vcmd_n)

txt_k_n = ctk.CTkEntry(dist_normal)
txt_k_n.place(relx=0.75, rely=0.2, anchor = tk.CENTER)
txt_k_n.configure(validate='key', validatecommand=vcmd_n)

txt_xj_n = ctk.CTkEntry(dist_normal)
txt_xj_n.place(relx=0.5, rely=0.3, anchor = tk.CENTER)
txt_xj_n.configure(validate='key', validatecommand=vcmd_n)

#Se crean los labels en la ventana para indicar los campos de mu, sigma, k y x_j
lbl_mu_n = ctk.CTkLabel(dist_normal, text='mu', bg_color= 'transparent')
lbl_mu_n.place(relx=0.25, rely=0.15, anchor = tk.CENTER)

lbl_sigma = ctk.CTkLabel(dist_normal, text='sigma', bg_color= 'transparent')
lbl_sigma.place(relx=0.5, rely=0.15, anchor = tk.CENTER)

lbl_k_n = ctk.CTkLabel(dist_normal, text='k', bg_color= 'transparent')
lbl_k_n.place(relx=0.75, rely=0.15, anchor = tk.CENTER)

lbl_xj_n = ctk.CTkLabel(dist_normal, text='xj', bg_color= 'transparent')
lbl_xj_n.place(relx=0.5, rely=0.25, anchor = tk.CENTER)

#Se crea el boton volver
btn_v_n = ctk.CTkButton(dist_normal, text='Volver', command = press_v)
btn_v_n.place(relx=0.9, rely=0.9, anchor = tk.CENTER)

#Se crea el boton limpiar
btn_l_n = ctk.CTkButton(dist_normal, text='Limpiar', command = press_l_n)
btn_l_n.place(relx=0.65, rely=0.4, anchor = tk.CENTER)

#Se crea el boton calcular
btn_c_n = ctk.CTkButton(dist_normal, text='Calcular', command = press_cn)
btn_c_n.place(relx=0.35, rely=0.4, anchor = tk.CENTER)

#Se crea el label de titulo en la ventana
lbl_titulo_normal = ctk.CTkLabel(dist_normal, text='Distribucion Normal', bg_color= 'transparent', font=('Arial', 20))
lbl_titulo_normal.place(relx=0.5, rely=0.05, anchor = tk.CENTER)

#Se crea el label de resultados en la ventana
lbl_resultados_n = ctk.CTkLabel(dist_normal, text='Resultados', bg_color= 'transparent', font=('Arial', 20))
lbl_resultados_n.place(relx=0.5, rely=0.5, anchor = tk.CENTER)

#Se crean textbox en la ventana para mostrar los resultados

txt_r_XK_menor_igual_n = ctk.CTkEntry(dist_normal)
txt_r_XK_menor_igual_n.place(relx=0.25, rely=0.65, anchor = tk.CENTER)
txt_r_XK_menor_igual_n.configure(state='readonly')

txt_r_XK_mayor_igual_n = ctk.CTkEntry(dist_normal)
txt_r_XK_mayor_igual_n.place(relx=0.5, rely=0.65, anchor = tk.CENTER)
txt_r_XK_mayor_igual_n.configure(state='readonly')

txt_r_Xi_Xj_n = ctk.CTkEntry(dist_normal)
txt_r_Xi_Xj_n.place(relx=0.75, rely=0.65, anchor = tk.CENTER)
txt_r_Xi_Xj_n.configure(state='readonly')

#Se crean labels en la ventana para indicar los campos de los resultados
lbl_XK_menor_igual_n = ctk.CTkLabel(dist_normal, text='P(X<=k)', bg_color= 'transparent')
lbl_XK_menor_igual_n.place(relx=0.25, rely=0.6, anchor = tk.CENTER)

lbl_XK_mayor_igual_n = ctk.CTkLabel(dist_normal, text='P(X>=k)', bg_color= 'transparent')
lbl_XK_mayor_igual_n.place(relx=0.5, rely=0.6, anchor = tk.CENTER)

lbl_Xi_Xj_n = ctk.CTkLabel(dist_normal, text='P(xi<X<xj)', bg_color= 'transparent')
lbl_Xi_Xj_n.place(relx=0.75, rely=0.6, anchor = tk.CENTER)

#Se muestra la ventana
inicio.mainloop()