module tb_multiplier4;
    reg [3:0] a, b;
    wire [7:0] product;
    multiplier4 uut(.a(a), .b(b), .product(product));
    initial begin
        a = 4'd3; b = 4'd5; #1;
        $display("product = %d", product);
        a = 4'd15; b = 4'd1; #1;
        $display("product = %d", product);
    end
endmodule