module testbench;
    reg a, b;
    wire sum, carry;

    // Instantiate the DUT
    half_adder dut (
        .a(a),
        .b(b),
        .sum(sum),
        .carry(carry)
    );

    // Generate stimulus
    initial begin
        $dumpfile("test_half_adder.vcd"); // Specify the VCD file name
        $dumpvars(0, testbench); // Dump all variables in the testbench
        $monitor("At time %t: a = %b, b = %b, sum = %b, carry = %b", $time, a, b, sum, carry);
        a = 0; b = 0;
        #10;
        a = 0; b = 1;
        #10;
        a = 1; b = 0;
        #10;
        a = 1; b = 1;
        #10;
        $finish;
    end
endmodule
