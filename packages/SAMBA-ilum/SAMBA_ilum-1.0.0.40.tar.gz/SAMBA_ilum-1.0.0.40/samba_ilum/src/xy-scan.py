# SAMBA_ilum Copyright (C) 2024 - Closed source


import numpy as np
import shutil
import os


"""
INSERIR FUNÇÃO PARA VERIFICAR SE O ARQUIVO POSCAR INICIAL ESTA ESCRITO EM COORDENADAS DIRETAS OU CARTESIANAS
SE ESTIVER ESCRITO EM COORDENADAS DIRETAS, CONVERTER PARA COORDENADAS CARTESIANAS
TALVEZ CRIAR UMA FUNÇÃO COM ESTE PROPOSITO SEJA PRATICO PARA O CODIGO TODO 
"""


# Atenção: ================================================================
# O código foi escrito pensado em uma Heteroestrutura com n_Lattice = 2 ===
# Para redes com n_Lattice > 2 testes e generalizações devem ser feitas === 
#==========================================================================

# Deslocamentos a ser aplicado no 2º material, referente ao vetor A1 da rede
displacement_A1 = replace_displacement_A1

# Deslocamentos a ser aplicado no 2º material, referente ao vetor A2 da rede    
displacement_A2 = replace_displacement_A2


"""
#----------------------------------------------------------------
# Testando a compatibilidade do arquivo POSCAR ------------------
#----------------------------------------------------------------
poscar = open('POSCAR', "r")
VTemp = poscar.readline().split()
poscar.close()
#-------------
crit = 0
for k in range(len(VTemp)):
    try:
       inteiro = int(VTemp[k])
       if (k > 0 and k < 3): crit += 1
    except ValueError:
       if (k == 0):  crit += 1
    #------------------------------
    if (len(VTemp) < 3 or crit < 3):
       print(f' ')
       print(f'========================================')
       print(f'Verifique o arquivo POSCAR utilizado!   ')
       print(f'INCOMPATIBILIDADE com o código detectada')
       print(f'========================================')
       print(f' ')
       #==========
       sys.exit()   
       #=========
"""


#----------------------------------------------------------------------------
# Função para listar todas as pastas dentro de um dado diretório ------------
#----------------------------------------------------------------------------
def list_folders(dir):
   l_folders = [name for name in os.listdir(dir) if os.path.isdir(os.path.join(dir, name))]
   return l_folders


#----------------
dir = os.getcwd()
#--------------------------
folders = list_folders(dir)
#---------------------------------------------------------
for i in range(len(folders)):  shutil.rmtree('folders[i]')
#--------------------------------------------------------------------
# if os.path.isfile('energy_scan.txt'):  os.remove('energy_scan.txt')


#==========================================================================
# Obtendo os vetores de rede da Heteroestrutura ===========================
#==========================================================================
poscar = open('POSCAR', "r")
#---------------------------
VTemp = poscar.readline()
VTemp = poscar.readline();  param = float(VTemp)
VTemp = poscar.readline().split();  A1x = float(VTemp[0])*param;  A1y = float(VTemp[1])*param;  A1z = float(VTemp[2])*param
VTemp = poscar.readline().split();  A2x = float(VTemp[0])*param;  A2y = float(VTemp[1])*param;  A2z = float(VTemp[2])*param
VTemp = poscar.readline().split();  A3x = float(VTemp[0])*param;  A3y = float(VTemp[1])*param;  A3z = float(VTemp[2])*param
#-------------
poscar.close()
#-------------


#==========================================================================
# Gerando e Armazenando os arquivos POSCAR deslocados no plano ============
#==========================================================================
os.mkdir('POSCAR_temp_cart')
#---------
number = 0
#---------
for ii in displacement_A1:
    for jj in displacement_A2:
        #-----------------------------------
        displacement_X = (ii*A1x) + (jj*A2x)        
        displacement_Y = (ii*A1y) + (jj*A2y)   
        #-----------------------------------
        number += 1
        #---------------------------
        poscar = open('POSCAR', "r")
        poscar_new = open('POSCAR_temp_cart/POSCAR_' + str(number), "w") 
        #---------------------------------------------------------------------------
        VTemp = poscar.readline()
        poscar_new.write(f'{VTemp}')
        VTemp = VTemp.split()
        nions1 = int(VTemp[2]);  nions2 = int(VTemp[3])
        #----------------------------------------------
        for k in range(7 + nions1):
            VTemp = poscar.readline()
            poscar_new.write(f'{VTemp}')
        #-------------------------------
        for k in range(nions2):
            VTemp = poscar.readline().split()
            poscar_new.write(f'{float(VTemp[0]) + displacement_X} {float(VTemp[1]) + displacement_Y} {VTemp[2]} \n')
        #-----------------------------------------------------------------------------------------------------------
        poscar.close()
        poscar_new.close()
        #-----------------


#=============================================================================
# Convertendo as coordenadas dos arquivos POSCAR de cartesiano para direto ===
#=============================================================================

#---------
number = 0
#----------
a = np.array([A1x, A1y, A1z])
b = np.array([A2x, A2y, A2z])
c = np.array([A3x, A3y, A3z])
T = np.linalg.inv(np.array([a, b, c]).T)  # Definindo a matriz de transformação
#------------------------------------------------------------------------------

for ii in displacement_A1:
    for jj in displacement_A2: 
        #----------
        number += 1
        #---------------------------------
        dir_temp = str(ii) + '_' + str(jj)
        os.mkdir(dir_temp)
        shutil.copyfile('contcar_update.py', dir_temp + '/contcar_update.py')
        shutil.copyfile('energy_scan.py', dir_temp + '/energy_scan.py')
        shutil.copyfile('KPOINTS', dir_temp + '/KPOINTS')
        shutil.copyfile('POTCAR', dir_temp + '/POTCAR')
        shutil.copyfile('INCAR', dir_temp + '/INCAR')
        #-----------------------------------------------------------
        poscar = open('POSCAR_temp_cart/POSCAR_' + str(number), "r")
        poscar_new = open(dir_temp + '/POSCAR', "w") 
        #-------------------------------------------
        for k in range(7):
            VTemp = poscar.readline()
            poscar_new.write(f'{VTemp}')
        #------------------------
        VTemp = poscar.readline()
        poscar_new.write(f'Direct \n')

        #----------------------------------------------------------------------------------------------------
        # Convertendo as posições atomicas cartesianas de todos os átomos da Supercélula para a forma direta,
        # e ajustando as posições dos átomos que se encontram fora da célula.
        #--------------------------------------------------------------------
        for k in range(nions1 + nions2):
            VTemp = poscar.readline().split()
            x = float(VTemp[0])
            y = float(VTemp[1])
            z = float(VTemp[2])    
            #----------------------
            r = np.array([x, y, z])        # Definindo o vetor posição cartesiano do átomo  
            #----------------------           
            f = np.dot(T, r)               # Calculando a correspondenre posição em coordenadas fracionárias
            for m in range(3):
                f = np.where(f < 0, f + 1, f)
                f = np.where(f > 1, f - 1, f)
            #-------------------------------- 
            for m in range(3):
                f[m] = round(f[m], 6)
                if (f[m] > 0.9999 or f[m] < 0.0001):
                   f[m] = 0.0
            poscar_new.write(f'{f[0]} {f[1]} {f[2]} \n')

        #-------------
        poscar.close()
        poscar_new.close()
        #-----------------


# os.remove('POSCAR')
# os.remove('KPOINTS')
# os.remove('POTCAR')
# os.remove('INCAR')

shutil.rmtree('POSCAR_temp_cart')
