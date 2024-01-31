#GUI = 1
#wave = 1  
TOPLEVEL_LANG ?= verilog
SIM ?= questa
PWD=$(shell pwd)


ifeq ($(TOPLEVEL_LANG),verilog)
    VERILOG_SOURCES = $(PWD)/clk_gen.sv
else ifeq ($(TOPLEVEL_LANG),vhdl)
    VHDL_SOURCES = $(PWD)/clk_gen.vhdl
else
    $(error A valid value (verilog or vhdl) was not provided for TOPLEVEL_LANG=$(TOPLEVEL_LANG))
endif

TOPLEVEL := clk_gen             #Module_NAME
MODULE   := tb                  #File_Python_Name

include $(shell cocotb-config --makefiles)/Makefile.sim