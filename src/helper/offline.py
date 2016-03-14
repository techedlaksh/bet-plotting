import urllib
from tabulate import tabulate

data = ''
months = {}
month = ''
year = 0
path = ''
url = ''

def dict2list(dict_given):
    conv_list = []
    for key, value in dict_given.iteritems():
        conv_list.append([key,value])
    return conv_list

def getdata(url):
    global data
    u = urllib.urlopen(url)
    data = u.read()
        
def file(path):
    global data
    try:
        print 'Creating the file!!'
        fh = open(path,'w')
        try:
            print 'Writing the data!!'
            fh.write(data)
        except IOError:
            print "Error: Can't write the file."
        finally:
            print "Closing the file!!"
            fh.close()
    except IOError:
        print "Error: can't make file."
    
def basic():
    global months,month,year,path,url
    year = input('Which year do you need? ')
    print 'Months'
    months = {1:'January' , 2:'February', 3:'March', 4:'April', 5:'May' , 6:'June', 7:'July', 8:'August', 9:'September', 10:'October' , 11:'November', 12:'December'}
    print tabulate(dict2list(months))
    mon = input('Which Month do you need? ')
    month = months[mon]
    print month
    path = '/home/laksh/Desktop/Values/HTML/' + month + '_' + str(year) + '.txt'
    url = 'http://satta-king.in/' + month + '-' + str(year) + '.php'


getdata(url)
file(path)
