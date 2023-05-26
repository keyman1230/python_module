# log Usage

ex)
###  # main.py
import log  
logger = log.set_log(module=__ name __, path="Log", lv="info")  
logger.info("im from main.py")  

### # funtion.py
import log  
logger = log.set_log(module=__ name __, path="Log", lv="info")  
logger.info("im from function.py")  


### # Log.log
2023-05-13 01:23:11,049 - __ main __ - INFO - im from main.py

2023-05-13 01:23:11,049 - function - INFO - I'm from function  

