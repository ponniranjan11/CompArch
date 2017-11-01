# Creating 64 KB memoryview
import numpy as np
memory = np.zeros([65536],dtype=np.dtype ((str,8)))


reg = np.zeros([8],dtype=np.dtype((int)))

bit=16
SET = 1
RESET = 0
Flags= {'N':0,'Z':0,'V':0,'C':0}
# Assighing Registers
# Assuming they dont reside onto memory 
global PC
def octal2bin (number):
    decimal = int(number, 8)
    return (dec2bin (decimal))
    
def dec2bin (number):
   x = format (number, '016b')
   return (x)

def octal2dec (number):
    decimal = int (number, 8)
    return (decimal)
def bin2dec (number):
    dec = int (number ,2)
    if (dec > 32767):
            dec = dec - 65536
    return (dec)

# Reading the ascii file 
def file_read (str):
        global temp
        global l
        global Total
        Total = 0
        with open(str,'r') as test2:
                l = test2.read()
                temp = l.splitlines() 
        for line in temp:
                print(line)
                Total += 1
                

file_read("OPsource.ascii")	
	  
#defining functions 	  
def putmem(AC,data):
        global memory
        memory[AC]=data[0:8]
        memory[AC+1]=data[8:16]
        #AC_octal=dec2octal
        with open('test1.txt','a') as f:
                f.write("1 %s \n"%oct(AC))

                
        

def getmem(data,AC):
        a = memory[AC]
        b = memory[AC+1]
        data=bin2dec(a+b)
        with open('test1.txt','a') as f:
                f.write("0 %s \n"%oct(AC))
        return(data)
        
	
                
def setir(PC):
        global IR
        IR_low=memory[PC]
        IR_high=memory[PC+1]
        IR=IR_low + IR_high
        print("IR is %s"%IR)
        with open('test1.txt','a') as f:
                f.write("2 %s \n"%oct(PC))
        return(IR)
                
        
	
def makefile ():
        with open('test1.txt', 'w') as f:
                pass

makefile()



	


def start():
        x=0
        global PC
        for a in range(0 , Total):
                #if (temp[a][0] == '@'):
                 #       print("WOOOOW")
                  #      PC=octal2dec(temp[a][1:7])
                if(temp[a][0] == '*'):
                        x=1
                        #a = input("starting address=")
                        PC_t = temp[a]
                #elif(temp[a][0] == '-'):
                      #  print("Yes")
        if(x == 1):
                PC=octal2dec(PC_t[1:7])
        else:
                b = input("starting address=")
                PC=octal2dec(b[0:6])
        print(PC)  
   


def load ():
	global data
	#global PC
	global PC_temp
	#PC = 0
	PC_temp=0
	for a in range(0 , Total):
		if (temp[a][0] == '@'):
			PC_temp=octal2dec(temp[a][1:7])
	
		
		
		
		#elif (temp[a][0] == '*'):
			#PC=octal2dec(temp[a][1:7])
			
	
	
	
		elif (temp[a][0]== '-'):
			#PC=PC
			data=octal2bin(temp[a][1:7])
			putmem(PC_temp,data)
			PC_temp +=2
			#PC += 2
			#setir(PC)
			
load()
start()		


#Selection of instruction type 
def inst_select(inst):
        global opcode
        global mode1
        global REG1
        global mode2
        global REG2
        if (inst[0:5] == '00001'):
                print("It is single_op")
                single_op(inst)
        elif(inst[0:10] == '0000000011'):
                print("It is Swab inst")
                swab(inst)
        elif(inst[0:7] == '0000100'):
                print("It is JSR inst")
                JSR(inst)
        elif(inst == '0000000000000000'):
                print("It is halt inst")
                halt(inst)
        elif(inst[1:5] == '0000'):
                print("It is cond branc inst")
                cond_bran(inst)
        else: print("It is double_op")
        double_op(inst)
#Selection of instruction type 

