module tb_shiftreg4;
    reg clk, rst, d;
    wire [3:0] q;
    shiftreg4 uut(.clk(clk), .rst(rst), .d(d), .q(q));
    integer i;
    initial begin
        clk = 0; rst = 1; d = 0;
        #2; rst = 0;
        for (i = 0; i < 8; i = i + 1) begin
            d = $random;
            #1; clk = ~clk; #1; clk = ~clk;
            $display("q = %b", q);
        end
    end
endmodule