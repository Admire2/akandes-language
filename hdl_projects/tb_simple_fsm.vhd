library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
entity tb_simple_fsm is end;
architecture test of tb_simple_fsm is
    signal clk, rst : std_logic;
    signal state : std_logic_vector(1 downto 0);
begin
    uut: entity work.simple_fsm port map(clk=>clk, rst=>rst, state=>state);
    process
    begin
        clk <= '0'; rst <= '1'; wait for 1 ns;
        rst <= '0';
        for i in 0 to 3 loop
            clk <= '1'; wait for 1 ns;
            clk <= '0'; wait for 1 ns;
            report "state=" & std_logic_vector'image(state);
        end loop;
        wait;
    end process;
end;