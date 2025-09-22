import logging

logging.basicConfig(
    filename = 'app1.log',
    filemode = 'w',
    level = logging.DEBUG,
    format = '%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S' 
)

logger = logging.getLogger("ArithmeticApp")

def add(a,b):
    result = a + b
    logger.debug(f"the result of {a} + {b} = {result}")
    return result

def multiply(a,b):
    result = a * b
    logger.debug(f"the result of {a} * {b} = {result}")
    return result

def substract(a,b):
    result = a - b
    logger.debug(f"the result of {a} - {b} = {result}")
    return result


def divide(a,b):
    try:
        result = a / b
        logger.debug(f"the result of {a} + {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("cant perform division operation")
        return None


add(10,15)
multiply(10,20)
substract(15,10)
divide(20,0)


# import logging

# ## logging setting

# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S',
#     handlers=[
#         logging.FileHandler("app1.log"),
#         logging.StreamHandler()
#     ]
# )

# logger=logging.getLogger("ArithmethicApp")

# def add(a,b):
#     result=a+b
#     logger.debug(f"Adding {a} + {b}= {result}")
#     return result

# def subtract(a, b):
#     result = a - b
#     logger.debug(f"Subtracting {a} - {b} = {result}")
#     return result

# def multiply(a, b):
#     result = a * b
#     logger.debug(f"Multiplying {a} * {b} = {result}")
#     return result

# def divide(a, b):
#     try:
#         result = a / b
#         logger.debug(f"Dividing {a} / {b} = {result}")
#         return result
#     except ZeroDivisionError:
#         logger.error("Division by zero error")
#         return None
    
# add(10,15)
# subtract(15,10)
# multiply(10,20)
# divide(20,0)