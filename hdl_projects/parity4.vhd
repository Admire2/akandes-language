library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
-- 4-bit parity checker
entity parity4 is
    port (
        a : in std_logic_vector(3 downto 0);
        parity : out std_logic
    );
end parity4;

architecture Behavioral of parity4 is
    
begin
    parity <= a(0) xor a(1) xor a(2) xor a(3);
end Behavioral;