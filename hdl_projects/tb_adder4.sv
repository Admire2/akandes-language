module tb_adder4;
    reg [3:0] a, b;
    wire [3:0] sum;
    wire carry;
    adder4 uut(.a(a), .b(b), .sum(sum), .carry(carry));
    initial begin
        a = 4'd3; b = 4'd5;
        #1;
        $display("sum = %d, carry = %b", sum, carry);
        a = 4'd15; b = 4'd1;
        #1;
        $display("sum = %d, carry = %b", sum, carry);
    end
endmodule