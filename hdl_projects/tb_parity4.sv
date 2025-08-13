module tb_parity4;
    reg [3:0] a;
    wire parity;
    parity4 uut(.a(a), .parity(parity));
    initial begin
        a = 4'b1010;
        #1;
        $display("parity = %b", parity);
        a = 4'b1111;
        #1;
        $display("parity = %b", parity);
    end
endmodule