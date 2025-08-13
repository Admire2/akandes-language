module tb_alu;
    reg [3:0] a, b;
    reg [1:0] op;
    wire [3:0] y;
    alu uut(.a(a), .b(b), .op(op), .y(y));
    initial begin
        a = 4'd3; b = 4'd5; op = 2'b00; #1;
        $display("y = %d (add)", y);
        op = 2'b01; #1;
        $display("y = %d (sub)", y);
        op = 2'b10; #1;
        $display("y = %d (and)", y);
        op = 2'b11; #1;
        $display("y = %d (or)", y);
    end
endmodule