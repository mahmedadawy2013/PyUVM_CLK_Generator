from pkg import * 

class  sequence_item(uvm_sequence_item,Randomized):
    def __init__(self,name):
        super().__init__(name)
        Randomized.__init__(self)
        self.rst         =  0  
        self.baud        =  0
        self.tx_clk      =  0
        self.period      =  0 

        self.add_rand("rst"        , list(range(0,2)                           )   ) 
        self.add_rand("baud"       , list([4800,9600,14400,19200,38400,57600]    )   ) 


    def display(self,name = "TRANSACTION"):
        cocotb.log.info("******************"+str(name)+"*******************")
        cocotb.log.info("the Value of rst        is   " + str(self.rst    ))
        cocotb.log.info("the Value of baud       is   " + str(self.baud   ))
        cocotb.log.info("the Value of tx_clk     is   " + str(self.tx_clk ))
        cocotb.log.info("the Value of period     is   " + str(self.period ))
        cocotb.log.info("**************************************************")
