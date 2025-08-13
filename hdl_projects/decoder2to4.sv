// 2-to-4 decoder
module decoder2to4  (
    input logic [1:0] a,
    output logic [3:0] y
);
    
    assign y = 4'b0001 << a;
endmodule