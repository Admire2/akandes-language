library ieee;
use ieee.std_logic_1164.all;
entity tb_encoder4to2 is end;
architecture test of tb_encoder4to2 is
    signal y : std_logic_vector(3 downto 0);
    signal a : std_logic_vector(1 downto 0);
begin
    uut: entity work.encoder4to2 port map(y=>y, a=>a);
    process
    begin
        y <= "0001"; wait for 1 ns;
        report "a=" & std_logic_vector'image(a);
        y <= "0010"; wait for 1 ns;
        report "a=" & std_logic_vector'image(a);
        y <= "0100"; wait for 1 ns;
        report "a=" & std_logic_vector'image(a);
        y <= "1000"; wait for 1 ns;
        report "a=" & std_logic_vector'image(a);
        wait;
    end process;
end;