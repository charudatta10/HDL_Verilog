module seq_ctr (
    input wire ip, clk, rst,
    output reg opt
);

parameter [2:0]s0=3'b000, s1=3'b001, s2=3'b010, s3=3'b011, s4=3'b100;
reg [2:0] st,nt;

always @(posedge clk)
begin
    if(rst==0)
    st<= s0;
    else
    st<= nt;
end

always @(*)
begin
    case(st)
    s0:
    begin
        if(ip==1)
        nt = s1;
        else
        nt = s0;
    end
    s1:
    begin
        if(ip==0)
        nt = s2;
        else
        nt = s1;
    end
    s2:
    begin
        if(ip==1)
        nt = s3;
        else
        nt = s0;
    end
    s3:
    begin
        if(ip==1)
        nt = s4;
        else
        nt = s2;
    end
    s3:
    begin
        if(ip==0)
        nt = s2;
        else
        nt = s1;
    end
    default: nt = s0;
    endcase
end

 
always @(*)
begin
    case(st)
    s0: opt= 0;
    s1: opt= 0;
    s2: opt= 0;
    s3: opt= 0;
    s4: opt= 1;
    default: opt = 0;
    endcase
end

endmodule