#single-operand instruction calling for execution 
def single_op(inst):
        if((inst[0:4] == '0000') and (inst[4:10] == '101000')):
           print("It is CLR")     
           mode1=inst[10:13]
           REG1=bin2dec(inst[13:16])
           opcode=inst[0:10]
           CLR(mode1,REG1)
        elif((inst[0:4] == '0000') and (inst[4:10] == '101001')):
           print("It is COM")     
           mode1=inst[10:13]
           REG1=bin2dec(inst[13:16])
           opcode=inst[0:10]
           COM(mode1,REG1)
        elif((inst[0:4] == '0000') and (inst[4:10] == '101010')):
           print("It is INC")     
           mode1=inst[10:13]
           REG1=bin2dec(inst[13:16])
           opcode=inst[0:10]
           INC(mode1,REG1)
        elif((inst[0:4] == '0000') and (inst[4:10] == '101011')):
           print("It is DEC")     
           mode1=inst[10:13]
           REG1=bin2dec(inst[13:16])
           opcode=inst[0:10]
           DEC(mode1,REG1)
        elif((inst[0:4] == '0000') and (inst[4:10] == '101100')):
           print("It is NEG")     
           mode1=inst[10:13]
           REG1=bin2dec(inst[13:16])
           opcode=inst[0:10]
           NEG(mode1,REG1)
        elif((inst[0:4] == '0000') and (inst[4:10] == '101101')):
           print("It is ADC")     
           mode1=inst[10:13]
           REG1=bin2dec(inst[13:16])
           opcode=inst[0:10]
           ADC(mode1,REG1)
        elif((inst[0:4] == '0000') and (inst[4:10] == '101110')):
           print("It is SBC")     
           mode1=inst[10:13]
           REG1=bin2dec(inst[13:16])
           opcode=inst[0:10]
           SBC(mode1,REG1)
        elif((inst[0:4] == '0000') and (inst[4:10] == '101111')):
           print("It is TST")     
           mode1=inst[10:13]
           REG1=bin2dec(inst[13:16])
           opcode=inst[0:10]
           TST(mode1,REG1)
        elif((inst[0:4] == '0000') and (inst[4:10] == '110000')):
           print("It is ROR")     
           mode1=inst[10:13]
           REG1=bin2dec(inst[13:16])
           opcode=inst[0:10]
           ROR(mode1,REG1)
        elif((inst[0:4] == '0000') and (inst[4:10] == '110001')):
           print("It is ROL")     
           mode1=inst[10:13]
           REG1=bin2dec(inst[13:16])
           opcode=inst[0:10]
           ROL(mode1,REG1)
        elif((inst[0:4] == '0000') and (inst[4:10] == '110010')):
           print("It is ASR")     
           mode1=inst[10:13]
           REG1=bin2dec(inst[13:16])
           opcode=inst[0:10]
           ASR(mode1,REG1)
        elif((inst[0:4] == '0000') and (inst[4:10] == '110011')):
           print("It is ASL")     
           mode1=inst[10:13]
           REG1=bin2dec(inst[13:16])
           opcode=inst[0:10]
           ASL(mode1,REG1)
#single-operand instruction calling for execution 


#double-operand instruction calling for execution         
def double_op(inst):
        if(inst[1:4] =='001'):
                print("It is MOV")
                opcode=inst[0:4]
                mode1=inst[4:7]
                REG1=bin2dec(inst[7:10])
                mode2=inst[10:13]
                REG2=bin2dec(inst[13:16])
                MOV(mode1,REG1,mode2,REG2)
        elif(inst[1:4] == '010'):
                print("It is CMP")
                opcode=inst[0:4]
                mode1=inst[4:7]
                REG1=bin2dec(inst[7:10])
                mode2=inst[10:13]
                REG2=bin2dec(inst[13:16])
                CMP(mode1,REG1,mode2,REG2)
        elif(inst[1:4] =='011'):
                print("It is BIT")
                opcode=inst[0:4]
                mode1=inst[4:7]
                REG1=bin2dec(inst[7:10])
                mode2=inst[10:13]
                REG2=bin2dec(inst[13:16])
                BIT(mode1,REG1,mode2,REG2)
        elif(inst[1:4] == '100'):
                print("It is BIC")
                opcode=inst[0:4]
                mode1=inst[4:7]
                REG1=bin2dec(inst[7:10])
                mode2=inst[10:13]
                REG2=bin2dec(inst[13:16])
                BIC(mode1,REG1,mode2,REG2)
        elif(inst[1:4] =='101'):
                print("It is BIS")
                opcode=inst[0:4]
                mode1=inst[4:7]
                REG1=bin2dec(inst[7:10])
                mode2=inst[10:13]
                REG2=bin2dec(inst[13:16])
                BIS(mode1,REG1,mode2,REG2)
        elif(inst[0:4] =='0110'):
                print("It is ADD")
                opcode=inst[0:4]
                mode1=inst[4:7]
                REG1=bin2dec(inst[7:10])
                mode2=inst[10:13]
                REG2=bin2dec(inst[13:16])
                ADD(mode1,REG1,mode2,REG2)
        elif(inst[0:4] =='1110'):
                print("It is SUB")
                opcode=inst[0:4]
                mode1=inst[4:7]
                REG1=bin2dec(inst[7:10])
                mode2=inst[10:13]
                REG2=bin2dec(inst[13:16])
                SUB(mode1,REG1,mode2,REG2)
