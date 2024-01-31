from pkg         import * 
from environment import * 
from sequence    import *

@pyuvm.test()
class test(uvm_test):
    def __init__(self, name, Parent):
        super().__init__(name, Parent)
        
    def build_phase(self):
        self.logger.info( " [TEST] WE ARE STARTING build_phase TEST")
        self.environment_instance    = uvm_factory().create_component_by_name("environment"   ,name = "environment_instance",parent = self)
        self.reset_sequence_Instance = uvm_factory().create_object_by_name("reset_sequence"   ,name = "reset_sequence_Instance")
        self.baud_sequence_Instance  = uvm_factory().create_object_by_name("baud_sequence"    ,name = "baud_sequence_Instance")
        self.dut                     = cocotb.top
        self.CLK                     = Clock(self.dut.clk, 20, units="ns")
        ConfigDB().set(self,"*","DUT",self.dut)


    def connect_phase(self):
        self.logger.info( " [TEST] WE ARE STARTING  connect_phase TEST")



    async def run_phase(self):
        self.raise_objection()
        self.logger.info( " [TEST] WE ARE STARTING run_phase TEST")
        await cocotb.start(self.CLK.start())
        await self.reset_sequence_Instance.start(self.environment_instance.agent_instance.sequencer_instance)
        for repition in range(20) : 
            await self.baud_sequence_Instance.start(self.environment_instance.agent_instance.sequencer_instance)
        await ClockCycles(self.dut.tx_clk, 4, rising=True)
        self.environment_instance.scoreboard_instance.report_test_cases()
        coverage_db.export_to_xml(filename="ALU_coverage.xml")
        self.drop_objection()



