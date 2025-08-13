library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
-- 4-bit ripple-carry adder
entity ripple_adder4 is
    port (
        a : in std_logic_vector(3 downto 0);
        b : in std_logic_vector(3 downto 0);
        cin : in std_logic;
        sum : out std_logic_vector(3 downto 0);
        cout : out std_logic
    );
end ripple_adder4;

architecture Behavioral of ripple_adder4 is
    signal c : std_logic_vector(4 downto 0);
begin
    c(0) <= cin;
    sum(0) <= a(0) xor b(0) xor c(0);
    c(1) <= (a(0) and b(0)) or (a(0) and c(0)) or (b(0) and c(0));
    sum(1) <= a(1) xor b(1) xor c(1);
    c(2) <= (a(1) and b(1)) or (a(1) and c(1)) or (b(1) and c(1));
    sum(2) <= a(2) xor b(2) xor c(2);
    c(3) <= (a(2) and b(2)) or (a(2) and c(2)) or (b(2) and c(2));
    sum(3) <= a(3) xor b(3) xor c(3);
    c(4) <= (a(3) and b(3)) or (a(3) and c(3)) or (b(3) and c(3));
    cout <= c(4);
end Behavioral;