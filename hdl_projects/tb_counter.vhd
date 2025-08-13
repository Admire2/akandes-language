library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
entity tb_counter is end;
architecture test of tb_counter is
    signal clk, rst : std_logic;
    signal q : std_logic_vector(7 downto 0);
begin
    uut: entity work.counter port map(clk=>clk, rst=>rst, q=>q);
    process
    begin
        clk <= '0'; rst <= '1'; wait for 1 ns;
        rst <= '0';
        for i in 0 to 3 loop
            clk <= '1'; wait for 1 ns;
            clk <= '0'; wait for 1 ns;
            report "q=" & integer'image(to_integer(unsigned(q)));
        end loop;
        wait;
    end process;
end;