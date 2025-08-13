// 8-bit register with async reset (Icarus Verilog compatible)
module register8  (
    input logic clk,
    input logic rst,
    input logic [7:0] d,
    output logic [7:0] q
);
    
    reg [7:0] q_reg;
    always @(posedge clk or posedge rst) begin
        if (rst) q_reg <= 8'b0;
        else q_reg <= d;
    end
    assign q = q_reg;
endmodule