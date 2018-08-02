function p = larg_prod_grid(grid, n)

    [lin, col] = size(grid);
    
    p = -Inf;
    
    for i = 1:(lin - n + 1)
        for j = 1:(col - n + 1)
            sub_grid = grid(i:i + n - 1, j:j + n - 1);
            test = larg_prod_sub_grid(sub_grid);
            if test > p
                p = test;
            end
        end
    end

end

function p = larg_prod_sub_grid(grid)

    p = -Inf;
    
    %   Largest product of lines
    for i = 1:length(grid)
        test = 1;
        for j = 1:length(grid)
            test = test*grid(i, j);
        end
        if test > p
                p = test;
        end
    end
 
    %   Largest product of columns
    for i = 1:length(grid)
        test = 1;
        for j = 1:length(grid)
            test = test*grid(j, i);
        end
        if test > p
                p = test;
        end
    end
    
    %   Product of primary daigonal
    test = 1;
    for i = 1:length(grid)
        test = test*grid(i, i);
    end
    if test > p
        p = test;
    end
    
    %   Product of secondary daigonal
    test = 1;
    for i = 1:length(grid)
        test = test*grid(length(grid) - (i - 1), i);
    end
    if test > p
        p = test;
    end

end