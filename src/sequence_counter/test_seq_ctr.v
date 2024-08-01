module testbench;
    reg ip, clk, rst;
    wire opt;

    // Instantiate the DUT
    seq_ctr dut (
        .ip(ip),
        .clk(clk),
        .rst(rst),
        .opt(opt)
    );

    // Generate stimulus
    initial begin
        $dumpfile("test_seq_ctr.vcd"); // Specify the VCD file name
        $dumpvars(0, testbench); // Dump all variables in the testbench
        $monitor("At time %t: a = %b, b = %b, sum = %b, carry = %b", $time, ip, clk, rst, opt);
        clk = 0; rst = 0; ip=0;
        #10;
        rst = 1; ip=0;
        #10;
        ip=1;
        #10;
        ip=0;
        #10;
        ip=1;
        #10;
        ip=1;
        #10;
        ip=1;
        #10;
        $finish;
    end
    always #5 clk = ~clk;
endmodule
