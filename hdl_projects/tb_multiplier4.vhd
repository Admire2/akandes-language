library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
entity tb_multiplier4 is end;
architecture test of tb_multiplier4 is
    signal a, b : std_logic_vector(3 downto 0);
    signal product : std_logic_vector(7 downto 0);
begin
    uut: entity work.multiplier4 port map(a=>a, b=>b, product=>product);
    process
    begin
        a <= "0011"; b <= "0101"; wait for 1 ns;
        report "product=" & integer'image(to_integer(unsigned(product)));
        a <= "1111"; b <= "0001"; wait for 1 ns;
        report "product=" & integer'image(to_integer(unsigned(product)));
        wait;
    end process;
end;