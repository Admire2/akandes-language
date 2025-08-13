library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
entity tb_subtractor4 is end;
architecture test of tb_subtractor4 is
    signal a, b, diff : std_logic_vector(3 downto 0);
    signal borrow : std_logic;
begin
    uut: entity work.subtractor4 port map(a=>a, b=>b, diff=>diff, borrow=>borrow);
    process
    begin
        a <= "1010"; b <= "0101"; wait for 1 ns;
        report "diff=" & integer'image(to_integer(unsigned(diff))) & ", borrow=" & std_logic'image(borrow);
        a <= "0011"; b <= "0101"; wait for 1 ns;
        report "diff=" & integer'image(to_integer(unsigned(diff))) & ", borrow=" & std_logic'image(borrow);
        wait;
    end process;
end;