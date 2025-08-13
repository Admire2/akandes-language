module tb_register8;
    reg clk, rst;
    reg [7:0] d;
    wire [7:0] q;
    register8 uut(.clk(clk), .rst(rst), .d(d), .q(q));
    integer i;
    initial begin
        clk = 0; rst = 1; d = 8'b0;
        #2; rst = 0;
        for (i = 0; i < 4; i = i + 1) begin
            d = $random;
            #1; clk = ~clk; #1; clk = ~clk;
            $display("q = %b", q);
        end
    end
endmodule