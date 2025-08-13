module tb_decoder2to4;
    reg [1:0] a;
    wire [3:0] y;
    decoder2to4 uut(.a(a), .y(y));
    initial begin
        a = 2'b00; #1;
        $display("y = %b", y);
        a = 2'b01; #1;
        $display("y = %b", y);
        a = 2'b10; #1;
        $display("y = %b", y);
        a = 2'b11; #1;
        $display("y = %b", y);
    end
endmodule