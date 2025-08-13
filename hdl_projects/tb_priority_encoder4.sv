module tb_priority_encoder4;
    reg [3:0] y;
    wire [1:0] a;
    wire valid;
    priority_encoder4 uut(.y(y), .a(a), .valid(valid));
    initial begin
        y = 4'b0000; #1; $display("a = %b, valid = %b", a, valid);
        y = 4'b0001; #1; $display("a = %b, valid = %b", a, valid);
        y = 4'b0010; #1; $display("a = %b, valid = %b", a, valid);
        y = 4'b0100; #1; $display("a = %b, valid = %b", a, valid);
        y = 4'b1000; #1; $display("a = %b, valid = %b", a, valid);
        y = 4'b1010; #1; $display("a = %b, valid = %b", a, valid);
        y = 4'b1111; #1; $display("a = %b, valid = %b", a, valid);
    end
endmodule