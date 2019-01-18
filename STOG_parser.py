import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import datetime

flag = 1

sampleName =		'Er2Ti2O7_pristine'						# sample name, uses as root for other files
numberOfFiles =		1										# don't adjust
SofQfile =			'NOM_9999ETO227_Pristine_c_SQ.dat'	# input SofQ file from Addie
Qmin =				0.5									# Qmin for F.T.
Qmax =				24.48									# Qmax for F.T.
Qdamp =				0.017659								# Qdamp of experiment
Qbroad = 			0.0191822								# Qbroad of experiment
offset =			1										# offset for SofQ
scale =				0.7										# re-scale for SofQ
xOffset =			0										# x-offset for SofQ
SofQ_raw_output = 	sampleName + '.sq'						# raw SofQ output
GofR_raw_output =	sampleName + '.gr'						# raw GofR output
rMax =				50										# rmax of PDF output
numberOfRPoints =	5000									# r points of PDF output
LorchYN	=			'Y'										# lorched PDF? choose Yes
numberDensity = 	0.0860031078203									# sample atom density
addValue = 			0										# add value SofQ
tryAddValue = 		'N'										# add value SofQ?
FourierFilterYN =	'Y'										# use Fourier Filter?
FFrMax = 			1.65							# FF rmax
SofQ_FFcorrected =	sampleName + '_ft.sq'					# FFcorrected SofQ output
QSofQ_FFcorrected = sampleName + '_ft.qsq'					# FFcorrected Q(SofQ-1) output
GofR_FFcorrected =	sampleName + '_ft.gr'					# FFcorrected GofR output
GofR_FF_lorched = 	sampleName + 'ftlorch.gr'				# FFcorrected,lorched GofR output
DofR_FF_lorched = 	sampleName + 'ftlorch.dr'				# FFcorrected,lorched DofR output
TofR_FF_lorched = 	sampleName + 'ftlorch.tr'				# FFcorrected,lorched TofR output
sum_ciBi_squared = 	0.20107071281							# (sum_ci*bi)^2
#sum_ciBisquared =	0.346119591818							# (sum_ci*bi^2)
FofQ_for_RMC = 		sampleName + '_rmc.fq'					# rmc FofQ output
GofR_for_RMC = 		sampleName + '_rmc.gr'					# rmc GofR output
zeroOut_rValue =	1.65										# rmc zero out everything below this r value ...
rMin_exception =	1.65									# ... except between here (rmin) ...
rMax_exception =	1.65										# ... and here (rmax)

while flag == 1:

	with open("getFile.txt", 'w') as target:
		target.write(str(numberOfFiles)+'\n')
		target.write(str(SofQfile)+'\n')
		target.write(str(Qmin)+' '+str(Qmax)+'\n')
		target.write(str(offset)+' '+str(scale)+'\n')
		target.write(str(xOffset)+'\n')
		target.write(str(SofQ_raw_output)+'\n')
		target.write(str(GofR_raw_output)+'\n')
		target.write(str(rMax)+'\n')
		target.write(str(numberOfRPoints)+'\n')
		target.write(str(LorchYN)+'\n')
		target.write(str(numberDensity)+'\n')
		target.write(str(addValue)+'\n')
		target.write(str(tryAddValue)+'\n')
		target.write(str(FourierFilterYN)+'\n')
		target.write(str(FFrMax)+'\n')
		target.write(str(SofQ_FFcorrected)+'\n')
		target.write(str(GofR_FFcorrected)+'\n')
		target.write(str(GofR_FF_lorched)+'\n')
		target.write(str(sum_ciBi_squared)+'\n')
		target.write(str(FofQ_for_RMC)+'\n')
		target.write(str(GofR_for_RMC)+'\n')
		target.write(str(zeroOut_rValue)+' '+str(rMin_exception)+' '+str(rMax_exception)+'\n')
		target.close()

	os.system("stog_new < getFile.txt")

	lorchr = []
	FFlorchr = []
	lorch_littlegofr = []
	lorch_dofr =[]
	lorch_tofr = []
	FFlorch_littlegofr = []
	qArray = []
	sqArray = []
	qSqminusOneArray = []
	
	with open(GofR_FF_lorched) as f2:
		next(f2)
		next(f2)
		for line in f2:
			line = line.strip()
			LorchFilecontent = line.split()
			r = float(LorchFilecontent[0])
			lorchr.append(r)
			littlegofr = float(LorchFilecontent[1])
			lorch_littlegofr.append(littlegofr)
			dofr = r*(littlegofr-1.0)
			lorch_dofr.append(dofr)
			tofr=r*(littlegofr)
			lorch_tofr.append(tofr)
	f2.close()
	
	with open(SofQ_FFcorrected) as f7:
		next(f7)
		next(f7)
		for line in f7:
			line = line.strip()
			SQcontent = line.split()
			Q = float(SQcontent[0])
			qArray.append(Q)
			SQ = float(SQcontent[1])
			sqArray.append(SQ)
			qSqminusOne = Q*(SQ-1.0)
			qSqminusOneArray.append(qSqminusOne)
	f2.close()
	
	with open(QSofQ_FFcorrected, 'w') as f8:
		for y in range(len(qArray)):
			f8.write(str(qArray[y])+str(' ')+str(qSqminusOneArray[y]) +'\n')
	f8.close()

	with open(DofR_FF_lorched, 'w') as f5:
		for y in range(len(lorchr)):
			f5.write(str(lorchr[y])+str(' ')+str(lorch_dofr[y]) +'\n')
	f5.close()
	
	with open(TofR_FF_lorched, 'w') as f6:
		for y in range(len(lorchr)):
			f6.write(str(lorchr[y])+str(' ')+str(lorch_tofr[y]) +'\n')
	f6.close()

	with open(GofR_FFcorrected) as f4:
		next(f4)
		next(f4)
		for line in f4:
			line = line.strip()
			FFFilecontent = line.split()
			r = float(FFFilecontent[0])
			FFlorchr.append(r)
			FFlittlegofr = float(FFFilecontent[1])
			FFlorch_littlegofr.append(FFlittlegofr)
	f4.close()
	
	plt.plot(FFlorchr, lorch_littlegofr, 'k-')
	plt.xlabel('r (angstrom)')
	plt.ylabel('g(r)')
	plt.legend(loc='upper left', prop={'size': 16}, frameon=False)
	plt.title('PDF lorched')
	#plt.savefig('PDF1.eps', format='eps', dpi=1200)
	plt.axhline(y=0.0, color='r', linestyle='dashed')
	plt.xlim([0, 7.5])
	plt.ylim([-3, 3])
	plt.show()

	with open("PDFGUI_" + str(GofR_FF_lorched) + ".gr", 'w') as f3:
		f3.write('#	' + str(numberOfRPoints)+'\n')
		f3.write('#	' + 'PDFGUI_' + str(GofR_FF_lorched)+'\n')
		f3.write('#	' + 'created: ' + str(datetime.datetime.now()) +'\n')
		f3.write('#	' + 'Comment: neutron, Qmax='+str(Qmax)+ ', Qdamp='+str(Qdamp)+ ', Qbroad='+str(Qbroad)+'\n')
		f3.write('#	'+'\n')
		for y in range(len(lorchr)):
			f3.write(str(lorchr[y])+str(' ')+str(lorch_dofr[y]) +'\n')
	f3.close()

	print "Current scale value is: ", scale
	userRescaleInput = input("Do you wish to rescale? yes (1) or no (2)	")
	if userRescaleInput == 2:
		flag = 0
	else:
		scale = input("What scale factor do you wish now?	")
		flag = 1