#double-operand instruction calling for execution
                
#Jump instruction calling for execution         
def cond_bran(inst):
        if((inst[0:5] == "00000") and (inst[5:8] == '001')):
                print("It is BR")
                opcode=inst[0:8]
                offset=bin2dec(inst[8:16])
                BR(offset)

        elif((inst[0:5] == "00000") and (inst[5:8] == '010')):
                print("It is BNE")
                opcode=inst[0:8]
                offset=bin2dec(inst[8:16])
                BNE(offset)
        elif((inst[0:5] == "00000") and (inst[5:8] == '011')):
                print("It is BEQ")
                opcode=inst[0:8]
                offset=bin2dec(inst[8:16])
                BEQ(offset)
        elif((inst[0:5] == "00000") and (inst[5:8] == '100')):
                print("It is BGE")
                opcode=inst[0:8]
                offset=bin2dec(inst[8:16])
                BGE(offset)
        elif((inst[0:5] == "00000") and (inst[5:8] == '101')):
                print("It is BLT")
                opcode=inst[0:8]
                offset=bin2dec(inst[8:16])
                BLT(offset)
        elif((inst[0:5] == "00000") and (inst[5:8] == '110')):
                print("It is BGT")
                opcode=inst[0:8]
                offset=bin2dec(inst[8:16])
                BGT(offset)
        elif((inst[0:5] == "00000") and (inst[5:8] == '111')):
                print("It is BLE")
                opcode=inst[0:8]
                offset=bin2dec(inst[8:16])
                BLE(offset)
        elif((inst[0:5] == "10000") and (inst[5:8] == '000')):
                print("It is BPL")
                opcode=inst[0:8]
                offset=bin2dec(inst[8:16])
                BPL(offset)
        elif((inst[0:5] == "10000") and (inst[5:8] == '001')):
                print("It is BMI")
                opcode=inst[0:8]
                offset=bin2dec(inst[8:16])
                BMI(offset)
        elif((inst[0:5] == "10000") and (inst[5:8] == '010')):
                print("It is BHI")
                opcode=inst[0:8]
                offset=bin2dec(inst[8:16])
                BHI(offset)
        elif((inst[0:5] == "10000") and (inst[5:8] == '011')):
                print("It is BLOS")
                opcode=inst[0:8]
                offset=bin2dec(inst[8:16])
                BLOS(offset)
        elif((inst[0:5] == "10000") and (inst[5:8] == '100')):
                print("It is BVC")
                opcode=inst[0:8]
                offset=bin2dec(inst[8:16])
                BVC(offset)
        elif((inst[0:5] == "10000") and (inst[5:8] == '101')):
                print("It is BVS")
                opcode=inst[0:8]
                offset=bin2dec(inst[8:16])
                BVS(offset)
#Jump instruction calling for execution         
def swab(inst):
        print("swab")
        x = fetch_oprand(mode1,REG1)
        print(x)
        d = dec2bin(x)
        s = d[0:8]
        g = d[8:16]
        f = s + g
        store_oprand(f,REG1,mode1)
def jummp(inst):
        print("jump")
        
def halt(inst):
        print("halt")
        
# Specifing all Single-op instrucions 
def CLR(mode1,REG1):
              print("exe_CLR")

              x= fetch_oprand(mode1,REG1)
              print(x)
              x = 0
              print(x)
              listvalues[0] = 0;
              listvalues[1] = 1;
              listvalues[2] = 0;
              listvalues[3] = 0;
              print (listflags)
              print (listvalues)
                        
              store_oprand(x, REG1, mode1)
