// 4-bit ALU: add, sub, and, or (Icarus Verilog compatible)
module alu  (
    input logic [3:0] a,
    input logic [3:0] b,
    input logic [1:0] op,
    output logic [3:0] y
);
    
    reg [3:0] y_reg;
    always @(*) begin
        case (op)
            2'b00: y_reg = a + b;
            2'b01: y_reg = a - b;
            2'b10: y_reg = a & b;
            2'b11: y_reg = a | b;
            default: y_reg = 4'b0000;
        endcase
    end
    assign y = y_reg;
endmodule