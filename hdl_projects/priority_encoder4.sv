// 4-to-2 priority encoder with valid output
module priority_encoder4  (
    input logic [3:0] y,
    output logic [1:0] a,
    output logic valid
);
    
    always @(*) begin
        casex (y)
            4'b1xxx: begin a = 2'b11; valid = 1'b1; end
            4'b01xx: begin a = 2'b10; valid = 1'b1; end
            4'b001x: begin a = 2'b01; valid = 1'b1; end
            4'b0001: begin a = 2'b00; valid = 1'b1; end
            default: begin a = 2'b00; valid = 1'b0; end
        endcase
    end
endmodule