def COM(mode1,REG1):
              print("exe_COM")
              x= fetch_oprand(mode1,REG1)
              print (x)
              x = ~x
              if x < 0:
                      listvalues[0]=1;
              else:
                      listvalues[0]=0;
              if x == 0:
                      listvalues[1]=1;
              else:
                      listvalues[1]=0;
              listvalues[2]=0;
              listvalues[3]=1;
              print (listflags)
              print (listvalues)
                      
              store_oprand(x, REG1,mode1)
def INC(mode1,REG1):
        x= fetch_oprand(mode1,REG1)
        print(x)
        if x == 32767:
                      x = 32767
                      listvalues[2]=1;
        else:
                      listvalues[2]=0;
                      x = x + 1
                
        print(x)
        if x < 0:
                      listvalues[0]=1;
        else:
                      listvalues[0]=0;
        if x == 0:
                      listvalues[1]=1;
        else:
                      listvalues[1]=0;
        print (listflags)
        print (listvalues)
        store_oprand(x, REG1, mode1)
                      
def DEC(mode1,REG1):
              print("exe_DEC")
              x,add= fetch_oprand(mode1,REG1)
              print ("Operand = %s"%x)  
              if x == -32768:
                      Flags['V'] = SET
              else:
                      Flags['V'] = RESET

              x = x -1
              if (x < -32768):
                      x = x + 65536
              print("Result DEC = %x"%x)
              if x < 0:
                      Flags['N'] = SET
              else:
                      Flags['N'] = RESET
              if x == 0:
                      Flags['Z'] = SET
              else:
                      Flags['Z'] = RESET
              print (Flags)
              a = dec2bin(x)
              putmem(add,a)
              #store_oprand(x,REG1,mode1)
                      
def NEG(mode1,REG1):
    
              print("exe_NEG")
              x = fetch_oprand(mode1,REG1)
              print(x)
              y = neg(x,16)
              if y < 0:
                      listvalues[0]=1;
              else:
                      listvalues[0]=0;
              if y == 0:
                      listvalues[1]=1;
                      listvalues[3]=0;
              else:
                      listvalues[1]=0;
                      listvalues[3]=1;
              if y == -32767:
                      listvalues[2]=1;
              else:
                      listvalues[2]=0;
              print (listflags)
              print (listvalues)
              store_oprand(y,REG1,mode1)
              
def ADC(mode1,REG1):
              print("exe_ADC")
              x = fetch_oprand(mode1,REG1)
              if x<0:
                      x = twos_comp(x,bit)
                      if x > 32767:
                              x = x - 65536  
              x = x + listvalues[3]
              if x<0:
                      listvalues[0]=1;
              else:
                      listvalues[0]=0;
              if x ==0:
                      listvalues[1]=1;
              else:
                      listvalues[1]=0;
              if x >32767:
                      listvalues[2]=1;
              else:
                      listvalues[2]=0;
              print (listflags)
              print (listvalues)
              store_oprand(x,REG1,mode1)
def SBC(mode1,REG1):
              print("exe_SBC")
              x = fetch_oprand(mode1,REG1)
              if x<0:
                      x = twos_comp(x,bit)
                      if x > 32767:
                              x = x - 65536
              x = x - listvalues[3]
              if x<0:
                      listvalues[0] = 1;
              else:
                      listvalues[0] = 0;
              if x == 0:
                      listvalues[1] = 1;
              else:
                      listvalues[1] = 0;
              if x < -32767:
                      listvalues[2] = 1;
              else:
                      listvalues[2] = 0;
              print (listflags)
              print (listvalues)
              store_oprand(x,REG1,mode1)
                
def TST(mode1,REG1):
              print("exe_TST")
              x = fetch_oprand(mode1,REG1)
              if x < 0:
                      listvalues[0]=1;
              else:
                      listvalues[0]=0;
              if x == 0:
                      listvalues[1]=1;
              else:
                      listvalues[1]=0;
              listvalues[2]=0;
              listvalues[3]=0;
              print (listflags)
              print (listvalues)
def ROR(mode1,REG1):
              print("exe_ROR")
              x = fetch_oprand(mode1,REG1)
              ror = lambda val, r_bits, max_bits: \
                    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
                    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))
              a = "%x" % ror(x,1,16)
              a = int(a,16)
              if a > 32767:
                      a = a - 65536
              print(a)
              if a < 0:
                      listvalues[0]=1;
              else:
                      listvalues[0]=0;
              if a == 0:
                      listvalues[1]=1;
              else:
                      listvalues[1]=0;
              print (listflags)
              print (listvalues)
              store_oprand(a,REG1,mode1)
