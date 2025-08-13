library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
entity tb_ripple_adder4 is end;
architecture test of tb_ripple_adder4 is
    signal a, b, sum : std_logic_vector(3 downto 0);
    signal cin, cout : std_logic;
begin
    uut: entity work.ripple_adder4 port map(a=>a, b=>b, cin=>cin, sum=>sum, cout=>cout);
    process
    begin
        a <= "0001"; b <= "0010"; cin <= '0'; wait for 1 ns;
        report "sum=" & integer'image(to_integer(unsigned(sum))) & ", cout=" & std_logic'image(cout);
        a <= "1111"; b <= "0001"; cin <= '1'; wait for 1 ns;
        report "sum=" & integer'image(to_integer(unsigned(sum))) & ", cout=" & std_logic'image(cout);
        a <= "1010"; b <= "0101"; cin <= '0'; wait for 1 ns;
        report "sum=" & integer'image(to_integer(unsigned(sum))) & ", cout=" & std_logic'image(cout);
        wait;
    end process;
end;