from lxml import etree
from offline import *

locations = {}

def dd(i,path):
    page = open(path).read()
    x = etree.HTML(page)
    DD = x.xpath('//td[@style="background:#fac090;"][1]/strong/text()')
    for numbers in DD:
        DD[i] = int(numbers)
	print DD[i] 
        i += 1
         
    
def gaziabad(i,path):
    page = open(path).read()
    x = etree.HTML(page)
    Gaz = x.xpath('//td[@style="background:#fac090;"][2]/strong/text()')
    for numbers in Gaz:
        Gaz[i] = int(numbers)
        i += 1

def gali(i,path):
    page = open(path).read()
    x = etree.HTML(page)
    Gali = x.xpath('//td[@style="background:#fac090;"][3]/strong/text()')
    for numbers in Gali:
        Gali[i] = int(numbers)
        i += 1

def faridabad(i,path):
    page = open(path).read()
    x = etree.HTML(page)
    frdbd = x.xpath('//td[@style="background:#fac090;"][4]/strong/text()')
    for numbers in frdbd:
        frdbd[i] = int(numbers)
        i += 1
    
def disawar(i,path):
    page = open(path).read()
    x = etree.HTML(page)
    dswr = x.xpath('//td[@style="background:#fac090;"][5]/strong/text()')
    for numbers in dswr:
        dswr[i] = int(numbers)
        i += 1

def main():
    global locations
    #area = raw_input('Which area record do you need ?')
    locations = {1:'Delhi-Darbar' , 2:'Gaziabad', 3:'Gali', 4:'Faridabad', 5:'Disawar'}
    print tabulate(dict2list(locations))


i = 0
path = '/home/laksh/Desktop/Values/HTML/' + month + '_' + str(year) + '.txt'
dd(i,path)
