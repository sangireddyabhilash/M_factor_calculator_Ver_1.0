# _*_ coding: utf-8 _*_
from flask import Flask, render_template, url_for, request, redirect
import os
import re
import glob

from unidecode import unidecode
app = Flask(__name__)


global odepth
odepth = 1.4

@app.route("/")
def main():
    return render_template('index.html')


@app.route('/success/<name>')
def success(name):
   Dict = {}
   tempo = name
   tempo1 = name
   tempo2 = name
   os.system("runenergyplus ./static/Data/"+tempo+"input/"+tempo+".idf /usr/local/EnergyPlus-8-1-0/WeatherData/epw/hongkong.epw")
   #print "runenergyplus ./static/Data/"+tempo+"input/"+tempo+".idf /usr/local/EnergyPlus-8-1-0/WeatherData/epw/hongkong.epw"
   k=glob.glob("./static/Data/"+tempo+"input/Output/*.html")
   pat = '<td align="right">Total Site Energy</td>'
   pat2= "\d+.\d+"

   for t in k:
      tuple1 = ()
      tuple2 = ()
      f=open(t,"r")
      for i in f:
         #print i
         tuple1=re.findall(pat,i,re.M)
         if len(tuple1)>0:
            break

      for j in f:
      #print j
         tuple2=re.findall(pat2,j)
         break

   Dict[tempo+'input'] = tuple2[0]
   while (float(tempo) > 0.05):
      os.system("runenergyplus ./static/Data/"+tempo+"/"+tempo+".idf /usr/local/EnergyPlus-8-1-0/WeatherData/epw/hongkong.epw")
      k=glob.glob("./static/Data/"+tempo+"/Output/*.html")
      pat = '<td align="right">Total Site Energy</td>'
      pat2= "\d+.\d+"

      for t in k:
         tuple1 = ()
         tuple2 = ()
         f=open(t,"r")
         for i in f:
         #print i
            tuple1=re.findall(pat,i,re.M)
            if len(tuple1)>0:
               break

         for j in f:
         #print j
            tuple2=re.findall(pat2,j)
            break

      Dict[tempo] = tuple2[0]
      tempo = float(tempo) - 0.05
      tempo = str(tempo)

      for ash in Dict:
         print ash+":"+Dict[ash]+'\n'


   os.system("rm -rf ./static/Data/*")
   while(float(tempo1) > 0.05):
      if((Dict[tempo1] >= Dict[tempo2+'input'])and (Dict[str(float(tempo1)-0.05)] <= Dict[tempo2+'input'])):
         a = tempo1
         break
      else:
         tempo1 = float(tempo1) - 0.05
         tempo1 = str(tempo1)

   slope = (float(Dict[a])-float(Dict[str(float(a)-0.05)])) / (0.05)
   const = float(Dict[a]) - slope*(float(a))
   final_shgc = (float(Dict[str(tempo2)+'input']) - float(const))/float(slope)
   final_shgc = round(final_shgc,2)
   print final_shgc
   final_shgc = final_shgc / 0.4


   fileP=open('/home/akshay/Desktop/output','a')
   fileP.write(str(final_shgc)+'\n')
   #return render_template('output.html', text = final_shgc)
   return redirect(url_for('poc'))
 



