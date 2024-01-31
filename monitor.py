from pkg import * 

class monitor(uvm_sequencer):
    
    def __init__(self, name, Parent):
        super().__init__(name, Parent)
        self.first_rise   = 0 
        self.seconed_rise = 0 

    def build_phase(self):
        self.logger.info( " [MONITOR] WE ARE STARTING  build_phase MONITOR")
        self.t_monitor         = uvm_factory().create_object_by_name("sequence_item"   ,name = "t_monitor")
        self.dut_monitor       = ConfigDB().get(self,"","DUT")
        self.mon_mail_s        = uvm_blocking_put_port("mon_mail_s"  ,self)
        self.mon_mail_su       = uvm_blocking_put_port("mon_mail_su" ,self)

    def connect_phase(self):
        self.logger.info( " [MONITOR] WE ARE STARTING  connect_phase MONITOR")

    async def run_phase(self):
        self.logger.info( "[Monitor] STARTING.")
        await RisingEdge(self.dut_monitor.clk)
        while(True):
            self.logger.info( "[Monitor] waiting for item ...")
            await RisingEdge(self.dut_monitor.clk)
            await ReadOnly()
            self.t_monitor.rst           =   int(self.dut_monitor.rst)
            self.t_monitor.baud          =   int(self.dut_monitor.baud)    
            if (self.t_monitor.rst):
                pass
            else :
                await RisingEdge(self.dut_monitor.tx_clk)
                self.first_rise   = (cocotb.utils.get_sim_time('ns'))
                await RisingEdge(self.dut_monitor.tx_clk)
                self.seconed_rise = (cocotb.utils.get_sim_time('ns'))
                self.t_monitor.period = self.seconed_rise - self.first_rise 
            self.t_monitor.display("MONITOR")  
            await self.mon_mail_s.put(self.t_monitor)
            await self.mon_mail_su.put(self.t_monitor)


   
                