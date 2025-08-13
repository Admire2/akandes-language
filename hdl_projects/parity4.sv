// 4-bit parity checker
module parity4  (
    input logic [3:0] a,
    output logic parity
);
    
    assign parity = ^a;
endmodule