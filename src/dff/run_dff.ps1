iverilog -o test_dff.vvp dff.v test_dff.v
vvp .\test_dff.vvp
gtkwave test_dff.vcd