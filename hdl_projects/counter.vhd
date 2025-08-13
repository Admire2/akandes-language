library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
-- 8-bit synchronous counter
entity counter is
    port (
        clk : in std_logic;
        rst : in std_logic;
        q : out std_logic_vector(7 downto 0)
    );
end counter;

architecture Behavioral of counter is
    signal cnt : unsigned(7 downto 0);
begin
    process(clk, rst)
    begin
        if rst = '1' then
            cnt <= (others => '0');
        elsif rising_edge(clk) then
            cnt <= cnt + 1;
        end if;
        q <= std_logic_vector(cnt);
    end process;
end Behavioral;