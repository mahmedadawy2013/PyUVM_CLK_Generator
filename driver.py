from pkg import * 
from sequence_item import * 
"""
register in the factory is done using the inheritance class driver(uvm_driver):

"""
class driver(uvm_driver):

    def __init__(self, name, Parent):
        super().__init__(name, Parent)


    def build_phase(self):
        self.logger.info( " [DRIVER] WE ARE STARTING  build_phase DRIVER")
        self.t_drive          = uvm_factory().create_object_by_name("sequence_item"   ,name = "t_drive")
        self.dut_driver       = ConfigDB().get(self,"","DUT")
        self.driv_handover     = Event(name=None) 

    def connect_phase(self):
        self.logger.info( " [DRIVER] WE ARE STARTING  connect_phase DRIVER")

    async def run_phase(self):
        while True:
            self.driv_handover.clear() 
            self.logger.info( " [DRIVER] WE ARE STARTING  run_phase DRIVER")
            self.t_drive = await self.seq_item_port.get_next_item()
            await FallingEdge(self.dut_driver.clk)
            self.t_drive.display("DRIVER")
            self.dut_driver.rst.value      = self.t_drive.rst
            self.dut_driver.baud           = self.t_drive.baud
            """             if (self.t_drive.rst ==  1 ):
                await RisingEdge(self.dut_driver.clk)
            else :
                await RisingEdge(self.dut_driver.clk)
                await RisingEdge(self.dut_driver.tx_clk)
                await RisingEdge(self.dut_driver.tx_clk) """
            await self.driv_handover.wait()
            self.seq_item_port.item_done()




   
                