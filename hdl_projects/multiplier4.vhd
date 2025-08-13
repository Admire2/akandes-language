library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
-- 4-bit multiplier
entity multiplier4 is
    port (
        a : in std_logic_vector(3 downto 0);
        b : in std_logic_vector(3 downto 0);
        product : out std_logic_vector(7 downto 0)
    );
end multiplier4;

architecture Behavioral of multiplier4 is
    
begin
    product <= std_logic_vector(unsigned(a) * unsigned(b));
end Behavioral;