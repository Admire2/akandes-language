library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
entity tb_comparator4 is end;
architecture test of tb_comparator4 is
    signal a, b : std_logic_vector(3 downto 0);
    signal eq, gt, lt : std_logic;
begin
    uut: entity work.comparator4 port map(a=>a, b=>b, eq=>eq, gt=>gt, lt=>lt);
    process
    begin
        a <= "0101"; b <= "0101"; wait for 1 ns;
        report "eq=" & std_logic'image(eq) & ", gt=" & std_logic'image(gt) & ", lt=" & std_logic'image(lt);
        a <= "1000"; b <= "0111"; wait for 1 ns;
        report "eq=" & std_logic'image(eq) & ", gt=" & std_logic'image(gt) & ", lt=" & std_logic'image(lt);
        a <= "0010"; b <= "0100"; wait for 1 ns;
        report "eq=" & std_logic'image(eq) & ", gt=" & std_logic'image(gt) & ", lt=" & std_logic'image(lt);
        wait;
    end process;
end;