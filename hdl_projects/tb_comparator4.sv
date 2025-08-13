module tb_comparator4;
    reg [3:0] a, b;
    wire eq, gt, lt;
    comparator4 uut(.a(a), .b(b), .eq(eq), .gt(gt), .lt(lt));
    initial begin
        a = 4'd5; b = 4'd5;
        #1;
        $display("eq = %b, gt = %b, lt = %b", eq, gt, lt);
        a = 4'd8; b = 4'd7;
        #1;
        $display("eq = %b, gt = %b, lt = %b", eq, gt, lt);
        a = 4'd2; b = 4'd4;
        #1;
        $display("eq = %b, gt = %b, lt = %b", eq, gt, lt);
    end
endmodule