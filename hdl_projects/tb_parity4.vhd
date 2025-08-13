library ieee;
use ieee.std_logic_1164.all;
entity tb_parity4 is end;
architecture test of tb_parity4 is
    signal a : std_logic_vector(3 downto 0);
    signal parity : std_logic;
begin
    uut: entity work.parity4 port map(a=>a, parity=>parity);
    process
    begin
        a <= "1010"; wait for 1 ns;
        report "parity=" & std_logic'image(parity);
        a <= "1111"; wait for 1 ns;
        report "parity=" & std_logic'image(parity);
        wait;
    end process;
end;