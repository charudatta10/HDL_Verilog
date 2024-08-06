module testbench;
    reg a, b, cin;
    wire sum, carry;

    // Instantiate the DUT
    full_adder dut (
        .a(a),
        .b(b),
        .cin(cin),
        .sum(sum),
        .carry(carry)
    );

    // Generate stimulus
    initial begin
        $dumpfile("build/full_adder.vcd"); // Specify the VCD file name
        $dumpvars(0, testbench); // Dump all variables in the testbench
        $monitor("At time %t: a = %b, b = %b, cin = %b, sum = %b, carry = %b", $time, a, b, cin, sum, carry);
        a = 0; b = 0; cin=0;
        #10;
        a = 0; b = 1; cin=0;
        #10;
        a = 1; b = 0; cin=0;
        #10;
        a = 1; b = 1; cin=0;
        #10;
        a = 0; b = 0; cin=1;
        #10;
        a = 0; b = 1; cin=1;
        #10;
        a = 1; b = 0; cin=1;
        #10;
        a = 1; b = 1; cin=1;
        #10;
        $finish;
    end
endmodule
