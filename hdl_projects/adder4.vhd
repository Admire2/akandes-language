library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
-- 4-bit adder
entity adder4 is
    port (
        a : in std_logic_vector(3 downto 0);
        b : in std_logic_vector(3 downto 0);
        sum : out std_logic_vector(3 downto 0);
        carry : out std_logic
    );
end adder4;

architecture Behavioral of adder4 is
    
begin
    sum <= std_logic_vector(unsigned(a) + unsigned(b));
    carry <= '1' when (unsigned(a) + unsigned(b)) > 15 else '0';
end Behavioral;