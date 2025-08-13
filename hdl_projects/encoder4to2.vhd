library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
-- 4-to-2 encoder
entity encoder4to2 is
    port (
        y : in std_logic_vector(3 downto 0);
        a : out std_logic_vector(1 downto 0)
    );
end encoder4to2;

architecture Behavioral of encoder4to2 is
    
begin
    a <= "00" when y = "0001" else "01" when y = "0010" else "10" when y = "0100" else "11";
end Behavioral;