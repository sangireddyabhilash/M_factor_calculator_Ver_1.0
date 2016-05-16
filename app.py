# _*_ coding: utf-8 _*_
from flask import Flask, render_template, url_for, request, redirect
import os
import re
import glob

from unidecode import unidecode
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')


@app.route('/success/<name>')
def success(name):
   Dict = {}
   tempo = name
   tempo1 = name
   tempo2 = name
   os.system("runenergyplus ./static/Data/"+tempo+"input/"+tempo+".idf /usr/local/EnergyPlus-7-2-0/WeatherData/epw/IND_Hyderabad_ISHRAE_2013.epw")
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
      os.system("runenergyplus ./static/Data/"+tempo+"/"+tempo+".idf /usr/local/EnergyPlus-7-2-0/WeatherData/epw/IND_Hyderabad_ISHRAE_2013.epw")
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
      if((Dict[tempo1] > Dict[tempo2+'input'])and (Dict[str(float(tempo1)-0.05)] < Dict[tempo2+'input'])):
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
   return render_template('output.html', text = final_shgc)
 



@app.route('/ecbc',methods = ['POST', 'GET'])
def ecbc():
      ecbc_Orientation = request.form['orien']
      ecbc_SHGC = request.form['shgc']
      ecbc_Win_H = request.form['wheight']
      ecbc_Win_L = request.form['wlength']

      ecbc_Building_L = float(ecbc_Win_L) + 2
      ecbc_Building_L = str(ecbc_Building_L)

      ohang = request.form['overhang']
      ecbc_Overhang_D = request.form['odepth']
      ecbc_Overhang_H = request.form['oheight']
      ecbc_Overhang_A = request.form['otilt']
      ecbc_Overhang_LE = request.form['le']
      ecbc_Overhang_RE = request.form['re']

      ecbc_Fin_L_E = request.form['fle']
      ecbc_Fin_L_AT = request.form['flda']
      ecbc_Fin_L_BB = request.form['fldb']
      ecbc_Fin_L_A = request.form['flt']
      ecbc_Fin_L_D = request.form['fld']
      ecbc_Fin_R_E = request.form['fre']
      ecbc_Fin_R_AT = request.form['frda']
      ecbc_Fin_R_BB = request.form['frdb']
      ecbc_Fin_R_A = request.form['frt']
      ecbc_Fin_R_D = request.form['frd']

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



if __name__ == "__main__":
    app.run(debug = True)


