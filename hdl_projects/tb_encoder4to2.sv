module tb_encoder4to2;
    reg [3:0] y;
    wire [1:0] a;
    encoder4to2 uut(.y(y), .a(a));
    initial begin
        y = 4'b0001; #1;
        $display("a = %b", a);
        y = 4'b0010; #1;
        $display("a = %b", a);
        y = 4'b0100; #1;
        $display("a = %b", a);
        y = 4'b1000; #1;
        $display("a = %b", a);
    end
endmodule