iverilog -o test_full_adder.vvp full_adder.v test_full_adder.v
vvp .\test_full_adder.vvp
gtkwave test_full_adder.vcd