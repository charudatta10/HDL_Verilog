iverilog -o test_seq_ctr.vvp seq_ctr.v test_seq_ctr.v
vvp test_seq_ctr.vvp
gtkwave test_seq_ctr.vcd