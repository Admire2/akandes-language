// 4-bit serial-in, parallel-out shift register
module shiftreg4  (
    input logic clk,
    input logic rst,
    input logic d,
    output logic [3:0] q
);
    
    reg [3:0] q_reg;
    always @(posedge clk or posedge rst) begin
        if (rst) q_reg <= 4'b0;
        else q_reg <= {q_reg[2:0], d};
    end
    assign q = q_reg;
endmodule