def ROL(mode1,REG1):
              print("exe_ROL")
              x = fetch_oprand(mode1,REG1)
              rol = lambda val, r_bits, max_bits: \
                    (val << r_bits%max_bits) & (2**max_bits-1) | \
                    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
              a = "%x" % rol(x,1,16)
              a = int(a,16)
              if a > 32767:
                      a = a - 65536
              print(a)
              if a < 0:
                      listvalues[0]=1;
              else:
                      listvalues[0]=0;
              if a == 0:
                      listvalues[1]=1;
              else:
                      listvalues[1]=0;
              print (listflags)
              print (listvalues)
              store_oprand(a,REG1,mode1)
              
def ASR(mode1,REG1):
              print("exe_ASR")
              x = fetch_oprand(mode1,REG1)
              str = dec2bin(x)
              str = x >> 1
              if str > 32767:
                      listvalues[0]=1;
                      str = str - 65536
              else:
                      listvalues[0]=0;
              if str == 0:
                      listvalues[1]=1;
              else:
                      listvalues[1]=0;
                
              print (listflags)
              print (listvalues)
              store_oprand(str,REG1,mode1)
def ASL(mode1,REG1):
              print("exe_ASL")
              x = fetch_oprand(mode1,REG1)
              str = dec2bin(x)
              str = x << 1
              if str > 32767:
                      listvalues[0]=1;
                      str = str - 65536
              else:
                      listvalues[0]=0;
              if str == 0:
                      listvalues[1]=1;
              else:
                      listvalues[1]=0;
                      
              print (listflags)
              print (listvalues)
              store_oprand(str,REG1,mode1)
# Specifing all Single-op instrucions 

# Specifing all Double-op instrucions 
def MOV(mode1,REG1,mode2,REG2):# Done with flags 
              print("exe_MOV")
              x,add = fetch_oprand(mode1,REG1)
              print("first operand = %s"%x)  
              y,add = fetch_oprand(mode2,REG2)
              print("second operand = %s"%y)
              y = x
              #print("Result = %s"%y)
              Flags['V'] = RESET
              if (x<0):
                      Flags['N'] = SET
              else:
                      Flags['N'] = RESET
              if(x==0):
                      Flags['Z'] = SET
              else:
                      Flags['Z'] = RESET
              print(Flags)
              b =dec2bin(y)
              putmem(add,b)
              #store_oprand(y,REG2,mode2)
def CMP(mode1,REG1,mode2,REG2):
              print("exe_CMP")
              x,add = fetch_oprand(mode1,REG1)
              print("first op = %s"%x)
              y,add = fetch_oprand(mode2,REG2)
              print("second op = %s"%y)
              a = x - y
              print("result = %s"%a)
              if a<0:
                      Flags['N'] = SET
              else:
                      Flags['N'] = RESET
              if(a==0):
                      Flags['Z'] = SET
              else:
                      Flags['Z'] = RESET
              #a_bin= dec2bin(a)  
              Flags['C']= (~(a & 65536)) 
              print(Flags)
                      
              
def BIT(mode1,REG1,mode2,REG2):
              print("exe_BIT")
              x = fetch_oprand(mode1,REG1)
              if (x < 0):
                      x = twos_comp(x,bit)
              y = fetch_oprand(mode2,REG2)
              

              if (y < 0):
                      y = twos_comp(y,bit)
                      
              a = x & y
              if a > 32767:
                      listvalues[0]=1;
              else:
                      listvalues[0]=0;
              if a == 0:
                      listvalues[1]=1;
              else:
                      listvalues[1]=0;
              listvalues[2]=0;
              print (listflags)
              print (listvalues)
              
              store_oprand(a,REG1,mode1)
def BIC(mode1,REG1,mode2,REG2):
              print("exe_BIC")
              x = fetch_oprand(mode1,REG1)
              y = fetch_oprand(mode2,REG2)
              if y<0:
                      y = twos_comp(y,bit)
              x = ~x
              if x<0:
                      x = twos_comp(x,bit)
              y = x & y
              if y > 32767:
                      listvalues[0]=1;
              else:
                      listvalues[0]=0;
              if y == 0:
                      listvalues[1]=1;
              else:
                      listvalues[1]=0;
              listvalues[2]=0;
              print (listflags)
              print (listvalues)
                
              store_oprand(y,mode2,REG2)
