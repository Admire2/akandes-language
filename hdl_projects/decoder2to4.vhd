library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
-- 2-to-4 decoder
entity decoder2to4 is
    port (
        a : in std_logic_vector(1 downto 0);
        y : out std_logic_vector(3 downto 0)
    );
end decoder2to4;

architecture Behavioral of decoder2to4 is
    
begin
    y <= "0001" when a = "00" else "0010" when a = "01" else "0100" when a = "10" else "1000";
end Behavioral;