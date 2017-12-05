import csv
import matplotlib.pyplot as plt
import numpy as np

def createFrequenceTab(arq):
	#tabela  de frequencia e um dicionario onde as chaves sao os dados
	#e o valores sao as frequencias.
	#chave "len" a quantidade total de dados.
	frequenceTab= {}
	tabLen=0
	teste= ""
	vetOrder=[]
	
	tab= arq.readlines()
	
	for row in tab:
		tabLen+=1
		value= ((row.split(","))[1]).rstrip('\n')
		if value not in frequenceTab.keys():
			frequenceTab[value] = 1
			vetOrder.append(int(value))
		else:
			frequenceTab[value]+= 1
			
	
	vetOrder= sorted(vetOrder)
	frequenceTab["len"]=tabLen
	
	return frequenceTab,vetOrder
	
def calcAverage(frequenceTab):
	#calcula a media 
	total= 0
	for key in (frequenceTab.keys()):
		if key != "len":
			total+= (int(key) * frequenceTab[key])
	return (total/frequenceTab["len"])
	
		 
def calcMode(frequenceTab):
	#calcula a moda
	valueMode = 0
	keyMode= ""
	for key in (frequenceTab.keys()):
		if key != "len":
			if (frequenceTab[key] > valueMode):
				valueMode= frequenceTab[key]
				keyMode= key
		
	return int(keyMode)

def calcMedian(frequenceTab, vetOrder):
	p1 = 0
	p2 = 0
	soma = 0
	median= 0
	
	if (frequenceTab["len"]%2 ==0):
		p1=findElement((frequenceTab["len"] / 2),vetOrder,frequenceTab)
		p2= findElement(((frequenceTab["len"]+2) / 2), vetOrder, frequenceTab)
		median=((p1+p2)/2)	
	else:	
		p1 = (frequenceTab["len"]+1)/2
		median= findElement(p1,vetOrder,frequenceTab)
		
	return median
					
def findElement(pos,vetOrder,frequenceTab):
	i = 0
	aux = 0
	for i in vetOrder:
		aux+= frequenceTab[str(i)]	
		if (pos <= aux):
			return i
			
def calcVariance(frequenceTab):
	average= calcAverage(frequenceTab)
	somatorio= 0
	
	for key in frequenceTab.keys():
		if (key != "len"):
			somatorio+= ((int(key) - average)**2) * frequenceTab[key]	
	
	return( somatorio / (frequenceTab["len"] ) )
				

def calcDesvPad(frequenceTab):
	var= calcVariance(frequenceTab)
	return(var**(1/2))


def calcFirstQ(frequenceTab,vetOrder):
	pos= 0
	elemen= 0
	
	pos= (frequenceTab["len"])//4
	elemen= findElement(pos,vetOrder,frequenceTab)
	return (elemen)
	


def calcThirdQ(frequenceTab,vetOrder):
	pos= 0
	elemen= 0
	
	pos= ((frequenceTab["len"])//4)*3
	elemen= findElement(pos,vetOrder,frequenceTab)
	return (elemen)	

def amplitudeQ(frequenceTab,vetOrder):
	q1= calcFirstQ(frequenceTab,vetOrder)
	q3= calcThirdQ(frequenceTab, vetOrder)
	return (q3-q1)
	
	
def showHistogram(frequenceTab,vetOrder):
	vetValues=[]
	for item in vetOrder:
		vetValues.append(frequenceTab[str(item)])

	fig= plt.figure()
	ax= fig.add_subplot(111)
	
	xx= range(1, len(vetValues) +1)
	
	ax.bar(xx,vetOrder, width=0.5, color=(0,1,1))
	ax.set_xticks(xx)
	ax.set_xticklabels(vetValues)
		
	plt.xlabel("Frequência. (n° de cidades)")
	plt.ylabel("Quantidade de mortes")
	plt.title("Histograma de Assassinatos por Municipio do ES em 2014")
	
	plt.show()
			

def showBloxPlot(frequenceTab,vetOrder):
	vetValues=[]
	for item in vetOrder:
		for i in range(frequenceTab[str(item)]):
			vetValues.append(item)
	plt.boxplot(vetValues)
	plt.title("BloxPlot de Assassinatos por Municipio do ES em 2014")
	plt.show()
	
def main(args):
	#abre arquivo em formato CSV
	arq= open("homicidios_Es2014.csv", "r")
	
	vetOrder=[]#Vetor de Xi em ordem
	
	#cria tabela de frequencia a partir do arquivo. 
	frequenceTab,vetOrder= createFrequenceTab(arq)
	
	#mostra Media
	print ("media: %d" %(calcAverage(frequenceTab)))
	#mostra Moda
	print ("moda: %d" %(calcMode(frequenceTab)))
	#mostra Mediana
	mediana= (calcMedian(frequenceTab,vetOrder))
	print ("mediana: Qtd.Mortes: %d" %(mediana) + "  Frequência: %d" %(frequenceTab[str(mediana)]))
	#mostra Variancia
	print ("variancia: %.2f" %(calcVariance(frequenceTab)))
	#mostra Desvio Padrao
	print("desvio padrao: %.2f" %(calcDesvPad(frequenceTab)))
	#mostra 1° Q
	print("1° Q : %d" %(calcFirstQ(frequenceTab,vetOrder)))
	#mostra 3° Q
	print("3° Q: %d" %(calcThirdQ(frequenceTab,vetOrder)))
	#mostra amplitudo entre Q's
	print("Amplitude: %d" %(amplitudeQ(frequenceTab,vetOrder)))
	
	showHistogram(frequenceTab,vetOrder)
	
	showBloxPlot(frequenceTab,vetOrder)

	
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
