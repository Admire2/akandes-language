module tb_mux2to1;
    reg a, b, sel;
    wire y;
    mux2to1 uut(.a(a), .b(b), .sel(sel), .y(y));
    initial begin
        a = 0; b = 1; sel = 0; #1;
        $display("y = %b", y);
        sel = 1; #1;
        $display("y = %b", y);
    end
endmodule