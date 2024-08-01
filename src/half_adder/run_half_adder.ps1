iverilog -o test_half_adder.vvp half_adder.v test_half_adder.v
vvp .\test_half_adder.vvp
gtkwave test_half_adder.vcd