@app.route('/ecbc/<name1>',methods = ['POST', 'GET'])
def ecbc(name1):
      ecbc_Orientation = '135'
      ecbc_SHGC = '0.4'
      ecbc_Win_H = '1'
      ecbc_Win_L = '1'

      ecbc_Building_L = float(ecbc_Win_L) + 2
      ecbc_Building_L = str(ecbc_Building_L)

      
      ecbc_Overhang_D = '0.01'
      ecbc_Overhang_H = '0'
      ecbc_Overhang_A = '90'
      ecbc_Overhang_LE = '0'
      ecbc_Overhang_RE = '0'

      ecbc_Fin_L_E = '0'
      ecbc_Fin_L_AT = '0'
      ecbc_Fin_L_BB = '0'
      ecbc_Fin_L_A = '90'
      ecbc_Fin_L_D = name1
      ecbc_Fin_R_E = '0'
      ecbc_Fin_R_AT = '0'
      ecbc_Fin_R_BB = '0'
      ecbc_Fin_R_A = '90'
      ecbc_Fin_R_D = name1

      temp = ecbc_SHGC

      os.system("mkdir"+ ' ./static/Data/'+ecbc_SHGC+'input')
      with open('./static/template.idf', 'rt') as f1:
            with open('./static/Data/'+ecbc_SHGC+'input/'+ecbc_SHGC+'.idf', 'wt') as f2:
                  for a in f1:
                     a = a.decode('utf-8')
                     a = a.replace('ecbc_SHGC',ecbc_SHGC)
                     a = a.replace('ecbc_Win_H',ecbc_Win_H)
                     a = a.replace('ecbc_Win_L',ecbc_Win_L)
                     a = a.replace('ecbc_Orientation',ecbc_Orientation)

                     a = a.replace('ecbc_Building_L',ecbc_Building_L)

                     a = a.replace('ecbc_Overhang_D',ecbc_Overhang_D)
                     a = a.replace('ecbc_Overhang_H',ecbc_Overhang_H)
                     a = a.replace('ecbc_Overhang_A',ecbc_Overhang_A)
                     a = a.replace('ecbc_Overhang_LE',ecbc_Overhang_LE)
                     a = a.replace('ecbc_Overhang_RE',ecbc_Overhang_RE)

                     a = a.replace('ecbc_Fin_L_E',ecbc_Fin_L_E)
                     a = a.replace('ecbc_Fin_L_D',ecbc_Fin_L_D)
                     a = a.replace('ecbc_Fin_L_AT',ecbc_Fin_L_AT)
                     a = a.replace('ecbc_Fin_L_BB',ecbc_Fin_L_BB)
                     a = a.replace('ecbc_Fin_L_A',ecbc_Fin_L_A)
                     a = a.replace('ecbc_Fin_L_D',ecbc_Fin_L_D)
                     a = a.replace('ecbc_Fin_R_E',ecbc_Fin_R_E)
                     a = a.replace('ecbc_Fin_R_D',ecbc_Fin_R_D)
                     a = a.replace('ecbc_Fin_R_AT',ecbc_Fin_R_AT)
                     a = a.replace('ecbc_Fin_R_BB',ecbc_Fin_R_BB)
                     a = a.replace('ecbc_Fin_R_A',ecbc_Fin_R_A)
                     a = a.replace('ecbc_Fin_R_D',ecbc_Fin_R_D)
                     a = a.encode('utf-8')
                     f2.write(a)
      f1.close()
      f2.close()

      while (float(ecbc_SHGC) > 0.05):
         
         os.system("mkdir"+ ' ./static/Data/'+ecbc_SHGC)
         with open('./static/template_2.idf', 'rt') as f1:
               with open('./static/Data/'+ecbc_SHGC+'/'+ecbc_SHGC+'.idf', 'wt') as f2:

                  for a in f1:
                     a = a.decode('utf-8')
                     a = a.replace('ecbc_SHGC',ecbc_SHGC)
                     a = a.replace('ecbc_Win_H',ecbc_Win_H)
                     a = a.replace('ecbc_Win_L',ecbc_Win_L)
                     a = a.replace('ecbc_Orientation',ecbc_Orientation)

                     a = a.replace('ecbc_Building_L',ecbc_Building_L)

                     a = a.replace('ecbc_Overhang_D',ecbc_Overhang_D)
                     a = a.replace('ecbc_Overhang_H',ecbc_Overhang_H)
                     a = a.replace('ecbc_Overhang_A',ecbc_Overhang_A)
                     a = a.replace('ecbc_Overhang_LE',ecbc_Overhang_LE)
                     a = a.replace('ecbc_Overhang_RE',ecbc_Overhang_RE)

                     a = a.replace('ecbc_Fin_L_E',ecbc_Fin_L_E)
                     a = a.replace('ecbc_Fin_L_D',ecbc_Fin_L_D)
                     a = a.replace('ecbc_Fin_L_AT',ecbc_Fin_L_AT)
                     a = a.replace('ecbc_Fin_L_BB',ecbc_Fin_L_BB)
                     a = a.replace('ecbc_Fin_L_A',ecbc_Fin_L_A)
                     a = a.replace('ecbc_Fin_L_D',ecbc_Fin_L_D)
                     a = a.replace('ecbc_Fin_R_E',ecbc_Fin_R_E)
                     a = a.replace('ecbc_Fin_R_D',ecbc_Fin_R_D)
                     a = a.replace('ecbc_Fin_R_AT',ecbc_Fin_R_AT)
                     a = a.replace('ecbc_Fin_R_BB',ecbc_Fin_R_BB)
                     a = a.replace('ecbc_Fin_R_A',ecbc_Fin_R_A)
                     a = a.replace('ecbc_Fin_R_D',ecbc_Fin_R_D)
                     a = a.encode('utf-8')
                     f2.write(a)
         ecbc_SHGC = float(ecbc_SHGC) - 0.05
         ecbc_SHGC = str(ecbc_SHGC)
         f1.close()
         f2.close()
      return redirect(url_for('success',name =  temp))


@app.route('/poc')
def poc():
   global odepth
   odepth = odepth+0.05
   fileP=open('/home/akshay/Desktop/odepth','a')
   fileP.write(str(odepth)+'\n')
   if  odepth<=1.6:
      #fileP=open('/home/akshay/Desktop/odepth1','a')
      #fileP.write(str(odepth)+'\n')
      return redirect(url_for('ecbc',name1= odepth))

   else :
      return render_template('output.html')


if __name__ == "__main__":
	
    app.run(debug = True)