def BIS(mode1,REG1,mode2,REG2):
              print("exe_BIS")
              x = fetch_oprand(mode1,REG1)
              if x < 0:
                      x = twos_comp(x,bit)
              y = fetch_oprand(mode2,REG2)
              if y < 0:
                      y = twos_comp(y,bit)
              y = x|y
              if y > 32767:
                      listvalues[0]=1;
              else:
                      listvalues[0]=0;
              if y == 0:
                      listvalues[1]=1;
              else:
                      listvalues[1]=0;
              listvalues[2]=0
              print (listflags)
              print (listvalues)
              store_oprand(y,mode2,REG2)
def ADD(mode1,REG1,mode2,REG2):
              print("exe_ADD")
              a,add = fetch_oprand(mode1,REG1)
              print("first operand %s"%a)
              
              b,add = fetch_oprand(mode2,REG2)
              print("second operand %s"%b)
              print(b)
              
              b = a + b
              if a<0:
                      Flags['N'] = SET
              else:
                      Flags['N'] = RESET
              if(a==0):
                      Flags['Z'] = SET
              else:
                      Flags['Z'] = RESET
              Flags['C'] = ~(b & 65536)  
              c=dec2bin(b)
              print("RESULT ADD =%s"%b)
              
              putmem(add,c)
              #store_oprand(b,REG2,mode2)
         
              
def SUB(mode1,REG1,mode2,REG2):
              print("exe_SUB")
              a = fetch_oprand(mode1,REG1)
              print(a)
              if a < 0:
                      a = twos_comp(a,bit)
                      if a > 32767:
                              a = a - 65536
              b = fetch_oprand(mode2,REG2)
              print(b)
              if b < 0:
                      b = twos_comp(b,bit)
                      if b > 32767:
                              b = b - 65536
                      
              b = b - a
              if b < -32767:
                      b = -32767
              if b < 0:
                      listvalues[0]=1;
              else:
                      listvalues[0]=0;
              if b == 0:
                      listvalues[1]=1;
              else:
                      listvalues[1]=0;

              print(b)
              print (listflags)
              print (listvalues)
              store_oprand(b,REG2,mode2)
# Specifing all Doube-op instrucions

# Specifing all Jump instrucions
def BR(offset):
        global PC
        print("exe_BR")
        print("offset= %s"%offset)
        if(offset>127):
                offset = offset - 256
        PC = PC + (2*offset)
        print("New PC value = %s"%PC)
def BNE(offset):
        global PC
        print("exe_BNE")
        if listvalues[1]==0:
                PC = PC + (2*offset)
                print(PC)
        else:
                PC = PC
                print(PC)
def BEQ(offset):
        global PC
        print("exe_BEQ")
        if listvalues[1] == 1:
                PC = PC + (2*offset)
                print(PC)
        else:
                PC = PC
                print(PC)
def BGE(offset):
        global PC
        print("exe_BGE")
        if listvalues[0] == listvalues[2]:
                PC = PC + (2*offset)
                print(PC)
        else:
                PC = PC
                print(PC)
        
def BLT(offset):
        global PC
        print("exe_BLT")
        if listvalues[0]^listvalues[2]:
                PC = PC + (2*offset)
                print(PC)
        else:
                PC = PC
                print(PC)
def BGT(offset):
        global PC
        print("exe_BGT")
        if listvalues[0] == listvalues[2]:
                PC = PC + (2*offset)
                print(PC)
        else:
                PC = PC
                print(PC)
def BLE(offset):
        global PC
        print("exe_BLE")
        if (Flags['Z'] | (Flags['N']^Flags['V'])):
                if(offset>127):
                        offset = offset - 256
                PC = PC + (2*offset)
                print("New PC = %s"%PC)
        else:
                PC = PC
                print(PC)
def BPL(offset):
        global PC
        print("exe_BPL")
        if listvalues[0] == 0:
                PC = PC + (2*offset)
                print(PC)
        else:
                PC = PC
                print(PC)
def BMI(offset):
        global PC
        print("exe_BMI")
        if listvalues[0] == 1:
                PC = PC + (2*offset)
                print(PC)
        else:
                PC = PC
                print(PC)
