import logging
logging.basicConfig(filename='sample.log', filemode='w', format='%(asctime)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
flag = 1
while flag==1:
    
    name = input("Enter Your Name:")
    logger.info("Username: " + name)

    t = input("contiue y/n")
    if(t=='n'):
        flag =0
    else:
        flag =1
    
    
