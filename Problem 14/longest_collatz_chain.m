function [n, ref] = longest_collatz_chain(limit)
    
    n = 0;
    ref = 0;
    for i = limit:-1:1
        
        test = collatz_chain_length(i);
        if test > n
            n = test;
            ref = i;
        end
    
    end

end
function chain_len = collatz_chain_length(n)

    chain_len = 1;
    
    while n ~= 1
        if mod(n, 2) == 0
            n = n/2;
        else
            n = 3*n + 1;
        end
        
        chain_len = chain_len + 1;
        
    end

end