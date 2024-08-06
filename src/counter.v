module synchronous_counter (
    input wire clk,
    output wire [3:0] count
);
    reg [3:0] count;
    always @(posedge clk)
        count <= count + 1;
endmodule
