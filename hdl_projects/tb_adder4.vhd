library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
entity tb_adder4 is end;
architecture test of tb_adder4 is
    signal a, b, sum : std_logic_vector(3 downto 0);
    signal carry : std_logic;
begin
    uut: entity work.adder4 port map(a=>a, b=>b, sum=>sum, carry=>carry);
    process
    begin
        a <= "0011"; b <= "0101"; wait for 1 ns;
        report "sum=" & integer'image(to_integer(unsigned(sum)));
        report "carry=" & std_logic'image(carry);
        a <= "1111"; b <= "0001"; wait for 1 ns;
        report "sum=" & integer'image(to_integer(unsigned(sum)));
        report "carry=" & std_logic'image(carry);
        wait;
    end process;
end;