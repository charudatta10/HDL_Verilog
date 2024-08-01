module testbench;
    reg d, clk, rst;
    wire q;

    // Instantiate the DUT
    dff dut (
        .d(d),
        .clk(clk),
        .rst(rst),
        .q(q)
    );

    // Generate stimulus
    initial begin
        $dumpfile("test_dff.vcd"); // Specify the VCD file name
        $dumpvars(0, testbench); // Dump all variables in the testbench
        $monitor("At time %t: a = %b, b = %b, sum = %b, carry = %b", $time, d, clk, rst, q);
        d = 0; clk = 0; rst=1;
        #10;
        rst = 0; d = 0;
        #10;
        d = 1;
        #10;
        d = 0;
        #10;
        $finish;
    end

always #5 clk = ~ clk;
endmodule