def BHI(offset):
        global PC
        print("exe_BHI")
        if listvalues[1] == 0:
                if listvalues[3] == 0:
                        PC = PC + (2*offset)
                        print(PC)
        else:
                PC = PC
                print(PC)
def BLOS(offset):
        global PC
        print("exe_BLOS")
        if listvalues[1]|listvalues[3]:
                PC = PC + (2*offset)
        else:
                PC = PC 
def BVC(offset):
        global PC
        print("exe_BVC")
        if listvalues[2]==0:
                PC = PC + (2*offset)
                print(PC)
        else:
                PC = PC
                print(PC)
def BVS(offset):
        global PC
        print("exe_BVS")
        if listvalues[2]==1:
                PC = PC + (2*offset)
                print(PC)
        else:
                PC = PC
                print(PC)
def BCC(offset):
        global PC
        print("exe_BCC")
        if listvalues[3]==0:
                PC = PC + (2*offset)
                print(PC)
        else:
                PC = PC
                print(PC)
def BCS(offset):
        global PC
        print("exe_BCS")
        if listvalues[3]==1:
                PC = PC + (2*offset)
                print(PC)
        else:
                PC = PC
                print(PC)
# Specifing all Jump instrucions

"""
def decode_JSR (instruction):
    print ("Decoding JSR")
    rrr = instruction [7:10]
    dddddd = instruction [10:16]

def decode_HALT (instruction):
     print ("Decoding Halt")
"""
#starting execution part

#fetching operand
def fetch_oprand(mode,REG):
        global temp
        if(mode == '000'):
                x = reg[REG]
                return(x)
        elif(mode == '001'):
                temp = reg[REG]
                x = getmem(data,temp)
                return(x,temp)
        elif(mode =='010'):
                global PC
                temp = reg[REG]
                #print("temp(M1) = %s"%temp)
                x = getmem(data,temp)
                #print("x(M1) = %s"%x)
                reg[REG] = reg[REG] + 2
                if(REG==7):
                        PC = reg[REG] 
                return(x,temp)
        elif(mode =='011'):
                temp = reg[REG]
                y = getmem(data,temp)
                #temp1 = memory[temp]
                x = getmem(data,y)
                '''c = memory[temp1]
                d = memory[temp1+1]
                x=bin2dec(c+d)'''
                #x =bin2dec(memory[temp1])
                return(x,y)
        elif(mode == '100'):
                temp=reg[REG]
                temp1= temp - 2
                x = getmem(data,temp1)
                '''
                a =memory[temp1]
                b = memory[temp1+1]
                x=bin2dec(a+b)'''
                #x =bin2dec(memory[temp1])
                return(x,temp1)
        elif(mode == '101'):
                temp=reg[REG]
                temp1= temp - 2
                y = getmem(data,temp1)
                '''
                a =memory[temp1]
                b = memory[temp1+1]
                add=bin2dec(a+b)'''
                #add= bin2dec(memory[temp1])
                x = getmem(data,y)
                #x = bin2dec(memory[add])
                return(x,y)
        elif(mode == '110'):
                #global PC
                temp=reg[REG]
                #print("temp = %s"%temp)
                #print("PC = %s"%PC)
                const = getmem(data,temp)
                #print("const = %s"%const)
                if (REG == 7):
                        add=temp + const + 2
                        PC = PC + 2
                        reg[REG] = PC
                elif(REG != 7):
                        add=temp + const              
                #print("add = %s"%add)
                x = getmem(data,add)
                #x = bin2dec(memory[add])
                return(x,add)
                #print("s")
        elif(mode == '111'):
                temp=reg[REG]
                x = getmem(data,temp)
                
                if(REG==7):
                        add=temp + const +2
                else:
                        add=temp + const
                #const= bin2dec(memory[PC])#already incremented
                z = getmem(data,add)        
                '''c = memory[add]
                d = memory[add+1]
                y=bin2dec(c+d)'''
                #y = memory[add]
                x = getmem(data,z)
                '''e = memory[y]
                f = memory[y+1]
                x=bin2dec(e+f)'''
                #x = bin2dec(memory[y])
                return(x,add)

        
         
      
