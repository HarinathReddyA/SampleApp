import logging
logging.basicConfig(filename='applog.log', filemode='w', format='%(asctime)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
import random
flag = 1
while flag==1:
    n = random.randint(200,2000)
    te = random.randint(0,9)
    if(te%2==0):
        logger.info("byteService connection time= "+str(n))
    else:
        logger.info("helloDB connection time= "+str(n))

    

    t = input("continue:  y/n  ")
    if(t=='n'):
        flag =0
    else:
        flag =1
    
    
