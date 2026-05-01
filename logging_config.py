import logging

def setup_logging():
    logging.basicConfig( #so we are recording every action here like 
        level=logging.INFO,#your recording iinfo in that 
        format='%(asctime)s - %(levelname)s - %(message)s',#format ur specifying
        handlers=[
            logging.FileHandler("trading.log"),
            logging.StreamHandler()#then handling logging file
        ]
    )
    return logging.getLogger("TradingBot")