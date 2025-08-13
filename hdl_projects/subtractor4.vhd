library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
-- 4-bit subtractor
entity subtractor4 is
    port (
        a : in std_logic_vector(3 downto 0);
        b : in std_logic_vector(3 downto 0);
        diff : out std_logic_vector(3 downto 0);
        borrow : out std_logic
    );
end subtractor4;

architecture Behavioral of subtractor4 is
    
begin
    diff <= std_logic_vector(unsigned(a) - unsigned(b));
    borrow <= '1' when unsigned(a) < unsigned(b) else '0';
end Behavioral;