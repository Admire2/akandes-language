library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
-- 2-bit FSM: 00->01->10->00
entity simple_fsm is
    port (
        clk : in std_logic;
        rst : in std_logic;
        state : out std_logic_vector(1 downto 0)
    );
end simple_fsm;

architecture Behavioral of simple_fsm is
    signal current : std_logic_vector(1 downto 0);
    signal next_state : std_logic_vector(1 downto 0);
begin
    process(clk, rst)
    begin
        if rst = '1' then
            current <= (others => '0');
        elsif rising_edge(clk) then
            current <= next_state;
        end if;
    end process;
    process(current)
    begin
        case current is
            when "00" => next_state <= "01";
            when "01" => next_state <= "10";
            when "10" => next_state <= "00";
            when others => next_state <= "00";
        end case;
        state <= current;
    end process;
end Behavioral;