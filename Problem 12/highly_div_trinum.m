function t = highly_div_trinum(num_div)

    div = 0;
    n = 0;
    while div < num_div
        n = n + 1;
        div = length(divisors(trinum(n)));
        disp(trinum(n));
        disp(div);
    end

    t = trinum(n);
    
end


function t = trinum(n)

    i = 1;
    t = 0;
    
    for k = 1:n
        t = t + i;
        i = i + 1;
    end
    
end