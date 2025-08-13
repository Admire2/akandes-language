library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
-- 4-bit comparator
entity comparator4 is
    port (
        a : in std_logic_vector(3 downto 0);
        b : in std_logic_vector(3 downto 0);
        eq : out std_logic;
        gt : out std_logic;
        lt : out std_logic
    );
end comparator4;

architecture Behavioral of comparator4 is
    
begin
    eq <= '1' when unsigned(a) = unsigned(b) else '0';
    gt <= '1' when unsigned(a) > unsigned(b) else '0';
    lt <= '1' when unsigned(a) < unsigned(b) else '0';
end Behavioral;