library ieee;
use ieee.std_logic_1164.all;
entity tb_decoder2to4 is end;
architecture test of tb_decoder2to4 is
    signal a : std_logic_vector(1 downto 0);
    signal y : std_logic_vector(3 downto 0);
begin
    uut: entity work.decoder2to4 port map(a=>a, y=>y);
    process
    begin
        a <= "00"; wait for 1 ns;
        report "y=" & std_logic_vector'image(y);
        a <= "01"; wait for 1 ns;
        report "y=" & std_logic_vector'image(y);
        a <= "10"; wait for 1 ns;
        report "y=" & std_logic_vector'image(y);
        a <= "11"; wait for 1 ns;
        report "y=" & std_logic_vector'image(y);
        wait;
    end process;
end;