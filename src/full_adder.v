module full_adder (
    input wire a, b, cin,
    output wire sum, carry
);
    assign sum = a ^ b ^ cin;
    assign carry = a & b | a & cin | b & cin;
endmodule