#store oprand
def store_oprand(x,REG1,mode):
        if(mode == '000'):
                reg[REG1] = x
                print(reg[REG1])
        elif(mode == '001'):
                temp= reg[REG1]
                putmem(temp,x)
                #memory[temp] = x
        elif(mode == '010'):
                temp=reg[REG1]
                putmem(temp,x)
                #memory[temp] = x
                #reg[REG1] = reg[REG1] + 2
        elif(mode == '011'):
                temp=reg[REG1]
                temp1 = getmem(data,temp)
                #temp1=memory[temp]
                putmem(temp1,x)
                #memory[temp1] = x
                reg[REG1] = reg[REG1] + 2
        elif(mode == '100'):
                temp=reg[REG1]
                temp1= temp - 2
                putmem(temp1,x)
                #memory[temp1] = x
        elif(mode == '101'):
                temp=reg[REG1]
                temp1= temp - 2
                print("temp1 = %s"%temp1)
                add = octal2dec(getmem(data,temp1))
                #add= octal2dec(memory[temp1])
                print(add)
                putmem(add,x)
                #memory[add] = x
        elif(mode == '110'):
                print("PC STORE %s"%PC)
                

                temp=reg[REG1]
                print("temp STORE %s"%temp)
                const = getmem(data,temp)
                
                '''a = memory[PC]
                b = memory[PC+1]
                const=bin2dec(a+b)'''
                #print("temp=%s"%temp)
                #const= bin2dec(memory[PC])# already incremented
                #print("const=%s"%const)
                add=temp + const + 2
                #print("add=%s"%add)
                c = dec2bin(x)
                #print("c = %s"%c)
                putmem(add,c)
                
                #memory[add]= c[0:8]
                #memory[add+1]= c[8:16]
                return(x)
        elif(mode == '111'):
                temp=reg[REG1]
                const = bin2dec(getmem(data,temp))
                #const= bin2dec(memory[PC])#already incremented 
                add=temp + const
                y = getmem(data,add)
                #y = memory[add]
                putmem(y,x)
                #memory[y]=x
                return(x) 

#defining Twos complement

def twos_comp(val,bits):
    if (val & (1 << (bits-1))) != 0:
        val = (1 << bits) + val  
    return val

def neg(val,bits):
    val = (1 << bits) + val
    val = 65536 - val
    return val



#put any instruction here

instruction = '0000101000001001' #CLR(001)
instruction = '0000101001001001' #Com(001)
instruction = '0000101010001001' #INC(001)
instruction = '0000101011001001' #DEC(001)
instruction = '0000101100001001' #NEG(001)
instruction = '0000101101001001' #ADC(001)
instruction = '0000101110001001' #SBC(001)
instruction = '0000101111001001' #TST(001)
instruction = '0000110000001001' #ROR(001)
instruction = '0000110001001001' #ROL(001)
instruction = '0000110010001001' #ASR(001)
instruction = '0000110011001001' #ASL(001)

instruction = '0001101001001001' #com(101,001)
instruction = '0010101001001001' #CMP(101,001)
instruction = '0011101001001001' #BIT(101,001)
instruction = '0100101001001001' #BIC(101,001)
instruction = '0101101001001001' #BIS(101,001)
instruction = '0110101001001001' #ADD(101,001)
instruction = '1110101001001001' #SUB(101,001)

instruction = '00000001001001001' #BR(101,001)
instruction = '00000010001001001' #BNE(101,001)
instruction = '00000011001001001' #BEQ(101,001) 
instruction = '00000100001001001' #BGE(101,001)
instruction = '00000101001001001' #BLT(101,001)
instruction = '00000110001001001' #BGT(101,001)
instruction = '00000111001001001' #BLE(101,001)
instruction = '10000000001001001' #BPL(101,001)
instruction = '10000001001001001' #BMI(101,001)
instruction = '10000011001001001' #BLOS(101,001)
instruction = '10000100001001001' #BVC(101,001)
instruction = '10000101001001001' #BVS(101,001)

instruction = '0110101001011001' #ADD(101,001)



def call_IR():
        global PC
        for a in range(0 , 49):
                setir(PC)
                print("STORE PC=%s"%PC)
                PC = PC + 2               
                reg[0]=0
                reg[1]=5
                reg[2]=8
                reg[3]=3
                reg[4]=4
                reg[5]=5
                reg[6]=0
                reg[7]=PC
                #PC=reg[7]
                inst_select(IR)
                
                
                
call_IR()








