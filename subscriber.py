from pkg import * 
from sequence_item import * 
from cocotb.triggers import * 
import cocotb
import cocotb.queue
from cocotb_coverage.coverage import *

@CoverPoint("top.baud"      , vname="baud"      , bins=  list([4800,9600,14400,19200,38400,57600]    ) )
@CoverPoint("top.rst"       , vname="rst"       , bins=list(range(0, 2  ))) 
@CoverPoint("top.tx_clk"    , vname="tx_clk"    , bins=list(range(0, 2  ))) 
def sample(baud,rst,tx_clk):
    pass

class subscriber(uvm_subscriber):


    def build_phase(self):
        self.logger.info( " [SUBSCRIBER] WE ARE STARTING  build_phase SUBSCRIBER")
        self.subsc_mail    = uvm_blocking_get_port("score_mail",self)
        self.t_subscriber  = uvm_factory().create_object_by_name("sequence_item"   ,name = "t_monitor")

    def connect_phase(self):
        self.logger.info( " [SUBSCRIBER] WE ARE STARTING  connect_phase SUBSCRIBER")

    async def run_phase(self):
        self.logger.info( " [SUBSCRIBER] WE ARE STARTING  run_phase SUBSCRIBER")
        while True :
            self.t_subscriber = await self.subsc_mail.get()
            self.t_subscriber.display("SUBSCRIBER")
            sample(self.t_subscriber.baud,self.t_subscriber.rst,self.t_subscriber.tx_clk)


