from pkg import * 

class scoreboard(uvm_scoreboard):

    def __init__(self, name, Parent):
        super().__init__(name, Parent)
        self.golden_period     = 0 
        self.passed_test_cases = 0 
        self.failed_test_cases = 0 

    def build_phase(self):
        self.logger.info( " [SCOREBOARD] WE ARE STARTING  build_phase SCOREBOARD")
        self.score_mail      = uvm_blocking_get_port("score_mail",self)
        self.t_scoreboard    = uvm_factory().create_object_by_name("sequence_item"   ,name = "t_monitor")
        self.score_handover  = Event(name=None) 

    def connect_phase(self):
        self.logger.info( " [SCOREBOARD] WE ARE STARTING  connect_phase SCOREBOARD")

    async def run_phase(self):
        self.logger.info( " [SCOREBOARD] WE ARE STARTING  run_phase SCOREBOARD")
        while True :
            self.t_scoreboard = await self.score_mail.get()
            self.t_scoreboard.display("SCOREBOARD")
            if   (self.t_scoreboard.baud == 4800  and self.t_scoreboard.rst == 0 ):
                self.golden_period = 10416 * 20 + 2 * 20 
                if (self.t_scoreboard.period == self.golden_period):
                    self.logger.info("First baud Test Case Passed ")
                    self.passed_test_cases += 1 
                else :
                    self.logger.info("First baud Test Case Failed ")
                    self.failed_test_cases += 1 
            elif (self.t_scoreboard.baud == 9600  and self.t_scoreboard.rst == 0 ):
                self.golden_period = 5208  * 20 + 2 * 20 
                if (self.t_scoreboard.period == self.golden_period):
                    self.logger.info("First baud Test Case Passed ")
                    self.passed_test_cases += 1 
                else :
                    self.logger.info("First baud Test Case Failed ")
                    self.failed_test_cases += 1 
            elif (self.t_scoreboard.baud == 14400 and self.t_scoreboard.rst == 0 ):
                self.golden_period = 3472  * 20 + 2 * 20 
                if (self.t_scoreboard.period == self.golden_period):
                    self.logger.info("First baud Test Case Passed ")
                    self.passed_test_cases += 1 
                else :
                    self.logger.info("First baud Test Case Failed ")
                    self.failed_test_cases += 1 
            elif (self.t_scoreboard.baud == 19200 and self.t_scoreboard.rst == 0 ):
                self.golden_period = 2604  * 20 + 2 * 20 
                if (self.t_scoreboard.period == self.golden_period):
                    self.logger.info("First baud Test Case Passed ")
                    self.passed_test_cases += 1 
                else :
                    self.logger.info("First baud Test Case Failed ")
                    self.failed_test_cases += 1 
            elif (self.t_scoreboard.baud == 38400 and self.t_scoreboard.rst == 0 ):
                self.golden_period = 1302  * 20 + 2 * 20 
                if (self.t_scoreboard.period == self.golden_period):
                    self.logger.info("First baud Test Case Passed ")
                    self.passed_test_cases += 1 
                else :
                    self.logger.info("First baud Test Case Failed ")
                    self.failed_test_cases += 1 
            elif (self.t_scoreboard.baud == 57600 and self.t_scoreboard.rst == 0 ):
                self.golden_period = 868 * 20 + 2 * 20 
                if (self.t_scoreboard.period == self.golden_period):
                    self.logger.info("First baud Test Case Passed ")
                    self.passed_test_cases += 1 
                else :
                    self.logger.info("First baud Test Case Failed ")
                    self.failed_test_cases += 1 
            self.score_handover.set() 

    def report_test_cases (self):
        self.total_test_cases = self.passed_test_cases + self.failed_test_cases
        self.logger.info("The Number Of Total  Test Cases is :  " + str(self.total_test_cases)) 
        self.logger.info("The Number Of Passed Test Cases is :  " + str(self.passed_test_cases))  
        self.logger.info("The Number Of Failed Test Cases is :  " + str(self.failed_test_cases))     

   
                