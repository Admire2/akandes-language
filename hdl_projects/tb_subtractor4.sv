module tb_subtractor4;
    reg [3:0] a, b;
    wire [3:0] diff;
    wire borrow;
    subtractor4 uut(.a(a), .b(b), .diff(diff), .borrow(borrow));
    initial begin
        a = 4'd10; b = 4'd5; #1;
        $display("diff = %d, borrow = %b", diff, borrow);
        a = 4'd3; b = 4'd5; #1;
        $display("diff = %d, borrow = %b", diff, borrow);
    end
endmodule